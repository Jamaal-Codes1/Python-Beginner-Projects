
tasks = []

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