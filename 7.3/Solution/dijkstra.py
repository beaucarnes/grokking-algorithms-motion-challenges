'''
DO IT! CHALLENGE - 7.3 Dijkstra's Algorithm
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
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
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
    for k, v in graph[start].items():
        costs[k] = v
        parents[k] = start

def find_shortest(start, end):
    fill_costs_and_parents(start)


    # Find the lowest-cost node that you haven't processed yet.
    node = find_lowest_cost_node(costs)

    # If you've processed all the nodes, this while loop is done.
    while node is not None:
        cost = costs[node]
        # Go through all the neighbors of this node.
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If it's cheaper to get to this neighbor by going through this node...
            if costs[n] > new_cost:
                # ... update the cost for this node.
                costs[n] = new_cost
                # This node becomes the new parent for this neighbor.
                parents[n] = node
        # Mark the node as processed.
        processed.append(node)
        # Find the next node to process, and loop.
        node = find_lowest_cost_node(costs)
    return costs[end]

def get_names():
    names = []
    for key in graph:
        names.append(key)
    return names
