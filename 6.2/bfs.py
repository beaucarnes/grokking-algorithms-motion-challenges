'''
DO IT! CHALLENGE - 6.2 Breadth-first search

The code for the search function in 'bfs.py' comes directly from the 'Implementing the Graph' video.
Your job is to modify the code so it accepts both a name AND item. Return the person that is
associated with the item that is passed in. Test you code by running 'contactapp.py'.
'''


from collections import deque

graph = {}
graph["you"] = {"item": "balloon", "friends": ["alice", "bob", "claire"]}
graph["bob"] = {"item": "mango", "friends": ["anuj", "peggy", "you"]}
graph["alice"] = {"item": "mosquito", "friends": ["peggy", "you"]}
graph["claire"] = {"item": "house", "friends": ["thom", "jonny", "you"]}
graph["anuj"] = {"item": "bear", "friends": ["bob"]}
graph["peggy"] = {"item": "unicycle", "friends": ["bob", "alice"]}
graph["thom"] = {"item": "unicycle", "friends": ["claire"]}
graph["jonny"] = {"item": "bear", "friends": ["claire"]}

def search(name, item):
    search_queue = deque()
    search_queue += graph[name]
    # This array is how you keep track of which people you've searched before.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if not person in searched:
            if person_is_seller(person):
                print person + " is a mango seller!"
                return True
            else:
                search_queue += graph[person]
                # Marks this person as searched
                searched.append(person)
    return False

def get_names():
    names = []
    for key in graph:
        names.append(key)
    return names

def get_items():
    items = []
    for value in graph.values():
        items.append(value["item"])
    return items