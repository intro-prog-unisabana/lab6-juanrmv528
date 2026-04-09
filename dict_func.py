# Write your code here!

def employee_print(employee):
    if not employee:
        print("Name: N/A")
        print("Age: N/A")
        print("Department: N/A")
        return
    
    print(f"Name: {employee.get('name', 'N/A')}")
    print(f"Age: {employee.get('age', 'N/A')}")
    print(f"Department: {employee.get('department', 'N/A')}")
    
    for key, value in employee.items():
        if key not in ["name", "age", "department"]:
            print(f"{key}: {value}")