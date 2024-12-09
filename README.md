# Task management system

Create a class called Task_manager to manage tasks in a to-do list. Each task will have a title, description, priority, and status.

## Attributes:
* tasks: A list of dictionaries, where each dictionary represents a task with the following keys:
  * title: The title of the task.
  * description: A brief description of the task.
  * priority: An integer (e.g., 1 for high, 2 for medium, 3 for low).
  * status: A string ("Incomplete" or "Complete").

## Methods:
* add_task(title, description, priority):
  * Adds a new task to the list with the given attributes.
  * Default status should be "Incomplete".
* remove_task(title):
  * Removes a task by its title.
  * If the task doesn't exist, print an appropriate message.
* mark_complete(title):
  * Marks the specified task as "Complete".
* view_tasks(sort_by="priority"):
  * Displays all tasks in a formatted way.
  * Allows sorting by priority or status, default is priority.
  * __HOT TIP__ - this is not easy, you will need to look up _lambda funciton_ in Python.
* search_task(title):
  * Searches for a task by title and displays its details.

## Examples
```
manager = TaskManager()

manager.add_task("Buy groceries", "Milk, eggs, bread", 2)
manager.add_task("Clean room", "Tidy up and vacuum", 3)
manager.add_task("Finish project", "Complete Python assignment", 1)

manager.view_tasks()
➞ 
1 Finish project (Priority: 1, Status: Incomplete)
2. Buy groceries (Priority: 2, Status: Incomplete)
3. Clean room (Priority: 3, Status: Incomplete)

manager.mark_complete("Buy groceries")
manager.view_tasks()
 ➞ 
 1. Finish project (Priority: 1, Status: Incomplete)
 2. Buy groceries (Priority: 2, Status: Complete)
 3. Clean room (Priority: 3, Status: Incomplete)

manager.search_task("Clean room")
 ➞ {"title": "Clean room", "description": "Tidy up and vacuum", "priority": 3, "status": "Incomplete"}

manager.remove_task("Clean room")
manager.view_tasks()
 ➞ 
 1. Finish project (Priority: 1, Status: Incomplete)
 2. Buy groceries (Priority: 2, Status: Complete)
```
