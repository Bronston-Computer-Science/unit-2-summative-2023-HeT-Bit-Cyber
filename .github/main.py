import math

def show_menu():
    print("Menu:")
    print("1. Basic math operations")
    print("2. Trigonometric calculations")
    print("3. Unit conversions")
    print("4. Exit")

def show_basic_math_menu():
    print("Basic Math Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Back to main menu")

def show_trigonometric_menu():
    print("Trigonometric Calculations:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    print("4. Back to main menu")

def show_unit_conversion_menu():
    print("Unit Conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Back to main menu")

def perform_basic_math_operation(operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == 1:
        result = num1 + num2
        print("Result: ", result)
    elif operation == 2:
        result = num1 - num2
        print("Result: ", result)
    elif operation == 3:
        result = num1 * num2
        print("Result: ", result)
    elif operation == 4:
        result = num1 / num2
        print("Result: ", result)

def perform_trigonometric_calculation(operation):
    angle = float(input("Enter the angle in degrees: "))

    if operation == 1:
        result = math.sin(math.radians(angle))
        print("Result: ", result)
    elif operation == 2:
        result = math.cos(math.radians(angle))
        print("Result: ", result)
    elif operation == 3:
        result = math.tan(math.radians(angle))
        print("Result: ", result)

def perform_unit_conversion(operation):
    if operation == 1:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit: ", fahrenheit)
    elif operation == 2:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius: ", celsius)

# Main program
while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        basic_math_options = {
            1: "Add",
            2: "Subtract",
            3: "Multiply",
            4: "Divide",
            5: "Back to main menu"
        }

        for operation, operation_name in basic_math_options.items():
            print(f"{operation}. {operation_name}")

        for i in range(1, 6):
            operation = int(input("Enter the operation: "))

            if operation == 5:
                break

            if operation in basic_math_options:
                perform_basic_math_operation(operation)
            else:
                print("Invalid operation. Please try again.")

    elif choice == 2:
        trigonometric_options = {
            1: "Sine",
            2: "Cosine",
            3: "Tangent",
            4: "Back to main menu"
        }

        for operation, operation_name in trigonometric_options.items():
            print(f"{operation}. {operation_name}")

        for i in range(1, 5):
            operation = int(input("Enter the operation: "))

            if operation == 4:
                break

            if operation in trigonometric_options:
                perform_trigonometric_calculation(operation)
            else:
                print("Invalid operation. Please try again.")

    elif choice == 3:
        unit_conversion_options = {
            1: "Celsius to Fahrenheit",
            2: "Fahrenheit to Celsius",
            3: "Back to main menu"
        }

        for operation, operation_name in unit_conversion_options.items():
            print(f"{operation}. {operation_name}")

        for i in range(1, 4):
            operation = int(input("Enter the operation: "))

            if operation == 3:
                break

            if operation in unit_conversion_options:
                perform_unit_conversion(operation)
            else:
                print("Invalid operation. Please try again.")

    elif choice == 4:
        break

    else:
        print("Invalid choice. Please try again.")