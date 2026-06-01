#!/usr/bin/env python3
"""Create a lightweight, evidence-oriented repository snapshot."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    "vendor",
    "dist",
    "build",
    ".next",
    ".nuxt",
    "coverage",
    "target",
    ".venv",
    "venv",
    "env",
}

MANIFESTS = {
    "package.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "package-lock.json",
    "pyproject.toml",
    "requirements.txt",
    "Pipfile",
    "poetry.lock",
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "settings.gradle",
    "composer.json",
    "Gemfile",
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
}

ENTRYPOINT_HINTS = {
    "main.py",
    "app.py",
    "manage.py",
    "server.py",
    "index.js",
    "index.ts",
    "main.js",
    "main.ts",
    "src/main.ts",
    "src/main.tsx",
    "src/App.tsx",
    "src/App.jsx",
    "src/app/page.tsx",
    "src/app/layout.tsx",
    "pages/index.tsx",
    "pages/index.jsx",
    "app/routes.ts",
}

DOC_NAMES = {"README.md", "readme.md", "CONTRIBUTING.md", "docs", "doc"}
TEST_MARKERS = {"test", "tests", "__tests__", "spec", "cypress", "playwright"}


def run_git(repo: Path, args: list[str]) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo,
            text=True,
            capture_output=True,
            timeout=4,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def iter_files(repo: Path, max_files: int) -> list[Path]:
    files: list[Path] = []
    for root, dirs, names in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".cache")]
        for name in names:
            path = Path(root) / name
            try:
                rel = path.relative_to(repo)
            except ValueError:
                continue
            files.append(rel)
            if len(files) >= max_files:
                return files
    return files


def read_package_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return {}


def detect_frameworks(repo: Path, files: list[Path]) -> list[str]:
    found: set[str] = set()
    package = repo / "package.json"
    if package.exists():
        data = read_package_json(package)
        deps = {}
        for key in ("dependencies", "devDependencies"):
            deps.update(data.get(key, {}) if isinstance(data.get(key), dict) else {})
        checks = {
            "React": "react",
            "Next.js": "next",
            "Vue": "vue",
            "Nuxt": "nuxt",
            "Svelte": "svelte",
            "Express": "express",
            "NestJS": "@nestjs/core",
            "Vite": "vite",
            "Tailwind CSS": "tailwindcss",
            "Prisma": "prisma",
            "Electron": "electron",
            "Playwright": "@playwright/test",
        }
        for label, dep in checks.items():
            if dep in deps:
                found.add(label)
    names = {str(p).replace("\\", "/") for p in files}
    if "manage.py" in names:
        found.add("Django")
    if "go.mod" in names:
        found.add("Go")
    if "Cargo.toml" in names:
        found.add("Rust")
    if "pom.xml" in names or "build.gradle" in names:
        found.add("Java/JVM")
    if "pyproject.toml" in names or "requirements.txt" in names:
        found.add("Python")
    return sorted(found)


def summarize(repo: Path, max_files: int) -> dict[str, Any]:
    files = iter_files(repo, max_files=max_files)
    file_strings = [str(p).replace("\\", "/") for p in files]
    ext_counts = Counter((p.suffix.lower() or "[no extension]") for p in files)
    top_dirs: defaultdict[str, int] = defaultdict(int)
    for p in files:
        parts = p.parts
        top_dirs[parts[0] if len(parts) > 1 else "."] += 1

    manifests = [f for f in file_strings if Path(f).name in MANIFESTS]
    docs = [
        f
        for f in file_strings
        if Path(f).name in DOC_NAMES or any(part.lower() in {"docs", "doc"} for part in Path(f).parts)
    ]
    entrypoints = [f for f in file_strings if f in ENTRYPOINT_HINTS or Path(f).name in ENTRYPOINT_HINTS]
    tests = [
        f
        for f in file_strings
        if any(marker in [part.lower() for part in Path(f).parts] for marker in TEST_MARKERS)
        or Path(f).name.lower().startswith(("test_",))
        or ".test." in Path(f).name
        or ".spec." in Path(f).name
    ]

    package_scripts: dict[str, str] = {}
    package = repo / "package.json"
    if package.exists():
        data = read_package_json(package)
        scripts = data.get("scripts", {})
        if isinstance(scripts, dict):
            package_scripts = {str(k): str(v) for k, v in scripts.items()}

    git = {
        "branch": run_git(repo, ["rev-parse", "--abbrev-ref", "HEAD"]),
        "commit": run_git(repo, ["rev-parse", "--short", "HEAD"]),
        "status": run_git(repo, ["status", "--short"]),
        "recent_commits": run_git(repo, ["log", "--oneline", "-5"]),
    }

    return {
        "root": str(repo),
        "file_count_sampled": len(files),
        "sample_limited": len(files) >= max_files,
        "top_directories": dict(sorted(top_dirs.items(), key=lambda item: item[1], reverse=True)[:12]),
        "extensions": dict(ext_counts.most_common(12)),
        "manifests": manifests[:30],
        "docs": docs[:30],
        "entrypoints": entrypoints[:30],
        "tests": tests[:30],
        "frameworks": detect_frameworks(repo, files),
        "package_scripts": package_scripts,
        "git": git,
    }


def render_markdown(data: dict[str, Any]) -> str:
    lines = [
        "# Repository Snapshot",
        "",
        f"- Root: `{data['root']}`",
        f"- Files sampled: {data['file_count_sampled']}{' (limit reached)' if data['sample_limited'] else ''}",
    ]
    git = data.get("git", {})
    if git.get("branch") or git.get("commit"):
        lines.append(f"- Git: `{git.get('branch') or 'unknown'}` at `{git.get('commit') or 'unknown'}`")
    if data["frameworks"]:
        lines.append(f"- Detected stack hints: {', '.join(data['frameworks'])}")

    sections = [
        ("Top Directories", data["top_directories"]),
        ("Extension Mix", data["extensions"]),
        ("Manifests", data["manifests"]),
        ("Docs", data["docs"]),
        ("Likely Entry Points", data["entrypoints"]),
        ("Tests", data["tests"]),
        ("Package Scripts", data["package_scripts"]),
    ]
    for title, value in sections:
        lines.extend(["", f"## {title}"])
        if not value:
            lines.append("- None found in sample")
        elif isinstance(value, dict):
            for key, item in value.items():
                lines.append(f"- `{key}`: {item}")
        else:
            for item in value:
                lines.append(f"- `{item}`")

    if git.get("status"):
        lines.extend(["", "## Git Status", "```", git["status"], "```"])
    if git.get("recent_commits"):
        lines.extend(["", "## Recent Commits", "```", git["recent_commits"], "```"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", help="Repository path to inspect")
    parser.add_argument("--max-files", type=int, default=2000, help="Maximum files to sample")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists() or not repo.is_dir():
        parser.error(f"repo path does not exist or is not a directory: {repo}")

    data = summarize(repo, max_files=args.max_files)
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(render_markdown(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
