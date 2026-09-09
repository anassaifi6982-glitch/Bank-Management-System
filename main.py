import json
import random
from pathlib import Path


class Bank:

    database = "data.json"
    data = []

    # Load existing data
    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            data = []
            with open(database, "w") as fs:
                json.dump(data, fs, indent=4)

    except Exception as err:
        print(f"An error occurred while loading data: {err}")
        data = []

    # Save data
    @staticmethod
    def update():
        try:
            with open(Bank.database, "w") as fs:
                json.dump(Bank.data, fs, indent=4)
        except Exception as err:
            print(f"An error occurred while saving data: {err}")

    # Find user
    @staticmethod
    def find_user(acc_no, pin):
        for user in Bank.data:
            if user["accountNo"] == acc_no and user["pin"] == pin:
                return user

        return None

    # Create Account
    def create_account(self):

        print("\n========== CREATE ACCOUNT ==========")

        name = input("Enter your Name: ")
        
        try:
            age = int(input("Enter your Age: "))
            pin = int(input("Enter your 4-digit PIN: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        email = input("Enter your Email: ")

        # Age validation
        if age < 18:
            print("Sorry, you must be 18 or older to create an account.")
            return

        # PIN validation
        if len(str(pin)) != 4:
            print("PIN must contain exactly 4 digits.")
            return

        # Generate unique account number
        while True:
            account_no = random.randint(1000, 9999)

            if not any(
                user["accountNo"] == account_no
                for user in Bank.data
            ):
                break

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": account_no,
            "balance": 0
        }

        Bank.data.append(info)
        Bank.update()

        print("\nAccount created successfully!")
        print("--------------------------------")
        print(f"Name       : {name}")
        print(f"Age        : {age}")
        print(f"Email      : {email}")
        print(f"Account No : {account_no}")
        print(f"Balance    : ₹0")
        print("--------------------------------")
        print("Please note down your Account Number.")

    # Deposit Money
    def deposit_money(self):

        print("\n========== DEPOSIT MONEY ==========")

        try:
            acc_no = int(input("Enter your Account Number: "))
            pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        user = Bank.find_user(acc_no, pin)

        if user is None:
            print("Sorry, no account found.")
            return

        try:
            amount = int(input("Enter amount to deposit: "))
        except ValueError:
            print("Please enter a valid amount.")
            return

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > 100000:
            print("You can deposit maximum ₹100000 at a time.")
            return

        user["balance"] += amount

        Bank.update()

        print("\nAmount deposited successfully!")
        print(f"Deposited Amount : ₹{amount}")
        print(f"Current Balance  : ₹{user['balance']}")

    # Withdraw Money
    def withdraw_money(self):

        print("\n========== WITHDRAW MONEY ==========")

        try:
            acc_no = int(input("Enter your Account Number: "))
            pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        user = Bank.find_user(acc_no, pin)

        if user is None:
            print("Sorry, no account found.")
            return

        try:
            amount = int(input("Enter amount to withdraw: "))
        except ValueError:
            print("Please enter a valid amount.")
            return

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > user["balance"]:
            print("Insufficient balance.")
            print(f"Your current balance is ₹{user['balance']}")
            return

        user["balance"] -= amount

        Bank.update()

        print("\nAmount withdrawn successfully!")
        print(f"Withdrawn Amount : ₹{amount}")
        print(f"Current Balance  : ₹{user['balance']}")

    # Show Account Details
    def show_details(self):

        print("\n========== ACCOUNT DETAILS ==========")

        try:
            acc_no = int(input("Enter your Account Number: "))
            pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        user = Bank.find_user(acc_no, pin)

        if user is None:
            print("Sorry, no account found.")
            return

        print("\nYour Account Information")
        print("--------------------------------")
        print(f"Name       : {user['name']}")
        print(f"Age        : {user['age']}")
        print(f"Email      : {user['email']}")
        print(f"Account No : {user['accountNo']}")
        print(f"Balance    : ₹{user['balance']}")
        print("--------------------------------")

    # Update Account Details
    def update_details(self):

        print("\n========== UPDATE ACCOUNT ==========")

        try:
            acc_no = int(input("Enter your Account Number: "))
            pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        user = Bank.find_user(acc_no, pin)

        if user is None:
            print("Sorry, no account found.")
            return

        print("\nYou can update Name, Email and PIN.")
        print("Press Enter if you don't want to change anything.\n")

        new_name = input("Enter new Name: ")
        new_email = input("Enter new Email: ")
        new_pin = input("Enter new 4-digit PIN: ")

        # Update name
        if new_name.strip() != "":
            user["name"] = new_name

        # Update email
        if new_email.strip() != "":
            user["email"] = new_email

        # Update PIN
        if new_pin.strip() != "":
            if not new_pin.isdigit() or len(new_pin) != 4:
                print("PIN must contain exactly 4 digits.")
                return

            user["pin"] = int(new_pin)

        Bank.update()

        print("\nAccount details updated successfully!")

    # Delete Account
    def delete_account(self):

        print("\n========== DELETE ACCOUNT ==========")

        try:
            acc_no = int(input("Enter your Account Number: "))
            pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        user = Bank.find_user(acc_no, pin)

        if user is None:
            print("Sorry, no account found.")
            return

        print("\nAccount found!")
        print(f"Name    : {user['name']}")
        print(f"Balance : ₹{user['balance']}")

        confirmation = input(
            "\nAre you sure you want to delete this account? (y/n): "
        ).lower()

        if confirmation == "y":

            Bank.data.remove(user)
            Bank.update()

            print("\nAccount deleted successfully!")

        else:
            print("\nAccount deletion cancelled.")


# ==========================================
# MAIN PROGRAM
# ==========================================

user = Bank()

while True:

    print("\n")
    print("======================================")
    print("       BANK MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Account Details")
    print("5. Update Account")
    print("6. Delete Account")
    print("7. Exit")
    print("======================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        user.create_account()

    elif choice == 2:
        user.deposit_money()

    elif choice == 3:
        user.withdraw_money()

    elif choice == 4:
        user.show_details()

    elif choice == 5:
        user.update_details()

    elif choice == 6:
        user.delete_account()

    elif choice == 7:
        print("\nThank you for using Bank Management System!")
        break

    else:
        print("Invalid choice. Please select 1 to 7.")