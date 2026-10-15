"""6. Student Grade Report
Concepts: list of tuples, tuple unpacking, for, if/elif grading, max/min by manual
tracking
Start with:
students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
Print each student's letter grade (A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F). Then print
the class average and the top and bottom scorers. Find the top and bottom scorers with
a loop, not with max() and a key."""
students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
total_score=0
top_student=None
top_score=-1
bottom_student=None
bottom_score=101
for name ,score in students:
    if score >=90:
        grade="A"
    elif score >=80:
        grade="B"
    elif score >=70:
        grade="C"
    elif score >=60:
        grade="D"
    else:
        grade="F"
    print(f"{name}:{score} ({grade})")
    total_score += score
    if score>top_score:
        top_score=score
        top_student=name
    if score < bottom_score:
        bottom_score=score
        bottom_student=name
avg=total_score/len(students)
print(f"{top_student}:{top_score}")
print(f"{bottom_student}:{bottom_score}")

