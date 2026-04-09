def student_averages(students):
    result = {}
    for student, grades in students.items():
        if grades:
            avg = sum(grades.values()) / len(grades)
            result[student] = round(avg)
    return result


def assignment_averages(students):
    if not students:
        return {}
    
    assignments = {}
    
    for grades in students.values():
        for assignment, score in grades.items():
            assignments.setdefault(assignment, []).append(score)
    
    return {
        a: round(sum(scores) / len(scores))
        for a, scores in assignments.items()
    }