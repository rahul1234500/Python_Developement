# Dictionary in Python 


person_Data = {
    "name" : "Rahul Vikas Kale",
    "age" : 23,
    "address" : ["Pune", "Maharashtra", "India", 421010]
}
# check type in dictionary 
print(type(person_Data["address"]))

# sorted 
print(sorted(person_Data))

# values 
print(person_Data.values())

# items 
print(person_Data.items())

# get 

print(person_Data.get("address"))

# update  

person_Data.update({"age" : 22})

print(person_Data)

# some practice example and useful cases 

employee_data = {
    101 : ["Rahul Kale", "Java Developer", 25000.00, "Pune",],
    102 : ["Pritham Shende", "Angular Developer", 60000.00, "Mumbai",],
    103 : ["Arpit Kulkanrne", "Frontend Developer", 30000.00, "Nagpur",],
    104 : ["Alex Doo", "Full Stack Developer", 80000.00, "USA",],
}


del employee_data[104]

print(employee_data)
print(employee_data[101])
print(employee_data[101][0:-1])
print(type(employee_data[102]))

print(list(employee_data.keys()))

print(list(employee_data.values()))

