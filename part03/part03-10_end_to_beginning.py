# Write your solution here
string = str(input("Please type in a string: "))
length = len(string)
count = length - 1
	
while count >= 0:
	print(string[count])
	count -= 1
