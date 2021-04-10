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

beacon = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]

universe[1:5, 1:5] = beacon

plt.imshow(universe, cmap='binary')
plt.show()