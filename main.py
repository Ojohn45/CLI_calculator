"""Entry point for the Expense Tracker."""
from cli import run_menu

def main():
    try:
        run_menu()
    except (KeyboardInterrupt, EOFError):
        print("\nInterrupted. Goodbye.")

if __name__ == "__main__":
    main()