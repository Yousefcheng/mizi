'''
    
'''
import numpy as np


import numpy as np
list = [int(i) for i in range(0,5)]
it = iter(list)
x = np.fromiter(it, dtype = int)

print(x)