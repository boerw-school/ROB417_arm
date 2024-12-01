import matplotlib.pyplot as plt
import numpy as np
import copy as copy

import threeD_joint_axis_set
from threeD_robot_arm_links import *
import vector_set_rotate
from Rx import *
from Ry import *
from Rz import *
from vector_set_rotate import *
from vector_set_cumulative_sum import *
from rotation_set_cumulative_product import *
from threeD_rotation_set import *
from build_links import *
from place_links import *
from threeD_joint_axis_set import *
from threeD_robot_arm_endpoints import *
from vector_set_difference import *

def arm_Jacobian(link_vectors,joint_angles,joint_axes,link_number):

    a= threeD_robot_arm_endpoints(link_vectors,joint_angles,joint_axes) 
    link_ends=copy.deepcopy(a[0])
    R_joints=copy.deepcopy(a[1])
    R_links=copy.deepcopy(a[2])
    link_vectors_in_world =copy.deepcopy( a[3])
    link_end_set=copy.deepcopy(a[4])
    link_end_set_with_base =copy.deepcopy(a[5])
    

    v_diff = vector_set_difference(link_end_set[link_number],link_end_set_with_base)

    joint_axis_vectors = threeD_joint_axis_set(joint_axes)

   
    joint_axis_vectors_R = vector_set_rotate(joint_axis_vectors,R_links)

    J =  np.zeros((3, len(joint_angles)))

    joint_axis_row_num = np.size(joint_axis_vectors_R,0)
    joint_axis_column_num =np.size(joint_axis_vectors_R,1) 

    #for n in range(0 , joint_axis_row_num):
    #    for n2 in range(0 , joint_axis_column_num):
    #        tf = isa(joint_axis_vectors_R[n2,n],'sym')
    #        if tf(1) == 1:
    #            J=sym(J)

    for idx in range (0 , link_number+1):
        joint = np.reshape(joint_axis_vectors_R[idx][:,0],(3,1))
        v = np.reshape(v_diff[idx][:,0],(3,1))

        cross_n = np.cross(joint,v,axis=0)
        J[0,idx]=cross_n[0][0]
        J[1,idx]=cross_n[1][0]
        J[2,idx]=cross_n[2][0]
 
    return [J,link_ends,link_end_set,link_end_set_with_base,v_diff,joint_axis_vectors,joint_axis_vectors_R,R_links] 