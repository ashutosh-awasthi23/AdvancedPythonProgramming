# dicto={}
# while True:
#     choice=int(input("Enter 1.Add items to inventory\n Enter 2. Update prices and quantities\n Enter 3. Calculate Total value of inventory \n Enter 4 to Exit"))
#     def addItems():
#         global dicto
#         k=[]
#         itemname=input("Enter the name of items")
#         quantities=int(input("Enter quantities:"))
#         k.append(quantities)
#         price=int(input("Enter price"))
#         k.append((price))
#         dicto[itemname]=k
#
#     def updatevalues():
#         global dicto
#         itemname = input("Enter the name of items")
#         num=int(input("Enter 1 to update quantity\n Enter 2 to update prices"))
#         if num==1:
#             dicto[itemname][0]=int(input("Enter the updated quantities"))
#         elif num==2:
#             dicto[itemname][1] = int(input("Enter the updated pricing"))
#
#
#     def totalValue():
#         sumi=0
#
#         for value in dicto.values():
#             sumi=sumi + value[0]*value[1]
#         print(f"The total value is {sumi}")
#
#     if choice==1:
#         addItems()
#     elif choice==2:
#         updatevalues()
#     elif choice==3:
#         totalValue()
#     elif choice==4:
#         break
#     else :
#         continue


# Aaryan Pal


# inventory = {}
#
#
# def add_item(details):
#     item_name, quantity, price = details.split(',')
#     lst = [int(quantity), int(price)]
#     inventory[item_name] = lst
#     print("\n\nItem added; Updated inventory: ", inventory)
#
#
# def update_item(details):
#     item_name, quantity, price = details.split(',')
#     if item_name in inventory:
#         lst = [int(quantity), int(price)]
#         inventory[item_name] = lst
#         print(f"\n\nItem {item_name} values updated; Updated inventory: ", inventory)
#     else:
#         print("\n\nItem is not present in inventory!! First add the item.")
#
#
# def total_value():
#     i_sum = 0
#     for values in inventory.values():
#         x = values[0] * values[1]
#         i_sum = i_sum + x
#     return i_sum
#
#
# print("*** Inventory management system ***")
#
# while True:
#     print("Press 1 to add item")
#     print("Press 2 to update item")
#     print("Press 3 to print total value")
#     print("Press 4 to see the inventory")
#     print("Press 5 to exit\n\n")
#
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         details = input("\n\nInput item details in comma separated values [name, quantity, price]: ")
#         add_item(details)
#     elif choice == 2:
#         details = input("\n\nInput item details in comma separated values [name, quantity, price]: ")
#         update_item(details)
#     elif choice == 3:
#         print("\n\nTotal value of the inventory: ", total_value(), "\n")
#     elif choice == 4:
#         print(inventory)
#     elif choice == 5:
#         break
#
