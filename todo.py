todo = []
while True:
    print("1.add task")
    print("2.remove task")
    print("3.view task")
    print("4.Exit")
    choice = input("enter your choice: ")

    if choice == "1":
        item = input("what do you want to add: ")
        todo.append(item)

    elif choice == "2":
        item = input("what do you want to remove: ")
        if item in todo:
            todo.remove(item)
        else:
            print("Item not found.")

    elif choice == "3":
        for i, v in enumerate(todo, 1):
            print(i, v)

    elif choice == "4":
        print("thanks!")
        break

    else:
        print("Invalid choice. Try again.")
11