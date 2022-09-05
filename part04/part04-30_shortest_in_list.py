# Write your solution here
def shortest(list):
	shortest_list = []
	for x in range(len(list)):
	    shortest_list.append(len(list[x]))
	shortest = list[shortest_list.index(min(shortest_list))]
	return shortest
if __name__ == "__main__":
	my_list = [ "abaasd", "abc", "aaabdc"]
	result = shortest(my_list)
	print(result)
