'''
DO IT! CHALLENGE - 10.1 K-Nearest Neighbors
'''

import k_nearest

def print_menu():
    print('1. Print Contacts')
    print('2. Add a Contact')
    print('3. Remove Contact')
    print('4. Determine Closest Match')
    print('5. Quit')
    print('')

categories = ['comedy', 'action', 'drama', 'horror', 'romance']

people = {'Judah': [1,4,5,2,3],
          'Beau': [5,2,1,3,5],
          'Aditya': [4,4,2,1,5],
          'Bob': [2,3,5,5,1],
          'Alice': [2,1,1,4,5],
          'Claire': [5,2,1,2,1],
          'Anuj': [3,1,4,5,4],
          'Peggy': [3,4,3,5,2],
          'Thom': [5,2,1,3,5]}

menu_choice = 0

print_menu()

while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("All contacts: ")
        for person in people:
            print person
    elif menu_choice == 2:
        print("Add Contact")
        name = raw_input("Name: ")
        ratings = []
        for category in categories:
            score = int(raw_input("How does " + name +  " rank '" + category + "' on a scale of 1 to 5? "))
            ratings.append(score)
        people[name] = ratings
    elif menu_choice == 3:
        print("Remove Contact")
        name = raw_input("Name: ")
        people.pop(name, None)
        print(name + " was deleted")
    elif menu_choice == 4:
        person = raw_input("Determine closest match for who? ")
        print k_nearest.nearest(people, person)
    elif menu_choice != 5:
        print_menu()