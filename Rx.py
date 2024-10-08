import numpy as np

def Rx(psi):
    R = np.array([[1, 0, 0] , [0, np.cos(psi), -np.sin(psi)], [0 , np.sin(psi) , np.cos(psi)]])
    return R
