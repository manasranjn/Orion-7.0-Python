import numpy as np
import time

size = 10000000
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [(x + y) for x, y in zip(l1, l2)] #(x =1, y=1)
print("Python list took: ", (time.time() - start) * 1000)

start = time.time()
result = a1 + a2
print("Numpy array took: ", (time.time() - start) * 1000)

