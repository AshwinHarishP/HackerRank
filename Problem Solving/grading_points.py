def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        if grade < 38:
            final_grades.append(grade)
        elif grade % 5 >= 3:
            final_grades.append(grade + (5 - grade % 5))
        else:
            final_grades.append(grade)
    return final_grades

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grade = int(input().strip())
        grades.append(grade)

    results = gradingStudents(grades)
    for grade in results:
        print(grade)
