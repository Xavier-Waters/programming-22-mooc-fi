# Copy here code of line function from previous exercise
def line(length, string):
	if string == "":
	    print(str("*")*length)
	else:
	    print(string[0]*length)
	
def square(size, character):
	# You should call function line here with proper parameters
	height = size
	while height > 0:
	    line(size, character)
	    height -= 1
	
# You can test your function by calling it within the following block
if __name__ == "__main__":
	square(5, "x")
