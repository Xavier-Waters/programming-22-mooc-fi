# Write your solution here
def sum_of_positives(list):
	list_positive = []
	for i in range(0,len(list)):
	    if list[i] > 0:
	        list_positive.append(list[i])
	    print(list_positive)
	return sum(list_positive)
if __name__ == "__main__":
	list = [1, -1, 2, -2, 3, -3]
	result = sum_of_positives(list)
	print("The result is", result)
