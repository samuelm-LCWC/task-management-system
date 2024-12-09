class Task_manager:
    def __init__(self) -> None:
        self.__tasks = []

    def add_task(self, title, description, priority, status="Incomplete"):
        self.__tasks.append(
            {
                "title": title,
                "description": description,
                "priority": priority,
                "status": status
            }
        )

    def remove_task(self, title):
        for item in self.__tasks:
            if title in item.values():             
                self.__tasks.remove(item)
                return(item)
        else:
            return f"No item in list with the title: {title}"
        
    def mark_complete(self, title):
        for item in self.__tasks:
            if title in item.values():
                item.update({"status": "Complete"})

    def view_tasks(self, sort_by="priority"):
        return sorted(self.__tasks, key=lambda x: x[sort_by])
    
    def search_tasks(self, title):
        for item in self.__tasks:
            if title in item.values():
                return f"Title: {title}\nDescription: {item.get('description')}\nPriority: {item.get('priority')}\nStatus: {item.get('status')}"
        else:
            return f"No task found with title {title}"
    
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

test_case = Task_manager()
test_case.add_task(title=test_item_1.get("title"), description=test_item_1.get("description"), priority=test_item_1.get("priority"))
test_case.add_task(title=test_item_2.get("title"), description=test_item_2.get("description"), priority=test_item_2.get("priority"))
print(test_case.search_tasks("Dishes"))
"""
test = Task_manager()

print(test.__tasks)
"""