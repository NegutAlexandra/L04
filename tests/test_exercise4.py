import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin():
    # Test with correct admin password
    assert check_admin("admin123") == True
    
    # Test with wrong password (should return False)
    assert check_admin("wrong") == False


# bug report 2
def test_r2_sql_injection_vulnerability():
    import sqlite3
    import pytest
    
    # Create an in-memory database
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, email TEXT)")
    db.execute("INSERT INTO users VALUES ('ana', 'ana@mail.com')")
    db.commit()
    
    # Test with SQL injection payload
    vulnerable_username = "' OR '1'='1'"
    result = find_user(db, vulnerable_username)
    
    # The bug causes this to return a row even if no user exists
    # This is a vulnerability - it should return None
    assert result is None
