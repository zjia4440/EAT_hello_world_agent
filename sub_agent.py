"""Functions used by the main agent."""


def answer_agent() -> str:
    """Return the required Hello World answer."""
    return "Hello, world!"


def validate_agent(answer: str) -> str:
    """Check whether the answer is exactly the required response."""
    if answer == "Hello, world!":
        return "VALID"
    return f"INVALID: expected 'Hello, world!', received {answer!r}."
