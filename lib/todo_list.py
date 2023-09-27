class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)
      
    def incomplete(self):
        incomplete_tasks = []
        for todo in self.todos:
            if not todo.complete:
                incomplete_tasks.append(todo)
        return incomplete_tasks

    def complete(self):
        complete_tasks = []
        for todo in self.todos:
            if todo.complete:
                complete_tasks.append(todo)
        return complete_tasks

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todos:
            todo.complete = True