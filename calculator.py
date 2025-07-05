operation = input ("what is the operation:")
first_number = input ("what is the first number:")
second_number = input ("what is the second number:")
first_number = float (first_number)
second_number = float (second_number)
if  operation == '+':
    result = first_number + second_number
if operation == '-':
    result = first_number - second_number
if operation == '*':
    result = first_number * second_number
if operation == '/':
    result = first_number / second_number
result = str (result)
print ("the result is " + result + " ! corect?")