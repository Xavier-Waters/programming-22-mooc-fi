# Write your solution here
def distinct_numbers(list):
	list = sorted(list)
	list_distinct = []
	for x in range(len(list)):
	    if list[x] not in list_distinct:
	        list_distinct.append(list[x])
	return list_distinct
if __name__ == "__main__":
	my_list = [1, 2, 3, 5, 4, 4, 4, 4, 4, 4, 4, 5, 8, 4, 4, 4]
	print(distinct_numbers(my_list)) # [1, 2, 3]
