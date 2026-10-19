"""Interactive menu for the Expense Tracker."""
from expenses import add_expense, get_expenses, get_total, ExpenseError

MENU = """
=== Expense Tracker ===
1) Add expense
2) View expenses
3) Show total
q) Quit
"""

def run_menu():
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            print("Goodbye.")
            break

        elif choice == "1":
            desc = input("Description: ")
            amt_str = input("Amount (₦): ")
            try:
                new_exp = add_expense(desc, amt_str)
                print(f"✓ Added: {new_exp['description']} (₦{new_exp['amount']:.2f})")
            except ExpenseError as e:
                # Explains the problem and returns to menu without saving
                print(f"✗ Error: {e}")

        elif choice == "2":
            expenses = get_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\n--- Your Expenses ---")
                for i, exp in enumerate(expenses, 1):
                    print(f"{i}. {exp['description']}: ₦{exp['amount']:.2f}")
                print("---------------------")

        elif choice == "3":
            total = get_total()
            print(f"Total: ₦{total:.2f}")

        else:
            print("✗ Error: Unknown option. Please choose 1, 2, 3, or q.")