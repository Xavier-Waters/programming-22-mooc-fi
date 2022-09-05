# Write your solution here
def squared(string, length):
	index = 0
	iter = 0
	while iter < length:
	    iter2 = 0
	    while iter2 < length:
	        print(string[index % len(string)], end='', sep='')
	        index += 1
	        iter2 += 1
	    iter += 1
	    print("")
	
if __name__ == "__main__":
	squared("aybabtu", 5)
