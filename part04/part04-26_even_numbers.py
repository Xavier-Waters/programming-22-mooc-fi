# Write your solution here
def even_numbers(list):
	list_even = []
	for i in range(len(list)):
	    if list[i] % 2 == 0:
	        list_even.append(list[i])
	return list_even
	
if __name__ == "__main__":
	my_list = [1, 2, 3, 4, 5]
	new_list = even_numbers(my_list)
	print("original", my_list)
	print("new", new_list)
