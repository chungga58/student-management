import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import search_students

def test_search_found():
    result = search_students("Nguyen")
    assert len(result) > 0

def test_search_not_found():
    result = search_students("XyzNonExistent")
    assert len(result) == 0

def test_search_case_insensitive():
    result_lower = search_students("nguyen")
    result_upper = search_students("NGUYEN")
    assert len(result_lower) == len(result_upper)
