from lib.grammer_stats import GrammarStats

"""
Given a sentence starting with a capitol letter and ending in a fullstop it returns true
"""
def test_with_valid_sentance():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello world.")
    assert result == True

"""
Given a sentance starting with a capitol letter but no full stop or other mark it returns false
"""
def test_with_capitol_but_no_ending_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello world")
    assert result == False

"""
Given a sentance starting with a capitol letter and ending with a question mark it returns true
"""
def test_with_capitol_and_ending_with_question_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Is it raining?")
    assert result == True

"""
Given a sentance starting with a capitol and ends with a comma it returns false
"""
def test_with_capitol_but_ending_with_comma():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello world,")
    assert result == False

"""
Given a sentance starting with no capitol letter but a full stop it returns false
"""
def test_with_no_capitol_but_ending_with_fullstop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello world.")
    assert result == False

"""
Given one text with that passes the #check 
returns 100
"""
def test_with_one_pass():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello world.")
    result = grammar_stats.percentage_good()
    assert result == 100

"""
Given one text with fails the #check 
returns 0
"""
def test_with_one_text_one_fail():
    grammar_stats = GrammarStats()
    grammar_stats.check("hello world.")
    result = grammar_stats.percentage_good()
    assert result == 0

"""
Given two texts with one passing & one failing the #check 
returns 50
"""
def test_with_two_texts_one_failing():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello world.")
    grammar_stats.check("hello world.")
    result = grammar_stats.percentage_good()
    assert result == 50

"""
Given three texts with one passing & two failing the #check 
returns 33
"""
def test_with_three_texts_one_passing_two_failing():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello world.")
    grammar_stats.check("hello world.")
    grammar_stats.check("Hello world,")
    result = grammar_stats.percentage_good()
    assert result == 33

"""
Given three texts with one passing & two failing the #check 
returns 33
"""
def test_with_three_texts_one_passing_tw_failing():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello world.")
    grammar_stats.check("Passing sentence!")
    grammar_stats.check("Another one?")
    grammar_stats.check("ello world.")
    grammar_stats.check("Hello world,")
    result = grammar_stats.percentage_good()
    assert result == 60