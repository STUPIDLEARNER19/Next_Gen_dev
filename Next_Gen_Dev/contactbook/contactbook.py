class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []  # Initialize an empty list to store contacts

    def add_contact(self, name, phone):
        contact = Contact(name, phone)  # Create a Contact object with given name and phone
        self.contacts.append(contact)  # Add the contact to the contacts list
        print(f"Contact '{name}' added successfully!")  # Print a success message

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")  # If contacts list is empty, print no contacts found
        else:
            print("Contacts:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone}")  # Print each contact's name and phone number

    def menu(self):
        while True:
            print("\n===== Contact Book Menu =====")
            print("1. Add Contact")
            print("2. Display Contacts")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ").strip()  # Prompt user for menu choice

            if choice == '1':
                name = input("Enter contact name: ").strip()  # Prompt for contact name
                phone = input("Enter contact phone: ").strip()  # Prompt for contact phone
                self.add_contact(name, phone)  # Call add_contact method to add the contact
            elif choice == '2':
                self.display_contacts()  # Call display_contacts method to show all contacts
            elif choice == '3':
                print("Exiting Contact Book. Goodbye!")  # Exit the program
                break
            else:
                print("Invalid choice. Please enter a valid option (1-3).")  # Handle invalid input

def main():
    contact_book = ContactBook()  # Create an instance of ContactBook
    contact_book.menu()  # Call the menu method to start the contact book application

if __name__ == "__main__":
    main()
