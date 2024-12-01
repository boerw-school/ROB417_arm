import numpy as np
import copy
from threeD_rotation_set import *

def rotation_set_cumulative_product(R_set):
    
    R_set_c = copy.deepcopy(R_set)
    
    for number_of_angles in range(1, len(R_set_c)):
        R_set_c[number_of_angles] = np.matmul(np.array(R_set_c[(number_of_angles-1)]),np.array(R_set_c[number_of_angles]))
 


    return R_set_c
