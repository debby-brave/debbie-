import json

with open("student.json", "r") as file:
     
    student = json.load(file)


print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Country:", student["country"])
print("Student Course:", student["course"])