"""A tiny greeting package with a contributing guide."""


def greet(name: str) -> str:
    """Return a greeting; a blank name greets the world."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
