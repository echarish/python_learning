#ROCK PAPER SCISSOR
# ROCK beats SCISSOR
# SCISSOR beats PAPER
# PAPER beats ROCK
import random


def computerMove():
	VALID_MOVES = ["ROCK", "PAPER", "SCISSOR"]
	randomIndex = random.randint(0,2)
	return VALID_MOVES[randomIndex]

computer_win_count = 0
player_win_count = 0



continue_game = "y"

while continue_game == "y" :
	did_player_win = False
	print("Please make a choice from ROCK, PAPER, SCISSOR : ")
	player1_choice = input(" You : ")

	player2_choice = computerMove()

	if player1_choice and player2_choice :
		player1_choice = player1_choice.upper()
		player2_choice = player2_choice.upper()
		if player1_choice == player2_choice:
			print("Shoot you both selected same, GO AGAIN!")
		elif player1_choice == "ROCK":
			if player2_choice == "SCISSOR":
				did_player_win = True
			elif player2_choice == "PAPER":
				did_player_win = False
		elif player1_choice == "PAPER":
			if player2_choice == "SCISSOR":
				did_player_win = False
			elif player2_choice == "ROCK":
				did_player_win = True
		elif player1_choice == "SCISSOR":
			if player2_choice == "ROCK":
				did_player_win = False
			elif player2_choice == "PAPER":
				did_player_win = True
		
		if did_player_win:
			print("You Win!")
			player_win_count += 1
		else:
			print("Computer Win!")
			computer_win_count += 1

		print(f"You choose {player1_choice} and Computer choose {player2_choice}")
		print("\n ----------- Score Board --------- \n"  )
		print(f" Computer won : {computer_win_count}")
		print(f" Player   won : {player_win_count}")
		print("\n -------------------------------- \n")
		continue_game = input("Do you want to continue playing y/n : ")
		print("\n")
	else:
		print("Something is fishy, not a valid choice you are making")

