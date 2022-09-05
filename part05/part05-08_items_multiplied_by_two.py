def double_items(numbers: list):
	copy = []
	for item in numbers:
	    copy.append(item*2)
	return copy
if __name__ == "__main__":
	numbers = [2, 4, 5, 3, 11, -4]
	numbers_doubled = double_items(numbers)
	print("original:", numbers)
	print("doubled:", numbers_doubled)
