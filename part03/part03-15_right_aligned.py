# Write your solution here
string = str(input("Please type in a string: "))
count = len(string)
	
while count < 20:
	string = "*" + string
	count += 1
print(string)
