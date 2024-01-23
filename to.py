import json
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Task List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter task priority (high/medium/low): ").lower()
    due_date_str = input("Enter due date (YYYY-MM-DD, leave empty if none): ")

    if due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
    else:
        due_date = None

    task = {
        'title': title,
        'priority': priority,
        'due_date': due_date.strftime('%Y-%m-%d') if due_date else None,
        'completed': False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTodo List Application\n")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            print("Exiting Todo List Application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
