# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

class TaskTracker():
    def add_task(self, task):
        #Parameters
        #   task: string representing a tast
        pass

    def list_tasks(self):
        # Returns
        #   a list of imcomplete tasks
        pass

    def mark_complete(self):
        # Parameters
        #   index: an integer representing the tasks to complete
        # Side-effect:
        #   removes the task fromt the list of tasks 
        pass


```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Initailly there are no tasks
"""
tracker = Tracker
tracker.list_tasks() # => []

"""
When we add a task it is reflected in the list of tasks
"""
tracker = Tracker
tracker.add_task("walk the dog")
tracker.list_tasks() # => ["walk the dog"]

"""
When we add multiple task 
they are all reflected in the list of tasks
"""
tracker = Tracker
tracker.add_task("walk the dog")
tracker.add_task("walk the cat")
tracker.add_task("walk the frog")
tracker.list_tasks() # => ["walk the dog", "walk the cat", "walk the frog"]

"""
When we add multiple task 
and mark one as complete
it disapears from the task list 
"""
tracker = Tracker
tracker.add_task("walk the dog")
tracker.add_task("walk the cat")
tracker.add_task("walk the frog")
tracker.mark_complete(1)
tracker.list_tasks() # => ["walk the dog", "walk the frog"]


"""
If we try to mark a track complete that does not exist (too low)
It raises an error
"""
tracker = Tracker
tracker.add_task("walk the dog")
tracker.mark_complete(-1) #raises an error "No such task to mark complete"

"""
If we try to mark a track complete that does not exist (too high)
It raises an error
"""
tracker = Tracker
tracker.add_task("walk the dog")
tracker.mark_complete(2) #raises an error "No such task to mark complete"
tracker.list_tasks() # => ["walk the dog"]

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


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
