# Write your solution here
	# You can test your function by calling it within the following block
def greatest_number(a,b,c):
	if a >= b and a >= c:
	    return a
	elif b >= c and b >= a:
	    return b
	elif c >= b and c >= a:
	    return c
if __name__ == "__main__":
	greatest = greatest_number(5, 4, 8)
	print(greatest)

