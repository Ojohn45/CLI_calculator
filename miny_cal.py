# This function does the maths.
# It takes two numbers (num1, num2) and an operation symbol (op),
# then returns the answer (or an error message as text).
def calculate(num1, num2, op):
    if op == "+":                       # if the user chose addition
        return num1 + num2
    elif op == "-":                     # otherwise, if they chose subtraction
        return num1 - num2
    elif op == "*":                     # otherwise, if they chose multiplication
        return num1 * num2
    elif op == "/":                     # otherwise, if they chose division
        if num2 == 0:                   # dividing by zero is impossible, so stop here
            return "Can't divide by zero!"
        return num1 / num2              # safe to divide
    else:                               # none of the symbols matched
        return "Invalid operation!"


# Ask the user for input. input() always gives back text (a string).
first = input("Enter first number: ")
op = input("Choose operation (+, -, *, /): ")
second = input("Enter second number: ")

# Try to turn the typed text into real decimal numbers
try:
    num1 = float(first)
    num2 = float(second)
except ValueError:
    # This runs if the conversion failed, e.g. the user typed "hello"
    print("Please enter valid numbers!\n")
else:
    # This runs only if the try block worked with no errors.
    # Call calculate() and show the result.
    print(f"Result: {calculate(num1, num2, op)}\n")