contacts = {}


def addContacts():
    fname = input("First Name: ").capitalize()
    lname = input("Last Name: ").capitalize()
    fullName = f"{fname} {lname}"
    if fullName in contacts:
        print(f"\n{fullName} is already a contact. Update instead.")
    else:
        phoneNumber = input("Phone Number: ")
        contacts[fullName] = phoneNumber
        print(f"\n{fullName} was successfully added.")

def deleteContact():
    fname = input("First Name: ").capitalize()
    lname = input("Last Name: ").capitalize()
    fullName = f"{fname} {lname}"
    if fullName in contacts:
        del contacts[fullName]
        print(f"\n{fullName} was successfully deleted.")
    else:
        print("\nNo such contact.")

def updateContact():
    fname = input("First Name: ").capitalize()
    lname = input("Last Name: ").capitalize()
    fullName = f"{fname} {lname}"
    if fullName in contacts:
        newNumber = input("New number: ")
        contacts[fullName] = newNumber
        print(f"\n{fullName}'s number was updated to {newNumber}")
    else:
        print("\nNo such contact.")

def searchContact():
    nameOrNumber = input("Search by name or phone number? ('1' for name, '2' for phone): ")

    if nameOrNumber == '1':
        searchName = input("Enter first name or full name: ").lower()
        found = False
        for name, number in contacts.items():
            if searchName in name.lower():
                print(f"{name} : {number}")
                found = True
        if not found:
            print("No such contact.")

    elif nameOrNumber == '2':
        phoneNumber = input("Phone number: ")
        found = False
        for name, number in contacts.items():
            if number == phoneNumber:
                print(f"{name} : {number}")
                found = True
        if not found:
            print("No such contact.")
    else:
        print("Invalid choice.")



def displayContacts():
    if contacts: 
        print("\n===CONTACT LIST===")
        for name, number in contacts.items():
            print(f"{name} : {number}")
    else:
        print("\nNo contacts yet.")


while True:
    choice = input("\n1 to add, 2 to delete, 3 to update, 4 to search, 5 to display, 6 to exit: ")
    if choice == '1':
        addContacts()
    elif choice == '2':
        deleteContact()
    elif choice == '3':
        updateContact()
    elif choice == '4':
        searchContact()
    elif choice == '5':
        displayContacts()
    elif choice == '6':
        print("Terminated.")
        break
    else:
        print("Invalid.")

