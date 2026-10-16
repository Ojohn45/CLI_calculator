def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "%":
        return num1 % num2
    elif op == "/":
        if num2 == 0:
            return "Can't divide by zero!"
        return a / b
    else:
        return "Invalid operation!"


print("=== Simple CLI Calculator ===")
print("Type 'q' at any time to quit.\n")

while True:
    first = input("Enter first number: ")
    if first == "q":
        break

    op = input("Choose operation (+, -, *, /, %): ")
    if op == "q":
        break

    second = input("Enter second number: ")
    if second == "q":
        break

    try:
        num1 = float(first)
        num2 = float(second)
    except ValueError:
        print("Please enter valid numbers!\n")
        continue

    print(f"Result: {calculate(num1, num2, op)}\n")

print("Goodbye! 👋")