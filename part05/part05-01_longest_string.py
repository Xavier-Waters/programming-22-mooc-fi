# Write your solution here
def longest(list: list):
	length_list = []
	for x in range(len(list)):
	    length_list.append(len(list[x]))
	index = length_list.index(max(length_list))
	return list[index]
