# Bug reports for exercise3.py

Line: 3
Problem: The function `average(numbers)` will raise a `ZeroDivisionError` when the input list is empty because `len(numbers)` will be 0, and dividing by zero is undefined. The docstring states that an empty list has an average of 0, but the current code does not handle this edge case.
Example: average([]) → raises ZeroDivisionError, but should return 0
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The function `first_word(text)` will raise an `IndexError` when the input text is empty (or contains only whitespace), because `text.split()[0]` will access the first element of an empty list after splitting. The docstring states that it should return "" in such cases.
Example: first_word("") → raises IndexError, but should return ""
Fix: return text.split()[0] if text.strip() else ""

Line: 12
Problem: The function `percent(part, total)` will raise a `ZeroDivisionError` when `total` is 0, even though the docstring says the result should be 0. The current code does not handle this edge case.
Example: percent(5, 0) → raises ZeroDivisionError, but should return 0
Fix: return part / total * 100 if total != 0 else 0
