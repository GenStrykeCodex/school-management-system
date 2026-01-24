""" School Management System version 1.0 (Initial Release) """

# importing modules
from services.student_service import (
    add_student,
    get_students_by_class,
    find_student_by_id,
    find_student_by_roll,
    update_student_marks,
    delete_student
)

from services.teacher_service import (
    add_teacher,
    get_all_teachers,
    find_teacher_by_id,
    update_teacher_salary,
    delete_teacher
)

from services.report_service import (
    get_student_report,
    get_class_topper,
    get_class_average,
    get_class_pass_fail
)


# constant values
STUDENT_MENU_SIZE = 6
TEACHER_MENU_SIZE = 6
REPORT_MENU_SIZE = 5


# greeting users
print("\nWelcome to School Management System v1.0!")


''' Helper Functions '''

# helper function for pauses between actions
def pause():
    input("\nPress Enter to return")


# helper function to get user choice
def choice(num):
    while True:
        try:
            option = int(input(f"\nChoose an option (1-{num}): "))
            return option

        except ValueError:
            print("Sorry! That's not an valid option.")


# helper function to get marks of student
def get_marks():
    marks = []
    sub = 0
    while sub < 5:
        mark = input(f"Enter marks in subject {sub+1}: ")
        try:
            mark = float(mark)
            marks.append(mark)
        except ValueError:
            print("Sorry! Please enter a numeric value.")
            continue

        sub += 1

    return marks


# helper function to get salary
def get_salary():
    while True:

        try:
            salary = float(input("Enter salary: "))
            return salary

        except ValueError:
            print("Sorry! Please enter a numeric value.")


''' Menu Functions '''

# student manager menu
def student_menu():
    print("\n------- Student Manager -------\n")
    print("1. Add Student details")
    print("2. View all students in a class")
    print("3. Search a Student")
    print("4. Update Student Marks")
    print("5. Remove Student")
    print("6. Return to main menu")
    print("\n-------------------------------")


# teacher manager menu
def teacher_menu():
    print("\n------- Teacher Manager -------\n")
    print("1. Add Teacher details")
    print("2. View all Teachers")
    print("3. Search a Teacher")
    print("4. Update Teacher Salary")
    print("5. Remove Teacher")
    print("6. Return to main menu")
    print("\n-------------------------------")


# reports & analytics menu
def reports_menu():
    print("\n------- Reports & Analytics -------\n")
    print("1. View Student Report")
    print("2. View Class Topper")
    print("3. View Class Average")
    print("4. View Class Report")
    print("5. Return to main menu")
    print("\n----------------------------------")


# main menu of the application
def main_menu():
    print("\n----- School Management System -----\n")
    print("1. Student Management")
    print("2. Teacher Management")
    print("3. Reports & Analytics")
    print("4. Exit")
    print("\n------------------------------------")


''' Student Handler Functions '''

# handle adding students
def add_student_handler():
    print("\nFill the Student Details --")

    name = input("\nEnter student name: ")
    st_class = input("Enter the Class: ")
    roll_no = input("Enter roll no: ")
    marks = get_marks()

    success, result = add_student(name, st_class, roll_no, marks)

    if success:
        print("Student added successfully with ID:", result)
    else:
        print("Error:", result)


# handle view students
def view_student_handler():
    print("\nView the Students in a class --")
    st_class = input("\nEnter the Class: ")

    success, result = get_students_by_class(st_class)

    if success:
        print("\n" + "=" * 45)
        print(f"{'#':<5} {'ID':<7} {'Name':<20} {'Roll No':<10}")
        print("=" * 45)

        for i, student in enumerate(result):
            student_id = list(student.values())[0]
            student_name = list(student.values())[1]
            student_roll = list(student.values())[3]

            print(f"{i+1:<5} {student_id:<7} {student_name:<20} {student_roll:<10}")

        print("=" * 45)

    else:
        print("Error:", result)


# handle find students
def find_student_handler(para):
    if para == "id":
        student_id = input("Enter student ID: ")
        success, result = find_student_by_id(student_id)

    elif para == "roll":
        st_class = input("Enter the Class: ")
        roll_no = input("Enter roll no: ")
        success, result = find_student_by_roll(st_class, roll_no)

    else:
        success = False
        result = "Invalid argument for searching students"

    if success:
        student_id = list(result.values())[0]
        student_name = list(result.values())[1]
        student_class = list(result.values())[2]
        student_roll = list(result.values())[3]

        print("\nStudent Details --\n")
        print(f"ID: {student_id}")
        print(f"Name: {student_name}")
        print(f"Class: {student_class}")
        print(f"Roll: {student_roll}")

    else:
        print("Error:", result)


# handle marks update
def marks_update_handler():
    print("\nUpdate the Student Marks --")

    student_id = input("Enter student ID (eg., 'ID_2'): ")
    new_marks = get_marks()

    success, result = update_student_marks(student_id, new_marks)

    if success:
        print(result)
    else:
        print("Error:", result)


# handle student deletion
def student_delete_handler():
    print("\nDelete a Student by ID --")

    student_id = input("Enter student ID (eg., 'ID_2'): ")

    confirm = input("\nAre you sure you want to delete this student? (y/n): ").lower()

    if confirm == "y":
        success, result = delete_student(student_id)

        if success:
            print(result)
        else:
            print("Error:", result)
    else:
        print("Student Deletion Cancelled by User..")


''' Teacher Handler Functions '''

# handle adding teachers
def add_teacher_handler():
    print("\nFill the Teacher Details --")

    name = input("\nEnter teacher name: ")
    subject = input("Enter the subject: ")
    salary = get_salary()

    success, result = add_teacher(name, subject, salary)

    if success:
        print("Teacher added successfully with ID:", result)
    else:
        print("Error:", result)


# handle view teachers
def view_teacher_handler():
    print("\nView all Teachers --")

    success, result = get_all_teachers()

    if success:
        print("\n" + "=" * 65)
        print(f"{'#':<5} {'ID':<7} {'Name':<20} {'Subject':<20} {'Salary':<10}")
        print("=" * 65)

        for i, teacher in enumerate(result):
            teacher_id = list(teacher.values())[0]
            teacher_name = list(teacher.values())[1]
            teacher_subject = list(teacher.values())[2]
            teacher_salary = list(teacher.values())[3]

            print(f"{i + 1:<5} {teacher_id:<7} {teacher_name:<20} {teacher_subject:<20} {teacher_salary:<10}")

        print("=" * 65)
    else:
        print("Error:", result)


# handle find teachers
def find_teacher_handler():
    print("\nFind a Teacher by ID -- ")
    teacher_id = input("Enter teacher ID (eg., 'TCH_2'): ")

    success, result = find_teacher_by_id(teacher_id)

    if success:
        teacher_id = list(result.values())[0]
        teacher_name = list(result.values())[1]
        teacher_subject = list(result.values())[2]
        teacher_salary = list(result.values())[3]

        print("\nStudent Details --\n")
        print(f"ID: {teacher_id}")
        print(f"Name: {teacher_name}")
        print(f"Subject: {teacher_subject}")
        print(f"Salary: {teacher_salary}")
    else:
        print("Error:", result)


# handle salary update
def update_salary_handler():
    print("\nUpdate the Teacher Salary --")

    teacher_id = input("Enter teacher ID (eg., 'TCH_2'): ")
    new_salary = get_salary()

    success, result = update_teacher_salary(teacher_id, new_salary)

    if success:
        print(result)
    else:
        print("Error:", result)


# handle teacher deletion
def teacher_delete_handler():
    print("\nDelete a Teacher by ID --")

    teacher_id = input("Enter teacher ID (eg., 'TCH_2'): ")

    confirm = input("\nAre you sure you want to delete this student? (y/n): ").lower()

    if confirm == "y":
        success, result = delete_teacher(teacher_id)

        if success:
            print(result)
        else:
            print("Error:", result)
    else:
        print("Teacher Deletion Cancelled by User..")


''' Reports Handler Functions '''

# handle student report
def student_report_handler():
    print("\nGet Student Reports --")

    student_id = input("\nEnter student ID (eg., 'ID_2'): ")

    success, result = get_student_report(student_id)

    if success:
        student = list(result.values())

        print("\nStudent Details --\n")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Class: {student[2]}")
        print(f"Roll: {student[3]}")
        print(f"Marks: {student[4]}")
        print(f"Percentage: {student[5]} %")
        print(f"Status: {student[6]}")

    else:
        print("Error:", result)


# handle class topper
def class_topper_handler():
    print("\nView Class Topper --")

    st_class = input("\nEnter the Class: ")

    success, result = get_class_topper(st_class)

    if success:
        print(f"Class {st_class} Topper -- ")
        topper_id = list(result.values())[0]
        topper_name = list(result.values())[1]
        topper_roll = list(result.values())[3]
        topper_percent = list(result.values())[4]

        print("\n" + "=" * 55)
        print(f"{'ID':<7} {'Name':<20} {'Roll No':<10} {'Percentage':<20}")
        print("=" * 55)
        print(f"{topper_id:<7} {topper_name:<20} {topper_roll:<10} {topper_percent:<20}")
        print("=" * 55)

    else:
        print("Error:", result)


# handle class average percentage
def class_average_handler():
    print("\nView Class Average --")

    st_class = input("\nEnter the Class: ")

    success, result = get_class_average(st_class)

    if success:
        print(f"\nAverage percentage of Class {st_class}: {result}%")

        if result < 40:
            print("Very poor performance! Needs improvement.")

        elif result < 70:
            print("Poor performance! Needs improvement.")

        elif result < 90:
            print("Good performance! Needs slight improvement.")

        else:
            print("Great Performance! Keep up the pace.")

    else:
        print("Error:", result)


# handle class report
def class_report_handler():
    print("\nView Class Report --")

    st_class = input("\nEnter the Class: ")
    print("\nDefault passing percentage is 40 %")
    option = input("Go with default value (y/n): ").lower()

    if option == "y":
        success, result = get_class_pass_fail(st_class)

    else:
        while True:
            print("Set a new Passing Percentage --")
            try:
                pass_percent = float(input("Percent: "))

                if not 30 < pass_percent < 60:
                    success = False
                    result = "Passing percent must be between 30 and 60"
                    break

                success, result = get_class_pass_fail(st_class, pass_percent)
                break

            except ValueError:
                print("Please enter a valid percentage")

    if success:
        report = list(result.values())
        print(f"\nClass {st_class} Details --\n")
        print(f"Total Students: {report[1]}")
        print(f"Passed Students: {report[2]}")
        print(f"Failed Students: {report[3]}")

    else:
        print("Error:", result)


''' Main Controller Functions '''

# main function of student manager
def student_main():
    while True:
        student_menu()  # display the student manager menu

        while True:
            option = choice(STUDENT_MENU_SIZE)

            if option == 1:
                # add a student
                add_student_handler()

                pause()
                break

            elif option == 2:
                # view student by class
                view_student_handler()

                pause()
                break

            elif option == 3:
                # find a student by ID or roll
                print("Find a student by -- ")
                para = input("\n'ID' or 'Roll': " ).lower()

                find_student_handler(para)

                pause()
                break

            elif option == 4:
                # update student marks
                marks_update_handler()

                pause()
                break

            elif option == 5:
                # remove a student
                student_delete_handler()

                pause()
                break

            elif option == 6:
                print("Returning to main menu...")
                return

            else:
                print("Sorry! Your choice is out of valid range.")


# main function of teacher manager
def teacher_main():
    while True:
        teacher_menu()  # display the student manager menu

        while True:
            option = choice(TEACHER_MENU_SIZE)

            if option == 1:
                # add a teacher
                add_teacher_handler()

                pause()
                break

            elif option == 2:
                # view all teachers
                view_teacher_handler()

                pause()
                break

            elif option == 3:
                # search a teacher
                find_teacher_handler()

                pause()
                break

            elif option == 4:
                # update teacher salary
                update_salary_handler()

                pause()
                break

            elif option == 5:
                # remove a teacher
                teacher_delete_handler()

                pause()
                break

            elif option == 6:
                print("Returning to main menu...")
                return

            else:
                print("Sorry! Your choice is out of valid range.")


# main function of reports & analytics
def reports_main():
    while True:
        reports_menu()  # display the report menu

        while True:
            option = choice(REPORT_MENU_SIZE)

            if option == 1:
                # view student report
                student_report_handler()

                pause()
                break

            elif option == 2:
                # view class topper
                class_topper_handler()

                pause()
                break

            elif option == 3:
                # view class average
                class_average_handler()

                pause()
                break

            elif option == 4:
                # view class report
                class_report_handler()

                pause()
                break

            elif option == 5:
                print("Returning to main menu...")
                return

            else:
                print("Sorry! Your choice is out of valid range.")


# main function of the application
def main():
    while True:
        main_menu()  # display the main menu

        while True:
            option = choice(4)

            if option == 1:
                print("\nInitiating Student Manager...")
                student_main()
                break

            elif option == 2:
                print("\nInitiating Teacher Manager...")
                teacher_main()
                break

            elif option == 3:
                print("\nInitiating Reports & Analytics...")
                reports_main()
                break

            elif option == 4:
                print("\nExiting the application...")
                return

            else:
                print("Sorry! Your choice is out of valid range.")


if __name__ == "__main__":
    main()

print("Thank you for using our application :)")