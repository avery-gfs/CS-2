class Task:
    def __init__(self, name):
        # Keep track of task name and status (done or undone)
        # Task should start out undone
        pass

    def __repr__(self):
        # Display the name and status of task
        return f""

class TodoList:
    def __init__(self):
        # Keep track of a tasks list, which starts out empty
        pass

    def addTask(self, name):
        # Add a new task with a given name
        pass

    def setIsDone(self, name, isDone):
        # Update the status of the task that matches name
        pass

    def remove(self, name):
        # Remove the task that matches name
        pass

    def __repr__(self):
        # Return a representation of the to do list that
        # shows each task (name and status), the total number
        # of tasks, and the number of undone tasks
        result = ""
        return result

todo = TodoList()

# todo.addTask("feed dog")
# todo.addTask("water plants")
# todo.setIsDone("feed dog", True)

print(todo)
