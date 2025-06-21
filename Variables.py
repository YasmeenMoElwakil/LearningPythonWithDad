currant_year = input("what is the currant year?: ")
currant_year = int(currant_year) 
name = input("Enter your name: ") 
print("Hello, " + name + "!")

year_of_birth = input("Enter your year of birth: ")
year_of_birth = int(year_of_birth)
age = currant_year - year_of_birth
age = str(age) 
print("So your name is " + name + " and you are " + age + " years old, correct?") 