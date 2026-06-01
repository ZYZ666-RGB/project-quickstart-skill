# Output Rubric

Use this reference when the user wants a polished explanation, project brief, study guide, or interview-prep answer.

## Minimum Useful Answer

- State what the project appears to do in one sentence.
- Name the main runtime stack and cite the files that prove it.
- Identify the entry point or main app/module.
- Explain one primary user or data flow from input to output.
- Include one Mermaid diagram for polished guides: architecture overview, request flow, data flow, or module dependency flow.
- Include an evidence map for important claims: claim, supporting file/command, confidence.
- Preserve a balanced evaluation: strengths, risks, and improvement opportunities.
- Give the learner a short reading path.
- State verification status: what was run, what was not run, and what remains uncertain.

## Student-Friendly Explanation

Prefer concrete phrasing:

- "This file starts the server" instead of "bootstrap layer".
- "The frontend calls this API route" instead of "client-server interaction".
- "This model/table stores users" instead of "persistence abstraction".

When a term is useful, define it once in plain language.

## Visuals

Prefer simple Mermaid diagrams over decorative diagrams. Use one diagram unless the user asks for a deep report.

Good diagram types:

- Architecture overview: user/client, API/controller, services, storage, external services.
- Main flow: upload, processing, retrieval, generation, response.
- Agent loop: planner, executor, tools, feedback.

Keep labels short. Use quoted node labels when labels contain punctuation.

## Interview-Ready Brief

Include:

- 30-second pitch: product purpose, users, and outcome.
- 1-minute pitch: add architecture and one hard technical decision.
- 3-minute pitch: add tradeoffs, risks, and improvement plan.
- Tech stack: language, framework, database, infrastructure, testing.
- Architecture: 3-6 important modules and how they talk.
- Hard parts: auth, data consistency, async work, performance, deployment, testing, UX, or state management.
- Tradeoffs: what the project chose and what could improve.
- Ownership-safe wording: "I studied", "I implemented a feature in", "I refactored", or "I can explain" as appropriate.
- Likely questions: at least five, with short answer cues.
- Verification caveat: mention when behavior was inferred from code instead of confirmed by running the app.

## Study Plan

For beginners, organize learning in passes:

1. Run/read: README, scripts, env examples, demo path.
2. Map: entry points, routes/pages, models, services, tests.
3. Trace: one feature end to end.
4. Modify: make one safe UI/text/test change.
5. Explain: summarize the architecture without looking.

## Evidence Rules

- Cite local files when making claims.
- Prefer exact commands from manifests over guessed commands.
- Mark generated inferences with "likely", "appears", or "based on".
- If tests are not run, say so.
- Avoid vague source phrases like "I fully explored the project" unless the inspection scope is stated.
- Do not present a file count as proof of correctness; pair it with the kinds of files inspected.
