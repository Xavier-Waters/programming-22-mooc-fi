# Write your solution here
list = []
index = 0
i = 0
same = 0
while True:
	word = str(input("Word: "))
	list.append(word)
	index += 1
	i = index - 1
	while i > 0:
	    i -= 1
	    if list[i] == word:
	        same = 1
	if same == 1:
	    index -= 1
	    print(f"You typed in {index} different words")
	    break
