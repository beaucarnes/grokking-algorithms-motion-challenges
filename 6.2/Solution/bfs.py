'''
ASSIGNMENT - 6.2 Breadth-first search
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
    search_queue += graph[name]["friends"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if item == graph[person]["item"]:
                return person
            else:
                search_queue += graph[person]["friends"]
                searched.append(person)
    return None

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