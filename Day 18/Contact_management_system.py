Contact_List={}
temp=0

def add_Contact():
    global Contact_List
    global temp
    contact_name = input("Enter the Contact Name : ")
    phone_num1 = input("Enter the phone num 1 : ")
    phone_num2 = input("Enter the phone num 2 :")
    email = input("Enter the Email :")
    valuedict = {"Name": contact_name, "Phone Number": phone_num1, "Mobile Number": phone_num2, "Email": email}
    temp=temp+1
    Contact_List[temp] = valuedict

def update_details():
    global Contact_List
    global temp
    contact_name = input("Enter the Contact Name : ")
    if contact_name in list(Contact_List.keys()):
        contact_name = input("Enter the Contact Name : ")
        phone_num1 = input("Enter the phone num 1 : ")
        phone_num2 = input("Enter the phone num 2 :")
        email = input("Enter the Email :")
        valuedict = {"Name": contact_name, "Phone Number": phone_num1, "Mobile Number": phone_num2, "Email": email}
        Contact_List[temp] = valuedict
    else:
        print("No such contact exits")

def delete_contact():

    global Contact_List

    print(list(Contact_List.keys()))
    contact_name = input("Enter the Contact Name : ")
    if contact_name in list(Contact_List.keys()):
        del Contact_List[contact_name]
    else:
        print("No such contact exits")

def view_contact():

    global Contact_List

    print(list(Contact_List.keys()))
    contact_name = input("Enter the Contact Name : ")
    if contact_name in list(Contact_List.keys()):
        print(Contact_List[contact_name])

while True:
    print("==========================================================================================")
    ch=input("Press 1: Add Contact\n\nPress 2 Update Contact\n\n Press 3 Delete Contact\n\n Press 4 View Contact")
    print("==========================================================================================")
    if ch=="1":
        add_Contact()
    elif ch=="2":
        update_details()
    elif ch=="3":
        delete_contact()
    elif ch=="4":
        view_contact()
    else:
        print("Wrong choice entered")
    print("==========================================================================================")
    ch2=input("Press 1 to continue")
    print("==========================================================================================")
    if ch2=="1":
        continue
    else:
        break
