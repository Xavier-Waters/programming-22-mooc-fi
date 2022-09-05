# Write your solution here
def count_matching_elements(matrix: list, element: int):
	count = 0
	for x in range(len(matrix)):
	    count += matrix[x].count(element)
	return count
if __name__ == "__main__":
	m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
	print(count_matching_elements(m, 1))
