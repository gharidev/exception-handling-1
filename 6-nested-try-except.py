try:
   # Outer try block
   x = 1 / 1
   try:
      # Inner try block
      y = 4 + 3
   except TypeError:
      print("unsupported operand type(s) for +: 'str' and 'int'")
   print(name)
except ZeroDivisionError:
   print("division by zero!")
except NameError:
   print("Variable not defined.")