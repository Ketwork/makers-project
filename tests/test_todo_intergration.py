from lib.todo import Todo
from lib.todo_list import TodoList

"""
Given I add todo entries 
I see them back in the incomplete list
"""
def test_adds_and_lists_todo_entries():
    todo_list = TodoList()
    todo1 = Todo("Finish coding project")
    todo2 = Todo("Buy groceries")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1, todo2]

"""
Given I add todo entries that have not been completed
I see an empty list in completed
"""
def test_adds_and_lists_todo_entries_and_checks_complete_list():
    todo_list = TodoList()
    todo1 = Todo("Finish coding project")
    todo2 = Todo("Buy groceries")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.complete() == []

"""
Given I add two todo entries with one completed
I see #complete return the completed task 
"""
def test_adds_and_lists_todo_entries():
    todo_list = TodoList()
    todo1 = Todo("Finish coding project")
    todo2 = Todo("Buy groceries")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo1.mark_complete()
    assert todo_list.complete() == [todo1]

"""
#give_up marks all tasks as complete
returns all tasks when #complete is called
"""
def test_give_up_returns_all_as_completed():
    todo_list = TodoList()
    todo1 = Todo("Finish coding project")
    todo2 = Todo("Buy groceries")
    todo3 = Todo("Water Plants")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo_list.give_up() 
    assert todo_list.complete() == [todo1, todo2]