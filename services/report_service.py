from utils.file_handler import load_data
from utils.validators import validate_class, validate_student_id

STUDENT_FILE = "data/students.json"


# calculate the percentage
def calculate_percentage(marks):
    if not isinstance(marks, list):
        raise ValueError("Marks must be provided as a list")

    if len(marks) == 0:
        raise ValueError("Marks list cannot be empty")

    total_marks = sum(marks)
    max_marks = len(marks) * 100  # assuming each subject is out of 100

    percentage = (total_marks / max_marks) * 100

    return round(percentage, 2)


# get the report of a student from ID
def get_student_report(student_id):
    try:
        validate_student_id(student_id)

        students_data = load_data(STUDENT_FILE)

        for student in students_data:
            if student["student_id"] == student_id:

                marks = student["marks"]
                percentage = calculate_percentage(marks)

                if percentage >= 40:
                    status = "Pass"
                else:
                    status = "Fail"

                report = {
                    "student_id": student["student_id"],
                    "name": student["name"],
                    "class": student["class"],
                    "roll_no": student["roll_no"],
                    "marks": marks,
                    "percentage": percentage,
                    "status": status
                }

                return True, report

        return False, "Student not found"

    except ValueError as e:
        return False, str(e)


# get the topper of a given class
def get_class_topper(student_class):
    try:
        validate_class(student_class)

        students_data = load_data(STUDENT_FILE)

        topper = None
        topper_percentage = 0

        for student in students_data:
            if student["class"] == student_class:
                percentage = calculate_percentage(student["marks"])
                if percentage > topper_percentage:
                    topper_percentage = percentage
                    topper = student

        if topper is None:
            return False, "No students found in this class"

        topper_report = {
            "student_id": topper["student_id"],
            "name": topper["name"],
            "class": topper["class"],
            "roll_no": topper["roll_no"],
            "percentage": topper_percentage
        }

        return True, topper_report

    except ValueError as e:
        return False, str(e)


# get the average percentage of a class
def get_class_average(student_class):
    try:
        validate_class(student_class)

        students_data = load_data(STUDENT_FILE)

        percentage_list = []

        for student in students_data:
            if student["class"] == student_class:
                percentage_list.append(calculate_percentage(student["marks"]))

        if not percentage_list:
            return False, "No students found in this class"

        class_average = sum(percentage_list) / len(percentage_list)

        return True, round(class_average, 2)

    except ValueError as e:
        return False, str(e)


# get the pass or fail status of students in a class
def get_class_pass_fail(student_class, pass_percentage=40):
    try:
        validate_class(student_class)

        students_data = load_data(STUDENT_FILE)

        pass_count = 0
        fail_count = 0
        total_students = 0

        for student in students_data:

            if student["class"] == student_class:

                total_students += 1

                percentage = calculate_percentage(student["marks"])

                if percentage >= pass_percentage:
                    pass_count += 1
                else:
                    fail_count += 1

        if total_students == 0:
            return False, "No students found in this class"

        report = {
            "class": student_class,
            "total_students": total_students,
            "passed": pass_count,
            "failed": fail_count
        }

        return True, report

    except ValueError as e:
        return False, str(e)
