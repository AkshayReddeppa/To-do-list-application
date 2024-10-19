import json

tasks = []
filename = "tasks.json"

def add_task(title, description=""):
    task = {"title": title, "description": description, "is_complete": False}
    tasks.append(task)
    print(f"Task '{title}' added.")

def edit_task(index, title=None, description=None):
    if 0 <= index < len(tasks):
        if title:
            tasks[index]["title"] = title
        if description:
            tasks[index]["description"] = description
        print(f"Task {index} updated.")
    else:
        print("Invalid task index.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task['title']}' deleted.")
    else:
        print("Invalid task index.")

def mark_task_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["is_complete"] = True
        print(f"Task '{tasks[index]['title']}' marked as complete.")
    else:
        print("Invalid task index.")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks):
        status = "Complete" if task["is_complete"] else "Incomplete"
        print(f"{idx}. {task['title']}: {task['description']} - [{status}]")

def save_tasks():
    with open(filename, 'w') as file:
        json.dump(tasks, file)
    print("Tasks saved to file.")

def load_tasks():
    try:
        with open(filename, 'r') as file:
            global tasks
            tasks = json.load(file)
        print("Tasks loaded from file.")
    except FileNotFoundError:
        print("No saved tasks found.")

def main():
    load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. List Tasks")
        print("6. Save Tasks")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == "2":
            index = int(input("Enter task index to edit: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            edit_task(index, title or None, description or None)
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            delete_task(index)
        elif choice == "4":
            index = int(input("Enter task index to mark as complete: "))
            mark_task_complete(index)
        elif choice == "5":
            list_tasks()
        elif choice == "6":
            save_tasks()
        elif choice == "7":
            save_tasks()  # Save before exiting
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
