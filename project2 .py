# Expense Tracker - Professional Version

def expense_tracker():
    expenses = []

    print("=" * 40)
    print("      EXPENSE TRACKER SYSTEM")
    print("=" * 40)

    while True:
        try:
            amount = input("\nEnter expense amount (or 'q' to quit): ")

            if amount.lower() == 'q':
                break

            amount = float(amount)

            if amount < 0:
                print("Expense cannot be negative!")
                continue

            expenses.append(amount)
            print(f"✓ Expense of Rs. {amount:.2f} added successfully.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("\n" + "=" * 40)
    print("         EXPENSE REPORT")
    print("=" * 40)

    if expenses:
        total = sum(expenses)
        highest = max(expenses)
        lowest = min(expenses)
        average = total / len(expenses)

        print(f"Total Expenses : {len(expenses)}")
        print(f"Total Spent    : Rs. {total:.2f}")
        print(f"Highest Expense: Rs. {highest:.2f}")
        print(f"Lowest Expense : Rs. {lowest:.2f}")
        print(f"Average Expense: Rs. {average:.2f}")

        print("\nExpense List:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Rs. {expense:.2f}")

    else:
        print("No expenses recorded.")

    print("=" * 40)
    print("Thank you for using Expense Tracker!")
    print("=" * 40)


# Run Program
expense_tracker()
