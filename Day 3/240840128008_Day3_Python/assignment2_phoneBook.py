dicto = {}
while True:
    choice = int(
        input("Enter 1.Add contacts \n Enter 2. Update contacts\n Enter 3. Delete contacts \n Enter 4 to View\nEnter 5 to search\n Enter 6 to exit"))


    def addContact():

        global dicto
        k = []
        name = input("Enter the name of contact")
        name=name.lower()

        phoneno = input("Enter phonenumber:")
        k.append(phoneno)
        email = input("Enter email")
        k.append((email))
        dicto[name] = k


    def updateContact():
        global dicto
        itemname = input("Enter the name of name")
        num = int(input("Enter 1 to update phoneno\nEnter 2 to update email"))
        if num == 1:
            dicto[itemname][0] = input("Enter the updated phonenumber")
        elif num == 2:
            dicto[itemname][1] = input("Enter the updated email")
        else:
            print("Wrong choice entered")


    def deleteContact():
        global dicto
        name = input("Enter the name of contact you want to delete")
        del (dicto[name])
    def show():
        print(dicto)

    def search():
        name = input("Enter the name of contact")
        name=name.lower()
        print(f"{name}:{dicto[name]}")



    if choice == 1:
        addContact()
    elif choice == 2:
        updateContact()
    elif choice == 3:
        deleteContact()
    elif choice == 4:
        show()
    elif choice == 5:
        search()
    elif choice == 6:
        break
    else:
        continue
