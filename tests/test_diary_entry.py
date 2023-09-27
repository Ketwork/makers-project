from lib.diary_entry import DiaryEntry
import pytest

"""
given an empty title and contents
Raises an error

"""
def test_errors_on_empty_string_and_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "")
    assert str(err.value) == "Diary entries must have a title or contents"

"""
given a title and contents
#format returns a formatted entry, like:
"my Title: These are the contents"
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

"""
when I initialise with a title and contents
I can get that title and contents back
"""
def tests_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry._title == "My Title"
    assert diary_entry._contents == "My Contents"


# """
# given a title and contents
# #count_words returns the number of words in the title and contents
# """
# def tests_counts_words_in_both_title_and_contents():
#     diary_entry = DiaryEntry("My Title", "Some contents")
#     result = diary_entry.count_words()
#     assert result == 4

"""
When I initialise with a five-word contents
#count_words should return five
"""
def tests_counts_words_returns_word_count_of_contents():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    result = diary_entry.count_words()
    assert result == 5

"""
given wpm of 2
And a text with 2 words
#reading_time returns 1 minute
"""
def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
given wpm of 2
And a text with 4 words
#reading_time returns 2 minute
"""
def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntry("My Title", "Some contents three four")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
given wpm of 2
And a text with 3 words
#reading_time returns 2 minute
"""
def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "Some contents three")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
given wpm of 0
reading_time raises and error
"""
def test_errors_on_wpm_of_0():
    diary_entry = DiaryEntry("My Title", "Some contents")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Cannot calculate reading time with wpm of 0"

"""
Given a contents of six words
given wpm of 2
And a minutes of 1
#reading_chunk returns the first two words
"""

def test_reading_chunk_with_two_wpm_and_one_minute():
    diary_entry = DiaryEntry("My Title", "Some contents three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Some contents"

"""
Given a contents of six words
given wpm of 2
And a minutes of 2
#reading_chunk returns the first two words
"""

def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry("My Title", "Some contents three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "Some contents three four"

"""
Given a contents of six words
given wpm of 2 and a minutes of 1
first #reading_chunk returns the first two words
next time, "three four
"""
def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"

"""
When I initialise with a five-word contents
Then, on the third call, #reading_chunk should return the final, partial chunk
"""
def test_readable_chunk_third_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "five"

"""
When I initialise with a five-word contents
Then, on the fouth call, #reading_chunk should start again from the beginning
"""
def test_readable_chunk_fouth_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"

"""
When I initialise with a six-word contents
Then, on the fouth call, #reading_chunk should start again from the beginning
"""
def test_readable_chunk_fouth_chunk_with_exact_chunks():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"