from Rx import *
from Ry import *
from Rz import *

import numpy as np

def threeD_rotation_set(joint_angles,joint_axes):
    

    R_set = [None]*len(joint_angles)
    for n in range(0,len(joint_angles)):
        axis = joint_axes[n]
        
        if axis == 'x':
        
            R_set[n]=Rx(joint_angles[n])
            
        elif axis == 'y':
           R_set[n]=Ry(joint_angles[n])
            
        elif axis == 'z':
            
            R_set[n]=Rz(joint_angles[n])
            

        else:
            print('joint axis is not a known joint axis')
            
    return R_set

