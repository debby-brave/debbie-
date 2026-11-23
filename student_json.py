import json

student = {
    "name": "Deborah",
    "age": 20,
    "country": "Nigeria",
    "course": "Computer Engineering"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

   