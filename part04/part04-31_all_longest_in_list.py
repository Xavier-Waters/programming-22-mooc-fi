# Write your solution here
def all_the_longest(list):
	list_lengths = []
	list_modified = []
	list_final = []
	for shlonk in range(len(list)):
	    list_lengths.append(len(list[shlonk]))
	maximum = max(list_lengths)
	for shlonk in range(list_lengths.count(maximum)):
	    list_modified.append(list_lengths.index(maximum))
	    list_lengths[list_lengths.index(maximum)] = 0
	for shlonk in list_modified:
	    list_final.append(list[shlonk])
	return list_final
if __name__ == "__main__":
	my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
	result = all_the_longest(my_list)
	print(result)
