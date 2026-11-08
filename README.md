# AI Engineering Playbooks

Practical, reusable workflows for engineering teams building and maintaining AI enabled products. This is a documentation first portfolio of playbooks and templates, not a software platform or execution engine.

The playbooks are human authored and intended for human review. Adapt them to your team's architecture, risk level, and definition of done before using them.

## Playbooks

| Playbook | Use it for |
| --- | --- |
| [Feature Development](playbooks/feature-development.md) | Taking a scoped product change from requirements through delivery |
| [Bug Investigation](playbooks/bug-investigation.md) | Reproducing, diagnosing, fixing, and preventing a defect |
| [FastAPI Endpoint Design](playbooks/fastapi-endpoint-design.md) | Designing and implementing a typed HTTP endpoint in a FastAPI service |
| [PostgreSQL Migrations](playbooks/postgresql-migrations.md) | Making safe, reviewable schema and data changes |
| [React API Integration](playbooks/react-api-integration.md) | Connecting a React user interface to an HTTP API |
| [AI-Assisted Code Review](playbooks/ai-assisted-code-review.md) | Using an AI assistant to support a human code review |

## Start here

1. Choose the playbook that matches the work.
2. Check its preconditions and constraints; adapt steps to local conventions.
3. Record decisions, critical events, and verification evidence in the relevant issue or pull request.
4. Review the expected output with the responsible engineer before considering the work complete.

Use [PLAYBOOK_TEMPLATE.md](PLAYBOOK_TEMPLATE.md) to create a playbook. See the [worked feature development example](examples/feature-development.md) for a filled-in instance. For repository changes, read [CONTRIBUTING.md](CONTRIBUTING.md).

## Local validation

The validator checks that each Markdown file directly under `playbooks/` contains all required sections. It uses only Python's standard library.

```bash
python3 scripts/validate_playbooks.py
```

GitHub Actions runs the same check when playbooks, the validator, or its workflow change.

## Scope

This repository contains engineering guidance and a small documentation validator. It does not provide an application, backend, frontend, database, agent runtime, or AI generation engine.
