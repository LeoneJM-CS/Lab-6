import Lab_6_setup as ls
import pickle

courseList = []
while 1:
    print("1. Add Course and Students")
    print("2. Display Courses and Student's")
    print("0. Exit Program")
    choice = int(input())

    if choice == 1:
        cc = ls.Course_grades()
        cc.course()
        courseList.append(cc)
        d = open('Courses.dat', 'ab')
        pickle.dump(cc, d)
        d.close()
    if choice == 2:
        d = open('Courses.dat', 'rb')
        while 2:
            try:
                data = pickle.load(d)
                print(data.course_name)
                print(data.stuName)
                print(data.stuID)
                print(data.stu_grades)
            except EOFError:
                break
        d.close()
    if choice == 0:
        print("Program Terminated")
        break
