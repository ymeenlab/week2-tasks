
phonebook = {}  # Use a dictionary to store contact records

def create_contact():
    #Creates a new student record.
    number = input("Enter number: ")
    if number in phonebook:
        print("Number already exists.")
        return
    name = input("Enter the name of number's owner: ")
    number = input("Enter number: ")
    # Storing details as a dictionary
    phonebook[number] = {"name": name, "number": number}
    print("contact record  is created.", )
    
def read_contact():
    #Reads and displays a contact record.
    number = input("Enter number to view: ")
    if number in phonebook:
        record = phonebook[number]  # Retrieve the student dictionary
        print("contact Details:", record)
        
    else:
        print("record  not found.")

def update_contact():
    #Updates a student record.
    number = input("Enter numbrer to update: ")
    if number in phonebook:
        record = phonebook[number]
        print("Current Details:", record)  # Show current details
        for key in record: #Go through each key
            new_value = input(f"Enter new {key} (or press Enter to skip): ")
            if new_value:  # Update only if a new value is provided
                record[key] = new_value
        print("contact record updated.")
    else:
        print("record not found.")

def delete_contact():
    #Deletes a contact record.
    number = input("Enter number for deletion")   
    if number in phonebook:
            del phonebook[number]
            print("record deleted.")
    else:
            print("record not found.")
            


# --- Main Menu ---
while True:
    print("\nPhonebook Record System")
    print("1. Create Contact")
    print("2. Read contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_contact()
    elif choice == '2':
        read_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice.")
import json
json_file_path = "contact.json"
 
def load_contacts():
    try:
        with open(json_file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print('file not found')
        