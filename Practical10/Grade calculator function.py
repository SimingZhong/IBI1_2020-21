def grade_calculator(name, code_grade, poster_grade, exam_grade): #define a function
    final_grade = 0.4*code_grade + 0.3*poster_grade + 0.3*exam_grade #calculate the grade
    print(name, final_grade)
    return

#name is in string type
grade_calculator('Ben', 100,90,100)
