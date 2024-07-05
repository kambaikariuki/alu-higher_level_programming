import time
try: 
    numerator = int(input("Enter a number to divide: "))
    time.sleep(0.5)
    denominator = int(input("Enter a number to divide by: "))
    print("Calculating... ")
    time.sleep(0.5)
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("Failed. You can't divide by zero.")
except ValueError as e:
    print(e)
    print("You can only divide numbers.")
except Exception as e:
    print(e)
    print("Something went wrong.")