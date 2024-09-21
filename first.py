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

# Set to store unique names
names = set()

while True:

    name = input("Enter a name (or press Enter to quit): ")

    if name == '':
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nThe names you entered are:")
for name in names:
    print(name)

    # Dictionary to store ICAO codes and airport names
    airports = {}

    while True:
        # Display options to the user
        print("\nChoose an option:")
        print("1: Enter a new airport")
        print("2: Fetch airport information")
        print("3: Quit")

        option = input("Your choice: ")

        airports = {}

        while True:
            # Display options to the user
            print("\nChoose an option:")
            print("1: Enter a new airport")
            print("2: Fetch airport information")
            print("3: Quit")

            option = input("Your choice: ")

            if option == '1':
                # Option to enter a new airport
                icao_code = input("Enter the ICAO code: ").upper()
                airport_name = input("Enter the airport name: ")

                # Store the airport in the dictionary
                airports[icao_code] = airport_name
                print(f"Airport {airport_name} with ICAO code {icao_code} added.")

            elif option == '2':
                # Option to fetch airport information
                icao_code = input("Enter the ICAO code: ").upper()

                # Fetch and print the airport name if it exists
                if icao_code in airports:
                    print(f"Airport name: {airports[icao_code]}")
                else:
                    print(f"No information found for ICAO code {icao_code}.")

            elif option == '3':
                # Option to quit the program
                print("Exiting the program.")
                break

            else:
                print("Invalid option. Please choose 1, 2, or 3.")