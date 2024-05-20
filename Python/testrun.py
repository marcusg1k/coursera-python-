#pass fail using if-elif-else statements

def exam_grade(score): 
    if score > 95: 
        return "Top Score"
    elif score >= 60: 
        return "Pass"
    else: 
        grade = "Fail"
        return grade
    
print(exam_grade(65)) # Pass
print(exam_grade(55)) # Fail
print(exam_grade(96)) # Top Score