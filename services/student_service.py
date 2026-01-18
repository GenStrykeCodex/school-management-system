from utils.file_handler import load_data, save_data
from utils.id_generator import generate_id

STUDENT_FILE = "data/students.json"

# adding students in the dictionary and updating JSON
def add_student(name, student_class, roll_no, marks):

    students = load_data(STUDENT_FILE)          # loading JSON data in list

    student_id = f"ID_{generate_id(students)}"  # generating unique ID for students

    student_details = {
        "student_id": student_id,
        "name": name,
        "class": student_class,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student_details)            # updating the list
    save_data(STUDENT_FILE, students)           # updating the JSON data

    return student_id


def get_all_students(st_class):
    pass

def find_student_by_id(student_id):
    pass

def find_student_by_roll_no(roll_no):
    pass

def update_student_marks(student_id, new_marks):
    pass

def delete_student(student_id):
    pass