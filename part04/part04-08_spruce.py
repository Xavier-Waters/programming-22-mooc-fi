# Write your solution here
# You can test your function by calling it within the following block
def spruce(size):
	# vArIaBlEs
	i = 1
	index = 1
	index_2 = 1
	# pRiNtInG
	print("a spruce!")
	print(" "*(size-i-1), "*"*index_2, " "*(size-i-1))
	#wHiLe LoOp tHaT pRiNtS tReE!1!1
	while index < size:
	    index_2 += 2
	    i += 1
	    index += 1
	    if size-i > 0:
	        print(" "*(size-i-1), "*"*index_2, " "*(size-i-1))
	    else:
	        print("*"*index_2)
	# pRiNtS bOtToM oF tReE
	print(" "*(i-2), "*", " "*(i-2))
	
# Retarded testing thing because of mooc    
if __name__ == "__main__":
	spruce(7)
