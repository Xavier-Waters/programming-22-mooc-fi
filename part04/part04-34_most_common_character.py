# Write your solution here
def most_common_character(string):
	list = []
	for char in string:
	    list.append(string.count(char))
	index = list.index(max(list))
	return string[index]
if __name__ == "__main__":
	print(most_common_character("exemplaryelementary"))
