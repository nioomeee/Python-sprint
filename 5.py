# dictionaries
student = {
    "name" : "Niomi",
    "rank" : 3,
    "skills" : ["Java", "Python"]
}

# unsafe way: student["name"]

# safe way:
name = student.get("name")
age = student.get("age")
print(name)
print(age)