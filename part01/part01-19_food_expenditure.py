cafeteria_week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
groceries_week = float(input("How much money do you spend on groceries in a week? "))
weekly_food = cafeteria_week * lunch_price + groceries_week
daily_food = weekly_food / 7
print("Average food expenditure: ")
print(f"Daily: {daily_food} euros")
print(f"Weekly: {weekly_food} euros")
