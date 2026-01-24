from models.teacher import Teacher
from utils.file_handler import load_data, save_data
from utils.id_generator import generate_id
from utils.validators import validate_name, validate_subject, validate_salary, validate_teacher_id

TEACHER_FILE = "data/teachers.json"


# adding teachers in the dictionary and updating JSON
def add_teacher(name, subject, salary):
    try:
        teachers_data = load_data(TEACHER_FILE)

        validate_name(name)
        validate_subject(subject)
        validate_salary(salary)

        teacher_id = generate_id(teachers_data, "teacher_id", prefix="TCH_")

        teacher = Teacher(teacher_id, name, subject, salary)

        teachers_data.append(teacher.to_dict())
        save_data(TEACHER_FILE, teachers_data)

        return True, teacher_id

    except ValueError as e:
        return False, str(e)


# show the list of all teachers
def get_all_teachers():
    try:
        teachers_data = load_data(TEACHER_FILE)

        if not teachers_data:
            return False, "No teachers found"

        return True, teachers_data

    except Exception as e:
        return False, str(e)


# searching students
def find_teacher_by_id(teacher_id):
    try:
        validate_teacher_id(teacher_id)

        teachers_data = load_data(TEACHER_FILE)

        for teacher in teachers_data:
            if teacher["teacher_id"] == teacher_id:
                return True, teacher

        return False, "Teacher not found"

    except ValueError as e:
        return False, str(e)


# updating salary of teachers based on ID
def update_teacher_salary(teacher_id, new_salary):
    try:
        validate_teacher_id(teacher_id)
        validate_salary(new_salary)

        teachers_data = load_data(TEACHER_FILE)

        for teacher in teachers_data:
            if teacher["teacher_id"] == teacher_id:
                teacher_name = teacher["name"]
                old_salary = teacher["salary"]
                teacher["salary"] = new_salary
                save_data(TEACHER_FILE, teachers_data)

                return True, f"Salary of {teacher_name} successfully updated from {old_salary} to {new_salary}"

        return False, "Teacher not found"

    except ValueError as e:
        return False, str(e)


# delete a student by the ID
def delete_teacher(teacher_id):
    try:
        validate_teacher_id(teacher_id)

        teachers_data = load_data(TEACHER_FILE)

        for index, teacher in enumerate(teachers_data):
            if teacher["teacher_id"] == teacher_id:
                del teachers_data[index]
                save_data(TEACHER_FILE, teachers_data)

                return True, "Teacher deleted successfully"

        return False, "Teacher not found"

    except ValueError as e:
        return False, str(e)
