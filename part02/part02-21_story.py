# Write your solution here
words = ""
prev_word = ""
while True:
	word = input("Please type in a word: ")
	if word == "end":
	    break
	if word == prev_word:
	    break
	words = words + word + " "
	prev_word = word
print(words)
