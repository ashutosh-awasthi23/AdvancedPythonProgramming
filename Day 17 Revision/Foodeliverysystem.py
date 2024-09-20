class FoodItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        print(f"Food Item Name: {self.name}, Category: {self.category}, Price: {self.price}")


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.order_history = []

    def place_order(self, food_item, quantity):
        total = food_item.price * quantity
        self.order_history.append({self.customer_id: {'name': self.name, 'food': food_item.name, 'total': total}})
        print(f"Order Placed by: {self.name}, Item: {food_item.name}, Total: {total}")
        pass

    def view_order_history(self):
        print("-----------------------------------------------------------------------------------------")
        print(f"Order History of ID: {self.customer_id}, Name: {self.name}: {self.order_history}")
        print("-----------------------------------------------------------------------------------------")

class RegularCustomer(Customer):
    discount = 5.0

    def __init__(self, name, customer_id, discount):
        super().__init__(name, customer_id)
        self.discount = discount

    def place_order(self, food_item, quantity):
        # Apply discount
        total = (food_item.price * quantity) - (food_item.price * quantity * self.discount / 100)
        self.order_history.append({self.customer_id: {'name': self.name, 'food': food_item.name, 'total': total}})
        print(f"Order Placed by: {self.name}, Item: {food_item.name}, Total: {total}")
        pass


class PremiumCustomer(Customer):
    discount = 15
    priority_delivery = False

    def __init__(self, name, customer_id, discount, priority_delivery):
        super().__init__(name, customer_id)
        self.priority_delivery = priority_delivery
        self.discount = discount

    def place_order(self, food_item, quantity):
        # Apply discount
        total = (food_item.price * quantity) - (food_item.price * quantity * self.discount / 100)
        self.order_history.append({self.customer_id: {'name': self.name, 'food': food_item.name, 'total': total}})
        print(f"Order Placed by: {self.name}, Item: {food_item.name}, Total: {total}")
        pass


class Restaurant:
    def __init__(self):
        self.menu = []
        self.customers = []

    def add_food_item(self, food_item):
        self.menu.append(food_item.name)
        pass

    def add_customer(self, customers):
        self.customers.append({customers.customer_id: customers.name})
        pass

    def display_menu(self):
        print("-----------------------------------------------------------------------------------------")
        print("The menu is as follows:")
        print(self.menu)
        print("-----------------------------------------------------------------------------------------")
        pass

    def display_customer(self):
        print("-----------------------------------------------------------------------------------------")
        print("The Customers are as follows:")
        print(self.customers)
        print("-----------------------------------------------------------------------------------------")
        pass


food_item1 = FoodItem('Burger', 20, "Starter")
food_item2 = FoodItem('Chilli Potato', 80, "Starter")
food_item3 = FoodItem('Matar Paneer', 200, "Main Course")
food_item4 = FoodItem('Cold Coffee', 50, "Beverages")

reg1 = RegularCustomer("Aryan", 1, 5)
reg2 = RegularCustomer("Aryan1", 2, 5)
reg3 = RegularCustomer("Aryan2", 3, 5)

prem1 = PremiumCustomer("Ashutosh", 4, 100, True)
prem2 = PremiumCustomer("Ashutosh1", 5, 10, False)
prem3 = PremiumCustomer("Ashutosh2", 6, 10, True)


restaurant = Restaurant()
restaurant.add_food_item(food_item1)
restaurant.add_food_item(food_item2)
restaurant.add_food_item(food_item3)
restaurant.add_food_item(food_item4)

restaurant.add_customer(reg1)
restaurant.add_customer(reg2)
restaurant.add_customer(reg3)
restaurant.add_customer(prem1)
restaurant.add_customer(prem2)
restaurant.add_customer(prem3)

restaurant.display_customer()
restaurant.display_menu()

customer1 = Customer('AP', 100)
customer1.place_order(food_item3, 1)
reg1.place_order(food_item3, 1)
prem1.place_order(food_item3, 1)


reg1.place_order(food_item2, 10)
reg1.view_order_history()
prem1.view_order_history()


