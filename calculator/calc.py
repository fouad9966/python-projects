# def add(num1,num2):
#     print(num1 + num2)

# def minus(num1,num2):
#     print(num1 - num2)

# def multiply(num1,num2):
#     print(num1 * num2)

# def divide(num1,num2):
#     print(num1 / num2)

# num1= float(input("First Value: ")) 
# num2= float(input("Second Value: ")) 

# choose= input(
# """
# Choose your operation:
# a. Add
# b. Subtract
# c. Multiply
# d. Divide
# """)
# if choose== "a":
#    print("The answer is: ")
#    add(num1,num2)
# elif choose== "b":
#     print("The answer is: ")
#     minus(num1,num2)
# elif choose== "c":
#     print("The answer is: ")
#     multiply(num1,num2)
# elif choose== "d":
#     print("The answer is: ")
#     divide(num1,num2)
# else:
#     print("Invalid operation")

info = {}
for i in range(7):
    information1 = input('Enter your name: ')
    information2 = input('Enter your address: ')
    info[information1] = information2
print(info)
questions = ("How many days are in a week?: ",
            "How many states do we have in Nigeria?: ",
            "How many colors are there in a rainbow?: ",
            "How old is Nigeria?: ",
            "What is the current fuel price?: ")
options = (("A. 7 ","B. 5","C. 8","D. 10 "),
                ("A. 28 ","B. 36 ","C. 50 ","D. 41"),
                ("A. 6 ","B. 5","C. 4","D. 7"),
                ("A. 60","B. 40 ","C. 67 ","D. 62 "),
                ("A. 580 ","B. 780 ","C. 150 ","D. 680 "))
answers = ("A", "B", "D", "D", "A")
score = 0
ques_numb = 0
guesses = []
for question in questions:
    print("------------------------")
    print(question)
    print(options[ques_numb])
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[ques_numb]:
       score += 10
       print("CORRECT")
    else:
       print("INCORRECT")
       print(f"{answers[ques_numb]} is the correct answer")
       score -= 5
    ques_numb += 1
print(score)


# import random 
# student_info = {}
# num_of_reg = input("Enter number to start registration or stop to quit: ").strip().lower()
# print("welcome to SQI")
# while num_of_reg != "stop":
#     student =[]
#     info = ["First_name", "middle_name", "Last_name", "Age", "Gender", "Address", "Phone_number"]
#     for x in info:
#         information = input(f"Enter your {x}: ").strip().capitalize()
#         while x == "Phone_number" and len(information) != 11:
#             information = input(f"Enter your {x}: ")
#         student.append(information)
#     std_reg_num = student[6][6:]
#     student.append(std_reg_num)
#     matric_num = random.randrange(200250,480450)
#     new_matric_num = "SQI/2019/" + str(matric_num)
#     student.append(new_matric_num)
#     student_info.update({num_of_reg : student})
#     num_of_reg = input("Enter number to start registration or stop to quit: ").strip().lower()
# else:
#     print("Thanks for shecking up on us!")
# print("Student Details are :\n", student_info)













import random 
student_info = {}
password = []
matric_regs = []
num_of_reg = input("Enter number to start registration or stop to quit: ").strip().lower()
print("welcome to SQI")
while num_of_reg != "stop":
    student =[]
    info = ["First_name", "middle_name", "Last_name", "Age", "Gender", "Address", "Phone_number"]
    for x in info:
        information = input(f"Enter your {x}: ").strip().capitalize()
        while x == "Phone_number" and len(information) != 11:
            information = input(f"Enter your {x}: ")
        student.append(information)
    std_reg_num = student[6][6:]
    student.append(std_reg_num)
    matric_num = random.randrange(200250,480450)
    new_matric_num = "SQI/2019/" + str(matric_num)
    matric_regs.append(new_matric_num)
    student.append(matric_regs)
    pwd = input("Enter your password: ")
    password.append(pwd)
    student.append(password)
    student_info.update({num_of_reg : student})
    num_of_reg = input("Enter number to start registration or stop to quit: ").strip().lower()
else:
    print("Thanks for shecking up on us!")
print("Student Details are :\n", student_info)
log = list(zip(matric_regs, password))

def cbt():
        import time
        score, nt = 0, 0


        questions = ["who is the president of Nigeria?\n", "where is zuma rock located in Nigeria?\n",
                     "when did Nigeria gain independence?\n"]
        
        options = ["a). Tinubu\n b). Atiku\n c). Obi\n",
                   "a). Oyo\n b). Ogun\n c). Abuja",
                   "a). 1980\n b). 1960 c). 1999"]
        
        answers = ["a", "c", "b"]

        name =input("Enter your name: ")
        print(f"Hello, {name}, Welcome to quit nation!!")
        for index, question in enumerate(questions, start=1):
             print(index,question)
        time.sleep(2)
        print()
        print(options[nt])
        student_answer = input("Enter your answer: ")
        if student_answer == answers[nt]:
             print("CORRECT!")
             score += 10
        else:
             print("FAILED!")
             score -= 5
        nt += 1
        time.sleep(2)
        print(f"final score is,{score}")

def calculator():
        val1 = float(input("Enter the first value: "))
        operation = input("""
                          Enter 1 to perform addition
                          Enter 2 to perform subtraction
                          Enter 3 to perform multiplication
                          Enter 4 to perform division: """)
        val2 = float(input("Enter the second value: "))
        if operation == 1:
             print(val1 + val2)
        elif operation == 2:
             print(val1 - val2)
        elif operation == 3:
             print(val1 * val2)
        elif operation == 4:
             print(val1 / val2)
        else:
             print("invalid operation")

def sett():
        s1, s2, s3 = [],[],[]

        for i in range(4):
             se1 = input("Enter number for the first set: ")
             se2 = input("Enter number for the second set: ")
             se3 = input("Enter number for the third set: ")
             s1.append(se1)
             s2.append(se2)
             s3.append(se3)
        set1, set2, set3 = set((s1)), set((s2)), set((s3))
        print(set1, set2, set3)
        operation = input(""" choose operation to perform
                          Enter 1 for union
                          Enter 2 for intersection
                          Enter 3 for symmetric difference: """)
        if operation == "1":
             set4 = set1.union(set2).union(set3)
             print(set4)
        elif operation == "2":
             set4 = set1.intersection(set2).intersection(set3)
             print(set4)
        elif operation == "3":
             print(set1.symmetric_difference(set2))
        else:
             print("invalid operation!")

def foodseller():
        value1 = str(input("which food is available? "))
        value1 = str(input("which of the protein is available "))

        food = "rice"
        protein = "egg"

        if food == "rice" and protein == "egg":
         print("i will buy rice and egg")
        else:
         print("i will not buy anything")

log_in = input("Do you want to login? (yes/no: )").strip().lower()
if log_in == "yes":
     uname = input("Enter your matric number: ")
     psword = input("Enter your password: ")
     while (uname,psword) in log:
          print("LOGIN SUCCESSFUL!")
          operation = input("Enter your preffered option (1. CBT 2. calculator 3. set operation 4. foodseller) or stop with 5")
          while operation != "stop":
               if operation == "1":
                    cbt()
                    break
               elif operation == "2":
                    calculator()
                    break
               elif operation == "3":
                    sett()
                    break
               elif operation == "4":
                    foodseller()
                    break
               else:
                    break

            
        
        

    