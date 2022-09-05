# Write your solution here
word_1 = str(input("Please type in the 1st word: "))
word_2 = str(input("Please type in the 2nd word: "))
	
if word_1 > word_2:
	print(word_1, "comes alphabetically last")
elif word_2 > word_1:
	print(word_2, "comes alphabetically last")
elif word_1 == word_2:
	print("You gave the same word twice.")
