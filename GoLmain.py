#######################################################################
#   Conway's Game of Life | CSCI 154
#   
#   Reference: https://electronut.in/simple-python-matplotlib-implementation-of-conways-game-of-life/
#   
#   Group: Mitchell Maltezo, Micah Mercado, David Andrade, Harpreet Ghag
#
#   Language: Python
#
#######################################################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 10

vals = [1, 0]

# populate grid with random values with probability 3/10 for a live cell
#grid = np.random.choice(vals, N*N, p=[0.3,0.7]).reshape(N, N)

# for all OFF values to test other objects, comment out line 24 and uncomment line 26
grid = np.random.choice(vals, N*N, p=[0,1]).reshape(N, N)

# Delete quotations for spaceship 
"""spaceship = [[0, 0, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0]]

grid[1:5, 1:6] = spaceship"""

# Delete quotations for a beacon
"""beacon = [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]]

grid[1:5, 1:5] = beacon"""

# Delete quotations for glider
glider = [[0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0],
             [0, 1, 1, 1, 0]]

grid[1:4, 1:6] = glider

def update(data):
  global grid
  # copy grid since we require 8 neighbors for calculation
  # iterate line by line
  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):
      # compute 8-neighbor sum (Add the amount of live/dead cells around the current cell)
      # using toroidal boundary conditions - x and y wrap around current position
      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
               grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
      
      # apply Conway's rules based on sum (neighbor count)
      if grid[i, j] == 1:
        if (total < 2) or (total > 3):
          newGrid[i, j] = 0
      else:
        if total == 3:
          newGrid[i, j] = 1
          
  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

# set animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()