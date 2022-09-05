# Write your solution here
def length_of_longest(list):
	length_list = []
	for x in range(len(list)):
	    length_list.append(len(list[x]))
	return max(length_list)
if __name__ == "__main__":
	my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
	result = length_of_longest(my_list)
	print(result)
