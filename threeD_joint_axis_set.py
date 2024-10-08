import numpy as np

def threeD_joint_axis_set(joint_axes):

    joint_axis_vectors = np.empty((1,3,len(joint_axes)))
    
    for n in range(0,len(joint_axis_vectors)):
        axis = joint_axes[n]
        
        if axis == 'x':
            joint_axis_vectors[n]=np.array([[1],[0],[0]])
            
        elif axis == 'y':
            joint_axis_vectors[n]=np.array([[0],[1],[0]])
            
        elif axis == 'z':
            joint_axis_vectors[n]=np.array([[0],[0],[1]])
            

        else:
            print('joint axis is not a known joint axis')
            
    return joint_axis_vectors