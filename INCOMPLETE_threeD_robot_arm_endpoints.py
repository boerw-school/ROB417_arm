from Rx import *
from Ry import *
from Rz import *
from vector_set_rotate import *
from vector_set_cumulative_sum import *
from rotation_set_cumulative_product import *
from threeD_rotation_set import *

#link_vectors must be in this form-> link_vectors = np.array([1,0,0]) 
#joint_angles must be in this form-> joint_angles = np.array([np.pi/4, -np.pi/2, 0])
#joint_axes must be in this form-> joint_axes = np.array(['x','z','y'])
#can be more or less terms though


def threeD_robot_arm_endpoints(link_vectors,joint_angles,joint_axes):
    #appears to work
    R_joints = threeD_rotation_set(joint_angles , joint_axes)
    #appears to work
    R_links = rotation_set_cumulative_product(R_joints)
    
# FIX HERE
    link_vectors_in_world = vector_set_rotate(link_vectors , R_links)
    
    link_end_set = vector_set_cumulative_sum(link_vectors_in_world)
    
   
    
    link_end_set_with_base = np.array([[[0],[0],[0]] , [link_end_set]])
    
            
    # PUT NEXT LINE BACK   
    #link_ends = np.array([link_end_set_with_base{:}]) 
    
    #DELETE LINE BELOW
    link_ends=1 # TEMPORARY

    return [link_ends,R_joints,R_links,link_vectors_in_world,link_end_set,link_end_set_with_base]




a = np.array([1,0,0])
b = np.array([np.pi/4, -np.pi/2])
c = np.array(['x','z'])
threeD_robot_arm_endpoints(a,b,c)