# React API Integration

## Objective

Connect a React interface to an HTTP API with clear data boundaries, responsive state handling, and accessible user feedback.

## When to use

- Adding a screen or interaction that reads from or writes to an API.
- Replacing mocked data with a service integration or changing an existing API flow.

## Preconditions

- The API contract, authentication approach, and expected failure responses are understood.
- The application’s React version, routing, data-fetching conventions, and design system are known.
- Loading, empty, error, and success behavior can be described for the user flow.

## Execution steps

1. Identify the user action and data needed. Confirm the API contract and whether generated or shared types are available.
2. Use the existing API client or data-fetching library; centralize request behavior according to project conventions.
3. Model loading, success, empty, and error states explicitly. Keep server state distinct from local presentation state where practical.
4. Handle cancellation or stale responses when navigation or changing inputs can make a request obsolete.
5. Present errors in understandable language, preserve user input when appropriate, and provide a safe retry path where useful.
6. Make interactive controls and status feedback keyboard accessible and compatible with the application's accessibility patterns.
7. Add tests for the primary flow and important loading, empty, failure, and interaction states.

## Constraints

- Do not put secrets in client code or expose data beyond the user's authorization.
- Follow the API's pagination, caching, retry, and rate-limit behavior; avoid uncontrolled duplicate requests.
- Keep components aligned with existing conventions and avoid adding a new state library for a single integration.
- Do not treat client validation as a substitute for server-side validation.

## Critical events

- Escalate a mismatch between frontend assumptions and the API contract before relying on undocumented behavior.
- Record changes to authentication, sensitive data display, or user-facing error behavior for review.
- Surface outages or persistent API failures through the team's support and telemetry path without logging sensitive payloads.

## Verification

- Check success, loading, empty, error, and retry behavior with representative responses.
- Verify keyboard interaction, focus behavior, and accessible status announcements where applicable.
- Run relevant component or integration checks and inspect browser console and network behavior.

## Expected output

- A reviewed React integration that follows the API and application conventions.
- Automated coverage for key states and a user experience that communicates progress and failure clearly.
