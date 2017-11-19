'''
DO IT! CHALLENGE - 9.3 Dynamic Programming

SOLUTION
'''

def best_value(people, size_limit, return_grid = False):
    grid = {}
    for i in range(len(people)):
        for j in range(size_limit):

            if (j+1) >= people[i]['time']:
                if i == 0:
                    grid[i,j] = people[i]['value']
                else:
                    remaining_space = 0
                    if (i-1, j-people[i]['time']) in grid:
                        remaining_space = grid[i-1, j-people[i]['time']]
                    previous_max = grid[i-1,j]
                    current_value = people[i]['value']
                    grid[i,j] = max(previous_max, current_value + remaining_space)
            else:
                if i == 0:
                    grid[i, j] = 0
                else:
                    grid[i, j] = grid[i - 1, j]
    if return_grid:
        return grid
    else:
        return grid[len(people)-1, size_limit-1]