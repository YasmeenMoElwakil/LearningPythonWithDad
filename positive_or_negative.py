number = input ("enter a number:")
number = float (number)
number_anwser = 0
if number == 0:
    number_anwser = "zero"
if number > 0 :
    number_anwser = "positive"
if number < 0:
    number_anwser = "negative"
number_anwser = str (number_anwser)
print ("number is " + number_anwser + "!")
print ("thanks for using positive_or_negative.py to make sure that the number is positive or negative or even zero !")