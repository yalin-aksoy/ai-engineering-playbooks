# Feature Development

## Objective

Deliver a bounded product change that meets an agreed user need, fits the existing architecture, and has reviewable evidence of correctness.

## When to use

- A feature or product improvement has been prioritized and needs implementation.
- A change crosses code, tests, documentation, or operational behavior and needs a shared delivery path.

## Preconditions

- A product owner or requester can explain the user problem and desired outcome.
- An engineer has identified the relevant repository, ownership, and development conventions.
- Scope, dependencies, and acceptance criteria are clear enough to estimate and review.

## Execution steps

1. Write the user problem, intended outcome, acceptance criteria, and explicit exclusions in the issue.
2. Inspect the existing implementation and identify the smallest design that meets the criteria. Record consequential design choices and dependencies.
3. Break the work into reviewable changes. Identify data, API, security, accessibility, and rollout impacts where relevant.
4. Implement the change using established repository patterns. Keep unrelated cleanup out of scope.
5. Add or update automated checks and user or operator documentation appropriate to the behavior.
6. Review the diff against each acceptance criterion. Request domain or security review when the change warrants it.
7. Prepare a pull request that summarizes behavior, tradeoffs, verification evidence, and any rollout or follow-up work.

## Constraints

- Do not expand scope without updating acceptance criteria and communicating the impact.
- Preserve existing contracts unless a breaking change has been explicitly approved and planned.
- Do not place secrets or sensitive user data in code, logs, fixtures, or review artifacts.
- Follow the team's release, accessibility, security, and data-handling requirements.

## Critical events

- Record unresolved ambiguity, a material scope change, or a dependency that changes the delivery plan.
- Escalate a security, privacy, data-loss, or compatibility concern before merging.
- Document any accepted risk, migration, feature flag, or staged rollout decision in the issue or pull request.

## Verification

- Map each acceptance criterion to a test, inspection, or other observable evidence.
- Run the repository's relevant checks and report commands and outcomes in the pull request.
- Confirm the change has been reviewed by the required code owners and stakeholders.
- Check that documentation and rollout instructions match the delivered behavior.

## Expected output

- A reviewed pull request that satisfies agreed acceptance criteria.
- Tests or other verification evidence, updated documentation where needed, and recorded rollout or follow-up actions.
