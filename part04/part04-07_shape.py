def line(length, string):
	if string == "":
	    print(str("*")*length)
	else:
	    print(string[0]*length)
	
def shape(length_1, string_1, length_2, string_2):
	# You should call function line here with proper parameters
	i = 0
	while i < length_1:
	    i += 1
	    line(i, string_1)
	index = length_2
	while index > 0:
	    line(i, string_2)
	    index -= 1
if __name__ == "__main__":
	shape(5, "a", 4, "b")
