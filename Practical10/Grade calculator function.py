def grade_calculator(name, code_grade, poster_grade, exam_grade):
    final_grade = 0.4*code_grade + 0.3*poster_grade + 0.3*exam_grade
    print(name, final_grade)
    return

#name is in string type
grade_calculator('Siming', 100,90,100)