contacts = {}

def add_contact():
    name = input("Please enter your name: ")
    phone = input("Please enter your phone number: ")
    email = input("Please enter your email: ")
    address = input("Please  enter your address: ")

    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' added successfully!\n")

def view_contact_list():
    if not contacts:
        print("OOoopss!!!.....Contact list is empty.\n")
        return

    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print()

def search_contact():
    keyword = input("Enter name or phone number to search from contact book: ").lower()

    results = [(name, details) for name, details in contacts.items()
               if keyword in name.lower() or keyword in details['phone']]
    
    if results:
        print("Search Results are as  mentioned below:")
        for name, details in results:
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()
    else:
        print("Something wrong No matching contacts found.\n")

def update_contact():
    name = input("Enter the name of the contact to update in contact book: ")

    if name in contacts:
        print(f"Update contact '{name}':")
        contacts[name]['phone'] = input("Enter the new phone number: ")
        contacts[name]['email'] = input("Enter the new email: ")
        contacts[name]['address'] = input("Enter the new address: ")
        print(f"Contact '{name}' updated successfully!\n")
    else:
        print(f"Contact '{name}' not found in contact book something went wrong .\n")

def delete_contact():
    name = input("Enter the name of the contact to delete from contact book: ")

    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print(f"Contact '{name}' not found in contact book something went wrong.\n")

def main():
    while True:
        print("******************Contact Book Menu:*******************")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice in between (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("The choice you have given is invalid. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()

