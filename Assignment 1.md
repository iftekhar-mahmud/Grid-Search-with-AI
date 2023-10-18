Your assignment mustn’t contain any animation. Just submit the py file no zip file.
SUBMIT only 1 .py file (convert into .py file if you use jupyter etc). You don’t need to upload the csv files. Don’t copy. Copy checker will be used. File name: id.py
2011212057.py
You’re designing a robot stated in a grid at a starting position (4, 1). You can sense the intensity of Carbon monoxide in the four adjacent cells (top, left, bottom, right iff that cell is an empty cell). A cell can be of two types: Obstacle: O & Empty: E.  You can only move to the top, left, bottom or right empty cell from a certain cell position. You need to find the source of the  Carbon monoxide gas. You want to get there as fast as possible. Show how many moves are required to reach there using A star algorithm. 

The grid description is given. Each of the cells is given a small intensity value if the cell is empty, otherwise ‘O’ is marked for that cell. 

Smell intensity is inversely proportional to the distance squared. You will need this for heuristic calculation. 

Node cost = start node to node actual cost + node to goal heuristic cost
node to goal heuristic cost = 1 / sqrt(intensity)

Goal test: How to know if I have reached the cell with CO source? Hint: All adjacent cells will have lower smell intensities. 

Example cell:
grid = [
   [42, 48, 55, 58, 59, 58],
   [44, 50, 56, 'O', 61, 60],
   [45, 49, 57, 'O', 65, 62],
   [39, 45, 55, 60, 'O', 60],
   [38, 40, 50, 55, 59, 58],
   [37, 45, 48, 49, 50, 49],
]


Output: (2, 4) is the cell with Carbon Monoxide
And show the path you got

The grid’s lower left is (0, 0) and upper right is (max_x, max_y)
