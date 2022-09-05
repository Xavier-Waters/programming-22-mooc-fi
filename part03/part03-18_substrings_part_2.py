# Write your solution here
string = str(input("Please type in a string: "))
length = len(string)
count = length - 1
while count < length and count >= 0:
	print(string[count:length])
	count -= 1
