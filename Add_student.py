import csv

name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter student course: ")

if name == "":
    print("Error: Student name cannot be empty.")

elif not age.isdigit() or int(age) <= 0:
    print("Error: Please enter a valid age.")

elif course == "":
    print("Error: Course cannot be empty.")

else:
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, course])

    print("New student added successfully!")