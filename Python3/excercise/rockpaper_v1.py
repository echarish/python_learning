#ROCK PAPER SCISSOR
# ROCK beats SCISSOR
# SCISSOR beats PAPER
# PAPER beats ROCK


print("Please make a choice from ROCK, PAPER, SCISSOR : ")
player1_choice = input(" PLAYER 1 : ")
player2_choice = input(" PLAYER 2 : ")

if player1_choice and player2_choice :
	player1_choice = player1_choice.upper()
	player2_choice = player2_choice.upper()
	if player1_choice == player2_choice:
		print("Shoot you both selected same, GO AGAIN!")
	elif player1_choice == "ROCK":
		if player2_choice == "SCISSOR":
			print("Player 1 Wins!")
		elif player2_choice == "PAPER":
			print("Player 2 Wins!")
	elif player1_choice == "PAPER":
		if player2_choice == "SCISSOR":
			print("Player 2 Wins!")
		elif player2_choice == "ROCK":
			print("Player 1 Wins!")
	elif player1_choice == "SCISSOR":
		if player2_choice == "ROCK":
			print("Player 2 Wins!")
		elif player2_choice == "PAPER":
			print("Player 1 Wins!")
	print(f"Player 1 choose was {player1_choice} and Player 2 choose {player2_choice}")
else:
	print("Something is fishy, not a valid choice you are making")
