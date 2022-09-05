# Write your solution here
def row_correct(sudoku: list, row: int):
	if sudoku[row].count(1) <= 1 and sudoku[row].count(2) <= 1 and sudoku[row].count(3) <= 1 and sudoku[row].count(4) <= 1 and sudoku[row].count(5) <= 1 and sudoku[row].count(6) <= 1 and sudoku[row].count(7) <= 1 and sudoku[row].count(8) <= 1 and sudoku[row].count(9) <= 1:
	    return True
	else:
	    return False
def column_correct(sudoku: list, column: int):
	column_list = []
	for x in range(len(sudoku)):
	    column_list.append(sudoku[x][column])
	if column_list.count(1) <= 1 and column_list.count(2) <= 1 and column_list.count(3) <= 1 and column_list.count(4) <= 1 and column_list.count(5) <= 1 and column_list.count(6) <= 1 and column_list.count(7) <= 1 and column_list.count(8) <= 1 and column_list.count(9) <= 1:
	    return True
	else:
	    return False
# Write your solution here
def block_correct(sudoku: list, row: int, column: int):
	block = []
	results = []
	block_2 = []
	for x in range(row+3):
	    y = sudoku[x]
	    block.append(y[column:column+3])#[column:column+2])
	for x in range(len(block)-3):
	    block[x] = " "
	for x in range(block.count(" ")):
	    block.remove(" ")
	for x in range(len(block)):
	    for number in block[x]:
	        block_2.append(number)
	for x in range(len(block)):
	    if block_2.count(1) <= 1 and block_2.count(2) <= 1 and block_2.count(3) <= 1 and block_2.count(4) <= 1 and block_2.count(5) <= 1 and block_2.count(6) <= 1 and block_2.count(7) <= 1 and block_2.count(8) <= 1 and block_2.count(9) <= 1:
	        return True
	    else:
	        return False
def sudoku_grid_correct(sudoku):
	results_list = []
	for x in range(9):
	    results_list.append(row_correct(sudoku, x))
	    results_list.append(column_correct(sudoku, x))
	for x in range(0, 9, 3):
	    for y in range(0, 9, 3):
	        results_list.append(block_correct(sudoku, x, y))
	if results_list.count(False) == 0:
	    return True
	else:
	    return False
	
if __name__ == "__main__":
	sudoku1 = [
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
	
	print(sudoku_grid_correct(sudoku1))
	
	sudoku2 = [
	[2, 6, 7, 8, 3, 9, 5, 0, 4],
	[9, 0, 3, 5, 1, 0, 6, 0, 0],
	[0, 5, 1, 6, 0, 0, 8, 3, 9],
	[5, 1, 9, 0, 4, 6, 3, 2, 8],
	[8, 0, 2, 1, 0, 5, 7, 0, 6],
	[6, 7, 4, 3, 2, 0, 0, 0, 5],
	[0, 0, 0, 4, 5, 7, 2, 6, 3],
	[3, 2, 0, 0, 8, 0, 0, 5, 7],
	[7, 4, 5, 0, 0, 3, 9, 0, 1]
	]
	
	print(sudoku_grid_correct(sudoku2))
	
	sudoku3 = [
	[ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
	[ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
	[ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
	[ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
	[ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
	[ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
	[ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
	[ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
	[ 0, 8, 0, 4, 6, 3, 5, 7, 1 ]
	]
	print(sudoku_grid_correct(sudoku3))
