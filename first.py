def airport_manager():
    airports = {}

    while True:
        print("\n1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            icao = input("Enter the ICAO code: ").strip().upper()
            name = input("Enter the name of the airport: ").strip()
            airports[icao] = name
            print(f"Airport {name} with ICAO code {icao} added.")

        elif choice == "2":
            icao = input("Enter the ICAO code: ").strip().upper()
            if icao in airports:
                print(f"The airport name is: {airports[icao]}")
            else:
                print("Airport not found.")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


airport_manager()
