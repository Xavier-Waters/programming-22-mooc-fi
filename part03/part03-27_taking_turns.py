# Write your solution here
number = int(input("Please type in a number: "))
top_integer = number
bottom_integer = 1
while bottom_integer < top_integer:
	print(bottom_integer)
	print(top_integer)
	bottom_integer += 1
	top_integer -= 1
if top_integer - bottom_integer == 0:
	print(bottom_integer)
