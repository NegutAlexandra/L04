import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin():
    assert check_admin("admin123") == True  # Correct password
    assert check_admin("wrong") == True     # Incorrect password - should be False


# bug report 2
def test_r2_sql_injection_vulnerability():
    # Test with a username that could cause SQL injection
    username = "' OR '1'='1'"
    result = find_user(None, username)
    # The bug causes this to return a result even if no user exists
    # This is incorrect and vulnerable to SQL injection
    assert result is None, "SQL injection vulnerability: query should not return a result for malicious input"
