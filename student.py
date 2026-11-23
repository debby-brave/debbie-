name = "Deborah"
course = "Computer Engineering"

with open("student.txt", "w") as file:
    file.write(name + "\n")
    file.write(course)

print("Student information saved successfully!")