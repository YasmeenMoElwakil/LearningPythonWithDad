dog = "dog"
cat = "cat"
lion = "lion"
polar_bear = "polar bear"
yes_or_no = "yes"
while yes_or_no == "yes":
    animal = input ("what is your favorite animal:")
    if animal == dog :
        print ("dogs are born def")
    if animal == cat :
        print ("cats have more than 500 muscles and more than 200 bones")
    if animal == lion :
        print ("darker manes are more likely to atract female lions")
    if animal == polar_bear : 
        print ("despite being classified as bears, polar bears are considered marine mammals")
    if animal != dog and animal != cat and animal!= lion and animal != polar_bear :
        print ("I have no fun facts about that animal")
    yes_or_no = input ("do you want to learn about a different animal(yes/no):")
print ("thanks for using")