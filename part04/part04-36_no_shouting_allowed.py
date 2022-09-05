def no_shouting(list):
	list_modified = []
	for i in range(len(list)):
	    if list[i].isupper() == False:
	        list_modified.append(list[i])
	return list_modified
if __name__ == "__main__":
	my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
	pruned_list = no_shouting(my_list)
	print(pruned_list)
