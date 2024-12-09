import pytest
from task_manager import Task_manager

test_item_1 = {
    "title": "Dishes",
    "description": "Ensure all dishes are washed!",
    "priority": 2
}

test_item_2 = {
    "title": "Homework",
    "description": "Complete all homework on time",
    "priority": 3
}

def test_task_manager_add_and_view():
    test_case = Task_manager()
    test_case.add_task(title=test_item_1.get("title"), description=test_item_1.get("description"), priority=test_item_1.get("priority"))
    test_case.add_task(title=test_item_2.get("title"), description=test_item_2.get("description"), priority=test_item_2.get("priority"))
    tasks = test_case.view_tasks()
    assert tasks == [{'title': 'Dishes', 'description': 'Ensure all dishes are washed!', 'priority': 2, 'status': 'Incomplete'}, {'title': 'Homework', 'description': 'Complete all homework on time', 'priority': 3, 'status': 'Incomplete'}]

def test_task_manager_remove():
    test_case = Task_manager()
    test_case.add_task(title=test_item_1.get("title"), description=test_item_1.get("description"), priority=test_item_1.get("priority"))
    test_case.add_task(title=test_item_2.get("title"), description=test_item_2.get("description"), priority=test_item_2.get("priority"))
    test_case.remove_task("Dishes")
    tasks = test_case.view_tasks()
    assert tasks == [{'title': 'Homework', 'description': 'Complete all homework on time', 'priority': 3, 'status': 'Incomplete'}]

def test_task_manager_remove_non_existant():
    test_case = Task_manager()
    test_case.add_task(title=test_item_1.get("title"), description=test_item_1.get("description"), priority=test_item_1.get("priority"))
    test_case.add_task(title=test_item_2.get("title"), description=test_item_2.get("description"), priority=test_item_2.get("priority"))
    assert test_case.remove_task("Shopping") == "No item in list with the title: Shopping"

def test_task_manager_mark_complete():
    test_case = Task_manager()
    test_case.add_task(title=test_item_1.get("title"), description=test_item_1.get("description"), priority=test_item_1.get("priority"))
    test_case.add_task(title=test_item_2.get("title"), description=test_item_2.get("description"), priority=test_item_2.get("priority"))
    test_case.mark_complete("Dishes")
    assert test_case.view_tasks() == [{'title': 'Dishes', 'description': 'Ensure all dishes are washed!', 'priority': 2, 'status': 'Complete'}, {'title': 'Homework', 'description': 'Complete all homework on time', 'priority': 3, 'status': 'Incomplete'}]

def test_view_by_completed():
    test_case = Task_manager()
    test_case.add_task(title=test_item_1.get("title"), description=test_item_1.get("description"), priority=test_item_1.get("priority"))
    test_case.add_task(title=test_item_2.get("title"), description=test_item_2.get("description"), priority=test_item_2.get("priority"))
    test_case.mark_complete("Dishes")
    assert test_case.view_tasks(sort_by="status") == [{'title': 'Dishes', 'description': 'Ensure all dishes are washed!', 'priority': 2, 'status': 'Complete'}, {'title': 'Homework', 'description': 'Complete all homework on time', 'priority': 3, 'status': 'Incomplete'}]

def test_search_task():
    test_case = Task_manager()
    test_case.add_task(title=test_item_1.get("title"), description=test_item_1.get("description"), priority=test_item_1.get("priority"))
    test_case.add_task(title=test_item_2.get("title"), description=test_item_2.get("description"), priority=test_item_2.get("priority"))
    assert test_case.search_tasks("Dishes") == "Title: Dishes\nDescription: Ensure all dishes are washed!\nPriority: 2\nStatus: Incomplete"

def test_search_task_missing():
    test_case = Task_manager()
    assert test_case.search_tasks("Dishes") == "No task found with title Dishes"

def test_tasks_private():
    with pytest.raises(AttributeError):
        test_case = Task_manager()
        test_case.__tasks
        test_case.tasks