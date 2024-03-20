import mysql.connector as connection
import random
myconn= connection.connect(host ="127.0.0.1", user = 'root', password ="Moneylion9966!", database = "Class_Bank")
cursor = myconn.cursor()
class Bank:
    def __init__(self):
        print("You're welcome")
        self.start()

    def start(self):
        self.decision= input("""
        Which operation would you like to perform? 
        Enter 1 to login
        Enter 2 to create a new account
        Enter 3 to deposit money
        Enter 4 to send money
        Enter 5 to buy airtime
        Enter 6 to buy data
        Enter 7 to pay for utiliy """)
        if self.decision == "1":
            self.login()
        elif self.decision =="2":
            self.create()
        elif self.decision == "3":
            self.deposit()
        elif self.decision == "4":
            self.send_money()
        elif self.decision == "5":
            self.buy_airtime()
        elif self.decision == "6":
            self.buy_data()
        elif self.decision == "7":
            self.paybill()
        else:
            self.start()
    
    def create(self):
        self.name= input("Enter your full name: ")
        self.username= input("Enter your username: ")
        self.password= input("Enter your password: ")
        self.accountbal = 0
        self.phone_number = input("Enter your phone number: ")
        self.account_num = self.phone_number[1:]
        self.which()
    
    def which(self):
        self.decide = input("Which bank do you want to open? ").title()
        if self.decide == "Kuda":
            self.querry = "INSERT INTO Kuda(CustomersName, account_num, username, password, account_balance, phone_number) VALUES(%s, %s, %s, %s, %s, %s)"
            self.committing()
        elif self.decide == "Palmpay":
            self.querry = "INSERT INTO Palmpay(CustomersName, account_num, username, password, account_balance, phone_number) VALUES(%s, %s, %s, %s, %s, %s)"
            self.committing()
        elif self.decide == "Access":
            self.querry = "INSERT INTO Access(CustomersName, account_num, username, password, account_balance, phone_number) VALUES(%s, %s, %s, %s, %s, %s)"
            self.committing()
        else:
            print("The Bank you entered is not available, please try again")
            self.which
    
    def committing(self):
        self.val =(self.name, self.account_num, self.username, self.password, self.accountbal, self.phone_number)
        cursor.execute(self.querry, self.val)
        myconn.commit()
        print("Registration successful")
    
    def login(self):
        self.user = input("Enter your username ").strip()
        self.password = input("Enter your password ").strip()
        self.banking= input("Which bank are you login into? ").title()
        if self.banking == "Kuda":
            self.querry = "SELECT * FROM Kuda WHERE username = %s "
            self.confirm()
            self.operation()
        elif self.banking == "Palmpay":
            self.querry = "SELECT * FROM Palmpay WHERE username = %s "
            self.confirm()
            self.operation()
        else:
            print("Login failed")
            self.login()

    def confirm(self):
        self.val = (self.user,)
        cursor.execute(self.querry, self.val)
        self.result = cursor.fetchone()
        if self.user == self.result[3] and self.password == self.result[4]:
            print("Login successful")
        else:
            print("Login failed")
            self.login()

    def operation(self):
        self.op= input("Which operation will you like to perform?\nEnter 1 to send money\n2 to buy airtime ")
        if self.op == "1":
            self.send_money()

    def send_money(self):
        self.recipient = input("Enter recipient account number: ")
        self.choose = input("""
           Choose a bank to send money to
           Enter 1 for Kuda:
           Enter 2 for palmpay:
           Enter 3 for Access: """)
        if self.choose == "1":
            self.query = "SELECT * FROM Kuda WHERE account_num = %s"
            self.querry = "UPDATE Kuda SET accountbal = %s WHERE account_num = %s"
        elif self.choose == "2":
            self.query = "SELECT * FROM palmpay WHERE account_num = %s"
            self.querry = "UPDATE palmpay SET accountbal = %s WHERE account_num = %s"
        elif self.choose == "3":
            self.query = "SELECT * FROM access WHERE account_num = %s"
            self.querry = "UPDATE access SET accountbal = %s WHERE account_num = %s"
            self.done()
        else:
            print("Invalid Selection") 
        
    def done(self):
        self.val = (self.recipient,)
        cursor.execute(self.query, self.val)
        self.result = cursor.fetchone()
        print(self.result)
        if self.result:
            print(f"You are about to send money to {self.result[1]}")
            self.amount = int(input("Enter the amount you want to send: "))
            if self.amount > self.result[5]:
                print("Insufficient funds")
                self.done()
            else:
                print(f"You are about to send money to {self.result[1]}")
                self.new_amount = self.result[5] + self.amount
                self.val = (self.new_amount, self.recipient)
                cursor.execute(self.querry, self.val)
                myconn.commit()
                print(f"{self.amount} sent successfully to {self.result[1]}")
        else:
            print("Invalid account number")
            self.send_money()



        
    
    def deposit(self):
        print("Welcome")
        self.choosing_bank = input("Choose a bank you want to deposit into:\n Enter 1 for Kuda \n Enter 2 for Palmpay: ")
        self.receiver = input("Enter receiver account number: ")
        if self.choosing_bank == "1":
            self.query = "SELECT * FROM Kuda where Account_num = %s"
            self.querry = "UPDATE Kuda SET account_balance =%s WHERE Account_num =%s"
            self.done()
        elif self.choosing_bank == "2":
            self.query = "SELECT * FROM Palmpay where Account_num = %s"
            self.querry = "UPDATE Palmpay SET account_balance =%s WHERE Account_num =%s"
            self.done()

    def confirmation(self):
        self.val = (self.receiver,)
        cursor.execute(self.query, self.val)
        self.result = cursor.fetchone()
        if self.result:
            print(f"You are sending money to {self.result[1]}")
            self.amount = int(input("Enter the amount to deposit"))
            self.new_amount = self.result[5] + self.amount
            self.val =(self.new_amount, self.receiver)
            cursor.execute(self.querry, self.val)
            myconn.commit()
            print(f"{self.amount} sent successfully to {self.result[1]}")

        else:
            print("No record matches your account number")
            self.deposit()
        
Bank()
