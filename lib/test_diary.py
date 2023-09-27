from lib.diary import Diary

"""
Initially has an empty list of string
"""
def test_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []

"""
Initially, word count is zero
"""
def tests_initially_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0