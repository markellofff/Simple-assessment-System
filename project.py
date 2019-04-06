def index():
    print("""=======================================================
    Welcome to the Student and Assessment Management System
    <A>add details of a student.
    <I>insert assignment marks of a student
    <S>search assessment marks for a student.
    <Q>quit.
=======================================================""")


index()
select = input()


def Add():
    stud_id = input("Please enter the student ID: ")
    name = input("Please enter the student name: ")
    course = input("Please enter the course: ")
    file = open("student.txt", "a")
    file.write(stud_id + " " + name + " " + course + "\n")
    file.close()
    print(f"Student Id : {stud_id}\nStudent Name : {name}\nEntered course:{course}")
    print("\n\nThe record has been successfully added to the students.txt file.")


def insert():
    stud_id = input("Please enter the student ID: ")
    subject_code = input("Please enter the subject code: ")
    assessment_number = input("Please enter the assessment number: ")
    marks = input("Please enter assessment marks: ")
    file = open("assesment.txt", "a")
    file.write(stud_id + " " + subject_code + " " + assessment_number + " " + marks + "\n")
    file.close()
    print(f"""The details of the student you entered are as follows:
Student ID: {stud_id}
Subject code: {subject_code}
Assessment number: {assessment_number}
Assessment marks: {marks}
""")
    print("\n\nThe record has been successfully added to the assessments.txt file")


def search():
    student_id = input("Please enter the student ID you want to search assessment marks for: ")
    print("Thank You !")
    stud_file = open("student.txt", "r")
    z = stud_file.readlines()
    for i in z:
        y = i.split()
        if (y[0] == student_id):
            print("\nA student has been found:")
    for i in z:
        y = i.split()
        if (y[0] == student_id):
            print(f"Student Id: {y[0]}\nName :{y[1]} {y[2]}\nCourse : {y[3]}")
            break
    asses_file = open("assesment.txt", "r")
    data = asses_file.readlines()
    print("\n\nSubject Code     Assessment Number   Marks")
    for i in data:
        # Splitting data into list so that can access that from .txt file
        data = i.split()
        if (y[0] == student_id):
            print(data[1], "          ", data[2], "                ", data[3])



#  I use .casefold () method everywhere where i have to take input because user may enter in lower case or lower case
if select.casefold() == "a":
    Add()
    print("""Thank You!\n
The details of the student you entered are as follows:""")
    choice = input("Do you want to enter details for another student (Y/N)? ")
    if choice.casefold() == "N":
        index()
        select = input()
    else:
        exit()


elif select.casefold() == "i":
    insert()
    choice = input("Do you want to enter marks for another assessment (Y/N)?")
    if choice.casefold() == "N":
        index()
        select = input()
    else:
        exit()

elif (select.casefold() == "s"):
    search()
    se_choice = input("Do you want to search assessment marks for another student (Y/N)? ")
    if se_choice.casefold() == "y":
        index()
        select = input()
    else:
        exit()
