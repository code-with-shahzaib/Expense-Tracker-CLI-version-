import json
import os
from datetime import datetime

DATA_FILE = "dataStorage.json"

# A Helper Function To Take Non-Empty Inputs
def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty!!")

# Function to Load Saved Data from the File if Exists.
def load_data():
    if os.path.exists(DATA_FILE) and os.path.isfile(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Warning: Data file is corrupt or empty, initializing new data.")
                return []
    return []

# Function to Save Data into JSON File.
def save_data(data):
    with open(DATA_FILE, "w") as dataFile:
        json.dump(data, dataFile, indent=5)

# Function to Add Expense in JSON File.
def add_expense():
    expense_name = get_non_empty("Enter Your Expense: ")
    category = get_non_empty("Enter Expense Category (e.g. Food, Transprot,..): ")
    description = get_non_empty("Enter some Description of Expense: ")
    currency = input("Enter Expense Currency (e.g. PKR, INR): ").strip().upper()
    if not currency:
        currency = "PKR"

    while True:
        date_input = input("Enter Date (e.g. YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input
            break
        except ValueError:
            print("Invalid Date Format. (Enter YYYY-MM-DD)")

    while True:
        try:
            amount = float(input("Enter Amount of Expense: "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    expense = {
        "expense" : expense_name,
        "category" : category,
        "description" : description,
        "amount" : amount,
        "date" : date,
        "currency" : currency
    }

    expense_data = load_data()
    expense_data.append(expense)
    save_data(expense_data)
    print("Your Expense Saved Successfully!")

# Function to Show Main Menu
def show_menu():
    print("\n====== Main Menu ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Expense Summary")
    print("5. Export Report")
    print("6. Exit")


# Function to View all the Expenses Saved Before.
def view_all_expenses():
    expenses_list = load_data()
    if not expenses_list:
        print("There is no Expense to Show!!!")
        return

    for expense in expenses_list:
        print("================================")
        print(f"\nExpense Name: {expense['expense']}\nCategory: {expense['category']}\nDescription:"
              f" {expense['description']}\nAmount: {expense['amount']}\nDate: {expense['date']}\nCurrency: "
              f"{expense['currency']}\n")


while True:
    show_menu()

    try:
        choice = int(input("Select option (1-6): "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_all_expenses()

        elif choice == 3:
            print("Feature Coming Soon...")

        elif choice == 4:
            print("Feature Coming Soon...")

        elif choice == 5:
            print("Feature Coming Soon...")

        elif choice == 6:
            print("Thanks for using Expense Manager.")
            break

        else:
            print("Invalid option. Choose between 1-6.")

    except ValueError:
        print("Invalid input. Enter numbers only.")