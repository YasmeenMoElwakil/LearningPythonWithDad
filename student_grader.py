score = input ("Enter your score (out of 100):")
score = float (score)
grade = ""


if score >= 90 and score <= 100 :
    grade = "A"
if score >= 80 and score <= 89 :
    grade = "B"
if score >= 70 and score <= 79 :
    grade = "C"
if score >= 60 and score <= 69 :
    grade = "D"
if score < 60:
    grade = "F"

print ("your grade is " + grade + " !")