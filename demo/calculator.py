a = int(input("enter first number :"))
operator = input("enter operator :")
b = int(input("enter second number :"))

match operator:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "/":
            print(f"{a} / {b} = {a / b}")
    case "%":
        print(f"{a} % {b} = {a % b}")
    case "**":
        print(f"{a} ** {b} = {a ** b}")
    case _:
        print("Invalid operator")
        


