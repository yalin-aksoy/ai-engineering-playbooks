# Worked Example: Add a Saved Search Filter

This example shows how a team might apply the [Feature Development playbook](../playbooks/feature-development.md). Names and acceptance criteria are illustrative; adapt them to the product and repository.

## Objective

Let signed-in support analysts save a named filter for the incident list and restore it later, reducing repeated manual filter setup.

## When to use

- The product team has prioritized saved filters for the incident list.
- The work spans the existing web interface and its API, and needs a coordinated implementation plan.

## Preconditions

- Product has agreed that the first release supports up to ten saved filters per analyst.
- A saved filter consists of a name and the supported incident-list filter fields; sort order is excluded from the first release.
- The team has identified the incident list UI, its existing filter API, and the persistence owner.
- Acceptance criteria are recorded in the issue.

## Execution steps

1. Confirm acceptance criteria: an analyst can save a valid named filter, see their saved filters, apply one to the list, rename it, and delete it. Names are unique per analyst after trimming and case normalization.
2. Inspect the existing filter model and API. Agree on a per-user persistence model and API contract with the owning team; avoid storing filters in browser local storage because they must follow the analyst across devices.
3. Split implementation into contract and persistence, UI controls and states, and documentation and rollout. Keep sort order and shared team filters out of scope.
4. Implement validation for name length, allowed filter fields, and the per-user limit. Apply existing authorization patterns so analysts can only access their own saved filters.
5. Add UI for listing, saving, applying, renaming, and deleting filters. Include loading, empty, error, and confirmation behavior consistent with the design system.
6. Add API and UI coverage for normal operations, duplicate names, limit reached, unauthorized access, invalid filters, and API failures.
7. Review the pull request against each criterion, deploy behind the team's normal release process, and monitor endpoint errors and support feedback after release.

## Constraints

- Persist filter definitions only; do not snapshot incident records or include sensitive incident content in the saved-filter object.
- Enforce ownership on the server, even if the interface only displays the current analyst's filters.
- Keep the initial release limited to ten filters per analyst and supported filter fields.
- Preserve existing incident-list behavior for users who do not save or apply a filter.

## Critical events

- The API owner flags that an existing filter field contains sensitive values; pause and review the data model and authorization implications.
- A database migration is needed; apply the PostgreSQL Migrations playbook and coordinate rollout compatibility.
- If the API contract cannot support rename or deletion safely, record the limitation and agree scope before implementation continues.

## Verification

- Verify all acceptance criteria with API and UI checks, including ownership and invalid input cases.
- Confirm analysts cannot read, modify, or delete another user's saved filter by changing a client-supplied identifier.
- Confirm the incident list remains usable when saved-filter requests fail.
- Review analytics and logs to ensure they do not capture filter contents if those contents may be sensitive.
- In the pull request, report the relevant checks, results, and deployment considerations.

## Expected output

- A reviewed feature change that lets an analyst manage and apply their own saved filters.
- Automated coverage, updated usage guidance, and a recorded rollout plan with the persistence and authorization decisions.
