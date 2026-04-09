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
            proper = name.title()
            data[proper] = {}
            print(f"Student {proper} successfully added to the grades management system.")

        elif option == "2":
            if not data:
                print("No students available.")
            else:
                for student in data:
                    print(student)

        elif option == "3":
            names = input("Enter names separated by comma: ").split(",")
            names = [n.strip() for n in names]

            for name in names:
                proper = name.title()
                if proper in data:
                    print(proper)
                else:
                    print(f"{proper} not found!")

        elif option == "4":
            break

        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()