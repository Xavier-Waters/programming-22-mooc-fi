# Write your solution here
number = int(input("Please type in a number: "))
number_1 = 1
while number_1 <= number:
	number_2 = 1
	while number >= number_2:
	    print(f"{number_1} x {number_2} = {number_1 * number_2}")
	    number_2 += 1
	number_1 += 1
