# Write your solution here
def list_sum(list_1, list_2):
	list_sum = []
	for x in range(0, len(list_1)):
	    list_sum.append(list_1[x] + list_2[x])
	return list_sum
if __name__ == "__main__":
	a = [1, 2, 3]
	b = [7, 8, 9]
	print(list_sum(a, b)) # [8, 10, 12]
