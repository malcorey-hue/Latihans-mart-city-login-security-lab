# Smart City Login Security Lab (Intentionally Vulnerable)

This is a small, local-only training project for learning defensive code review.
It intentionally contains security weaknesses. Do not deploy it, expose it to the internet,
or use real credentials or data.

## Training objectives
- Identify SQL injection risk in the login query.
- Identify unsafe secret handling.
- Practice writing findings with severity, impact, and remediation.

## Run locally (optional)
This is an illustrative Python file and does not require a database to review.
You can inspect `src/app.py` directly.

## Run a Codex Security scan
1. Put this folder in a Git repository you control (a private practice repository is fine).
2. Open Codex Security and choose **Run a Codex Security scan on this repository**.
3. Select the practice repository and start the scan.
4. Review the findings. Treat them as candidates to validate, not as unquestionable facts.
5. Ask for each finding: evidence, attack preconditions, impact, severity rationale, and a minimal fix.
6. Do not deploy this intentionally vulnerable sample.

## Expected learning points
- User input is concatenated into a SQL statement.
- A credential-like secret is hard-coded in source.
- The sample lacks robust authentication protections and is not production-ready.

## Suggested prompt after the scan
"Review each finding against the code. For each one, show the exact evidence, explain realistic exploitability and impact, assign severity with rationale, and recommend the smallest safe remediation. Separate confirmed issues from potential issues."
