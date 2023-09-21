from lib.check_sentance_grammar import *


"""
Given a sentance starting with a capitol letter and ending in a fullstop it returns true
"""

def test_with_valid_sentance():
    result = check_sentance_grammar("Hello world.")
    assert result == True

"""
Given a sentance starting with a capitol letter but no full stop or other mark it returns false
"""
def test_with_capitol_but_no_ending_mark():
    result = check_sentance_grammar("Hello world")
    assert result == False

"""
Given a sentance starting with a capitol letter and ending with a question mark it returns true
"""
def test_with_capitol_and_ending_with_question_mark():
    result = check_sentance_grammar("Is it raining?")
    assert result == True

"""
Given a sentance starting with a capitol and ends with a comma it returns false
"""
def test_with_capitol_but_ending_with_comma():
    result = check_sentance_grammar("Hello world,")
    assert result == False

"""
Given a sentance starting with no capitol letter but a full stop it returns false
"""
def test_with_no_capitol_but_ending_with_fullstop():
    result = check_sentance_grammar("hello world.")
    assert result == False