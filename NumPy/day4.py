# Stacking in NumPy
import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

# Vertical stacking
vertical = np.vstack([a1, a2])
# print(vertical)

# Horizontal stacking
horizontal = np.hstack([a1, a2])
# print(horizontal)

# Concatination
concat = np.concatenate([a1, a2])
# print(concat)

# Splitting in NumPy
a3= np.array([[1, 2, 3, 10], [4, 5, 6, 20], [7, 8, 9, 30]])
# Vertical splitting
# vertical_split = np.vsplit(a3, 3)
# print(vertical_split)

# Horizontal splitting
horizontal_split = np.hsplit(a3, 4)
print(horizontal_split)