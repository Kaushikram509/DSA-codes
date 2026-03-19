student_name = ""
student_status = ""

def show_menu():
    print("\n -----Attendance Tracker-----")
    print("1. Add attendance")
    print("2. view Attendance")
    print("3. exit")

def Add_attendance():
    global student_name
    global student_status

    student_name = input("Enter student name: ")
    student_status = input("enter student status(present/abscent): ")

    print("attandance added successfully....")

def view_attandance():
    if(student_name==""):
        print("attendance rocord found")
    else:
        print("\n-------attendance record-------")
        print(student_name,"-",student_status)

def main():
    while True:
        show_menu()
        choice = input("Entert your choice: ")

        if(choice==1):
            Add_attendance()
        elif(choice==2):
            view_attandance()
        elif(choice==3):
            print("exiting attendance prgm")
            break
        else:
            print("invalid data")
main()
