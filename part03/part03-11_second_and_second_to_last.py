# Write your solution here
string = str(input("Please type in a string: "))
length = len(string) - 2
if string[1] == string[length]:
	print(f"The second and the second to last characters are {string[1]}")
else:
	print("The second and the second to last characters are different")
