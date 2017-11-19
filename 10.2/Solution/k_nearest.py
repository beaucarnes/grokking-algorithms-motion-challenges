'''
DO IT! CHALLENGE - 10.1 K-Nearest Neighbors

SOLUTION
'''
import math

def nearest(people, selected_person):
    closest_distance = 1000;
    closest_person = "";
    r1 = people[selected_person]
    for person, ratings in people.items():
        if person == selected_person: continue
        r2 = ratings
        distance = math.sqrt((r1[0] - r2[0]) ** 2 +
                             (r1[1] - r2[1]) ** 2 +
                             (r1[2] - r2[2]) ** 2 +
                             (r1[3] - r2[3]) ** 2 +
                             (r1[4] - r2[4]) ** 2)
        if distance < closest_distance:
            closest_distance = distance
            closest_person = person
    return closest_person
