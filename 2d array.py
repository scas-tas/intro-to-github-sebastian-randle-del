#"""simple
import random
"""n = 5
grid = []
for row in range(5):
   row_list = []
   for col in range(5):
       row_list.append(" ")
   grid.append(row_list)


random.randrange(0,5)
print()

gr = list(range(6))

# Generate a random position and place 'X' there, 3 times
for i in range(3):
    pos = random.randint(0, 5)
    gr[pos] = 'X'

print(gr)



# Print with borders
for row in range(5):
   print("|", end="")
   for col in range(5):
       print(f" {grid[row][col]} |", end="")
   print()  # New line after row"""









# """simple
# Create empty 3x3 grid
grid = [
   [' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', ' ']
]

#print(grid)


def draw_grid():
   for row in grid:
       print('|'.join(row))
       print('')


#Mainline 
# Draw the grid
#draw_grid()
pos_full=0
for i in range(16):
    row = random.randrange(0,5)
    col = random.randrange(0,5)
    print(row, col)
   
if (i>1) or (grid[row][col] == "X"):
 pos_full = pos_full + 1
 grid[row][col] = 'X'  

print (pos_full)
#for 
# Draw again
print("\nUpdated grid:")
draw_grid()
#simple"""
