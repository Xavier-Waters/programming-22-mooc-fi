# Write your solution here
string_1 = str(input("Please type in string 1: "))
string_2 = str(input("Please type in string 2: "))
length_1 = len(string_1)
length_2 = len(string_2)
	
if length_1 == length_2:
	print("The strings are equally long")
elif length_1 > length_2:
	print(f"{string_1} is longer")
else:
	print(f"{string_2} is longer")
