# Write your solution here
# You can test your function by calling it within the following block
def first_word(string):
	i = 0
	# Loops until it finds a space and then returns the first word
	while True:
	    i += 1
	    first = string[0:i]
	    if string[i] == " ":
	        return string[0:i]
def second_word(string):
	i = 0
	# Loops until it finds a space then breaks
	while True:
	    i += 1
	    second = string[0:i]
	    if string[i] == " ":
	        index = i
	        break
	# Loops until it finds a second space or the string terminates
	while True:
	    index += 1
	    second = string[i:index]
	    if string[index] == " ":
	        i += 1
	        return string[i:index]
	    elif index >= (len(string) - 1):
	        i += 1
	        return string[i:]
	
def last_word(string):
	i = len(string)
	# Loops backwards, basically a reversed version of first_word
	while True:
	    i -= 1
	    last = string[i:]
	    if string[i] == " ":
	        i += 1
	        return string[i:]
if __name__ == "__main__":
	sentence = "first second"
	print(first_word(sentence))
	print(second_word(sentence))
	print(last_word(sentence))
