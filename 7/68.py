'''
    
'''
import numpy as np
arr=eval(input())

np.std

mean = np.array([np.mean(arr[:, i]) for i in range(arr.shape[1])])
scale = np.array([np.std(arr[:, i]) for i in range(arr.shape[1])])