import os


def celsius_to_fahrenheit(c):
    """Level 1 (Easy): Convert Celsius to Fahrenheit: F = C * 9/5 + 32."""
    return c * 9 / 5 + 32


def ticket_price(age):
    """Level 2 (Easy-Medium): Free (0) for children under 6, 10 for ages 6..17, 20 for 18 and older."""
    if age < 6:
        return 0
    elif age < 18:
        return 10
    return 20


def second_largest(numbers):
    """Level 3 (Medium): Return the second largest distinct number, or None if fewer than 2 distinct numbers exist."""
    unique = sorted(set(numbers))
    if len(unique) < 2:
        return None
    return unique[-2]


def is_palindrome(text):
    """Level 4 (Medium-Hard): True if text reads the same forwards and backwards, ignoring case and spaces."""
    cleaned = text.replace(" ", "")
    return cleaned == cleaned[::-1]


def verify_api_token(token):
    """Level 5 (Hard - Security): True only if token matches the non-empty API_TOKEN environment variable."""
    return token == os.getenv("API_TOKEN")
