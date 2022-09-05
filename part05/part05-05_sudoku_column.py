# Write your solution hereA
def column_correct(sudoku_list: list, column: int):
	column_list = []
	for x in range(len(sudoku_list)):
	    column_list.append(sudoku_list[x][column])
	if column_list.count(1) <= 1 and column_list.count(2) <= 1 and column_list.count(3) <= 1 and column_list.count(4) <= 1 and column_list.count(5) <= 1 and column_list.count(6) <= 1 and column_list.count(7) <= 1 and column_list.count(8) <= 1 and column_list.count(9) <= 1:
	    return True
	else:
	    return False
	
if __name__ == "__main__":
	sudoku = [
	    [9, 0, 0, 0, 8, 0, 3, 0, 0],
	    [2, 0, 0, 2, 5, 0, 7, 0, 0],
	    [0, 2, 0, 3, 0, 0, 0, 0, 4],
	    [2, 9, 4, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 7, 3, 0, 5, 6, 0],
	    [7, 0, 5, 0, 6, 0, 4, 0, 0],
	    [0, 0, 7, 8, 0, 3, 9, 0, 0],
	    [0, 0, 1, 0, 0, 0, 0, 0, 3],
	    [3, 0, 0, 0, 0, 0, 0, 0, 2]
	]
	
	print(column_correct(sudoku, 0))
	print(column_correct(sudoku, 1))
