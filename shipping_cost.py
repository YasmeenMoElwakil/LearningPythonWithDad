pounds = input ("Enter package weight (in pounds):")
method = input ("Enter shipping method (ground/air/express):")
total = 0
pounds = float (pounds)
if method == 'ground':
    total = pounds * 1.5
    if total < 5 :
        total = 5 
if method == 'air':
    total = pounds * 2.5
    if total < 10 :
        total = 10
if method == "express" :
    total = pounds * 5
    if total < 20 :
        total = 20
pounds = str (pounds)
total = str (total)

print ("shipping method : " + method)
print ("weight : " +  pounds)
print ("total shipping cost : $" + total )
