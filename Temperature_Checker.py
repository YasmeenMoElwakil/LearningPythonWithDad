'''
Problem: Temperature Checker

Write a program that asks the user for the current temperature in Fahrenheit and their name. 
The program should greet the user and tell them whether they should wear a jacket or not based on the temperature.

Requirements:
    If the temperature is 60 degrees or below, tell them to wear a jacket
    If the temperature is above 60 degrees, tell them they don't need a jacket
    Use the user's name in your responses
'''

name = input ("what is your name:")
temprature = input ("what is the temprature in Fehrenheit today:")

temprature = int (temprature)
print ("Hi " + name )
if temprature>60:
    print ("you don't need a jacket today")
else:
    print ("you need a jacket today")