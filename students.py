import csv

with open("students.csv", "w",  newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Deborah", 20, "Computer Engineering"])
    writer.writerow(["Grace", 22, "Mathematics"])

print("Student records saved successfully!")

