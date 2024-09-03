toDo = []

while True:
    action = int(input("\nPress\t1: View Tasks\t2: Add Tasks\t3:  Remove Tasks\t4: Exit\nEnter your choice: "))

    if action == 1:
        print("Your tasks: ", toDo)
    elif action == 2:
        task = input("Input your task to add: ")
        toDo.append(task)
    elif action == 3:
        task = input("Input the task to remove: ")
        if task in toDo:
            toDo.remove(task)
        else:
            print("Task is not in the list")
    elif action == 4:
        break
    else:
        continue

