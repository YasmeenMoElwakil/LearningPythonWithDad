#Assignment: Grade Calculator
#In this assignment, you will create a Python program that calculates the grades of multiple students based on their scores in Math, Science, and English.

#What is an Average?
#An average is a way to calculate the middle value of a set of numbers. It's calculated by adding up all the numbers and then dividing by how many numbers there are. For example, if you have scores of 90, 85, and 95, the average would be:
#(90 + 85 + 95) / 3 = 90

#What is a Letter Grade?
#A letter grade is a way to show how well a student did based on their average score. The grading scheme used in this assignment is:
#A: 90-100 (Excellent)
#B: 80-89 (Good)
#C: 70-79 (Fair)
#D: 60-69 (Passing)
#F: below 60 (Failing)
#The letter grade is determined by looking at the average score and matching it to the corresponding grade range.

#Your Task:
#Create a Python program that calculates the grades of multiple students based on their scores in Math, Science, and English. The program should:
#Ask the user for the number of students.
#Use a for loop to iterate over each student.
#For each student, ask the user for the student's name and scores in Math, Science, and English.
#Calculate the average score for each student by adding up the scores and dividing by 3.
#Determine the letter grade based on the average score using the grading scheme above.
#Print out each student's name, average score, and letter grade.
#Example Output:

#Enter the number of students: 2
#Enter student's name: John
#Enter Math score: 90
#Enter Science score: 85
#Enter English score: 95
#John's average score is 90.0
#John's grade is A

#Enter student's name: Jane
#Enter Math score: 70
#Enter Science score: 75
#Enter English score: 80
#Jane's average score is 75.0
#Jane's grade is C

the_sum_of_averages = 0
number_of_students = input ("Enter number of students:")
number_of_students = int (number_of_students)
for student_number in range (0,number_of_students):
    name = input ("Enter student name:")
    math = input ("Enter math score:")
    science = input ("Enter science score:")
    english = input ("Enter english score:")
    math = float (math)
    science = float(science)
    english = float(english)
    average = (math + science + english) / 3
    the_sum_of_averages = the_sum_of_averages + average # accumalator
    letter_grade = ""
    if average <= 100 and average > 89 :
         letter_grade = "A"
    if average <= 89 and average > 79 :
        letter_grade = "B"
    if average <= 79 and average >69 :
        letter_grade = "C"
    if average <= 69 and average > 59 :
        letter_grade = "D"
    if average < 60 :
        letter_grade = "F"
    print (name + "'s grade is " + letter_grade)
    average = str (average)
    print (name +"'s average score is " + average)
   # After calculating the grades for all students, calculate the overall average score of all students by summing up their individual average scores and dividing by the total number of students, then print out the result.
average_of_the_averages = the_sum_of_averages / number_of_students
average_of_the_averages = str (average_of_the_averages)
print ("the overall average is " + average_of_the_averages)