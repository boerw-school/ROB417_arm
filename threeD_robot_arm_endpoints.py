from Rx import *
from Ry import *
from Rz import *
from vector_set_rotate import *
from vector_set_cumulative_sum import *
from rotation_set_cumulative_product import *
from threeD_rotation_set import *




def threeD_robot_arm_endpoints(link_vectors,joint_angles,joint_axes):
    #works
    R_joints = threeD_rotation_set(joint_angles , joint_axes)

    R_links = rotation_set_cumulative_product(R_joints)

    
    #ISSUE HERE
    link_vectors_in_world = vector_set_rotate(link_vectors , R_links)
    
    link_end_set = vector_set_cumulative_sum(link_vectors_in_world)
    
   
    
    a =np.array([[0],[0],[0]])
  
    link_end_set_with_base= [a]+link_end_set
    
    
         
    link_ends = ((link_end_set_with_base[:]))
    
    link_ends = np.concatenate(link_ends,axis=1)

    return [link_ends,R_joints,R_links,link_vectors_in_world,link_end_set,link_end_set_with_base]





