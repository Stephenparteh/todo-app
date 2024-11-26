import json
import os

class TodoList:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        return self.tasks

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

def show_menu():
    print("\nTodo List Management")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    todo_list = TodoList()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added.")

        elif choice == '2':
            tasks = todo_list.view_tasks()
            if not tasks:
                print("No tasks available.")
            else:
                print("Tasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")

        elif choice == '3':
            tasks = todo_list.view_tasks()
            if not tasks:
                print("No tasks available to update.")
            else:
                try:
                    task_index = int(input("Enter task number to update: ")) - 1
                    new_task = input("Enter new task: ")
                    todo_list.update_task(task_index, new_task)
                    print("Task updated.")
                except (ValueError, IndexError):
                    print("Invalid task number.")

        elif choice == '4':
            tasks = todo_list.view_tasks()
            if not tasks:
                print("No tasks available to delete.")
            else:
                try:
                    task_index = int(input("Enter task number to delete: ")) - 1
                    todo_list.delete_task(task_index)
                    print("Task deleted.")
                except (ValueError, IndexError):
                    print("Invalid task number.")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
