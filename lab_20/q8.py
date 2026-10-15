"""8. Course Enrollment Analysis
Concepts: sets, set operations, converting lists to sets, len()
python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
Remove the duplicates, then print:
• students taking both courses
• students taking only Python
• students taking exactly one course
• every unique student, in sorted order
Finally, ask for a name and say which course(s) that student is enrolled in."""
python_class= ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class= ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
def course_enrollment_analysis(python_class,java_class):
    python_set=set(python_class)
    java_set=set(java_class)
    both=python_set & java_set
    only_python=python_set - java_set
    only_one_course=python_set ^ java_set
    everyone=sorted(python_set | java_set)
    print("Students taking both the course: ",both)
    print("Students enrolled in python: ",only_python)
    print("Exactly one course: ",only_one_course)
    print("Total unique students: ",len(everyone))

    name=input("Enter your name: ")
    if name in both:
        print("Taken both the courses")
    elif name in python_set:
        print("Only enrolled python")
    elif name in java_set:
        print("Only enrolled in java")
    else:
        print("Not enrolled in any class")
course_enrollment_analysis(python_class,java_class)
