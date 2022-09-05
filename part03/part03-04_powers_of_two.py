# Write your solution here
upper_limit = int(input("Upper limit: "))
number = 1
	
if number < 2:
	print(number)
	number += 1
while number <= upper_limit:
	print(number)
	number = number * 2
