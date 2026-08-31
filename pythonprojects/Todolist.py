tasks = []
option = 0
while option != 4:


    print("================================")
    print("TO-DO LIST")
    print("================================")

    print("Welcome back Jamaal,")
    print(f"You currently have {len(tasks)} tasks in your to do list. ")


    print("1: Set a Task")
    print("2: view your Tasks")
    print("3: Remove your Task")
    print("4: Exit")

    option = int(input("Select your option"))

    if option == 1:
        task = input("set a task")
        tasks.append(task)
        print(f"Task added successfully {task}")
    elif option == 2:
        if not tasks:
            print("You have no tasks")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        input("press enter to return to menu")
    elif option == 3:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        removal = int(input("Which number task do you want to remove: "))
        removal -= 1

        removed_task = tasks.pop(removal)

        print(f"The task {removed_task} has been removed")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        input("Press Enter to return to menu...")