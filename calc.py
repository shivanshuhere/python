# num1 = 0 
# num2 = 0 
# operator = None
# result =  0


# num1 =  int(input("Enter your first number :"))
# num2 =  int(input("Enter your second number :"))
# operator =  input("Enter your operator : + - * / ")


# def add():
#     result = num1 + num2
#     return result

# def sub():
#     result = num1 - num2
#     return result

# if (operator == "+"):
#     print(f"sum is :{add()}")
# elif (operator == "-"):
#     print(f"sum is :{sub()}")
# else:
#     print("invalid operator")
    
    
import random

otp = ""
def generateOtp(digits):
    for i in range(digits):
        otp += str(random.randint(0, 10))
    return otp


generateOtp(4)
generateOtp(5)
generateOtp(7)




