# Write your solution here
def who_won(game_board: list):
	count_1 = 0
	count_2 = 0
	for x in range(len(game_board)):
	    count_1 += game_board[x].count(1)
	    count_2 += game_board[x].count(2)
	if count_1 > count_2:
	    return 1
	elif count_2 > count_1:
	    return 2
	else:
	    return 0
	
if __name__ == "__main__":
	board = [
	    [2, 1, 1, 2, 1, 1, 1, 0, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 0],
	    [2, 1, 1, 2, 1, 1, 1, 0, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 0, 1, 1]
	]
	print(who_won(board))
