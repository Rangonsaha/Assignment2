# Initialize an empty list to store tasks
tasks = []

# Function to create a new task
def create_task(task):
    tasks.append(task)
    print(f"Task '{task}' created successfully.")

# Function to read all tasks
def read_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to update a task
def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        print(f"Task {index} updated successfully.")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task {index} ('{deleted_task}') deleted successfully.")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nTodo List:")
    print("1. Create Task")
    print("2. Read Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        task = input("Enter the task: ")
        create_task(task)
    elif choice == "2":
        read_tasks()
    elif choice == "3":
        index = int(input("Enter the task index to update: "))
        new_task = input("Enter the new task: ")
        update_task(index, new_task)
    elif choice == "4":
        index = int(input("Enter the task index to delete: "))
        delete_task(index)
    elif choice == "5":
        print("Exiting the Todo App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
