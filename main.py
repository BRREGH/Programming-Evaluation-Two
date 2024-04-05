# -------------------------------- QUESTION 1 -----------------------------------------------
#Create a program that asks the user to input their grade for Course 1, Course 2, Course 3 and Course 4. The program should take the 4 course grades and calculate the average. Once the average is calculated, determine the overall letter grade for the student.

#inputs that ask for the user's grades
course1 = int(input("Enter your grade for course 1: "))
course2 = int(input("Enter your grade for course 2: "))
course3 = int(input("Enter your grade for course 3: "))
course4 = int(input("Enter your grade for course 4: "))

#Calculates average based on user input
average = (course1 + course2 + course3 + course4) / 4

#if statements that determine the letter grade based on the average
#All A letter grades
if average <= 100 and average >= 95:
    print("Your average is:", average, "your grade is an A+")
elif average <= 94 and average >= 87:
    print("Your average is:", average, "your grade is an A")
elif average < 87 and average >= 80:
    print("Your average is:", average, "your grade is an A-")


#All B letter grades
if average <= 80 and average > 77:
    print("Your average is:", average, "Your grade is a B+")
elif average <= 76 and average > 72:
    print("Your average is:", average, "your grade is a B")
elif average <= 71 and average > 70:
    print("Your average is:", average, "your grade is a B-")


#All C letter grades
if average <= 70 and average > 67:
    print("Your average is:", average, "your grade is a C+")
elif average <= 66 and average > 63:
    print("Your average is:", average, "your grade is a C")
elif average <= 62 and average > 60:
    print("Your average is:", average, "your grade is a C-")


#All D letter grades
if average <= 60 and average > 57:
    print("Your average is:", average, "your grade is a D+")
elif average <= 56 and average > 54:
    print("Your average is:", average, "your grade is a D")
elif average <= 53 and average > 50:
    print("Your average is:", average, "your grade is a D-")


#All F letter grades
if average <= 50 and average > 0:
    print("Your average is:", average, "your grade is an F, you failed!")
