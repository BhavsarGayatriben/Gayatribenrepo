def gallons_to_liters(gallons):
    return gallons * 3.78541


def main():
    while True:
        gallons = float(input("Enter quantity of gasoline in gallons (negative to stop): "))
        if gallons < 0:
            print("Program ended.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is {liters:.2f} liters.")

main()