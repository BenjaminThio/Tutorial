GameOver = False
Player = False
Board = ["🟡" for i in range(9)]
Symbol = ["❌", "⭕️"]

while not GameOver:
	Position = input("Please type a number between 1-9: ")
	if Position.isdigit() and int(Position) > 0 and int(Position) <= 10:
		Board[int(Position) - 1] = Symbol[int(Player)]
		print(f"{Board[0]}{Board[1]}{Board[2]}\n{Board[3]}{Board[4]}{Board[5]}\n{Board[6]}{Board[7]}{Board[8]}")
	else: continue
	if Board[0] == Board[1] == Board[2] == Symbol[int(Player)] or Board[3] == Board[4] == Board[5] == Symbol[int(Player)] or Board[6] == Board[7] == Board[8] == Symbol[int(Player)] or Board[0] == Board[3] == Board[6] == Symbol[int(Player)] or Board[1] == Board[4] == Board[7] == Symbol[int(Player)] or Board[2] == Board[5] == Board[8] == Symbol[int(Player)] or Board[0] == Board[4] == Board[8] == Symbol[int(Player)] or Board[2] == Board[4] == Board[6] == Symbol[int(Player)]:
		print(f"Game Over! Player {int(Player) + 1} wins!")
		GameOver = True
	elif "🟡" not in Board:
		print("Game Over! It was a tie!")
		GameOver = True
	Player = not Player