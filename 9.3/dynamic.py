'''
DO IT! CHALLENGE - 9.3 Dynamic Programming

Given how much time it takes to visit each friend and how much you want to visit each friend (the value),
write an algorithm to determine the maximum value you can get from visiting friends in the amount of
time that is passed in.
'''

def best_value(people, size_limit, return_grid = False):
    grid = {}
    for i in range(len(people)):
        for j in range(size_limit):
            '''
            Fill in the grid with the answers using dynamic programming.              
            In the video, a two-dimensional array is used. Here it is a dictionary with the
            rows and column as the key. For example, set a grid element like this:
            grid[i,j] = number
            '''






    if return_grid:
        return grid
    else:
        return grid[len(people)-1, size_limit-1]