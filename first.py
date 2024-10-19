def find_season():
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    month = int(input("Enter the number of the month (1-12): "))

    if month in [12, 1, 2]:
        print("The season is:", seasons[0])
    elif month in [3, 4, 5]:
        print("The season is:", seasons[1])
    elif month in [6, 7, 8]:
        print("The season is:", seasons[2])
    elif month in [9, 10, 11]:
        print("The season is:", seasons[3])
    else:
        print("Invalid month number!")


find_season()
