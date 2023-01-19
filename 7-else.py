try:
    # some code that could raise an exception
    x = 1 / 0
except ZeroDivisionError:
    # code to handle the ZeroDivisionError exception
    print("division by zero!")
else:
    # code to run if no exception was raised
    print("all good!")