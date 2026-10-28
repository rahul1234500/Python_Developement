# Set in python 

colors = {'red','green','blue'}

print('red' in colors)


# Define pass list in set and remove duplicate elements 

list1 = [1,3,4,2,5,6,7]
print("List Element : ",list1 , "Type check" , type(list1)) 
num_set = set(list1)

print( "Given List : ", list1 , "convert list to set", num_set)
print(type(num_set))

list2 = [1,2,3,1,2,3]

set1 = set(list2)

print(set1)

print(len(set1))
set1.add("hello")
print(set1)
print(len(set1))

# remove element 

set1.remove("hello")
print(set1)

# set operations

A = {0,2,4,6,8}
B = {1,2,3,4,5}

# union 

print(A | B , type(A))
print(A.union(B))
print(len(A.union(B)))

# intersection

print(A & B)
print(A.intersection(B))


# symmetric difference 

print(A^B)

print("-----------------")

val1 = [1,2,3,4,5,6,1,2,3]
val2 = [5,6,7,8,9,1,2,3]

final_set = set(val1) & set(val2)

print(final_set)
