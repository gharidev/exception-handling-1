while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")
        if operator == "+":
            result = num1 + num2
            print("Result:", result)
        elif operator == "-":
            result = num1 - num2
            print("Result:", result)
        elif operator == "*":
            result = num1 * num2
            print("Result:", result)
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("division by zero")
            else:
                result = num1 / num2
                print("Result:", result)
        elif operator == "q" or operator == "Q":
            print("Exiting...")
            break
        else:
            raise ValueError("Invalid operator")

    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except:
        print("An error occured")
