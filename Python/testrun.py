#modify the student grade function using the format method

def student_grade(name, grade):
    return "{name} received {grade}% on the exam".format(name=name, grade=grade)

print(student_grade("Marcus", 100))
print(student_grade("npc", 80))