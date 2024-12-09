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
manager = Task_manager()

manager.add_task("Buy groceries", "Milk, eggs, bread", 2)
manager.add_task("Clean room", "Tidy up and vacuum", 3)
manager.add_task("Finish Project", "Complete Python assignment", 1)

print(manager.view_tasks())
# [{'title': 'Finish Project', 'description': 'Complete Python assignment', 'priority': 1, 'status': 'Incomplete'}, {'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'priority': 2, 'status': 'Incomplete'}, {'title': 'Clean room', 'description': 'Tidy up and vacuum', 'priority': 3, 'status': 'Incomplete'}]   

manager.mark_complete("Buy Groceries")
print(manager.view_tasks())
# [{'title': 'Finish Project', 'description': 'Complete Python assignment', 'priority': 1, 'status': 'Incomplete'}, {'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'priority': 2, 'status': 'Incomplete'}, {'title': 'Clean room', 'description': 'Tidy up and vacuum', 'priority': 3, 'status': 'Incomplete'}]

print(manager.search_tasks("Clean room"))

# Title: Clean room
# Description: Tidy up and vacuum
# Priority: 3
# Status: Incomplete

manager.remove_task("Clean room")

print(manager.view_tasks())
# [{'title': 'Finish Project', 'description': 'Complete Python assignment', 'priority': 1, 'status': 'Incomplete'}, {'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'priority': 2, 'status': 'Incomplete'}]

print(manager.search_tasks("Clean room"))
# No task found with title Clean room
```
