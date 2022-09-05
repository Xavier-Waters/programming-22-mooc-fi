number = int(input("Please type in a number: "))
index = 1
even = -1
odd = -1
while index <= number:
	if index % 2 == 0:
	    even = index
	    if odd != -1:
	        print(even)
	        print(odd)
	elif index % 2 == 1:
	    odd = index
	index += 1
if number != even:
	print(number)
