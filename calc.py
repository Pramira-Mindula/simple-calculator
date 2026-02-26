while True:

    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))

    op = input("Enter an Operation (+ , - , x . /) : ")

    if op == "+":
        print(f"Result = {num1 + num2}")

    elif op == "-":
        print(f"Result = {num1 - num2}")

    elif op.lower() == "x":
        print(f"Result = {num1 * num2}")

    elif op == "/":
        if (num2 != 0):
            print(f"Result = {num1 / num2}")
        else:
            print("Cannot Divide by Zero")

    else:
        print("Invalid Operator\n")


    again = input("Don another? (y/n) :")

    if again == "n" or again == "":
        break