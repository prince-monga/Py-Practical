def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        print("This block always executes, whether there is an exception or not.")

num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))
divide_numbers(num1, num2)
