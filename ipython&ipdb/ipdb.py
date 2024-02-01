# # simple examples of ipdb in python use examples

# # 1.setting a BreakPoint
# import ipdb


# def factorial(n):
#     if n<=0:
#         return 1
#     else:
#         return n*factorial(n-1)
    

# ipdb.set_trace()
# num=5
# fac=factorial(num)
# print("The factorial of ",num,"is ",fac)