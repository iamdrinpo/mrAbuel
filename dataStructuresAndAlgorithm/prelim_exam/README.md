Contacts - Exam Documentation

This program lets you create and manage a list of contacts. Each contact is saved using a first name, last name, and phone number. You can add new contacts, update existing ones, delete them, search for them, and display all saved contacts. The contacts are stored in memory using a Python dictionary, so once the program is closed, the list is cleared.

How it works

When you add a contact, the program combines the first and last name to make a full name. That full name is used as the key in the dictionary, and the phone number is the value.

If you try to add the same person again, the program will tell you the contact already exists.

You can update a phone number if it changes.

You can delete a contact when you no longer need it.

Searching works by either name (full or partial) or by the phone number.

Displaying shows all contacts that are currently saved.

How to use

Save the code as a .py file, for example contacts.py.

Open a terminal or command prompt.

Go to the folder where you saved the file.

Run the program with:

python contacts.py


You will see a menu with choices:

1 to add, 2 to delete, 3 to update, 4 to search, 5 to display, 6 to exit


Choose a number depending on what you want to do.

Example
1 to add, 2 to delete, 3 to update, 4 to search, 5 to display, 6 to exit: 1
First Name: John
Last Name: Doe
Phone Number: 1234567890

John Doe was successfully added.

1 to add, 2 to delete, 3 to update, 4 to search, 5 to display, 6 to exit: 5

===CONTACT LIST===
John Doe : 1234567890

Requirements

Python 3 installed on your computer.

Any text editor or IDE (like VS Code, PyCharm, or even Notepad).
