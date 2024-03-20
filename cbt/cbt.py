import mysql.connector as connection
myconn= connection.connect(host = "127.0.0.1", user = "root", password = "Moneylion9966!", database = "cbt")
cursor = myconn.cursor()
class cbt:
    def __init__(self):
        print ("you are welcome")
        self.start()

    def start (self):
        self.decision = input("which operation will you like to perform\n enter 1 to register\n enter 2 to login: ")
        if self.decision == "1":
            self.register()
        elif self.decision == "2":
            self.login()
        else:
            print("you have to register or login to proceed")
            self.start()

    def register(self):
        self.name = input("enter your full name: ").title()
        self.username = input("enter your username: ")
        self.password = input("enter your password: ")
        self.score = 0
        self.age = input("enter your age: ")
        self.gender = input("enter your gender: ")
        self.verify()
    
    def verify(self):
        self.querry = "insert into Student_info(name, username, password, age, gender, score) value( %s, %s, %s, %s, %s, %s)"
        self.val =(self.name, self.username, self.password, self.age, self.gender, self.score)
        cursor.execute(self.querry, self.val)
        myconn.commit()
        print("Registration successful")
        # self.login()

    def login(self):
        self.user = input("enter your username: ")
        self.pwd = input("enter your password: ")
        self.querry = "SELECT * FROM Student_info where username = %s "
        self.val = (self.user,)
        cursor.execute(self.querry, self.val)
        self.result = cursor.fetchone()
        if self.user == self.result[2] and self.pwd == self.result[3]:
            print("successfully logged in")
            # self.cbtquestion()
        else:
            print("login failed")
            self.login()

    # def cbtquestion(self):
    #         print("are you ready for your cbt exam")
            # self.student = input("enter yes to start: ")
            # if self.student == "yes":
            #     self.questions = ("How many days are in a week?: ",
            #         "How many states do we have in Nigeria?: ",
            #         "How many colors are there in a rainbow?: ",
            #         "How old is Nigeria?: ",
            #         "What is the current fuel price?: ")
            #     self.options = (("A. 7 ","B. 5","C. 8","D. 10 "),
            #                     ("A. 28 ","B. 36 ","C. 50 ","D. 41"),
            #                     ("A. 6 ","B. 5","C. 4","D. 7"),
            #                     ("A. 60","B. 40 ","C. 67 ","D. 62 "),
            #                     ("A. 580 ","B. 780 ","C. 150 ","D. 680 "))
            #     self.answers = ("A", "B", "D", "D", "A")
            #     self.score = 0
            #     self.ques_numb = 0
            #     for question in self.questions:
            #         print(question)
            #         print(self.options[self.ques_numb])
            #         ans = input("Enter (A, B, C, D): ").upper()
            #         if ans == self.answers[self.ques_numb]:
            #             self.score += 10
            #             print("CORRECT")
            #         else:
            #             print("INCORRECT")
            #             print(f"{self.answers[self.ques_numb]} is the correct answer")
            #         self.score -= 5
            #         self.ques_numb += 1
            #     print(self.score)
            # else:
            #     print("thank you")
            #     self.login()



cbt()