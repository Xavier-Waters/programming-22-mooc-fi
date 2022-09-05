# Write your solution here
def everything_reversed(list):
	list_modified = []
	list_modified_2 = []
	for x in range(len(list)):
	    string = list[x]
	    list_modified.append(string[::-1])
	for x in range(len(list_modified), 0, -1):
	    list_modified_2.append(list_modified[x-1])
	return list_modified_2
if __name__ == "__main__":
	my_list = ["Hi", "there", "example", "one more"]
	new_list = everything_reversed(my_list)
	print(new_list)
