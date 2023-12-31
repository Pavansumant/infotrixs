import json
import re

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def add_contact(contacts, name, phone, email):
    if not name.strip() or not phone.strip() or not email.strip():
        print("Error: Name, phone, and email cannot be empty.")
        return
    
    if not phone.isdigit() or len(phone) != 10:
        print("Error: Invalid phone number format.Phone Number must contain 10 digits.")
        return
    
    def is_valid_email(email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email)
    

    if not is_valid_email(email):
        print("Error: Invalid email address format.")
        return
    
    if any(contact['name'].lower() == name.lower() for contact in contacts):
        print(f"Error: Contact with name '{name}' already exists.")
        return
        
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
    }
    
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")
    save_contacts(contacts, contacts_filename)

def search_contact(contacts, name):
    if not name.strip():
        print("Error: Name cannot be empty.")
        return

    found_contacts = [contact for contact in contacts if contact['name'].lower() == name.lower()]
    if found_contacts:
        for contact in found_contacts:
            print(f"Contact '{name}' found successfully.")
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact(contacts, name):
    if not name.strip():
        print("Error: Name cannot be empty.")
        return

    contacts[:] = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    print(f"Contact '{name}' deleted successfully.")
    save_contacts(contacts, contacts_filename)

def update_contact(contacts, name, phone, email):
    if not name.strip() or not phone.strip() or not email.strip():
        print("Error: Name, phone, and email cannot be empty.")
        return
    
    if not phone.isdigit() or len(phone) != 10:
        print("Error: Invalid phone number format.Phone Number must contain 10 digits.")
        return
    
    def is_valid_email(email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email)
    

    if not is_valid_email(email):
        print("Error: Invalid email address format.")
        return

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = phone
            contact['email'] = email
            print(f"Contact '{name}' updated successfully.")
            save_contacts(contacts,contacts_filename)
            return
    print(f"No contact found with the name '{name}'.")



def main():
    global contacts_filename
    contacts_filename = "contacts.json"
    contacts = load_contacts(contacts_filename)

    while True:
        print('\n')
        print('-'*40)
        print("Contact Management System")
        print('-'*40)
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit\n")
        choice = input("Enter your choice (1/2/3/4/5):")

        if choice == "1":
            name = input("\nEnter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            print('\n')
            add_contact(contacts, name, phone, email)

        elif choice == "2":
            name = input("Enter the name to search: ")
            print('\n')
            search_contact(contacts, name)

        elif choice == "3":
            name = input("Enter the name to delete: ")
            print('\n')
            delete_contact(contacts, name)

        elif choice == "4":
            name = input("Enter the name to update: ")
            phone = input("Enter the updated phone number: ")
            email = input("Enter the updated email address: ")
            print('\n')
            update_contact(contacts, name, phone, email)

        elif choice == "5":
            print("\nExiting the Contact Management System. Goodbye!\n")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
