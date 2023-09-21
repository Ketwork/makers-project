from lib.reading_time import estimated_reading_time
import pytest
"""
Given a text of 200 words it will return 1 
"""
def test_with_two_hundred_words():
    result = estimated_reading_time("""
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten""") 
    assert result == 1.0

"""
Given a text of 400 words it will return 2 
"""
def test_with_four_hundred_words():
    result = estimated_reading_time("""
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten""") 
    assert result == 2.0

"""
Given a text of 300 words it will return 1 
"""
def test_with_three_hundred_words():
    result = estimated_reading_time("""
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten
                                one two three four five six seven eight nine ten""") 
    assert result == 1.5

"""
Given an empty text it will raise an error
"""
def test_with_empty_string():
    with pytest.raises(Exception) as e:
        estimated_reading_time("")
    error_message = str(e.value)
    assert error_message == "can't estimate reading time for empty text."
