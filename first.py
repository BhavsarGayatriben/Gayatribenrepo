def name_checker():
    names = set()

    while True:
        name = input("Enter a name (or press Enter to finish): ").strip()
        if not name:  # If the input is an empty string, break the loop
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nList of names entered:")
    for name in names:
        print(name)


name_checker()
