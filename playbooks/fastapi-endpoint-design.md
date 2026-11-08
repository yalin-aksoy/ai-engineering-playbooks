# FastAPI Endpoint Design

## Objective

Design an HTTP endpoint in a FastAPI service with a clear contract, validated inputs, predictable errors, and maintainable boundaries.

## When to use

- Adding a new endpoint or materially changing an existing endpoint in a FastAPI application.
- Reviewing endpoint contract, dependency, or response behavior before implementation.

## Preconditions

- The user or service need and expected endpoint behavior are understood.
- Existing API conventions, authentication model, and error format have been inspected.
- Data ownership and any required persistence or downstream service dependencies are known.

## Execution steps

1. Define the method, path, request and response schemas, status codes, and authorization requirements.
2. Check for an existing endpoint or contract that should be extended rather than duplicated.
3. Model request and response data with explicit Pydantic schemas and suitable validation constraints.
4. Implement the route with appropriate dependency injection for authentication, services, and resources; keep business logic outside the route handler where project conventions support it.
5. Map known domain failures to the service's established HTTP error responses. Avoid leaking internals in client-facing errors.
6. Document behavior, examples, and compatibility expectations in the API schema or supporting docs.
7. Add tests for the success path, validation failures, authorization, and relevant domain errors.

## Constraints

- Follow the service's supported Python, FastAPI, and Pydantic versions and established routing conventions.
- Do not expose internal models, secrets, stack traces, or fields the caller is not authorized to see.
- Avoid blocking work in async handlers unless the service's design explicitly supports it.
- Treat changes to public request or response fields as contract changes and assess compatibility.

## Critical events

- Record breaking contract changes and obtain the required API owner approval before release.
- Escalate changes to authentication, authorization, sensitive fields, or rate limits for appropriate review.
- Document new external dependencies and their failure behavior.

## Verification

- Verify OpenAPI output reflects the intended request, response, and error schemas.
- Exercise valid and invalid requests, authorization boundaries, and expected status codes.
- Run relevant unit and API tests and check that errors do not reveal internal details.

## Expected output

- An endpoint implementation with an explicit API contract, documented behavior, and relevant automated coverage.
- A pull request recording compatibility and operational considerations.
