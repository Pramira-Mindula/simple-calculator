import math

class Calculator:

    def __init__(self):
        self.history = []

    def show_history(self):
        if len(self.history) == 0:
            print("No history yet\n")
        else:
            print("\nCalculator History")
            for item in self.history:
                print(item)
            print()

    def clear_history(self):
        self.history.clear()
        print("History Cleared\n")

    def calculate(self, op, num1, num2):

        if op == "+":
            result = num1 + num2
            self.history.append(f"{num1} + {num2} = {result}")
            return result

        elif op == "-":
            result = num1 - num2
            self.history.append(f"{num1} - {num2} = {result}")
            return result

        elif op.lower() == "x":
            result = num1 * num2
            self.history.append(f"{num1} x {num2} = {result}")
            return result

        elif op == "/":
            if num2 != 0:
                result = num1 / num2
                self.history.append(f"{num1} / {num2} = {result}")
                return result
            else:
                return "Cannot Divide by Zero"

        elif op == "^":
            result = num1 ** num2
            self.history.append(f"{num1} ^ {num2} = {result}")
            return result

        else:
            return "Invalid Operator"

    def run(self):

        while True:

            op = input("Enter an Operation (+ , - , x , / , ^ , history , clear , exit) : ")

            if op.lower() == "exit":
                print()
                break

            elif op.lower() == "history":
                self.show_history()
                continue

            elif op.lower() == "clear":
                self.clear_history()
                continue

            try:
                num1 = float(input("Enter Number 1 : "))
                num2 = float(input("Enter Number 2 : "))
            except:
                print("Enter valid Numbers!\n")
                continue

            result = self.calculate(op, num1, num2)
            print(f"Result = {result}")

            again = input("Do another? (y/n) :")
            print()

            if again.lower() == "n" or again == "":
                break


calc = Calculator()
calc.run()