# Write your solution here
list = [1, 2, 3, 4, 5]
while True:
	index = int(input("Index: "))
	if index == -1:
	    break
	else:
	    new_value = int(input("New value: "))
	    if new_value == -1:
	        break
	    else:
	        list[index] = new_value
	        print(list)
