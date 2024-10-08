import numpy as np

def Ry(phi):
    R = np.array([[np.cos(phi), 0, np.sin(phi)],[0, 1, 0],[-np.sin(phi) , 0 , np.cos(phi)]])
    return R