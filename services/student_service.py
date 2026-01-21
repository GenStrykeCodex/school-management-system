from models.student import Student
from utils.file_handler import load_data, save_data
from utils.id_generator import generate_id
from utils.validators import validate_student_id, validate_name, validate_class, validate_roll_no, validate_marks

STUDENT_FILE = "data/students.json"


# adding students in the dictionary and updating JSON
def add_student(name, student_class, roll_no, marks):
    try:
        students_data = load_data(STUDENT_FILE)

        validate_name(name)
        validate_class(student_class)
        validate_roll_no(roll_no)
        validate_marks(marks)

        student_id = generate_id(students_data, "student_id")

        student = Student(student_id, name, student_class, roll_no, marks)

        students_data.append(student.to_dict())
        save_data(STUDENT_FILE, students_data)

        return True, student_id

    except ValueError as e:
        return False, str(e)


# show the list of all students in a given class
def get_students_by_class(student_class):
    try:
        validate_class(student_class)

        students_data = load_data(STUDENT_FILE)

        filtered_students = []

        for student in students_data:
            if student["class"] == student_class:
                filtered_students.append(student)

        return True, filtered_students

    except ValueError as e:
        return False, str(e)


# searching students
def find_student_by_id(student_id):
    try:
        validate_student_id(student_id)

        students_data = load_data(STUDENT_FILE)

        for student in students_data:
            if student["student_id"] == student_id:
                return True, student

        return False, "Student not found"

    except ValueError as e:
        return False, str(e)


def find_student_by_roll(student_class, roll_no):
    try:
        validate_class(student_class)
        validate_roll_no(roll_no)

        students_data = load_data(STUDENT_FILE)

        for student in students_data:
            if student["class"] == student_class and student["roll_no"] == roll_no:
                return True, student

        return False, "Student not found"

    except ValueError as e:
        return False, str(e)


# updating marks of students based on ID
def update_student_marks(student_id, new_marks):
    try:
        validate_student_id(student_id)
        validate_marks(new_marks)

        students_data = load_data(STUDENT_FILE)

        for student in students_data:
            if student["student_id"] == student_id:
                student["marks"] = new_marks
                save_data(STUDENT_FILE, students_data)

                return True, "Marks updated successfully"

        return False, "Student not found"

    except ValueError as e:
        return False, str(e)


# delete a student by the ID
def delete_student(student_id):
    try:
        validate_student_id(student_id)

        students_data = load_data(STUDENT_FILE)

        for index, student in enumerate(students_data):
            if student["student_id"] == student_id:
                del students_data[index]
                save_data(STUDENT_FILE, students_data)

                return True, "Student deleted successfully"

        return False, "Student not found"

    except ValueError as e:
        return False, str(e)
