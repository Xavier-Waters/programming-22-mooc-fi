# Write your solution here
word = str(input("Please type in a word: "))
character = str(input("Please type in a character: "))
char_length = len(word)
char_index = int(word.find(character))
char_end_index = char_index + 3
if char_length >= char_end_index:
	print(word[char_index:char_end_index])
