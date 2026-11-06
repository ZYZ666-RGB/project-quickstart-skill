# Project Quickstart Skill

[中文说明](README.zh-CN.md) · [Skill source](project-quickstart/SKILL.md) · [License: MIT](LICENSE)

**A Codex / OpenAI skill that turns an unfamiliar software repo into an interview-ready project brief in minutes.**

Built for students, job seekers, and new contributors who need a fast mental model — architecture, core flows, evidence-backed talking points — without overclaiming.

---

## Why this exists

Cloning a random GitHub project and being asked “walk me through it” is hard. READMEs skip the hard parts; grepping blindly wastes an afternoon.

This skill steers an agent to:

1. Inspect the repo (README, deps, entrypoints, tests, recent git)
2. Build a learner-friendly architecture + data-flow explanation
3. Cite **evidence** (file paths / commands) for every important claim
4. Produce interview / resume talking points with an explicit verification status

## Demo (what you get)

Ask:

> Use `$project-quickstart` to help me understand this repository and prepare an interview-ready project brief.

Typical output sections:

| Section | Contents |
| --- | --- |
| One-sentence summary | What the product does |
| How to run / inspect | Commands actually found in the repo |
| Architecture map | Modules ↔ responsibilities + file refs |
| Mermaid diagram | Architecture or core flow |
| Evidence map | Claim → file / command that supports it |
| Strengths / risks | Honest, scoped notes |
| Interview pitches | 30s / 1min / 3min options when relevant |
| Verification status | What was run vs still uncertain |

Optional helper script for a local checkout:

```bash
python project-quickstart/scripts/repo_snapshot.py /path/to/repo
```

Treat the snapshot as a map, not ground truth — the skill still reads the real files.

## Install

Clone, then copy the skill folder into your Codex skills directory.

**macOS / Linux**

```bash
git clone https://github.com/ZYZ666-RGB/project-quickstart-skill.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R project-quickstart-skill/project-quickstart "${CODEX_HOME:-$HOME/.codex}/skills/"
```

**Windows PowerShell**

```powershell
git clone https://github.com/ZYZ666-RGB/project-quickstart-skill.git
$skillsDir = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $HOME ".codex\skills" }
New-Item -ItemType Directory -Force $skillsDir | Out-Null
Copy-Item -Recurse .\project-quickstart-skill\project-quickstart $skillsDir
```

Restart Codex if the skill does not appear immediately.

## Usage

**Explicit**

```text
Use $project-quickstart to help me understand this repository and prepare an interview-ready project brief.
```

**Natural language** (routing cases live in [`evals/routing-cases.yaml`](project-quickstart/evals/routing-cases.yaml))

```text
Help me quickly understand this project for an interview.
I just cloned this repo — which files should I read first?
Turn this project into resume-ready experience and list the technical highlights.
```

## Repository layout

```text
project-quickstart/
├── SKILL.md                      # trigger description + core workflow
├── agents/openai.yaml            # agent wiring
├── assets/project-brief-template.md
├── evals/routing-cases.yaml      # positive / negative / edge routing tests
├── references/output-rubric.md   # quality bar for polished briefs
└── scripts/repo_snapshot.py      # optional structural scan
```

## Design principles

- **Evidence over vibes** — important claims need a file, command, or observed behavior
- **Say what you did not verify** — never “fully analyzed” unless you actually inspected it
- **Learner-friendly** — jargon explained briefly; files tied to product behavior
- **Interview-safe** — warn when the user should say “I studied/extended this” instead of implying sole authorship

## Related

- Skill spec: [`project-quickstart/SKILL.md`](project-quickstart/SKILL.md)
- Output rubric: [`project-quickstart/references/output-rubric.md`](project-quickstart/references/output-rubric.md)
- Chinese README: [`README.zh-CN.md`](README.zh-CN.md)

## License

[MIT](LICENSE)
