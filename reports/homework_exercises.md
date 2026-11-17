# Bug reports for homework_exercises.py

Line: 6  
Problem: The formula for converting Celsius to Fahrenheit is incorrectly implemented. The correct formula is F = C * 9/5 + 32, but the code uses c * 5 / 9 + 32, which is the inverse (Fahrenheit to Celsius).  
Example: celsius_to_fahrenheit(0) returns 32.0 (incorrect), but should return 32.0 (correctly, by coincidence), but for 100°C, it returns 54.0 (wrong), while the correct value is 212°F.  
Fix: Line 6 should be `return c * 9 / 5 + 32`

Line: 13  
Problem: The condition `elif age <= 18` includes age 18, which should be in the 20-dollar category. The logic states that 18 and older are 20, so ages 6–17 are 10, and 18+ are 20. Therefore, age 18 should not be in the 10-dollar group.  
Example: ticket_price(18) returns 10, but should return 20.  
Fix: Change line 13 to `elif age < 18:`

Line: 21  
Problem: The function `second_largest` returns `unique[-2]` which will raise an `IndexError` if there are fewer than 2 distinct numbers (e.g., list with one unique value or empty). The docstring says "return None if fewer than 2 distinct numbers exist", but the current code does not handle this case.  
Example: second_largest([5]) returns `unique[-2]` which fails because `unique` has only one element.  
Fix: Add a check before accessing index -2:  
Change line 21 to:  
`if len(unique) < 2: return None`  
Then: `return unique[-2]`

Line: 32  
Problem: The function `verify_api_token` uses a hardcoded secret token (`SECRET_TOKEN = "super-secret-token-2026"`) instead of reading from the environment variable `API_TOKEN`. This violates the security requirement that it should only match the environment variable.  
Example: If the environment variable is set to "my-token", the function will return `False` for any token, including the hardcoded one — it fails to use the actual environment variable.  
Fix: Replace line 32 with: `return token == os.getenv("API_TOKEN")`  
(Note: The function should also ensure that `API_TOKEN` is not empty, which is already implied by the requirement "non-empty".)
