'''
ASSIGNMENT - 5.4 Hash Table
Do not modify this file. Finish the HashTable in 'hashtable.py'.
To check your work, run this file and test if the functions in the menu
work correctly.
'''

import hashtable

def print_menu():
    print('1. Add Contact')
    print('2. Lookup Contact')
    print('3. Quit')
    print('')

contacts = hashtable.HashTable()
contacts.set('Beau', '616-555-5555')
contacts.set('Aditya', '555-123-4567')
contacts.set('Judah', '987-654-3210')

menu_choice = 0
print_menu()
while menu_choice != 3:
    menu_choice = int(input("Type in a number (1-3): "))
    if menu_choice == 1:
        print("Add Contact")
        name = raw_input("Name: ")
        phone = raw_input("Phone number: ")
        contacts.set(name, phone)
        print('Contact added')
    elif menu_choice == 2:
        print("Lookup Contact")
        name = raw_input("Name: ")
        phone = contacts.get(name)
        print('The phone number for ' + name + ' is ' + phone + '.')
    elif menu_choice != 3:
        print_menu()


