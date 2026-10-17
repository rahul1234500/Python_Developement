# simple variable just showing on terminal my name 
name = 'Rahul Kale'

print(name)

# Check data type with type method
print(type(name))

# User input form input()

# username = input("Enter your name :")

# print("Welcome", username)

a = True
b = 'True'

print(type(a))
print(type(b))


# Typecasting 

modelAcc = 91.2
print(modelAcc)

print(type(modelAcc))

modelAcc = int(modelAcc)
print(modelAcc)
print(type(modelAcc))


# example : 

# integer to float 
var1 = 100

print(type(var1))

new_var1 = float(var1)
print(new_var1)

# float to integer 

var2 = 99.99

new_var2 = int(var2)
print(new_var2)


# integer to string

new_message = str(var1)

print(type(new_message))


# string to integer

# var4 = "Hello my name"

# new_convert = int(var4)

# print(new_convert) 
# Traceback (most recent call last):
#   File "/workspaces/Python_Developement/Demo.py", line 63, in <module>
#     new_convert = int(var4)
# ValueError: invalid literal for int() with base 10: 'Hello my name'

# correct example 

val = "99"

val_int = int(val)
print(val_int)

# string to float 

val = "99.99"

# val_int = int(val) first convert it into float that original format inside double quotes 

val_float = float(val)
print(val_float)
print("val_float type :" , type(val_float) , val_float)

val_int = int(val_float)
print(val_int)