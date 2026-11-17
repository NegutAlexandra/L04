import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin():
    """Test that check_admin returns True only when password matches ADMIN_PASSWORD"""
    # Assuming ADMIN_PASSWORD is set to "admin123" in environment
    os.environ["ADMIN_PASSWORD"] = "admin123"
    
    # Correct password should return True
    assert check_admin("admin123") == True
    
    # Incorrect password should return False
    assert check_admin("wrong") == False


# bug report 2
def test_r2_sql_injection_vulnerability():
    import sqlite3
    
    # Create in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    conn.execute('''CREATE TABLE users (username TEXT, email TEXT)''')
    conn.execute("INSERT INTO users VALUES ('ana', 'ana@mail.com')")
    conn.commit()
    
    # Test with SQL injection payload
    vulnerable_username = "' OR '1'='1'"
    result = find_user(conn, vulnerable_username)
    
    # The vulnerable code would return a result (not None) due to SQL injection
    # The correct fix uses parameterized queries, which should return None
    assert result is None
