# Bug reports for exercise4.py

Line: 9
Problem: The condition `ADMIN_PASSWORD != ""` is always true because `ADMIN_PASSWORD` is defined as "admin123", which is a non-empty string. This check is redundant and logically incorrect — it does not validate the password correctly. The function should simply check if `password == ADMIN_PASSWORD`, not compare it against an empty string. Additionally, this condition could be misleading or cause confusion in logic flow.
Example: check_admin("admin123") returns True (correct), but check_admin("wrong") returns True (incorrect) because the condition `ADMIN_PASSWORD != ""` is always true and the actual password comparison is not performed.
Fix: return password == ADMIN_PASSWORD

Line: 14
Problem: The SQL query uses string concatenation to insert the username directly into the query without escaping. This creates a serious SQL injection vulnerability. An attacker could provide a username like `' OR '1'='1` to manipulate the query and potentially gain unauthorized access.
Example: If username is `' OR '1'='1`, the query becomes `SELECT * FROM users WHERE username = '' OR '1'='1'`, which will return a row even if no such user exists, leading to unauthorized access.
Fix: use parameterized queries instead of string formatting. Replace line 14 with: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
