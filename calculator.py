def calculator():
    # Get the first number
    num1 = float(input("Enter the first number: "))

    # Get the operator
    print("\nChoose an operator:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter your choice (1/2/3/4): ")

    # Validate operator choice
    while choice not in ['1', '2', '3', '4']:
        choice = input("Invalid choice. Please enter a number between 1 and 4: ")

    # Get the second number
    num2 = float(input("Enter the second number: "))

    # Perform calculation based on operator
    if choice == '1':
        result = num1 + num2
        operator = '+'
    elif choice == '2':
        result = num1 - num2
        operator = '-'
    elif choice == '3':
        result = num1 * num2
        operator = '*'
    else:
        if num2 != 0:
            result = num1 / num2
            operator = '/'
        else:
            print("Error! Division by zero is not allowed.")
            return

    # Display result
    print(f"\n{num1} {operator} {num2} = {format(result, '.20f')}".rstrip('0').rstrip('.'))

# Run the calculator
calculator()