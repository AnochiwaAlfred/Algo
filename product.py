# 2. Write a class called Product. The class should have fields called name, amount, and price,
# holding the product’s name, the number of items of that product in stock, and the regular
# price of the product. There should be a method get_price that receives the number of
# items to be bought and returns a the cost of buying that many items, where the regular price
# is charged for orders of less than 10 items, a 10% discount is applied for orders of between
# 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
# also be a method called make_purchase that receives the number of items to be bought and
# decreases amount by that much.
from tkinter import *


class Product:
    def __init__(self, name='Product Name', amount=0, price=0, num=0):
        self.name = name
        self.amount = amount
        self.price = price
        self.num = num
        
    def number_of_items(self):
        return eval(input('Enter the number of ' + self.name + 's you want to purchase: '))
        
        
    def get_price(self):
        cost=0
        self.num = self.number_of_items()
        num=self.num
        if num < 10:
            cost = self.price * num
        if 11<=num<=99:
            cost = (self.price - (self.price/10))*num
        if num>=100:
            cost = (self.price - (self.price/5))*num
        return cost
        
    def run(self):
        g = self.get_price()
        print('Total cost of items is $' + str(g))
        def make_purchase():
            self.amount = self.amount - self.num
            print('Stock Left:', self.amount)
        make_purchase()
    
p = Product(name='TP-Link POE Cable', amount=1000, price=1250)
p.run()
    
    



def button1():
    
    def callback():
        label.configure(text='Button Clicked')
        label2 = Label(text='Reallyyyyyyy?', font=('harrington', 14, 'bold'), fg='red')
        label2.grid(row=2, column=2)
        
    label =  Label(text='Not Clicked')
    button = Button(text='Click Me', command=callback)
    
    label.grid(row=0, column=0)
    button.grid(row=1, column=0)
# button1()