from lib.personal_diary import *

# if given an empty string it returns an empty string
def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""

# for a sting with 5 words or less returns the whole string
def test_5_or_less_words():
    result = make_snippet("less than five words")
    assert result == "less than five words"

# for more than 5 words returns string + "..."
def test_more_than_five_words():
    result = make_snippet("this string has move than five words")
    assert result == "this string has move than..."