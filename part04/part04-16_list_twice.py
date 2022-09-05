# Write your solution here
list = []
while True:
	item = int(input("New item: "))
	if item == 0:
	    print("Bye!")
	    break
	else:
	    list.append(item)
	    in_order = sorted(list)
	    print("The list now:", list)
	    print("The list in order:", in_order)
