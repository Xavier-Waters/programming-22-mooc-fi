# Write your solution here
word = str(input("Word: "))
length = int(len(word))
print("*"*30)
if length % 2 == 0:
	blank_space = (int(29) - length) // 2
	print("*" + str(" ")*blank_space + word + str(" ")*blank_space + "*")
else:
	blank_space = (int(29) - length) // 2
	print("*" + str(" ")*blank_space + word + str(" ")*(blank_space - 1) + "*")
print("*"*30)
