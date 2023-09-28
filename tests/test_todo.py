from lib.todo import Todo

"""
When we construct with a task
We get that task reflected in the title property
"""
def test_construct_with_a_task():
    todo = Todo("Walk the dog")
    assert todo.task == "Walk the dog"

"""
When we construct
The task is initially incomplete
"""
def test_is_initially_incomplete():
    todo = Todo("Walk the dog")
    assert todo.complete == False