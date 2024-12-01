import matplotlib.pyplot as plt
import numpy as np

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


    ##########
    # Specify link vectors as a 1x3 cell array of 3x1 vectors, named
    # 'link_vectors'

link_vectors = [np.array(np.reshape([1,0,0],(3,1))),np.array(np.reshape([1,0,0],(3,1))),np.array(np.reshape([0,0,0.5],(3,1)))]
    
    ##########
    # Specify joint angles as a 3x1 vector, named 'joint_angles'

joint_angles = ((np.pi/2.5) , (-np.pi/4) , (np.pi/4))
    
    ##########
    # Specify joint axes as a 3x1 cell array, named 'joint_axes'

joint_axes = ['z','y','x']

    ##########
    # Specify colors as a 3x1 cell array, named 'link_colors'    
link_colors = ['red','green','blue']

    #########
    # Generate a cell array named 'link_set' containing start-and-end
    # points for the links. Also get R_links as an output
    # from the function that generates 'link_set'.
    
robot_arm_links = threeD_robot_arm_links(link_vectors,joint_angles,joint_axes)     
link_set = robot_arm_links[0]
R_links = robot_arm_links[2]


  
    # Use 'threeD_joint_axis_set' to turn the joint axes into
    # a set of axis vectors called 'joint_axis_vectors'
joint_axis_vectors = threeD_joint_axis_set(joint_axes)
    
   
    
    # Use 'vector_set_rotate' to rotate the joint axes by the link
    # orienations (Note that although our convention is that the ith joint
    # is in the (i-1)th link, the vector associated with the joint axis is
    # the same in both frame (i-1) and frame i, so we can rotate the joint
    # axes directly into the corresponding frames (this means we don't have
    # to offset the joint axes when calling 'vector_set_rotate'). Call the
    # output of this rotation 'joint_axis_vectors_R'.
  
joint_axis_vectors_R = vector_set_rotate(joint_axis_vectors,R_links)



#creates x/y/z data for start/end as array, each value in array is for nth line
x_start= ([None])*len(link_vectors)
y_start=([None])*len(link_vectors)
z_start = ([None])*len(link_vectors)
x_end=([None])*len(link_vectors)
y_end= ([None])*len(link_vectors)
z_end = ([None])*len(link_vectors)
for n in range(len(link_vectors)):

    x_start[n]=link_set[n][:1,0]
    y_start[n]=link_set[n][:1,1]
    z_start[n]=link_set[n][:1,2]
    x_end[n]=link_set[n][1:,0]
    y_end[n]=link_set[n][1:,1]
    z_end[n]=link_set[n][1:,2]





fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
        



for n in range(len(link_vectors)):
    ax.plot([x_start[n],x_end[n]], [y_start[n],y_end[n]], [z_start[n],z_end[n]],color=link_colors[n])

''' #not currently working
#draw a dashed line from that joint to the point one unit from the joint in the direction of that joint's axis
l3_x_start= ([None])*len(link_vectors)
l3_y_start=([None])*len(link_vectors)
l3_z_start = ([None])*len(link_vectors)
l3_x_end=([None])*len(link_vectors)
l3_y_end= ([None])*len(link_vectors)
l3_z_end = ([None])*len(link_vectors)



for n in range(len(link_vectors)): 
    l3_x_start[n]=link_set[n][:1,0][0][0]
    l3_y_start[n]=link_set[n][:1,1][0][0]
    l3_z_start[n]=link_set[n][:1,2][0][0]
   

  
    l3_x_end[n]=l3_x_start[n]+joint_axis_vectors_R[0][0,n]

    l3_y_end[n]=l3_y_start[n]+joint_axis_vectors_R[0][1,n]

    l3_z_end[n]=l3_z_start[n]+joint_axis_vectors_R[0][2,n]

for n in range(len(link_vectors)):
    ax.plot([l3_x_start[n],l3_x_end[n]], [l3_y_start[n],l3_y_end[n]], [l3_z_start[n],l3_z_end[n]],color=link_colors[n])
'''    

plt.show()