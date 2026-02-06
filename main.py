import json
import os
from datetime import datetime

expense_FILE = "expenseStorage.json"

# A Helper Function To Take Non-Empty Inputs
def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty!!")

# Function to Load Saved expense from the File if Exists.
def load_expense():
    if os.path.exists(expense_FILE) and os.path.isfile(expense_FILE):
        with open(expense_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Warning: expense file is corrupt or empty, initializing new expense.")
                return []
    return []

# Function to Save expense into JSON File.
def save_expense(expense):
    with open(expense_FILE, "w") as expenseFile:
        json.dump(expense, expenseFile, indent=5)

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

    expense_expense = load_expense()
    expense_expense.append(expense)
    save_expense(expense_expense)
    print("Your Expense Saved Successfully!")


# Function to View all the Expenses Saved Before.
def view_all_expenses():
    expenses_list = load_expense()
    if not expenses_list:
        print("There is no Expense to Show!!!")
        return

    gap = ' ' * 3
    heading = f"{'Date':10s}{gap}{'Expense':10s}{gap}{'Category':10s}{gap}{'Amount':6s}{gap}{'Currency':9s}"

    print("=" * 60)
    print(heading)
    print("-" * 60)

    for expense in expenses_list:
        actual_expense = (
                          f"{expense['date']:10s}{gap}"
                          f"{expense['expense']:10s}{gap}"
                          f"{expense['category']:10s}{gap}"
                          f"{expense['amount']:7.2f}{gap}"
                          f"{expense['currency']:9s}"
                          )
        print(actual_expense)
    print("-" * 60)

# Function to Search Expenses Saved Before.
"""3.5 Search Expenses
Must support:
- Category search
- Date range search
"""

def search_expense():
    pass




# Function to Show Main Menu
def show_menu():
    print("\n====== Main Menu ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Expense Summary")
    print("5. Export Report")
    print("6. Exit")


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