# Write your solution here
list = []
index = 0
print(f"The list is now {list}")
while True:
	add_remove_exit = str(input("a(d)d, (r)emove or e(x)it: "))
	if add_remove_exit.lower() == "d":
	    index += 1
	    list.append(index)
	    print(f"The list is now {list}")
	elif add_remove_exit.lower() == "r":
	    i = index
	    list.remove(i)
	    index -= 1
	    print(f"The list is now {list}")
	elif add_remove_exit.lower() == "x":
	    print("Bye!")
	    break
