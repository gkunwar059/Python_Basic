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


# finally 
    #  sucess or not ==> conncetion is close finally 
    # file clean up /conncetion close 
    # n the end.
    # 
    # database kholeu hamle try and except block ma code j sukai operation hos finally ma chai conncetion close hunxa . jasari pani ending ma define hunxa 
    # 
    # You can use finally to make sure files or resources are closed or released regardless of whether an exception occurs, 




# -------------------------------------------------important topic of the finally block of exception handling --------------------------------------

    # The finally block is useful for cleanup code that must be executed under all circumstances. 
    # For example, if you open a file in a try block, you would close it in the finally block to 
    # ensure the file gets closed whether the operation was successful or an exception occurred.


# ///////////////////////////code cleanup ko laghi finally use garxau hamle ////////////////////////////////////////////////




