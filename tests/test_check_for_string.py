from lib.check_for_string import check_text_for_string

"""
Given a text that contains the string #TODO
It returns true
"""
def test_with_text_that_contains_correct_string():
    result = check_text_for_string("#TODO get milk") 
    assert result == True

"""
Given a text that does not contains the string #TODO
It returns false
"""
def test_with_text_that_does_not_contains_string():
    result = check_text_for_string("get milk") 
    assert result == False

"""
Given a text that contains the string TODO without the hashtag
It returns false
"""
def test_with_text_that_does_not_contain_hashtag_before_TODO():
    result = check_text_for_string("TODO get milk") 
    assert result == False

"""
Given a text that contains the string TODO with wrong case
It returns false
"""
def test_with_text_that_contains_wrong_TODO_case():
    result = check_text_for_string("#TOdO get milk") 
    assert result == False

"""
Given an empty string
It returns false
"""
def test_with_empty_string():
    result = check_text_for_string("") 
    assert result == False