# use a module 
import module 

module.greet("Ganesh kunwar")

# import the modules named mymodule , and acess the person1 dictonary 
a=module.person1['age']
print(a)



# remaining the name of the modules 
import module as mx
b=module.person1['name']
print(b)


# dir() funcction 
x=dir(module)
print(x)

# just call a specific modules 
from module import person1

# while we call like this we should not import module.person1['age']
print(person1['age'])