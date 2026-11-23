# Expense Tracker
# Add expenses by category, view them, and see totals

# Each expense is a dict: {"description": str, "category": str, "amount": float}
expenses = []


def add_expense(description, category, amount):
    # Build a dict for this expense and append it to the list
    expense = {
        "description": description,
        "category": category,
        "amount": amount,
    }
    expenses.append(expense)
    print(f"Added: {description} ({category}) — ${amount:.2f}")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. [{e['category']}] {e['description']}: ${e['amount']:.2f}")


def total_by_category():
    # Aggregate amounts into a dict keyed by category
    totals = {}
    for e in expenses:
        category = e["category"]
        totals[category] = totals.get(category, 0) + e["amount"]

    print("\n--- Totals by Category ---")
    for category, total in totals.items():
        print(f"  {category}: ${total:.2f}")


def grand_total():
    # Sum all expense amounts
    total = sum(e["amount"] for e in expenses)
    print(f"\nGrand Total: ${total:.2f}")


def show_menu():
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Totals by category")
    print("4. Grand total")
    print("5. Quit")


# --- Main loop ---
while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        desc = input("Description: ").strip()
        cat = input("Category (e.g. Food, Travel, Bills): ").strip()
        amt = float(input("Amount: $"))
        add_expense(desc, cat, amt)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_by_category()

    elif choice == "4":
        grand_total()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1–5.")
