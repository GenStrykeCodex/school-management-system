ALLOWED_SUBJECTS = [
    "Maths",
    "English",
    "Physics",
    "Chemistry",
    "Biology",
    "Computer Science"
]


def validate_student_id(student_id):
    if not student_id.startswith("ID_"):
        raise ValueError("Student ID must start with 'ID_'")

    numeric_part = student_id.split("_")[1]

    if not numeric_part.isdigit():
        raise ValueError("Student ID format invalid")

    return True


def validate_teacher_id(teacher_id):
    if not teacher_id.startswith("TCH_"):
        raise ValueError("Teacher ID must start with 'TCH_'")

    numeric_part = teacher_id.split("_")[1]

    if not numeric_part.isdigit():
        raise ValueError("Teacher ID format invalid")

    return True


def validate_name(name):
    if not name.replace(" ", "").isalpha():
        raise ValueError("Name should contain only letters and spaces.")
    return True


def validate_class(student_class):
    if not student_class.isdigit():
        raise ValueError("Class must be an integer.")

    student_class = int(student_class)

    if student_class < 1 or student_class > 12:
        raise ValueError("Class must be between 1 and 12.")

    return True


def validate_roll_no(roll_no):
    if not roll_no.isdigit():
        raise ValueError("Roll number must be an integer.")

    roll_no = int(roll_no)

    if roll_no <= 0:
        raise ValueError("Roll number must be positive.")

    return True


def validate_marks(marks):
    if not isinstance(marks, list):
        raise ValueError("Marks must be a list.")

    if len(marks) != 5:
        raise ValueError("Exactly 5 subject marks required.")

    for m in marks:
        if not isinstance(m, (int, float)):
            raise ValueError("Marks must be numeric.")

        if m < 0 or m > 100:
            raise ValueError("Marks must be between 0 and 100.")

    return True


def validate_subject(subject):
    normalized = subject.strip().title()

    if normalized not in ALLOWED_SUBJECTS:
        raise ValueError(f"Subject must be one of: {', '.join(ALLOWED_SUBJECTS)}")

    return normalized


def validate_salary(salary):
    if not isinstance(salary, (int, float)):
        raise ValueError("Salary must be numeric.")

    if salary <= 0:
        raise ValueError("Salary must be positive.")

    return True
