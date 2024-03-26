import mysql.connector as connection
import random
import sys
conn= connection.connect(host ="127.0.0.1", user = 'root', password ="Moneylion9966!", database = "Voting")
cursor = conn.cursor()
class vote:
    def __init__(self):
        self.dept = ["Datascience", "DataAnalysis", "Web_Development", "Cyber_Security", "UI_UX", "Graphic_Design", "Javascript"]
        self.president = ["Seun Adeowo","God Man", "Olanrewaju Afolabi"]
        self.v_president = ["NA Wire","Mary Bells","Oluwanishola Afolabi"]
        self.gen_sec = ["Mountain Dew","Wellsfargo Chase","Cunt Dick"]
        self.start()
    # The variable self.dept is a list of available departments in SQI
    # The variable self.president is a list of selected SQI students to be voted for as president
    # The varibale self.v_president is a list of selected SQI students to be voted for as vice president
    # The varibale self.gen_sec is a list of selected SQI students to be voted for as general secretary
   
    def start(self):
        print("Welcome to SQI")
        self.choose = input("Enter 1 to Register \n Enter 2 to Login: ")
        if self.choose == "1":
            self.register()
        elif self.choose == "2":
            self.login()
        else:
            print("Invalid selection")
            self.start()

    def register(self):
        self.userinput = input(f"Select your Department: {self.dept} ")
        while self.userinput not in self.dept:
            print("department not available")
            self.userinput = input(f"Select your Department: {self.dept} ")
        else:
            self.fname = input("Enter your first name: ")
            self.lname = input("Enter your last name: ")
            self.gender = input("Enter your Gender: ")
            self.level = int(input("Enter your Level: "))
            self.username = input("Enter your username: ")
            self.pwd = input("Enter your password: ")
            self.mat = random.randrange(23200,26100)
            self.userquery = f"INSERT into {self.userinput} (FirstName, LastName, Gender, level, Username, Password, Matric_Number) VALUES({'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'},{'%s'}, {'%s'}) "
            self.insert = (self.fname, self.lname, self.gender, self.level, self.username, self.pwd, self.mat)
            cursor.execute(self.userquery, self.insert)
            conn.commit()
            print(f"Your registration is successful and your matric number is {self.mat}")
            
    # this function is to register into the selected departmental database 
    
    def login(self):
        self.userinput = input(f"Enter your Department: {self.dept}: ")
        if self.userinput in self.dept:
            self.userid = input("Enter your username: ")
            self.userpd = input("Enter your password: ")
            self.inquery = f"select * from {self.userinput} where Username = {'%s'} and Password = {'%s'}"
            self.inval = (self.userid, self.userpd)
            cursor.execute(self.inquery, self.inval)
            self.result = cursor.fetchone()
            if self.result is not None:
                print("You have logged in successfully")
                self.operation()
            else:
                print("invalid login details")
                self.login()
    # this function is to login into the SQI departments to be able to perform other functions

    def operation(self):
        self.vote = input("Welcome, which of the following operation will you like to perform?\n 1 Register to voting platform \n 2 Cast your vote\n 3 Check your vote result: ")
        if self.vote == "1":
            self.registervote()
        elif self.vote == "2":
            self.check_vote()
        elif self.vote == "3":
            self.check_winner()
        else:
            print("Invalid selection")
            self.operation()

    def registervote(self):
        self.votersreg = input("Enter your Matric number to proceed: ")
        self.regdep = input("Enter your Department: ")
        if self.regdep in self.dept:
            self.votequery = f"SELECT * from {self.regdep} where Matric_Number = {'%s'}"
            self.voteval = (self.votersreg,)
            cursor.execute(self.votequery, self.voteval)
            self.voteresult = cursor.fetchone()
            if self.voteresult is not None:
                self.voters_card = random.randrange(41200,45000)
                self.fulln = self.voteresult[1] + " " + self.voteresult[2]
                self.lvl = self.voteresult[4]
                self.votequerry = "insert into Voters (voters_card, FullName, level, Department, Matric_Number, President, Vice_president, Gen_Sec) values(%s, %s, %s, %s, %s, %s, %s, %s)"
                self.vote_val = (self.voters_card, self.fulln, self.lvl, self.regdep, self.votersreg, "nill", "nill", "nill")
                cursor.execute(self.votequerry, self.vote_val)
                conn.commit()
                print(f"Your registration is successful, and your voters card number is {self.voters_card}")
                self.check_vote()
        else:
            print("Department entered not found")
    # The registervote function is used to register into the voting platform and random was used to generate random voter's card number 

    def check_vote(self):
        self.castvote = int(input("Enter your voter's card number: "))
        self.castvotequerry = "select * from Voters where voters_card = %s"
        self.castvoteval = (self.castvote,)
        cursor.execute(self.castvotequerry, self.castvoteval)
        self.castresult = cursor.fetchone()
        self.cast()
    
    def cast(self):
        if self.castresult is not None:
            self.castchoose = input("Enter\n 1 for President\n 2 for Vice-President\n 3 for General Secretary: ")
            if self.castchoose == "1":
                if self.castresult[5] != "nill":
                    print("You have already voted in this category")
                    self.cast()
                    # This loop is to avoid voters to be able to vote twice in the president category
                else:
                    print(f"These are the candidates avaliable to be voted for: {self.president}")
                    self.castcan = input("Enter the candidate of your choice: ")
                    while self.castcan not in self.president:
                        print("Candidate selected is not among the listed candidates")
                        self.castcan = input("Enter the candidate of your choice: ")
                    else:
                        self.castquerry = "update Voters set President = %s where voters_card = %s"
                        self.castval = (self.castcan, self.castvote)
                        cursor.execute(self.castquerry,self.castval)
                        conn.commit()
                        print(f"You have successfully voted for {self.castcan} ")
            elif self.castchoose == "2":
                if self.castresult[6] != "nill":
                    print("You have already voted in this category")
                    self.cast()
                else:
                    print(f"These are the candidates available to be voted for: {self.v_president}")
                    self.castcanv = input("Enter the candidate of your choice: ")
                    while self.castcanv not in self.v_president:
                        print("Candidate selected is not among the listed candidates")
                        self.castcanv = input("Enter the candidate of your choice: ")
                    else:
                        self.castquery = "update Voters set Vice_president = %s where voters_card = %s"
                        self.castvval = (self.castcanv, self.castvote)
                        cursor.execute(self.castquery, self.castvval)
                        conn.commit()
                        print(f"You have successfully voted for {self.castcanv}")
            elif self.castchoose == "3":
                if self.castresult[7] != "nill":
                    print("You have already voted in this category")
                    self.cast()
                else:
                    print(f"These are the candidates available to be voted for: {self.gen_sec}")
                    self.castcang = input("Enter the candidate of your choice: ")
                    while self.castcang not in self.gen_sec:
                        print("Candidate selected is not among the listed candidates")
                        self.castcang = input("Enter the candidate of your choice: ")
                    else:
                        self.castgquerry = "update Voters set Gen_Sec = %s where  voters_card = %s"
                        self.castgval = (self.castcang, self.castvote)
                        cursor.execute(self.castgquerry, self.castgval)
                        conn.commit()
                        print(f"You have successfully voted for {self.castcang}")
            else:
                print("invalid selection")
                self.cast()
        # This function allows a voter to only vote once in a category 
    
    def check_winner(self):
        self.checkv =input("Enter 1 to view the General Result\n Enter 2 to view your Departmental Result \n Enter 3 to go back to the Voting platform \n Enter 4 to exit: ")
        print(self.checkv)
        if self.checkv == "1":
            self.over =input("What category will you like to view \n 1 President \n 2 Vice-president \n 3 General Secretary: ")
            if self.over == "1":
                for x in self.president:
                    self.checkquery = "select count(President) from voters where President = %s"
                    self.checkval = (x,)
                    cursor.execute(self.checkquery, self.checkval)
                    self.resultt = cursor.fetchone()
                    print(f"{x} has {self.resultt[0]} votes")
            elif self.over == "2":
                for y in self.v_president:
                    self.checkvquery = "select count (Vice_president) from voters where Vice_president = %s "
                    self.checkvval = (y,)
                    cursor.execute(self.checkvquery, self.checkvval)
                    self.resultt = cursor.fetchone()
                    print(f"{y} has {self.resultt[0]} votes")
            elif self.over == "3":
                for z in self.gen_sec:
                    self.checkgquery = " select count (Gen_Sec) from voters where Gen_Sec = %s"
                    self.checkgval = (z,)
                    cursor.execute(self.checkgquery, self.checkgval)
                    self.resultt = cursor.fetchone()
                    print(f"{z} has {self.resultt[0]} votes")
        elif self.checkv == "2":
            self.userinput = input(f"Enter the Department to view: {self.dept} ")
            while self.userinput not in self.dept:
                print("department not available")
                self.userinput = input(f"Select your Department: {self.dept} ")
            else:
                self.over =input("What category will you like to view \n 1 President \n 2 Vice-president \n 3 General Secretary \n 4 Go back to hompage: ")
                if self.over == "1":
                    for x in self.president:
                        self.checkquery = "select count(President) from voters where President = %s and Department = %s"
                        self.checkval = (x, self.userinput)
                        cursor.execute(self.checkquery, self.checkval)
                        self.resultt = cursor.fetchone()
                        print(f"{x} has {self.resultt[0]} votes in {self.userinput} department ")
                elif self.over == "2":
                    for y in self.v_president:
                        self.checkvquery = "select count (Vice_president) from voters where Vice_president = %s and Department = %s"
                        self.checkvval = (y, self.userinput)
                        cursor.execute(self.checkvquery, self.checkvval)
                        self.resultt = cursor.fetchone()
                        print(f"{y} has {self.resultt[0]} votes in {self.userinput} department ")
                elif self.over == "3":
                    for z in self.gen_sec:
                        self.checkgquery = " select count (Gen_Sec) from voters where Gen_Sec = %s and Department = %s"
                        self.checkgval = (z, self.userinput)
                        cursor.execute(self.checkgquery, self.checkgval)
                        self.resultt = cursor.fetchone()
                        print(f"{z} has {self.resultt[0]} votes in {self.userinput} department ")
                elif self.over == "4":
                    self.start()
                else:
                    "Thank you for viewing the results"
        elif self.checkv == "3":
            self.cast()
        elif self.checkv == "4":
            self.start()
        else:
            "Thank you for your time...Remember SQI is No 1 Tech School in Nigeria"
    # this function is to check the result of the president,vice president and the gen_sec
        
vote()      