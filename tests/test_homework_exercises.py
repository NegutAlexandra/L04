import os
import sqlite3
import subprocess

import pytest

import homework_exercises
from homework_exercises import *


# bug report 1
def test_r1_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212.0


# bug report 2
def test_r2_ticket_price_age_18():
    assert ticket_price(18) == 20


# bug report 3
def test_r3_second_largest_edge_cases():
    # Test case with one unique value
    assert second_largest([5]) is None
    
    # Test case with empty list
    assert second_largest([]) is None
    
    # Test case with two identical values (only one unique value)
    assert second_largest([3, 3]) is None
    
    # Test case with two distinct values (should return the smaller one)
    assert second_largest([1, 5]) == 1
    
    # Test case with more than two distinct values
    assert second_largest([1, 2, 3, 4]) == 3


# bug report 4
def test_r4_verify_api_token():
    os.environ["API_TOKEN"] = "my-token"
    assert verify_api_token("my-token") is True
    assert verify_api_token("super-secret-token-2026") is False
