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
        if not user_task:
            print("No tasks yet!\n")
        # Show the available tasks
        for i, task in enumerate(user_task, 1):
            task_status = "✅" if task["Done"] else "❌"
            print(f"[{i}] {task['Task']}  {task_status}")
            print()
        # Get the task to mark complete
        task_selection = int(input("Enter the number of the task to mark completed: "))

        # Use number from task_selection number to get the task from the list
        index = task_selection - 1  # Account for zero indexing
        user_task[index]["Done"] = True
        print(f"Task {index + 1} is now complete!\n")

    elif user_selection == 4:
        # Check if list is empty
        if not user_task:
            print("No tasks to delete yet!\n")
        # Show tasks
        for i, task in enumerate(user_task, 1):
            task_status = "✅" if task["Done"] else "❌"
            print(f"[{i}] {task['Task']}  {task_status}")
            print()
        # Prompt task deletion
        delete_task = int(input("Enter the number of the task you wish to delete: "))
        # Correct for zero index
        update_index = delete_task - 1

        # Validate
        if 0 <= update_index < len(user_task):
            del user_task[update_index]
            print(f"Task {delete_task} has been removed!\n")
        else:
            print("Sorry, there are not that many items!")

    else:
        print("exit")
        break
