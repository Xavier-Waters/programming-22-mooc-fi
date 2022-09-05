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
if __name__ == "__main__":
	sudoku = [
	[ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # row 0
	[ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # row 1
	[ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # row 2
	[ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],   # row 3
	[ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # row 4
	[ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # row 5
	[ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # row 6
	[ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # row 7
	[ 3, 0, 1, 0, 0, 8, 0, 0, 2 ],   # row 8
	]
	print(block_correct(sudoku, 0, 0))
	
	#print(block_correct(sudoku, 0, 0))
	#print(block_correct(sudoku, 6, 6))
