tasks = []

while True:
    print("\n---------- TO DO LIST ----------")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Search for a task")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':                          
        task = input("Enter the task name: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("Tasks in the list:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        search = input("Enter task to search: ")
        found = False
        for task in tasks:
            if search.lower() in task.lower():
                print("Task Found:", task)
                found = True
        if not found:
            print(" Task not found!")

    elif choice == '4':
        if len(tasks) == 0:
            print("⚠ No tasks available to delete!")
        else:
            print("\n------ Tasks ------")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                delete_index = int(input("Enter task number to delete: "))
                if 1 <= delete_index <= len(tasks):
                    removed_task = tasks.pop(delete_index - 1)
                    print(f" '{removed_task}' deleted successfully!")
                else:
                    print("⚠ Invalid task number!")
            except ValueError:
                print("⚠ Please enter a valid number!")

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break                                  

    else:
        print("⚠ Invalid choice! Please try again.")