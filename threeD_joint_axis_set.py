import numpy as np

def threeD_joint_axis_set(joint_axes):

    joint_axis_vectors = [None]*len(joint_axes)
    for n in range(0,len(joint_axes)):
        
        axis = joint_axes[n]
      
        if axis == 'x':
            joint_axis_vectors[n]=np.array([[1],[0],[0]])
            
        if axis == 'y':
            joint_axis_vectors[n]=np.array([[0],[1],[0]])
            
        if axis == 'z':
            joint_axis_vectors[n]=np.array([[0],[0],[1]])
            
    return joint_axis_vectors