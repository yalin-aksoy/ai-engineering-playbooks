# PostgreSQL Migrations

## Objective

Change PostgreSQL schema or data safely with a migration that is reviewable, deployable, and compatible with the application's rollout plan.

## When to use

- Adding, changing, or removing a database object or constraint.
- Transforming stored data as part of an application change.

## Preconditions

- The target schema, affected tables, data volume, and application readers and writers are understood.
- The repository's migration tool and deployment ordering are known.
- Backup, recovery, and production change procedures are available for the environment.

## Execution steps

1. Define the desired schema or data state and identify dependent application versions and queries.
2. Assess lock behavior, runtime, table size, index strategy, nullability, and rollback or forward-repair options.
3. Prefer an expand and contract rollout for changes that must coexist with old and new application versions: add compatible structures first, migrate usage and data, then remove obsolete structures later.
4. Write the migration using the repository's migration tool and conventions. Make data transformations bounded and safe to resume where feasible.
5. Update application code and schema documentation in the rollout order required by compatibility.
6. Review the generated SQL and migration ordering. Test against representative schema and data volume where practical.
7. Apply through the approved release process, observe duration and database health, and complete any deferred contract step only when safe.

## Constraints

- Never edit an already-applied migration unless the repository's migration policy explicitly permits it.
- Avoid long blocking locks and unbounded updates on large tables; plan batching or concurrent operations where supported.
- Do not assume a migration is safely reversible. State the recovery strategy clearly.
- Follow data retention, privacy, and production access requirements.

## Critical events

- Obtain database owner or operations review for high-risk locks, large backfills, destructive changes, or extended execution.
- Stop and escalate if observed lock contention, replication lag, errors, or duration exceed agreed thresholds.
- Record the applied migration version, anomalies, and any manual recovery or follow-up action.

## Verification

- Apply migrations from a clean schema and from the supported prior schema state.
- Verify resulting schema, constraints, and representative transformed data.
- Confirm application versions involved in rollout remain compatible at each deployment stage.
- Monitor database health and migration completion in the target environment.

## Expected output

- A versioned migration and compatible application change with a documented rollout and recovery approach.
- Verification evidence and recorded deployment outcome.
