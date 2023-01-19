try:
    x = 1
    if num2 == 10:
        raise NameError("Just a nonsense errorr...")
except NameError as e:
    print(e)