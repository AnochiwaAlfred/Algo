from random import randint
from datetime import date

# Write a program that simulates a restaurant. The program should allow users to place orders, view the menu, and 
# check their total bill. The program should also keep track of inventory and notify staff when certain ingredients 
# need to be restocked.

class Restaurant:

    all=[]        
    
    def __init__(self, name):
        self.__name = name
        self.__account_balance = 50000
        self.staff = []
        
        if len(Restaurant.all)==0:
            Restaurant.all.append(self)
    
    def __str__(self):
        return self.__name
    
    def __repr__(self):
        return self.__name
    
    def get():
        return Restaurant.all[0]
    
    def name(self):
        return self.__name
    
    def get_account_balance(self):
        return self.__account_balance
    
    def add_to_balance(self, amount):
        self.__account_balance = self.__account_balance + amount
        
    def make_payment(self, amount):
        self.__account_balance = self.__account_balance - amount
        

class Staff:
    all = []
    STAFF_IDS = []
    
    @classmethod
    def message_staff(cls, message):
        for staff in cls.all:
            staff.messages.append(message)
    
    def __init__(self):
        self.id = self.__generate_staff_id()
        self.first_name = input('Enter Firstname: ')
        self.last_name = input('Enter Lastname: ')
        self.password = self.set_password()
        self.messages = []
        
        Staff.all.append(self)
        Staff.STAFF_IDS.append(self.id)
        restaurant = Restaurant.all[0]
        restaurant.staff.append(self)
        
    def __generate_staff_id(self):        
        staff_id = randint(10000, 99999)
        if str(staff_id) in Staff.STAFF_IDS:
            self.__generate_staff_id()
        else:
            return str(staff_id)
        
    def set_password(self):
        password1 = input('Enter Preferred Password: ')
        password2 = input('Enter Password Again: ')
        if password1==password2:
            return password1
        else:
            print('Password mismatch')
            self.set_password()
    
    def read_all_messages(self):
        for message in self.messages:
            print(f"\n{message}")
            
    def read_last_message(self):
            print(f"\n{self.message[-1]}")

    def __str__(self):
        return f"{self.first_name} {self.last_name}".title()
   
    def __repr__(self):
        return f"{self.first_name} {self.last_name}".title()
   

class Inventory:
    all = []
    ITEM_IDS = []
    
    def __init__(self, name, unit_price):
        self.id:int = self.__generate_id()
        self.name = name
        self.measurement = input('Enter lowest level of measurement, e.g. cup, bag, pint: ')
        self.measurement_plural = input('Enter plural of measurement name: ')
        self.verbose_name = f"A {self.measurement} of {self.name}"
        self.verbose_name_plural = f"{self.measurement_plural} of {self.name}"
        self.unit_price = unit_price
        self.__quantity_available = 50
        
        Inventory.ITEM_IDS.append(self.id)
        Inventory.all.append(self)
        
    def __generate_id(self):
        if len(Inventory.ITEM_IDS)==0:
            id = 1
            return id
        else:
            id = Inventory.ITEM_IDS[-1] + 1
            return id
    
    def get(id):
        for object in Inventory.all:
            if object.id==id:
                return object
    
    def get_quantity_available(self):
        return self.__quantity_available
    
    def release(self, quantity):
        self.__quantity_available = self.__quantity_available - quantity
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    def verbose_name(self):
        return self.verbose_name
    
    def verbose_name_plural(self):
        return self.verbose_name_plural
    

class Menu:
    all = []
    MENU_IDS = []
    
    def __init__(self, name, price):
        self.menu_id = self.__generate_menu_id()
        self.name = name
        self.price = price
        self.ingredients = []
        self.amount_available = 10
        self.__list_ingredients()
        
        Menu.all.append(self)
        Menu.MENU_IDS.append(self.menu_id)
           
    def __generate_menu_id(self):        
        menu_id = randint(10000, 99999)
        if menu_id in Menu.MENU_IDS:
            self.__generate_menu_id()
        else:
            return menu_id
    
    def __list_ingredients(self):
        print('ID', 'Item')
        for item in Inventory.all:
            print(f"{item.id} {item.name}")
        self.__get_item()
            
    def __get_item(self):
        item_id = int(input('Enter Item Number: '))
        item = Inventory.get(item_id)
        quantity = int(input('Enter Item quantity: '))
        self.ingredients.append([item_id, quantity, item])
        rerun = input('Add another ingredient? Y/N: ')
        if rerun.lower()=='y':
            self.__get_item()
        elif rerun.lower()=='n':
            pass
        else:
            pass
        
    def make(self, quantity):
        check = True
        ingredient_quantity = eval(ingredient[0])*quantity
        
        for ingredient in self.ingredients:
            item_id = ingredient[0]
            item = Inventory.get(item_id)
            available_quantity = item.get_quantity_available()
            if ingredient_quantity>available_quantity:
                print(f'Not enough {item}, available')
                Staff.message_staff(f"Not enough {item}, available")
                check&=False
            elif ingredient_quantity<=available_quantity:
                check&=True

        if check==True:
            for ingredient in self.ingredients:
                item_id = ingredient[0]
                item = Inventory.get(item_id)
                item.release(ingredient_quantity)
            self.amount_available = self.amount_available + quantity
            
    def serve(self, quantity):
        self.amount_available = self.amount_available - quantity
        price = self.price * quantity
        Restaurant.add_to_balance(price)
        
    def get(id):
        for object in Menu.all:
            if object.menu_id==id:
                return object
    
    def sell(self, quantity):
        self.amount_available = self.amount_available - quantity
            
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class Order:
    all = []
    ORDER_IDS = []
    
    def __init__(self, customer_id, order_items=[], total_price=0):
        self.order_id = self.__generate_order_id()
        self.customer = Customer.get(customer_id)
        self.order_items = order_items
        self.order_date = date.today()
        self.total_price = total_price
        
        restaurant = Restaurant.all[0]
        restaurant.add_to_balance(self.total_price)
        for order_item in order_items:
            for item in Menu.all:
                if item == order_item:
                    quantity = order_item[item]
                    item.sell(quantity)
        
    def __generate_order_id(self):        
        order_id = randint(10000, 99999)
        if order_id in Order.ORDER_IDS:
            self.__generate_order_id()
        else:
            return order_id
        

class Customer:
    all = []
    CUSTOMER_IDS = []
    
    def __init__(self):
        self.customer_id = self.__generate_customer_id()
        self.first_name = input('Enter First Name: ')
        self.last_name = input('Enter last Name: ')
        self.date_stamp = date.today()
        self.order_list = []
    
    def __generate_customer_id(self):
        customer_id = randint(10000, 99999)
        if customer_id in Customer.CUSTOMER_IDS:
            self.__generate_customer_id()
        else:
            return customer_id
    
    def get(id):
        for object in Customer.all:
            if object.customer_id==id:
                return object  
            
    def get_menu(self):
        for item in Menu.all:
            if item.amount_available>0:
                print(f'{item.menu_id} {item}')
        
    def make_order(self):
        self.get_menu()
        item_id = eval(input('Enter Item ID: '))
        if item_id in Menu.MENU_IDS:
            item = Menu.get(item_id)
            quantity = eval(input('Enter quantity: '))
            price = item.price*quantity
            self.order_list.append({item:quantity})
            rerun = input('Add another item? Y/N: ')
        if rerun.lower()=='y':
            self.make_order()
        elif rerun.lower()=='n':
            self.__checkout(price)
            self.order_list.clear()
            
    def __checkout(self, total_price):
        check = input(f'Total price is {total_price}. Checkout? Y/N: ')
        if check.lower()=='y':
            Order(self.customer_id, self.order_list, total_price)
            
    def __str__(self):
        return f'{self.first_name} {self.last_name}'    
            
    def __repr__(self):
        return f'{self.first_name} {self.last_name}'