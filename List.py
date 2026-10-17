# List in Python 

# List 

shopping_list = ['Pen', 'Notebook', 'Eraser', 'Shapner']

print(type(shopping_list))

# List 
my_list = [1, "Rahul", "Pune", True]

print(type(my_list))

# length 

print(len(my_list))

# nested list 

some_extra_details = [1,'Rahul kale','Pune', ['India', 'Maharashtra'], '9828182891']
#   0  1  2  3  4  -> positive indexing from left side 
#  -5 -4 -3 -2 -1  -> negative indexing from right side 
print(some_extra_details[3])
print(some_extra_details[3][0])
print(some_extra_details[-2][0])


# slicing 
print(some_extra_details[-1])


# list concatention 

list_1 = [1,2,3,4]
list_2 = [5,6,7,8]

new_list = list_1 + list_2

print(new_list)

new_list += [9,10]

print(new_list)

cart_1 = ["Mango", "Banana", "Apple"]
cart_2 = ["Pineapple", "Watermolen", "Orange"]

print("Pineapple" in cart_2)

# Mutability 

subject_list = ["Java", "Spring Boot", "Sql", "JavaScript", "ReactJs"] 
print(subject_list)
subject_list[-1] = "Angular.ts"
print(subject_list)

# extend method 
subject_marks = [50,20,40]
subject_marks.extend([60,50])
print(subject_marks)


# append method 

subject_marks.append([70])
print(subject_marks)

# del command 

del subject_marks[0]
print(subject_marks)

# pop method 

subject_marks.pop(2)
print(subject_marks)

# remove method 

subject_marks.remove(50)
print(subject_marks)

subject_index = [2,4,1,5,3,6,8,6,7]

# sort method 
subject_index.sort()
print(subject_index)
subject_index_ = subject_index.sort()
print(subject_index_)

subject_index.sort(reverse=True)

print(subject_index)
# sorted 


fruit_list_1 = ["Apple","Kiwi","Orange","Watermelon","Chiku"]

fruit_list_2 = sorted(fruit_list_1)

print(fruit_list_2)


# shallow copy

A = [10,30,50]
B = A
print(B)
print(A)

A.pop()
print(A)
print(B)

C = ["Mongo","Peach","Watermelon"]

D = C[0:3]

print(D)

C.pop()
print(C)
print(D)


str = "Rahul_Vikas_Kale"

my_name = str.split('_')

print(my_name)


