import pdb
bike1="Yamaha"
bike2="Bajaj"

bike1_price=2500

bike2_price=34560

pdb.set_trace()

name=input("Enter your name :\n")

choice=int(input("Enter 1 for yamaha and 2 for Bajaj !:\n"))
print(f" hello {name}")
# assumption error will be from here
# breakpoint()
# pdb

if choice==1:
    print(f"The price of {bike1} is {bike1_price}")

elif choice==2:
    print(f"the price of bike+ {bike2 +2000} is {bike1_price}")

else:
    print("Press only 1 or 2")
