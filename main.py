""" School Management System version 0.4 (UNDER DEVELOPMENT) """

# importing modules

# greeting users
print("\nWelcome to School Management System v0.4!")


# helper function for pauses between actions
def pause():
    input("Press Enter to return")


# helper function to get user choice
def choice(num):
    while True:
        try:
            option = int(input(f"\nChoose an option (1-{num}): "))
            return option

        except ValueError:
            print("Sorry! That's not an valid option.")


# student manager menu
def student_menu():
    print("\n------- Student Manager -------\n")
    print("1. Add Student details")
    print("2. View all students")
    print("3. Search a Student")
    print("4. Update Student details")
    print("5. Remove Student")
    print("6. Return to main menu")
    print("\n-------------------------------")


# teacher manager menu
def teacher_menu():
    print("\n------- Teacher Manager -------\n")
    print("1. Add Teacher details")
    print("2. View all Teachers")
    print("3. Search a Teacher")
    print("4. Update Teacher details")
    print("5. Remove Teacher")
    print("6. Return to main menu")
    print("\n-------------------------------")


# main menu of the application
def main_menu():
    print("\n----- School Management System -----\n")
    print("1. Student Management")
    print("2. Teacher Management")
    print("3. Reports & Analytics")
    print("4. Exit")
    print("\n------------------------------------")


# main function of student manager
def student_main():
    while True:
        student_menu()  # display the student manager menu

        while True:
            option = choice(6)

            if option == 1:
                # add a student
                pause()
                break

            elif option == 2:
                # view all students
                pause()
                break

            elif option == 3:
                # search a student
                pause()
                break

            elif option == 4:
                # update student details
                pause()
                break

            elif choice == 5:
                # remove a student
                pause()
                break

            elif choice == 6:
                print("Returning to main menu...")
                return

            else:
                print("Sorry! Your choice is out of valid range.")


# main function of student manager
def teacher_main():
    while True:
        teacher_menu()  # display the student manager menu

        while True:
            option = choice(6)

            if option == 1:
                # add a teacher
                pause()
                break

            elif option == 2:
                # view all teachers
                pause()
                break

            elif option == 3:
                # search a teacher
                pause()
                break

            elif option == 4:
                # update teacher details
                pause()
                break

            elif choice == 5:
                # remove a teacher
                pause()
                break

            elif choice == 6:
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

                break

            elif option == 3:
                print("\nInitiating Reports & Analytics...")

                break

            elif option == 4:
                print("\nExiting the application...")
                return

            else:
                print("Sorry! Your choice is out of valid range.")


if __name__ == "__main__":
    main()

print("Thank you for using our application :)")
