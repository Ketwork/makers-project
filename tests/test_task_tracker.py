from lib.task_tracker import TaskTracker
import pytest

"""
Initailly there are no tasks
"""
def test_initially_has_no_tracks():
    tracker = TaskTracker()
    result = tracker.list_tasks()
    assert result == []

"""
When we add a task it is reflected in the list of tasks
"""
def test_add_task_reflected_in_tasks():
    tracker = TaskTracker()
    tracker.add_task("walk the dog")
    assert tracker.list_tasks() == ["walk the dog"]

"""
When we add multiple task 
they are all reflected in the list of tasks
"""
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add_task("walk the dog")
    tracker.add_task("walk the cat")
    tracker.add_task("walk the frog")
    assert tracker.list_tasks()  == ["walk the dog", "walk the cat", "walk the frog"]

"""
When we add multiple task 
and mark one as complete
it disapears from the task list 
"""
def test_marks_tasks_complete():
    tracker = TaskTracker()
    tracker.add_task("walk the dog")
    tracker.add_task("walk the cat")
    tracker.add_task("walk the frog")
    tracker.mark_complete(1)
    assert tracker.list_tasks() == ["walk the dog", "walk the frog"]


"""
If we try to mark a track complete that does not exist (too low)
It raises an error
"""
def test_mark_task_that_is_too_low_complete():
    tracker = TaskTracker()
    tracker.add_task("walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1)
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_tasks() == ["walk the dog"]

"""
If we try to mark a track complete that does not exist (too low)
It raises an error
"""
def test_mark_task_that_is_too_high_complete():
    tracker = TaskTracker()
    tracker.add_task("walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(1)
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_tasks() == ["walk the dog"]