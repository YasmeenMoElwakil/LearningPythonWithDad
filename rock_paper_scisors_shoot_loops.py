import random
choices = ["rock","paper","scisors"]
play_again = "yes"
while play_again == "yes" :
    player_choice = input ("(rock/paper/scisors):")
    computer_choice = random.choice(choices)
    if player_choice == computer_choice :
        print ("it is a tie")
    if player_choice == "rock" and computer_choice == "scisors" :
        print ("human win")
    if player_choice == "rock" and computer_choice == "paper" :
        print ("computer win")
    if player_choice == "paper" and computer_choice == "rock":
        print ("human win")
    if player_choice == "paper" and computer_choice == "scisors" :
        print ("computer win")
    if player_choice == "scisors" and computer_choice == "rock" :
        print ("computer win")
    if player_choice == "scisors" and computer_choice == "paper" :
        print ("human win")
    print("computer choice: " + computer_choice)
    print ("human choice: " + player_choice)
    play_again = input ("play again?(yes/no):")
print ("goodbye")