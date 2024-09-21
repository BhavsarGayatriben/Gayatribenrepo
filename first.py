seasons = ("winter", "spring", "summer", "autumn")


month = int(input("Enter the number of the month (1-12): "))


if month in (12, 1, 2):
    season = seasons[0]  # winter
elif month in (3, 4, 5):
    season = seasons[1]  # spring
elif month in (6, 7, 8):
    season = seasons[2]  # summer
elif month in (9, 10, 11):
    season = seasons[3]  # autumn
else:
    season = "Invalid month number."

print(f"The season is: {season}")
