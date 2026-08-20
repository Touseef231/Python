students = ["Ali", "Sara", "Ahmed",]
option = 3982
def show_students():
    count = 1
    for student in students:
        print(f"{count}.{student}")
        count = count + 1
def add_students():
    student_adding = input("Enter Student name: ")
    students.append(student_adding)
    print("Sucessfully added")
def remove_student():
    count = 0
    for student in students:
        print(f"{count}.{student}")
        count = count + 1
    student_removing = int(input("Enter Student index to remove: "))
    if 0 <= student_removing < len(students):
        students.pop(student_removing)
        print("Student removed")
    else:
        print("Invalid student index")
while option != 4:
    print("===== Students-List =====",
    "1.Show Students",
    "2.Add Student",
    "3.Remove Student",
    "4.Exit", 
    sep = "\n")
    option = int(input("What you want to do: "))
    if option == 1:
        show_students()
    elif option ==2:
        add_students()
    elif option ==3:
        remove_student()
    elif option ==4:
        print("Get out")
    else:
        print("Learn to type and go to optometry")

    