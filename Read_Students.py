import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)     

    for row in reader:
        print("Name:", row[0])
        print("Age:", int(row[1]))
        print("Course:", row[2])
        print("-----------------")
  