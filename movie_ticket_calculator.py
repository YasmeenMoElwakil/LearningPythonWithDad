age = input ("enter your age:")
time_of_day = input ("enter time of day(morning/afternoon/evening):")
week = input ("enter the week (weekday/weekend):")
ticket_price = 0
age = float (age)
if age < 12:
    ticket_price = 5
if age >= 12 and age < 64 and time_of_day == "morning" and week == "weekday":
    ticket_price = 10
if age >= 12 and age < 64 and time_of_day == "afternoon" and week == "weekday":
    ticket_price = 10
if age >= 12 and age < 64 and time_of_day == "evening" and week == 'weekday':
    ticket_price = 15
if age >= 12 and age < 64 and time_of_day == "morning" and week == 'weekend':
    ticket_price = 15
if age >= 12 and age < 64 and time_of_day == 'afternoon' and week == 'weekend':
     ticket_price = 15
if age >= 12 and age < 64 and time_of_day == 'evening'and  week == 'weekend':
     ticket_price = 20
if age >= 65:
    ticket_price = 8
ticket_price = str (ticket_price)
print ("Your ticket price is: $" + ticket_price + ".00")