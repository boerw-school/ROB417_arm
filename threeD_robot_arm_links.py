import numpy as np
import copy
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
    #print(R_links) WORKS

    link_set_local = build_links(link_vectors)
    #print(link_set_local) WORKS

    link_vectors_in_world = vector_set_rotate(link_vectors, R_links)
    #print(link_vectors_in_world) WORKS

    links_in_world = vector_set_rotate(link_set_local, R_links)
    #print(links_in_world) WORKS
    

    link_end_set = vector_set_cumulative_sum(link_vectors_in_world)
    #print(link_end_set) WORKS

    a =np.array([[0],[0],[0]])
    
    link_end_set_with_base= [a]+copy.deepcopy(link_end_set)
    #print(link_end_set_with_base)  WORKS
   
    
    
    link_set = place_links(links_in_world,link_end_set_with_base)
    

    return [link_set,R_joints,R_links,link_set_local,link_vectors_in_world ,links_in_world,link_end_set,link_end_set_with_base]

#a = [np.array(np.reshape([1,0,0],(3,1))),np.array(np.reshape([0,1,0],(3,1))),np.array(np.reshape([0,0,0.5],(3,1)))]
#b = ((np.pi/2.5) , (-np.pi/4) , (np.pi/4))

#c = ['z','y','x']
#threeD_robot_arm_links(a,b,c)
