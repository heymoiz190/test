def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation_input():
    operations = {'1': 'Add', '2': 'Subtract', '3': 'Multiply', '4': 'Divide'}
    while True:
        print("\nSelect operation:")
        for key, value in operations.items():
            print(f"{key}. {value}")
        choice = input("Enter choice (1/2/3/4): ")
        if choice in operations:
            return choice
        else:
            print("Invalid choice. Please select a valid operation.")

def main():
    print("Welcome to the Python Calculator!")

    while True:
        operation = get_operation_input()
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")

        try:
            if operation == '1':
                result = add(num1, num2)
                op = "Addition"
            elif operation == '2':
                result = subtract(num1, num2)
                op = "Subtraction"
            elif operation == '3':
                result = multiply(num1, num2)
                op = "Multiplication"
            elif operation == '4':
                result = divide(num1, num2)
                op = "Division"
            
            print(f"\n{op} result: {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        next_calculation = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != 'yes':
            break

    print("Thank you for using the Python Calculator!")

if __name__ == "__main__":
    main()
