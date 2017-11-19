'''
DO IT! CHALLENGE - 7.3 Greedy

SOLUTION
'''

import greedy
import time

def print_menu():
    print('1. Print Contacts')
    print('2. Add a Contact')
    print('3. Remove Contact')
    print('4. Schedule Meetings')
    print('5. Quit')
    print('')

people = [{'name': 'Judah', 'start_time': '08:00', 'end_time': '09:00'},
          {'name': 'Beau', 'start_time': '09:30', 'end_time': '10:00'},
          {'name': 'Aditya', 'start_time': '11:30', 'end_time': '12:00'},
          {'name': 'Bob', 'start_time': '10:00', 'end_time': '11:30'},
          {'name': 'Alice', 'start_time': '09:00', 'end_time': '10:00'},
          {'name': 'Claire', 'start_time': '08:00', 'end_time': '08:30'},
          {'name': 'Anuj', 'start_time': '10:30', 'end_time': '11:30'},
          {'name': 'Peggy', 'start_time': '08:30', 'end_time': '09:30'},
          {'name': 'Thom', 'start_time': '11:00', 'end_time': '11:30'},
          {'name': 'Jonny', 'start_time': '10:00', 'end_time': '12:00'},
          {'name': 'Mykeem', 'start_time': '09:00', 'end_time': '09:30'}]

menu_choice = 0

print_menu()

def is_time_format(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False

while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("All contacts: ")
        sorted_people = sorted(people, key=lambda k: k['start_time'])
        for person in sorted_people:
            print person
    elif menu_choice == 2:
        print("Add Contact")
        name = raw_input("Name: ")
        start = raw_input("Start Time: ")
        while not is_time_format(start):
            start = raw_input("Try again. Start time must by format in HH:MM: ")
        end = raw_input("End Time: ")
        while not is_time_format(end):
            end = raw_input("Try again. End time must by format in HH:MM: ")
        start = "{0:0>5}".format(start)
        end = "{0:0>5}".format(end)
        people.append({'name': name, 'start_time': start, 'end_time': end})
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
        print("Scheduled Meetings")
        print("------------------")
        scheduled = greedy.schedule(people)
        for person in scheduled:
            print person['name'] + ' from ' + person['start_time'] +  " to " + person['end_time']
        print ""
    elif menu_choice != 5:
        print_menu()

