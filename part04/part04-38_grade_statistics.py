# Write your solution here
def exam_points_and_exercises():
	exam_points = []
	exercises = []
	while True:
	    # Asks for input
	    inputs = str(input("Exam exam_points and exercises completed: "))
	    # If there is an empty line stop asking for input
	    if inputs == "":
	        break
	    # Splits the 2 inputs into two seperate lists
	    elif inputs.count(" ") == 1:
	        split = inputs.split(" ")
	        if int(split[0]) <= 20 and int(split[1]) <= 100: 
	            exam_points.append(split[0])
	            exercises.append(split[1])
	# Returns both lists
	return exercises, exam_points
	
def exercise_points(exercises):
	# This function converts the amount of exercises completed into exercise points
	exercise_points = []
	# Sets the number of exercises
	exercise_num = 100
	for x in range(len(exercises)):
	    if int(exercises[x]) == exercise_num:
	        exercise_points.append(10)
	    elif int(exercises[x]) >= exercise_num*0.9:
	        exercise_points.append(9)
	    elif int(exercises[x]) >= exercise_num*0.8:
	        exercise_points.append(8)
	    elif int(exercises[x]) >= exercise_num*0.7:
	        exercise_points.append(7)
	    elif int(exercises[x]) >= exercise_num*0.6:
	        exercise_points.append(6)
	    elif int(exercises[x]) >= exercise_num*0.5:
	        exercise_points.append(5)
	    elif int(exercises[x]) >= exercise_num*0.4:
	        exercise_points.append(4)
	    elif int(exercises[x]) >= exercise_num*0.3:
	        exercise_points.append(3)
	    elif int(exercises[x]) >= exercise_num*0.2:
	        exercise_points.append(2)
	    elif int(exercises[x]) >= exercise_num*0.1:
	        exercise_points.append(1)
	    else:
	        exercise_points.append(0)
	return exercise_points
	
def statistics():
	# Sets the output of exam_points_and_exercises as a list
	list = exam_points_and_exercises()
	stat_list = []
	points_list = []
	# Sets exam points list
	exam = list[1]
	exercise = list[0]
	# Sets exercise points list
	exercise_point = exercise_points(exercise)
	for x in range(len(exercise)):
	    # Sets the total amount of points
	    total = int(exercise_point[x]) + int(exam[x])
	    points_list.append(total)
	    # Automatically fails the person if the points from the exam are less than 10
	    if int(exam[x]) < 10:
	        stat_list.append(0)
	    # Fails the person if total points are less or equal to than 14
	    elif int(total) <= 14:
	        stat_list.append(0)
	    # Gives a grade of one if points are less than or equal to 17
	    elif int(total) <= 17:
	        stat_list.append(1)
	    elif int(total) <= 20:
	        stat_list.append(2)
	    elif int(total) <= 23:
	        stat_list.append(3)
	    elif int(total) <= 27:
	        stat_list.append(4)
	    elif int(total) <= 30:
	        stat_list.append(5)
	# Returns the grade and the points in a list form
	return stat_list, points_list
	
stats = statistics()
# Defines grade as the first variable of the output of statistics and points as the second
grade = stats[0]
points = stats[1]
average_points = 0
# Gets the total amount of points
for x in range(len(points)):
	average_points += int(points[x])
# Devides the total amount of points by the amount of entries in the list
average_points /= len(points)
# Calculates the percentage of people that passed
pass_percentage = (grade.count(1) + grade.count(2) + grade.count(3) + grade.count(4) + grade.count(5))/len(grade)*100
print("Statistics: ")
print(f"Points average: {average_points:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution: ")
print("5:", "*"*grade.count(5))
print("4:", "*"*grade.count(4))
print("3:", "*"*grade.count(3))
print("2:", "*"*grade.count(2))
print("1:", "*"*grade.count(1))
print("0:", "*"*grade.count(0))
