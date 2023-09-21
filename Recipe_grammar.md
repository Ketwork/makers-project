# {{PROBLEM}} Function Design Recipe



## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

note: assuming its one sentance

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def reading time(text):
    """improve my grammar

    Parameters: (list all parameters and their types)
        text: a string representing the text

    Returns: (state the return value and its type)
        boolean true if valid, false otherwise

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a sentance starting with a capitol letter and ending in a fullstop it returns true
"""
check_sentance_grammar("Hello world.")
# => True

"""
Given a sentance starting with a capitol letter and ending with a question mark it returns true
"""
check_sentance_grammar("Is it raining?")
# => True

"""
Given a sentance starting with a capitol letter but no full stop or other mark it returns false
"""
check_sentance_grammar("Hello world")
# => False

"""
Given a sentance starting with a capitol and ends with a comma it returns false
"""
check_sentance_grammar("Hello world,")
# => False

"""
Given a sentance starting with no capitol letter but a full stop it returns false
"""
check_sentance_grammar("hello world.")
# => False


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!
