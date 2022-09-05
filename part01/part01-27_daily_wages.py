# Write your solution here
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
if day == "Sunday":
    wage = wage * 2
daily_wage = wage * hours
print(f"Daily wages: {daily_wage} euros")
