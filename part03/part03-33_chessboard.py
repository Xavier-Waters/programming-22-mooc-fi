# Write your solution here
def chessboard(length):
	count = 0
	while count < length:
	    if length % 2 == 0:
	        if count % 2 == 0:
	            print(str("10")*int((length/2)))
	        elif count % 2 == 1:
	            print(str("01")*int((length - 1)/2) + "01")
	        count += 1
	    elif length % 2 == 1:
	        if count % 2 == 0:
	            print(str("10")*int((length/2)) + "1")
	        elif count % 2 == 1:
	            print(str("01")*int((length - 1)/2) + "0")
	        count += 1
# Testing the function
if __name__ == "__main__":
	chessboard(3)
