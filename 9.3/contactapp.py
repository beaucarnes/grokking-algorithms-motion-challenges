'''
DO IT! CHALLENGE - 9.3 Dynamic Programming

Do not modify this file. Complete the code in 'dynamic.py'.
To check your work, run this file and test if the functions in the menu
work correctly.
'''

import dynamic

def print_menu():
    print('1. Print Contacts')
    print('2. Add a Contact')
    print('3. Remove Contact')
    print('4. Determine Greatest Value')
    print('5. View Complete Grid')
    print('6. Quit')
    print('')

people = [{'name': 'Judah', 'time': 1, 'value': 50},
          {'name': 'Beau', 'time': 3, 'value': 80},
          {'name': 'Aditya', 'time': 4, 'value': 10},
          {'name': 'Bob', 'time': 3, 'value': 90},
          {'name': 'Alice', 'time': 2, 'value': 100},
          {'name': 'Claire', 'time': 2, 'value': 20},
          {'name': 'Anuj', 'time': 3, 'value': 40},
          {'name': 'Peggy', 'time': 1, 'value': 10},
          {'name': 'Thom', 'time': 6, 'value': 80},
          {'name': 'Jonny', 'time': 5, 'value': 70},
          {'name': 'Mykeem', 'time': 1, 'value': 70}]

menu_choice = 0

print_menu()

while menu_choice != 6:
    menu_choice = int(input("Type in a number (1-6): "))
    if menu_choice == 1:
        print("All contacts: ")
        for person in people:
            print person
    elif menu_choice == 2:
        print("Add Contact")
        name = raw_input("Name: ")
        time = int(raw_input("Time (whole number): "))
        value = int(raw_input("Value: "))
        people.append({'name': name, 'time': time, 'value': value})
    elif menu_choice == 3:
        print("Remove Contact")
        name = raw_input("Name: ")
        removed = False
        for person in people:
            if person['name'] == name :
                people.remove(person)
                removed = True
        if removed:
            print(name + " was deleted")
        else:
            print(name + " was NOT found")
    elif menu_choice == 4:
        print("Greatest Value")
        size_limit = int(raw_input("How many hours do you have? "))
        print("Greatest value from meeting with friends:")
        print dynamic.best_value(people, size_limit)
    elif menu_choice == 5:
        print("Grid")
        size_limit = int(raw_input("How many hours do you have? "))
        grid = dynamic.best_value(people, size_limit, True)
        print("")
        for i in range(len(people)):
            print(people[i]['name'][0:5].rjust(6) + " |"),
            for j in range(size_limit):
                print(str(grid[i, j]).rjust(4)+" |"),
            print("")
    elif menu_choice != 6:
        print_menu()
