import numpy as np
import copy 
def vector_set_rotate(v_set, R_set):
    v_set_R = copy.deepcopy(v_set)
    
    for number_of_angles in range(0, len(v_set_R)):
        v_set_R[number_of_angles] = np.matmul(R_set[number_of_angles],v_set[number_of_angles])
    return v_set_R