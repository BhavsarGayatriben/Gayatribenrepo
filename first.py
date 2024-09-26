correct_username = "Gayatri"
correct_password = "Mihir"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        attempts += 1
        print(f"Incorrect credentials. You have {max_attempts - attempts} attempts left.")

if attempts == max_attempts:
    print("Access denied.")