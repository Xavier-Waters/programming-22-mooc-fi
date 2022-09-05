# Write your solution here
# You can test your function by calling it within the following block
def mean(list):
	length = len(list)
	list_sum = sum(list)
	return list_sum / length
if __name__ == "__main__":
	my_list = [1, 2, 3, 4, 5]
	result = mean(my_list)
	print(result)
