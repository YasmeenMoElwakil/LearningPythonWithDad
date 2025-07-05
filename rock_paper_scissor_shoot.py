player_1_choice = input ("player 1,pick one (rock/paper/scissor):")
player_2_choise = input ("player 2,pick one (rock/paper/scissor):")

if player_1_choice == player_2_choise:
    print ("it's a tie")
if player_1_choice == "rock" and player_2_choise == "paper":
    print ("player 2, you win")
if player_1_choice == "rock" and player_2_choise == "scissor":
    print ("player 1, you win")
if player_1_choice == "paper" and player_2_choise == "rock":
    print ("player 1, you win")
if player_1_choice == "paper" and player_2_choise == "scissor":
    print ("player 2, you win")
if player_1_choice == "scissor" and player_2_choise == "rock":
    print ("player 2, you win")
if player_1_choice == "scissor" and player_2_choise == "paper":
    print ("player 1, you win")