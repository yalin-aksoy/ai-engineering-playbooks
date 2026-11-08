# Bug Investigation

## Objective

Identify the cause of a defect, restore expected behavior with a bounded fix, and reduce the chance of recurrence.

## When to use

- A user-visible behavior differs from the documented or accepted behavior.
- An alert, support report, or regression indicates a failure that needs diagnosis.

## Preconditions

- The reported symptom, affected area, and approximate time or version are known where possible.
- The investigator can access relevant code and approved diagnostic information.
- For an active incident, an incident lead and communication path are established.

## Execution steps

1. Capture the observed behavior, expected behavior, impact, affected versions, and a safe reproduction path.
2. Triage severity and scope. For active production impact, follow incident procedures and prioritize mitigation.
3. Reproduce the issue in a suitable environment. Minimize the reproduction and preserve useful evidence without exposing sensitive data.
4. Trace the behavior through recent changes, boundaries, inputs, and relevant telemetry. Form and test one hypothesis at a time.
5. Identify the root cause and choose the smallest safe fix. Consider whether data repair, rollback, or compatibility handling is needed.
6. Add a regression check that would fail before the fix, then implement the correction.
7. Review and verify the change, deploy or release using the team's process, and monitor the affected behavior.
8. Record cause, impact, fix, and any preventive follow-up in the issue or incident record.

## Constraints

- Do not use production data or credentials outside approved access and handling procedures.
- Avoid speculative changes that obscure the cause or combine unrelated fixes.
- During an incident, follow the incident lead's prioritization and communication process.

## Critical events

- Escalate suspected security exposure, data corruption, or broad customer impact immediately through the incident process.
- Record when evidence rules out an initial hypothesis or changes severity assessment.
- Document any mitigation that changes user behavior, data, or service availability.

## Verification

- Confirm the reproduction no longer occurs with the fix and the regression check covers it.
- Run relevant tests and inspect logs or metrics for the affected path after release when appropriate.
- Confirm no unintended behavior changes in adjacent flows.

## Expected output

- A defect record with reproduction details, impact, root cause, and resolution.
- A reviewed fix with regression coverage and recorded release or monitoring follow-up.
