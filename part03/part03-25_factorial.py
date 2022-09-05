# Write your solution here
while True:
	number = int(input("Please type in a number: "))
	index = 1
	factor = 1
	if number > 0:
	    while index <= number:
	        factor *= index
	        index += 1
	    print(f"The factorial of the number {number} is {factor}")
	else:
	    print("Thanks and bye!")
	    break
