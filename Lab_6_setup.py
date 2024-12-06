
class Course_grades:
    def __init__(self):
        self.course_name = ""
        self.stuName = []
        self.stuID = []
        self.stu_grades = []

    def course(self):
        self.course_name = input("Enter the Course Name: ")
        for i in range(0, 5):
            self.stuName.append(input("Enter the Student's Name: "))
        for i in range(0, 5):
            self.stuID.append(input("Enter the Student's Id: "))
        for i in range(0, 5):
            self.stu_grades.append(input("Enter the Student's Grade(0/100): "))

    def display(self):
        print("Course name", self.course_name)
        print("Student Name: ")
        for y in range(0, len(self.stuName)):
            print(self.stuName)
        print("Student Id: ")
        for y in range(0, len(self.stuID)):
            print(self.stuID)
        print("Grades: ")
        for y in range(0, len(self.stu_grades)):
            print(self.stu_grades)
        print(" ")
