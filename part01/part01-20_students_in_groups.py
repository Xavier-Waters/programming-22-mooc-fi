# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
groups = students / group_size
groups_int = students // group_size
if groups != groups_int:
    groups = groups_int + 1
	 
print(f"Number of groups formed: {groups}")
