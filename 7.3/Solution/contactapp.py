'''
DO IT! CHALLENGE - 7.3 Dijkstra's Algorithm

Do not modify this file. Only change the code in 'bfs.py'.
To check your work, run this file and test if the functions in the menu
work correctly.
'''

import dijkstra

def print_menu():
    print('1. Find shortest distance between two people')
    print('2. List names')
    print('3. Quit')
    print('')


menu_choice = 0
print_menu()
while menu_choice != 3:
    menu_choice = int(input("Type in a number (1-3): "))
    if menu_choice == 1:
        print("Find shortest distance")
        start = raw_input("Start from: ")
        end = raw_input("End at: ")
        distance = dijkstra.find_shortest(start, end)
        print start + " and " + end + " are " + str(distance) + " apart."

    elif menu_choice == 2:
        print("List Names")
        print(dijkstra.get_names())

    elif menu_choice != 3:
        print_menu()


