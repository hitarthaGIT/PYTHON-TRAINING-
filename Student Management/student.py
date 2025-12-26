students = {}

def add_student(roll, name):
    students[roll] = name

def get_student(roll):
    return students.get(roll, "Student Not Found")
