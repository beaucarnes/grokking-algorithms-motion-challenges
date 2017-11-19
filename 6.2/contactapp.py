'''
ASSIGNMENT - 6.2 Breadth-first search
Do not modify this file. Fix the 'search' function in 'bfs.py'.
To check your work, run this file and test if the functions in the menu
work correctly.
'''

import bfs

def print_menu():
    print('1. Search for Item')
    print('2. List Names')
    print('3. List Items')
    print('4. Quit')
    print('')


menu_choice = 0
print_menu()
while menu_choice != 4:
    menu_choice = int(input("Type in a number (1-4): "))
    if menu_choice == 1:
        print("Search for Item")
        name = raw_input("Who to start search with: ")
        item = raw_input("Item: ")
        person = bfs.search(name, item)
        if person:
            print person + " is the closest " + item + " seller to " + name + " !"
        else:
            print "There are no " + item + " sellers accessible to " + name + "."

    elif menu_choice == 2:
        print("List Names")
        print(bfs.get_names())

    elif menu_choice == 3:
        print("List Items")
        print(bfs.get_items())

    elif menu_choice != 4:
        print_menu()


