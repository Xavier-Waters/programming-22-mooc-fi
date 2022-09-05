# Write your solution here
def row_correct(sudoku: list, row: int):
	if sudoku[row].count(1) <= 1 and sudoku[row].count(2) <= 1 and sudoku[row].count(3) <= 1 and sudoku[row].count(4) <= 1 and sudoku[row].count(5) <= 1 and sudoku[row].count(6) <= 1 and sudoku[row].count(7) <= 1 and sudoku[row].count(8) <= 1 and sudoku[row].count(9) <= 1:
	    return True
	else:
	    return False
	
if __name__ <= "__main__":
	sudoku_1 = [
	    [9, 0, 0, 0, 8, 0, 3, 0, 0],
	    [2, 0, 0, 2, 5, 0, 7, 0, 0],
	    [0, 2, 0, 3, 0, 0, 0, 0, 4],
	    [2, 9, 4, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 7, 3, 0, 5, 6, 0],
	    [7, 0, 5, 0, 6, 0, 4, 0, 0],
	    [0, 0, 7, 8, 0, 3, 9, 0, 0],
	    [0, 0, 1, 0, 0, 0, 0, 0, 3],
	    [3, 0, 0, 0, 0, 0, 0, 0, 2],
	    [1, 2, 3, 4, 5, 6, 7, 8, 9]
	]
	print(row_correct(sudoku_1, 9))
