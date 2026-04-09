def initialize_dict(name, grades):
    return {name: grades}


def add_student(data):
    name = input("Enter student name: ")
    proper = name.title()   
    
    data[proper] = {}
    print(f"Student {proper} successfully added to the grades management system.")
    return data


def get_students(data, names):
    result = {}
    lower_map = {k.lower(): k for k in data}
    
    for name in names:
        key = lower_map.get(name.lower())
        if key:
            result[key] = data[key]
        else:
            print(f"{name.capitalize()} not found!")
    
    return result


def avg_by_student(data, selected=None):
    lower_map = {k.lower(): k for k in data}
    
    if selected:
        for name in selected:
            key = lower_map.get(name.lower())
            if key:
                grades = data[key]
                if grades:
                    avg = sum(grades.values()) / len(grades)
                    print(f"{key}: {avg}")
            else:
                print(f"{name.capitalize()} not found!")
    else:
        for student, grades in data.items():
            if grades:
                avg = sum(grades.values()) / len(grades)
                print(f"{student}: {avg}")