def search_students(keyword):
    result = []
    for student in students:
        if keyword.lower() in student["name"].lower():
            result.append(student)
    return result

# Kiểm tra:
print(search_students("Nguyen"))

