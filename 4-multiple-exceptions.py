try:
    x = 1 / 0
except ZeroDivisionError:
    print("division by zero")
except TypeError:
    print("unsupported operand type")
except NameError:
    print("This variable is not defined.")
print("I reached here...")