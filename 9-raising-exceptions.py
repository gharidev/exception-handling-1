try:
    x = 1
    raise NameError("Just a nonsense errorr...")
except NameError as e:
    print(e)