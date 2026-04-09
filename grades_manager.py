def initialize_dict(name, grades):
    return {name: grades}

def add_student(data):
    name = input("Enter student name: ")
    data[name] = {}
    return data

def get_students(data, names):
    result = {}
    lower_data = {k.lower(): k for k in data}
    
    for name in names:
        key = lower_data.get(name.lower())
        if key:
            result[key] = data[key]
    return result

def avg_by_student(data, selected=None):
    if selected:
        selected = [s.lower() for s in selected]
    
    for student, grades in data.items():
        if selected and student.lower() not in selected:
            continue
        
        if grades:
            avg = sum(grades.values()) / len(grades)
            print(f"{student}: {round(avg)}")