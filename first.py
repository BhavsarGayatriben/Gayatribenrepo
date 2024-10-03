def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance for the withdrawal!")
    if amount < 0:
        raise ValueError("Cannot withdraw a negative amount!")
    return balance - amount

try:
    balance = float(input("Enter account balance: "))
    withdrawal = float(input("Enter withdrawal amount: "))
    new_balance = withdraw(balance, withdrawal)
    print(f"Transaction successful! New balance: {new_balance:.2f}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Invalid input: {e}")
