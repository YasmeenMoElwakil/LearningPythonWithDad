price = input ("price:")
dicount = input ("enter dicount(regular/ premuim / VIP):")
price = float (price) 
if dicount == "regular":
    price = price
if dicount == "premuim" :
    price = price / 10
if dicount == 'VIP':
    price = price /  20
price = str (price)
print ("your price: " + price + " !")
print ("have a nice day")