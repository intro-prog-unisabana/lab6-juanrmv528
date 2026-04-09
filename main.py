def main():
    data = {}
    
    print("Welcome to the Student Grades Manager!")
    
    while True:
        print("\n1. Add student")
        print("2. Show all students")
        print("3. Show selected students")
        print("4. Exit")
        
        option = input("Choose an option: ")
        
        if option == "1":
            name = input("Enter student name: ")
            data[name] = {}
            print(f"{name} added.")
        
        elif option == "2":
            for student in data:
                print(student)
        
        elif option == "3":
            names = input("Enter names separated by comma: ").split(",")
            names = [n.strip() for n in names]
            
            for name in names:
                if name in data:
                    print(name)
                else:
                    print(f"{name} not found!")
        
        elif option == "4":
            break
        
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()