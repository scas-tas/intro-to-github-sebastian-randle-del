import random
"""random.randrange(0, 10)
random.append('x')"""


# Initialise all cells
grid = list(range(11))

# Generate a random position and place 'X' there, 3 times
for i in range(3):
    pos = random.randint(0, 10)
    grid[pos] = 'X'

print(grid)