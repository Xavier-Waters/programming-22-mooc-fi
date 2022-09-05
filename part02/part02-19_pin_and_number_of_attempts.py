# Write your solution here
attempts = 0
pin = 4321
while True:
	user_pin = int(input("PIN: "))
	attempts += 1
	if user_pin == pin:
	    break
	else:
	    print("Wrong")
if attempts == 1:
	print("Correct! It only took you one single attempt!")
else:
	print(f"Correct! It took you {attempts} attempts")
