import math

history = []

while True:

    op = input("Enter an Operation (+ , - , x , / , ^ , history , clear , exit) : ")

    if (op.lower()) == "exit":
        print()
        break

    elif (op.lower()) == "history":
        if (len(history) == 0):
            print("No history yet\n")
        else:
            print("\nCalculator History")
            for item in history:
                print(item)
            print()
        continue

    elif op.lower() == "clear":
        history.clear()
        print("History Cleared\n")
        continue


    try:
        num1 = float(input("Enter Number 1 : "))
        num2 = float(input("Enter Number 2 : "))
    except:
        print("Enter valid Numbers!\n")
        continue


    if op == "+":
        result = (num1 + num2)
        history.append(f"{num1} + {num2} = {result}")
        print(f"Result = {result}")

    elif op == "-":
        result = (num1 - num2)
        history.append(f"{num1} - {num2} = {result}")
        print(f"Result = {result}")

    elif op.lower() == "x":
        result = (num1 * num2)
        history.append(f"{num1} x {num2} = {result}")
        print(f"Result = {result}")

    elif op == "/":
        if (num2 != 0):
            result = (num1 / num2)
            history.append(f"{num1} / {num2} = {result}")
            print(f"Result = {result}")
        else:
            print("Cannot Divide by Zero")

    elif op == "^":
        result = (num1 ** num2)
        history.append(f"{num1} ^ {num2} = {result}")
        print(f"Result = {result}")

    else:
        print("Invalid Operator\n")
        continue


    again = input("Don another? (y/n) :")
    print()

    if again.lower() == "n" or again == "":
        break