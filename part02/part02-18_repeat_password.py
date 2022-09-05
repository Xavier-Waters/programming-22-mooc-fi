# Write your solution here
password = input("Password: ")
while True:
	repeat_pass = input("Repeat password: ")
	if repeat_pass == password:
	    break
	else:
	    print("They do not match!")
print("User account created!")
