# AI-Assisted Code Review

## Objective

Use an AI assistant to help identify review questions and potential defects while keeping review judgment, findings, and approval with human engineers.

## When to use

- A reviewer wants a second pass over a bounded pull request diff.
- The change has complex logic or broad context where a structured review prompt may surface useful questions.

## Preconditions

- A human reviewer understands the change's purpose and has access to the relevant repository context.
- The tool and data handling policy permits the code and context to be shared with the chosen assistant.
- The pull request has a description, scope, and relevant acceptance criteria or design notes.

## Execution steps

1. Review the pull request description and diff yourself to understand intended behavior and high-risk areas.
2. Remove or avoid sending secrets, credentials, personal data, and restricted code or context to an unapproved tool.
3. Ask the assistant to identify concrete correctness, security, reliability, compatibility, or test gaps in the supplied diff. Request file and line references and uncertainty for each claim.
4. Check each suggestion against the code, tests, specifications, and runtime behavior. Discard unsupported or stylistic noise.
5. Reproduce or otherwise verify plausible findings. Add only actionable, human-validated comments to the review.
6. Record use of AI assistance if required by team policy and complete the normal human review and approval process.

## Constraints

- AI output is advisory and can be wrong, incomplete, or outdated; it is not evidence by itself.
- Do not paste protected data or source code into a service that is not approved for that data.
- Do not let the assistant approve, merge, or make the final risk decision on behalf of a responsible human.
- Keep prompts scoped to the change and provide only the context needed for review.

## Critical events

- Stop and follow policy if sensitive information is disclosed to an unapproved tool.
- Escalate a plausible security or data integrity finding through the team's review process and verify it before presenting it as fact.
- Record material disagreements between assistant suggestions and verified behavior when they affect the review decision.

## Verification

- Independently validate every finding before adding it to the pull request.
- Confirm review coverage against the change's intended behavior, tests, and project-specific requirements.
- Ensure a qualified human reviewer makes the final approval decision.

## Expected output

- A standard human review informed, where useful, by validated AI suggestions.
- Actionable findings with evidence, or no additional findings after human verification.
