def divide_numbers(a,b):
    try:
        result = a/b
        print("Result:",result)
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero")

divide_numbers(10,0)
