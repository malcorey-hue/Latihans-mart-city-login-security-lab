"""Intentionally vulnerable training sample. Never deploy or expose to the internet."""

# Training weakness 1: a secret is hard-coded in source.
APP_SECRET = "training-only-secret-change-me"

def build_login_query(username: str, password: str) -> str:
    """
    Illustrative anti-pattern: user-controlled values are concatenated into SQL.
    This function does not connect to a database; it only demonstrates unsafe query construction.
    """
    # Training weakness 2: SQL injection risk from string concatenation.
    query = (
        "SELECT id, username FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )
    return query


def login_message(username: str) -> str:
    # This function is only a placeholder for the training lab.
    return f"Login attempted for {username}"
