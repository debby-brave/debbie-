import csv

name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter student course:")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([name, age, course])

print("New student added successfully!")         