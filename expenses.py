"""Core logic for the Expense Tracker. Rules and in-memory storage live here."""

_expenses = []

class ExpenseError(Exception):
    """Raised when an expense is invalid."""
    pass

def add_expense(description, amount_str):
    """Validate and add an expense. Returns the new expense dict."""
    # Check description
    if not description or not description.strip():
        raise ExpenseError("Description cannot be empty.")
    
    # Check amount
    try:
        amount = float(amount_str)
    except ValueError:
        raise ExpenseError("Amount must be a valid number.")
        
    if amount <= 0:
        raise ExpenseError("Amount must be greater than zero.")
        
    # If valid, save and return
    expense = {
        "description": description.strip(),
        "amount": amount
    }
    _expenses.append(expense)
    return expense

def get_expenses():
    """Return the list of all recorded expenses."""
    return _expenses

def get_total():
    """Calculate the sum of all recorded amounts."""
    return sum(exp["amount"] for exp in _expenses)