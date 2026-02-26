num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))

op = input("Enter an Operation (+ , - , x . /) : ")

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "x" or op == "X":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)
    
else:
    print("Invalid Operator")