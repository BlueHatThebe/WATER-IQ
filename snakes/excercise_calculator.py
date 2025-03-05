def arithmetic_operation(op_code: int, num1: float, num2: float) -> float:
    """
    Performs an arithmetic operation on two numbers based on the operation code.
    
    Args:
        op_code (int): The operation code:
            1 for addition,
            2 for subtraction,
            3 for division,
            4 for multiplication,
            5 to exit.
        num1 (float): The first number.
        num2 (float): The second number.
    
    Returns:
        float: The result of the operation. The result is displayed, and the program loops until the user chooses to exit.
    
    Raises:
        ValueError: If the operation code is invalid or if division by zero is attempted.
    """
    if op_code == 1:
        return num1 + num2
    elif op_code == 2:
        return num1 - num2
    elif op_code == 3:
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        else:
            return num1 / num2
    elif op_code == 4:
        return num1 * num2
    else:
        raise ValueError("Invalid operation code")


def main():
    print("Simple Calculator")
    print("----------------")
    
    while True:
        print("\nAvailable operations:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Division")
        print("4: Multiplication")
        print("5: Exit")
        
        try:
            op_code = int(input("\nEnter operation code (1-4) or 5 to exit: "))
            
            if op_code == 5:
                print("Calculator exiting. Goodbye!")
                break
                
            if op_code not in [1, 2, 3, 4]:
                print("Error: Invalid operation code. Please enter a number between 1 and 4.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            result = arithmetic_operation(op_code, num1, num2)
            
            operations = {1: "+", 2: "-", 3: "/", 4: "*"}
            print(f"Result: {num1} {operations[op_code]} {num2} = {result}")
        
        except ValueError as e:
            if "division by zero" in str(e).lower():
                print("Error: Division by zero is not allowed.")
            elif "invalid operation code" in str(e).lower():
                print("Error: Invalid operation code. Please enter a number between 1 and 4.")
            elif "invalid literal" in str(e).lower():
                print("Error: Please enter valid numbers.")
            else:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()