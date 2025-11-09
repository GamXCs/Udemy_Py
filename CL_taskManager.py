user_task = []

while True:
    print("Welcome to your To-Do List!\n")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit\n")

    user_selection = int(input("Enter choice: \n"))

    if user_selection == 1:
        new_task = input("Please add new task: \n")
        user_task.append({"Task": new_task, "Done": False})
    elif user_selection == 2:
        if not user_task:
            print("No tasks yet!\n")
        for i, task in enumerate(user_task, 1):
            task_status = "✅" if task["Done"] else "❌"
            print(f"[{i}] {task['Task']}  {task_status}")
            print()
    elif user_selection == 3:
        print("Mark task complete")
    elif user_selection == 4:
        print("Delete task")
    else:
        print("exit")
        break
