---
name: project-quickstart
description: Load when the user wants fast orientation to an unfamiliar software repo for interviews, resumes, coursework, onboarding, contribution prep, or asks what files to read first, how to explain the project, architecture, data flow, tech stack, or project story.
---

# Project Quickstart

Help learners, job seekers, and students build a usable mental model of an unfamiliar codebase quickly, then turn that understanding into interview-ready or study-ready material.

## Core Workflow

1. Clarify the goal only when needed: interview prep, class learning, contribution, portfolio write-up, bug fixing, or general onboarding. If the goal is obvious from the user request, proceed.
2. Inspect the repository before explaining. Start with README/docs, dependency manifests, package scripts, entry points, route definitions, data models, tests, and recent git context.
3. Use `scripts/repo_snapshot.py <repo>` when a local repository is available and a quick structural scan would save time. Treat its output as a map, not ground truth.
4. Keep an evidence trail: for important claims, know which file, command, or observed behavior supports them.
5. Build the explanation from user-facing behavior inward: what the project does, how to run it, main features, architecture, data flow, important files, and where to read next.
6. Include useful visuals when the output format supports Markdown: at least one Mermaid architecture or flow diagram for polished project guides.
7. Keep the tone learner-friendly. Explain jargon briefly, connect files to product behavior, and separate confirmed facts from hypotheses.
8. Finish with concrete next actions: the 3-5 files to read first, commands to try, small exercises, likely interview questions, or contribution ideas.

## Output Shape

Default to the user's language. For Chinese requests, answer in Chinese unless the user asks otherwise.

Use this compact structure unless the user asks for another format:

- Project in one sentence
- How to run or inspect it
- Architecture map with file references
- Mermaid architecture or core-flow diagram when useful
- Main feature/data flow
- Tech stack and why it likely exists
- Evidence map for key claims
- Strengths, risks, and improvement opportunities
- What to study first
- Interview or resume talking points when relevant
- Verification status: commands/tests run, commands/tests not run, uncertainties, and what would confirm them

Read `references/output-rubric.md` when producing a polished project brief, study plan, review report, or interview-prep answer. Use `assets/project-brief-template.md` when the user asks for a reusable template or file-style deliverable.

## Interview Mode

When the user mentions resumes, interviews, school projects, internships, campus recruiting, portfolio review, or how to explain the project:

- Translate code facts into a credible project story without exaggerating ownership.
- Include 30-second, 1-minute, and 3-minute pitch options when the user wants interview prep or resume polish.
- Include technical highlights, tradeoffs, hard parts, and likely follow-up questions.
- Warn when the user should say "I studied/extended this project" instead of implying they built the whole thing.
- Prefer evidence-backed claims with file paths, commands, and observed behavior.

## Gotchas

- Do not pretend to understand modules that were not inspected. Mark them as "likely" or "not yet verified".
- Do not say "fully analyzed" unless enough source, config, tests, and runtime paths were actually inspected.
- Do not over-index on README claims if code disagrees; mention the mismatch.
- Do not load this skill for pure formatting, dependency installation, one-off syntax fixes, or general debugging unless the user also wants project understanding.
- Do not run network installs or destructive commands just to understand a project. If execution requires missing dependencies, explain the blocker and continue static analysis.
- For large monorepos, sample intentionally: identify packages/apps, choose the relevant app, and state what was left out.
- Do not generate Mermaid diagrams with unescaped parentheses, colons, or brackets inside node ids. Put human text in quoted labels.
