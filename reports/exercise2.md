# Bug reports for exercise2.py

Line: 13
Problem: The logic in the clamp function is incorrect. It uses `max(low, min(x, low))`, which simplifies to `max(low, low)` because `min(x, low)` will always be at most `low`. This means the function will always return `low`, regardless of the value of `x`. The correct behavior should be to return `max(low, min(x, high))` to clamp `x` between `low` and `high`.
Example: clamp(10, 5, 15) should return 10, but currently returns 5.
Fix: Line 13: `return max(low, min(x, high))`
