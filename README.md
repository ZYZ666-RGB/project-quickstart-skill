# Project Quickstart Skill

A Codex skill that helps students, job seekers, and new contributors quickly understand unfamiliar software repositories.

It guides an agent to inspect a repo, build a learner-friendly mental model, produce interview-ready talking points, and avoid overclaiming by citing evidence and verification status.

## What It Produces

- One-sentence project summary
- Architecture and core-flow explanation
- Mermaid architecture or flow diagram
- Important files to read first
- Evidence map for key claims
- Strengths, risks, and improvement opportunities
- Interview or resume talking points
- Verification status and remaining uncertainties

## Install

Clone this repository, then copy the skill folder into your Codex skills directory.

Windows PowerShell:

```powershell
git clone https://github.com/ZYZ666-RGB/project-quickstart-skill.git
$skillsDir = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $HOME ".codex\skills" }
New-Item -ItemType Directory -Force $skillsDir
Copy-Item -Recurse .\project-quickstart-skill\project-quickstart $skillsDir
```

macOS/Linux:

```bash
git clone https://github.com/ZYZ666-RGB/project-quickstart-skill.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R project-quickstart-skill/project-quickstart "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after installing the skill if it does not appear immediately.

## Usage

Explicit invocation:

```text
Use $project-quickstart to help me understand this repository and prepare an interview-ready project brief.
```

Natural-language invocation examples:

```text
Help me quickly understand this project for an interview.
```

```text
I just cloned this repo. Which files should I read first?
```

```text
Turn this project into resume-ready project experience and list the technical highlights.
```

## Included Resources

```text
project-quickstart/
├── SKILL.md
├── agents/openai.yaml
├── assets/project-brief-template.md
├── evals/routing-cases.yaml
├── references/output-rubric.md
└── scripts/repo_snapshot.py
```

## Evals

Routing and behavior cases live in:

```text
project-quickstart/evals/routing-cases.yaml
```

Use them to test positive, negative, and edge routing behavior across different orchestration models.

## License

MIT
