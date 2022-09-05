# Write your solution here
# You can test your function by calling it within the following block
def same_chars(string, index_1, index_2):
	if index_1 >= len(string):
	    return
	elif index_2 >= len(string):
	    if string[index_1] == string[len(string) - 1]:
	        return True
	    else:
	        return False
	elif string[index_1] == string[index_2]:
	    return True
	else:
	    return False
if __name__ == "__main__":
	print(same_chars("coder", 1, 10))
