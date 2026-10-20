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



input_dict = {'Name' : 'Rahul Kale', 'Profession' : 'Signer'}

if "Name" in input_dict.keys():
    print(input_dict["Name"])
else :
    print("NA")


my_dict = {
    "Z" : 100,
    "X" : 200,
    "M" : 300,
    "N" : 400,
    "Y" : 600,
    "A" : 50,
    "B" : 90
}

print(sorted(my_dict.values()))
print(sorted(my_dict.keys()))
print(sorted(my_dict.items()))