# Write your solution here
limit = int(input("Limit: "))
number = 0
count = 0
printer = str("")
	
while limit > number:
	number += count
	if count > 0:
	    printer += str(f"{count}")
	    if number < limit:
	        printer += str(" + ")
	    elif number >= limit:
	        printer += str(f" = {number}")
	count += 1
print(f"The consecutive sum: {printer}")
