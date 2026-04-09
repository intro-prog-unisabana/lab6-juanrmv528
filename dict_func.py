# Write your code here!

def employee_print(employee):
    if not employee:
        print("No employee data available.")
        return
    
    for key, value in employee.items():
        print(f"{key}: {value}")