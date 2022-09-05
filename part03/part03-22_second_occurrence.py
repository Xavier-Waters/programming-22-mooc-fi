# Write your solution here
string = str(input("Please type in a string: "))
substring = str(input("Please type in a substring: "))
	
index = 0
substring_1 = 0
substring_2 = 0
length = index + len(substring)
	
while length < len(string):
	correct = 0
	length = index + len(substring)
	if substring_1 == 1:
	    if string[index:length] == substring:
	        substring_2 = 1
	        break
	if string[index:length] == substring:
	    substring_1 = 1
	    correct = 1
	if correct == 1:
	    index += len(substring)
	else:
	    index += 1
if substring_2 == 1:
	print(f"The second occurrence of the substring is at index {index}.")
else:
	print("The substring does not occur twice in the string.")
