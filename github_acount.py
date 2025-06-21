name = input ("hi! what is your name:")
print ("hi "+ name + " !")
age = input ("how old are you " + name + " ?:")
age = int (age)
if age>= 13:
    print (name +" you can get a Github acount")
else:
    print ("sorry, " + name + " you can not get a Github acount")