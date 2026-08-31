def is_palindrome(text):
    """Return True if text reads the same forwards and backwards, ignoring case and spaces."""
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]


def add(a, b):
    """Return the sum of a and b."""
    return a + b
