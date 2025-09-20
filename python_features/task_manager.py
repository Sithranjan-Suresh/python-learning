"""
Problem: Simple Task Manager
----------------------------
Allows a user to manage a list of tasks with options to:
1. Add a task
2. Remove a task
3. Show all tasks
4. Exit the program
"""

# Initialize empty task list
tasks = []

while True:
    # Display menu
    print("\n1. Add task\n2. Remove task\n3. Show tasks\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        # Add a new task
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Added: {task}")

    elif choice == "2":
        # Remove an existing task
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Removed: {task}")
        else:
            print("Task not found.")

    elif choice == "3":
        # Display all tasks
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for t in tasks:
                print(f"- {t}")

    elif choice == "4":
        # Exit the program
        print("Goodbye!")
        break

    else:
        # Handle invalid input
        print("Invalid choice, try again.")
