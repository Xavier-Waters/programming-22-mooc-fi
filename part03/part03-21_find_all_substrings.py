# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
while True:
	index = word.find(character)
	if index == -1:
	    break
	end = index + 3
	start = index + 1
	if end > len(word):
	    break
	print(word[index:end])
	if len(word) <= 3:
	    break
	if len(word) >= end:
	    word = word[start:]
	else:
	    break
