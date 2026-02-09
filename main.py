import json
import os
from datetime import datetime

EXPENSE_FILE = "expenseStorage.json"

# ---------------- Helper Functions ----------------

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty!!")


def get_valid_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            return datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid Date Format. Use YYYY-MM-DD")


# ---------------- File Handling ----------------

def load_expense():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_expense(expenses):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(expenses, f, indent=5)


# ---------------- Table Utilities (AUTO-SIZED) ----------------

COLUMNS = [
    ("date", "Date"),
    ("expense", "Expense"),
    ("category", "Category"),
    ("amount", "Amount"),
    ("currency", "Currency")
]


def calculate_column_widths(expenses):
    widths = {}

    for key, title in COLUMNS:
        max_width = len(title)
        for expense in expenses:
            value = expense.get(key, "")
            value = f"{value:.2f}" if isinstance(value, float) else str(value)
            max_width = max(max_width, len(value))
        widths[key] = max_width

    return widths


def print_table(expenses):
    if not expenses:
        print("No expenses to show.")
        return

    widths = calculate_column_widths(expenses)
    gap = "   "
    total_width = sum(widths.values()) + len(COLUMNS) * len(gap)

    print("=" * total_width)

    header = ""
    for key, title in COLUMNS:
        header += f"{title:<{widths[key]}}{gap}"
    print(header)

    print("-" * total_width)

    for expense in expenses:
        row = ""
        for key, _ in COLUMNS:
            value = expense.get(key, "")
            value = f"{value:.2f}" if isinstance(value, float) else value
            row += f"{value:<{widths[key]}}{gap}"
        print(row)

    print("=" * total_width)


# ---------------- Core Features ----------------

def add_expense():
    expense = {
        "expense": get_non_empty("Enter Expense: "),
        "category": get_non_empty("Enter Category: "),
        "description": get_non_empty("Enter Description: "),
        "amount": float(input("Enter Amount: ")),
        "date": get_valid_date("Enter Date (YYYY-MM-DD): ").strftime("%Y-%m-%d"),
        "currency": input("Currency (PKR default): ").strip().upper() or "PKR"
    }

    expenses = load_expense()
    expenses.append(expense)
    save_expense(expenses)
    print("Expense Saved Successfully!")


def view_all_expenses():
    print_table(load_expense())


def search_by_category():
    keyword = input("Enter category to search: ").strip().lower()
    expenses = load_expense()

    results = [e for e in expenses if e["category"].lower() == keyword]
    print_table(results)


def search_by_date_range():
    expenses = load_expense()
    if not expenses:
        print("No expenses found.")
        return

    start_date = get_valid_date("Enter Start Date (YYYY-MM-DD): ")
    end_date = get_valid_date("Enter End Date (YYYY-MM-DD): ")

    results = []
    for e in expenses:
        expense_date = datetime.strptime(e["date"], "%Y-%m-%d")
        if start_date <= expense_date <= end_date:
            results.append(e)

    print_table(results)


def expense_summary():
    expenses = load_expense()
    if not expenses:
        print("No expenses available.")
        return

    total_amount = sum(e["amount"] for e in expenses)
    highest = max(expenses, key=lambda x: x["amount"])

    print(f"\nTotal Expense Amount: {total_amount:.2f}")
    print(
        f"Highest Expense: {highest['expense']} | "
        f"{highest['amount']} {highest['currency']} | "
        f"{highest['date']} | {highest['category']}"
    )


# ---------------- Menu ----------------

def show_menu():
    print("\n====== Main Menu ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Expense Summary")
    print("5. Exit")


while True:
    show_menu()

    try:
        choice = int(input("Select option (1-5): "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_all_expenses()

        elif choice == 3:
            print("\n1. Search by Category")
            print("2. Search by Date Range")
            sub = input("Choose option: ")

            if sub == "1":
                search_by_category()
            elif sub == "2":
                search_by_date_range()
            else:
                print("Invalid search option.")

        elif choice == 4:
            expense_summary()

        elif choice == 5:
            print("\nThanks for using Expense Manager.")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Invalid input. Enter numbers only.")