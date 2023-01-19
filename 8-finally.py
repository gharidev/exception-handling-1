try:
    x = 1 / 1
except ZeroDivisionError:
    print("division by zero!")
finally:
    print("This is excecuted in any case.")