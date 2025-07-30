#Assignment: Bookstore Sales
#Create a Python program that calculates the total sales of a bookstore over a period of days. #The program should:
# 1.Ask the user for the number of days.
# 2.Use a for loop to iterate over each day.
# 3.For each day, ask the user for the number of books sold and the price per book.
# 4.Calculate the total sales for each day by multiplying the number of books sold by the price per book.
# 5.Use an accumulator variable to store the total sales over all days.
# 6.After the loop, print out the total sales.
#Example Output:

#Enter the number of days: 2
#Day 1:
#Enter number of books sold: 10
#Enter price per book: 20
#Day 2:
#Enter number of books sold: 15
#Enter price per book: 25
#The total sales are: 575


total_sale = 0
days = input ("Enter number of days:")
days = int (days)
for day_number in range (0,days) :
    day_number = str (day_number)
    print ("day " + day_number + ":")
    books_sold = input ("Enter number of books sold:")
    price_per_book = input ("Enter price per book:")
    books_sold = int(books_sold)
    price_per_book = float (price_per_book)
    total_sale = total_sale + (price_per_book * books_sold)

total_sale = str (total_sale)
print ("The total sales are:" + total_sale)
