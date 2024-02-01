#     print("You can't divide zero !!")

# while True:
try:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    num=a/b

    
    print(num)
except ZeroDivisionError :
    print("You cant divide by zero ")


except ValueError:
    print("Please input the valid number")

else:
    print("Nice ")
