import numpy as np

from scipy.signal import convolve2d

def step(state):
    filter = np.array( [[1,1,1],
                        [1,0,1],
                        [1,1,1]])
    a = np.array(convolve2d(state.astype(int),filter,'same','wrap'))
    
    return np.logical_or(np.logical_and(a==2, state), a==3)
