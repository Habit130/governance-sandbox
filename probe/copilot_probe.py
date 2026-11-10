"""Fixture for a review probe. Never merge."""

GREETING = "I am a teapot"


def greeting() -> str:
    """Return the probe greeting."""
    return GREETING
