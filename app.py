import json

# Tải danh sách sinh viên từ tệp JSON
try:
    with open("students.json", "r") as f:
        students = json.load(f)
except FileNotFoundError:
    students = [{"name": "Nguyen Van A"}]

def search_students(keyword):
    result = []
    for student in students:
        if keyword.lower() in student["name"].lower():
            result.append(student)
    return result

if __name__ == "__main__":
    print(search_students("Nguyen"))
