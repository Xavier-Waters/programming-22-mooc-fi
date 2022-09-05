# Write your solution here
letter_1 = str(input("1st letter: "))
letter_2 = str(input("2nd letter: "))
letter_3 = str(input("3rd letter: "))
	
if letter_1 > letter_2 > letter_3:
	print(f"The letter in the middle is {letter_2}")
if letter_3 > letter_2 > letter_1:
	print(f"The letter in the middle is {letter_2}")
if letter_2 > letter_1 > letter_3:
	print(f"The letter in the middle is {letter_1}")
if letter_3 > letter_1 > letter_2:
	print(f"The letter in the middle is {letter_1}")
if letter_1 > letter_3 > letter_2:
	print(f"The letter in the middle is {letter_3}")
if letter_2 > letter_3 > letter_1:
	print(f"The letter in the middle is {letter_3}")
