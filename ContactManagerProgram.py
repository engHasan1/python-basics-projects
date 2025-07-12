import json

print('welcome to the Contact Manager Program!')

def menu():
    print("Contact Manager Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    pass

def addContact(contacts):
    name=input("Enter contact name: ")
    phone=input("Enter contact phone number: ")
    email=input("Enter contact email: ")
    if name and phone and email:
        contact={'name':name,'phone':phone,'email':email}
        contacts.append(contact)
        pass
    else:
        print ("All fields are required. Please enter valid contact details.")
        addContact()

def viewContacts(contacts):
    if not contacts:
        print('no contacts available.')
        pass
    else :
        print('current contacts:')
        for i,contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def searchContact(contacts):
    if not contacts:
        print('No contacts available to search.')
        pass
    else :
        searchName=input('Enter the name of the contact to search: ')
        found = False
        for contact in contacts:
            if contact['name'].lower() == searchName.lower():
                print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                found = True
                break
        if not found:
            print(f'Contact "{searchName}" not found.')

def deleteContact(contacts):
    if not contacts:
        print('No contacts available to delete.')
        pass
    else:
        delName = input('Enter the name of the contact to delete: ')
        matches = [contact for contact in contacts if contact['name'].lower() == delName.lower()]
        if not matches:
            print(f'No contact found with the name "{delName}".')
            return
        
        for i, contact in enumerate(matches, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        
        try:
            contactNum = int(input('Enter the contact number you want to delete: '))
            if 1 <= contactNum <= len(matches):
                to_delete = matches[contactNum - 1]
                contacts.remove(to_delete)
                print(f'Contact "{to_delete["name"]}" has been deleted.')
            else:
                print('Invalid contact number.')
        except ValueError:
            print('Invalid input. Please enter a valid contact number.')

def main():
    contacts = []

    file_path = r"C:\Users\HP\Desktop\contacts.json"

    try:
        with open(file_path, 'r') as file:
            contacts = json.load(file)
            print('Contacts loaded from file:')
            viewContacts(contacts)
    except FileNotFoundError:
        print('No existing contacts found. Starting with an empty contact list.')

    while True:
        menu()
        choice=input('Enter your choice (1-5): ')
        if choice == '1':
            addContact(contacts)
        elif choice == '2':
            viewContacts(contacts)
        elif choice == '3':
            searchContact(contacts)
        elif choice == '4':
            deleteContact(contacts)
        elif choice == '5':
            print('Thank you for using the Contact Manager Program!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

    with open(file_path, 'w') as file:
        json.dump(contacts, file, indent=4)
        print(f'Contacts saved to {file_path}')

if __name__ == '__main__':
    main()
