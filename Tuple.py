t = 1,2,3,4
print(type(t))


t1 = ("Rahul", True, 100, 200)

print(t1)

# len of tuple

t2 = (1,2,3,4)

print(len(t2))

# nested tuple

t3 = (10,20,30,(40,50),60)

print(t3)

# different data type 

t4 = (10, "RK", True, [100, 200])

var = t4[3]
print(var)
print(type(var))

person = (101, "Rahul Kale", 20000.00, ["Pune","Maharashtra","India"], 44210)

print(person[3][-2])

# can be defined in various way 

d1 = 1,2,3,4,5

print(d1)

d2 = 1,2,

print(d2)

d3 = (1,2,)

print(d3)

d4 = 1,

print(d4)

d5 = ("Rahul",)

print(d5)

# but this is not tuple it will be treated as int
d6 = 1

print(type(d6))

d7 = (1)

print(type(d7))

# indexing in tuple 

t = ("Python", 200, "Machine Learing", 500)

print(len(t))

print(t[:-3])

t2 = ("A", 10, "B", 100, "C")

print(t2[0:4])