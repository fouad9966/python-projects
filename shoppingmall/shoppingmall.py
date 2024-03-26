# Create a shopping mall app with 7 different collections. Collection 1: cooking wares,  collection 2: drinks, collection 3: computers, collection 4: toileteries,  collection 5: home appliances, collection 6: fashion(A: Men's wear, B: Women's wear), 
# customers can decide to add to cart without opening account but should not be able to pay out without account, or customer should open an account before making purchase.
# user should be able to buy from any of the collections they want, when they purchase from a collection, all your sales should be entering sales table.

import random
import mysql.connector as connection
conn = connection.connect(host = "127.0.0.1", user = "root", password = "Moneylion9966!", database = "shoppingmall")
cursor = conn.cursor()

class shopping:
    def __init__(self):
        self.trials = 0
        self.collection = ["cookingware","computer","drinks","home_appliances","men","toiletries","women"]
        self.status = "Not login"
        self.cartCategory = {}
        self.cartProduct = {}
        self.cartPrice = {}
        self.homepage()

    def homepage(self):
        self.home = input("Welcome to Sqi shopping mall,\n Enter 1 to register\n Enter 2 to login\n Enter 3 to add to cart\n Enter 4 to checkout: ")
        if self.home == "1":
            self.register()
        elif self.home == "2":
            self.login()
        elif self.home == "3":
            self.addcart()
        elif self.home == "4":
            self.checkout()
        else:
            self.homepage()
    
    def addcart(self):
        self.cat = input(f"which collection are you shopping from {self.collection}: ")
        if self.cat in self.collection:
            self.query = f"select product_name from {self.cat}"
            cursor.execute(self.query)
            self.result = cursor.fetchall()
            self.product = input(f"These are the products available under this collection {self.result} ")
            while (self.product,) not in self.result:
                print("product not available,kindly select from the available product")
                self.product = input(f"These are the products available under this collection {self.result} ")
            else:
                self.querry = f"select * from {self.cat} where product_name = {'%s'}"
                self.val = (self.product,)
                cursor.execute(self.querry, self.val)
                self.result = cursor.fetchone()
                print(f"The current price of {self.product} is {self.result[2]} and there are {self.result[1]} available")
                self.buy = int(input("How many are you willing to purchase?: "))
                while self.buy > self.result[1]:
                    print("Insufficient goods available in stock")
                    self.buy = int(input("How many are you willing to purchase?: "))
                else:
                    self.price = self.buy * self.result[2]
                    self.cartProduct.update({self.product: self.buy})
                    self.cartPrice.update({self.product: self.price})
                    self.cartCategory.update({self.cat:self.cartProduct})
                    print("Goods successfully selected")
        else:
            self.homepage()  

    def register(self):
        self.fullname = input("Enter your Full name: ")
        self.email= input("Enter your Email address: ") 
        self.username = input("Enter your username: ")
        self.pwd = input("Enter your password: ")
        self.age = int(input("Enter your age: "))
        self.phone = input("Enter your phone number: ")
        while len(self.phone) != 11:
            print("Kindly enter a valid phone number")
            self.phone = int(input("Enter your phone number: "))
        self.mem = random.randrange(200213, 300000)
        self.query = f"insert into registry (member_id, fullname, username, password, age, email,phonenumber) values ({'%s'},{'%s'},{'%s'},{'%s'},{'%s'},{'%s'},{'%s'})"
        self.add = (self.mem, self.fullname, self.username, self.pwd, self.age,self.email, self.phone)
        cursor.execute(self.query, self.add)
        conn.commit()
        print("You have successfully registered ")

    def login(self):
        self.log = input("Enter your username: ")
        self.passw = input("Enter your password: ")
        self.logquery = f"select * from registry where username = {'%s'} and password = {'%s'}"
        self.logval = (self.log, self.passw)
        cursor.execute(self.logquery, self.logval)
        self.result = cursor.fetchone()
        if self.result is None:
            self.trials += 1
            print("Invalid Login")
            if self.trials >= 3:
                self.homepage()
            else:
                self.login()
        else:
            print("You are successfully logged in")
            self.addcart()


shopping()


