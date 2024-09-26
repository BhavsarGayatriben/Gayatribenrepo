while True:
    inches = float(input("Enter inches (negative value to stop): "))
    if inches < 0:
        print("Program ended.")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters} centimeters.")