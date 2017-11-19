'''
DO IT! CHALLENGE - 8.2 Greedy Algorithm

SOLUTION
'''

def schedule(people):
    sorted_people = sorted(people, key=lambda k: k['end_time'])
    scheduled = []
    for person in sorted_people:
        if len(scheduled) == 0 or person['start_time'] >= scheduled[-1]['end_time']:
            scheduled.append(person)
    return scheduled

