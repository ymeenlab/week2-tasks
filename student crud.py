# 1. Student Record CRUD (Create, Read, Update, Delete) using a Dictionary

student_records = {}  # Use a dictionary to store student records (student_id: {details})

def create_student():
    #Creates a new student record.
    student_id = input("Enter student ID: ")
    if student_id in student_records:
        print("Student ID already exists.")
        return
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    # Storing details as a dictionary
    student_records[student_id] = {"name": name, "age": age, "grade": grade}
    print("Studentrecord is created.")

def read_student():
    #Reads and displays a student record.
    student_id = input("Enter student ID to view: ")
    if student_id in student_records:
        record = student_records[student_id]  # Retrieve the student dictionary
        print("Student Details:", record)
        
    else:
        print("Student not found.")

def update_student():
    #Updates a student record.
    student_id = input("Enter student ID to update: ")
    if student_id in student_records:
        record = student_records[student_id]
        print("Current Details:", record)  # Show current details
        for key in record: #Go through each key
            new_value = input(f"Enter new {key} (or press Enter to skip): ")
            if new_value:  # Update only if a new value is provided
                record[key] = new_value
        print("Student updated.")
    else:
        print("Student not found.")

def delete_student():
    #Deletes a student record.
    student_id = input("Enter student id for deletion: ")
    choose = input('enter 1 to delete a single entry in record and 2 to delete whole record')
    if choose == 1:
        if student_id in student_records:
            key = input('enter the key name you want to delete')
            del student_records[key]
            print("key deleted.")
        else:
            print("Student not found.")
    if choose == 2:    
        if student_id in student_records:
            del student_records[student_id]
            print("Student deleted.")
        else:
            print("Student not found.")


# --- Main Menu ---
while True:
    print("\nStudent Record System")
    print("1. Create Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_student()
    elif choice == '2':
        read_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice.")
