# Write your solution here
list = []
items = int(input("How many items: "))
count = 1
while items > 0:
	number = int(input(f"Item {count}: "))
	list.append(number)
	count += 1
	items -= 1
print(list)
