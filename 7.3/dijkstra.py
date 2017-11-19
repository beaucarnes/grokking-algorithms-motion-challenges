'''
DO IT! CHALLENGE - 7.3 Dijkstra's Algorithm

Just as in the video, the goal is to determine the quickest path from one node on the graph to another
node on the graph. However, now both the start and end nodes are set by the user. Instead of just going
one direction on the graph, each node is connected in both directions. You must change the 'find_shortest'
function so it returns the correct total cost to get from the start to end node. Also, you must complete the
'fill_costs_and_parents' function so it initialized the costs and parents dictionaries correctly.
'''

# the graph
graph = {}
graph["you"] = {}
graph["you"]["alice"] = 2
graph["you"]["bob"] = 1
graph["you"]["claire"] = 6

graph["bob"] = {}
graph["bob"]["anuj"] = 7
graph["bob"]["peggy"] = 2
graph["bob"]["you"] = 1
graph["bob"]["claire"] = 5

graph["alice"] = {}
graph["alice"]["peggy"] = 6
graph["alice"]["you"] = 2
graph["alice"]["jonny"] = 2

graph["claire"] = {}
graph["claire"]["thom"] = 2
graph["claire"]["you"] = 6
graph["claire"]["jonny"] = 1
graph["claire"]["bob"] = 5


graph["anuj"] = {}
graph["anuj"]["bob"] = 7
graph["anuj"]["peggy"] = 3

graph["peggy"] = {}
graph["peggy"]["anuj"] = 3
graph["peggy"]["bob"] = 2
graph["peggy"]["alice"] = 6

graph["thom"] = {}
graph["thom"]["claire"] = 2

graph["jonny"] = {}
graph["jonny"]["claire"] = 1
graph["jonny"]["alice"] = 2

# the costs table
infinity = float("inf")
costs = {}
costs["you"] = infinity
costs["bob"] = infinity
costs["alice"] = infinity
costs["claire"] = infinity
costs["anuj"] = infinity
costs["peggy"] = infinity
costs["thom"] = infinity
costs["jonny"] = infinity

# the parents table
parents = {}
parents["you"] = None
parents["bob"] = None
parents["alice"] = None
parents["claire"] = None
parents["anuj"] = None
parents["peggy"] = None
parents["thom"] = None
parents["jonny"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def reset():
    global processed
    processed = []
    for key in costs.keys():
        costs[key] = infinity
        parents[key] = None

def fill_costs_and_parents(start):
    reset()
    # Complete this function so it initialized the costs and parents dictionaries correctly. Remember to call this
    # at the beginning of 'find_shortest'



def find_shortest(start, end):
    # This is the code for dijkstra's algorithm from the video for section 7.3, except now both a start and end point
    # is passed in. Change the code so it returns the correct total cost to get to end.

    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs

def get_names():
    names = []
    for key in graph:
        names.append(key)
    return names
