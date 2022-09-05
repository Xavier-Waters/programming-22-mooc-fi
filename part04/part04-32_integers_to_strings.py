# Write your solution here
def formatted(list):
	new_list = []
	for x in range(len(list)):
	    new_list.append(f"{list[x]:.2f}")
	return new_list
if __name__ == "__main__":
	my_list = [0.123, 1.23, 0.0234]
	new_list = formatted(my_list)
	print(new_list)
