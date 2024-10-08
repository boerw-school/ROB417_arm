import numpy as np

from Rx import *
from Ry import *
from Rz import *
from vector_set_rotate import *
from vector_set_cumulative_sum import *
from rotation_set_cumulative_product import *
from threeD_rotation_set import *
from build_links import *
from place_links import *


def threeD_robot_arm_links(link_vectors,joint_angles,joint_axes):

    
    R_joints = threeD_rotation_set(joint_angles , joint_axes)
  
    R_links = rotation_set_cumulative_product(R_joints)
    
    link_set_local = build_links(link_vectors)
    
    link_vectors_in_world = vector_set_rotate(link_vectors, R_links)
    
    links_in_world = vector_set_rotate(link_set_local, R_links)
    
    link_end_set = vector_set_cumulative_sum(link_vectors_in_world)
                

    
    link_end_set_with_base = np.array([[[0],[0],[0]] , [link_end_set]])
    

    
    link_set = place_links(links_in_world,link_end_set_with_base)


    return link_set,R_joints,R_links,link_set_local,link_vectors_in_world ,links_in_world,link_end_set,link_end_set_with_base