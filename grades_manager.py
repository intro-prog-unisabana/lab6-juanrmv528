def avg_by_student(data, selected=None):
    lower_data = {k.lower(): k for k in data}
    
    if selected:
        for name in selected:
            key = lower_data.get(name.lower())
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