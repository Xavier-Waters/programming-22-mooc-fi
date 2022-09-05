# Write your solution here
	sentence = str(input("Please type in a sentence: "))
i = 1
	
print(sentence[0])
while len(sentence) > i:
	next_letter = 0
	if sentence[i] == " " and sentence [i + 1] != " ":
	    next_letter = 1
	i += 1
	if next_letter == 1:
	    print(sentence[i])

