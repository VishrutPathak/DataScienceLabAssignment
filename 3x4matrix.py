# write a numpy program to create a 3x4 array and itirate over it

import numpy as np


arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Iterate over the elements using nested loops
for row in arr:
    for element in row:
        print(element, end=' ')
    print()  
