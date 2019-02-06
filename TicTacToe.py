import itertools




def win(current_game):

	#horizontal winner
	for row in game :
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"Player {row[0]}  is the winner horizontally ")
			return True

	#vertical winner 
	for col in range(len(game)):
		col_check = []

		for row in game:
			col_check.append(row[col])

		if col_check.count(col_check[0]) == len(col_check) and col_check[0] != 0:
			print(f"Player {col_check[0]} is the winner vertically")
			return True

	#diagonal winner
	diags=[]
	for index in range(len(game)):
			diags.append(game[index][index])

	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
			print(f"Player {diags[0]} is the winner diagonally")
			return True

	diags=[]
	for col, row in enumerate(reversed(range(len(game)))):
	 	diags.append(game[row][col])

	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
			print(f"Player {diags[0]} is the winner diagonally")
			return True

	return False



def game_board(game_map, player=0, row=0, col=0, display=False):
	try:
		if(game_map[row][col]!= 0):
			print("position already occupied")
			
			return game_map, False
		print("   0, 1, 2")
		
		if not display:
			game_map[row][col] = player
			for count, row in enumerate(game_map):
				print(count, row)	
		return game_map, True	

	except Exception as e:
		print("Error has occured", e)
		return game_map, False


play = True
players = [1,2]
while play:
	game = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]

	game_won=False
	next_play = True
	game, next_play = game_board(game)
	player_move = itertools.cycle(players)
	

	while not game_won:

		if next_play:
			current_player = next(player_move)

		row_choice = int(input("Enter the row of choice: (0,1,2)? "))
		column_choice = int(input("Enter the column of choice: (0,1,2)? "))
		game , next_play = game_board(game, current_player, row_choice, column_choice)
		
		if win(game):
			game_won = True
			play_again = input("Another round? y/n")
			if play_again.upper() == 'Y':
				print("RESTART")
			elif play_again.upper() == 'N':
				play = False
				print("GAME OVER")
			else :
				print("Invalid choice")

		



	
 