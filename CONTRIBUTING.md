# Contributing

Contributions should make the playbooks more useful to engineering teams through practical, clear, and reviewable guidance. This repository is human authored and human reviewed. AI tools may assist drafting, but a person must verify and own every contribution.

## Before contributing

- Open an issue or discussion for a substantial new playbook or a change that affects several workflows.
- Prefer actionable steps and observable verification over broad principles alone.
- Keep guidance framework-aware when relevant, while identifying assumptions and version-sensitive details.
- Do not include secrets, private customer information, or proprietary material.

## Adding or editing a playbook

1. Use [PLAYBOOK_TEMPLATE.md](PLAYBOOK_TEMPLATE.md) as the starting point.
2. Keep all eight required sections and use their headings as written: Objective, When to use, Preconditions, Execution steps, Constraints, Critical events, Verification, and Expected output.
3. Use numbered steps in execution order. Make constraints and critical events concrete enough to guide action or escalation.
4. Add a worked example under `examples/` when it materially helps a reader apply the workflow.
5. Add the playbook to the README navigation.
6. Run `python3 scripts/validate_playbooks.py` and address any reported missing sections.

## Review expectations

- A human author is responsible for factual accuracy, clarity, and appropriate scope.
- Reviewers should check safety and privacy implications, internal consistency, applicability, and whether verification is actionable.
- AI-generated suggestions are not accepted without human validation.
- Pull requests should explain the audience, purpose, and any assumptions or tradeoffs.
