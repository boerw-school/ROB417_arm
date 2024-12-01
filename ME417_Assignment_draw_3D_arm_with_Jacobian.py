import matplotlib.pyplot as plt
import matplotlib.figure as fig
import numpy as np
import math 
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
from arm_Jacobian import *
from draw_vectors_at_point import *


link_vectors = [np.array(np.reshape([1,0,0],(3,1))),np.array(np.reshape([1,0,0],(3,1))),np.array(np.reshape([0,0,0.5],(3,1)))]
    
    ##########
    # Specify joint angles as a 3x1 vector, named 'joint_angles'
joint_angles = ((np.pi/2.5) , (-np.pi/4) , (np.pi/4))
    
    ##########
    # Specify joint axes as a 3x1 cell array, named 'joint_axes'
joint_axes = ['z','y','x']

link_colors = ['red','green','blue']

# Create an empty cell array named of the same size as link_vectors,
# named J

J=[None] * len(link_vectors)

# Loop over the elements of J
    
    # In each element of J, use arm_Jacobian to find the Jacobian for
    # the corresponding link on the arm. 
    # 
    # When you call arm_Jacobian, also get link_ends, link_end_set, 
    # and joint_axis_vectors_R
    # as outputs (they will be used for plotting). These outputs are
    # independent of the link number, so you don't need to store them
    # separately for each link number -- the easy way to do this is to
    # have the link_end outputs returned in each iteration of the loop,
    # which will overwrite them every time, and leave them at their
    # value from the final iteration

for n in range(0 , len(J)):
    b =arm_Jacobian(link_vectors,joint_angles,joint_axes,n)
    J[n] = b[0]
    link_ends= b[1]
    link_end_set=b[2]
    link_end_set_with_base=b[3]
    v_diff = b[4]
    joint_axis_vectors=b[5]
    joint_axis_vectors_R=b[6]
    R_links =b[7]

    
     
# Plotting

# Create figure and subaxes for the plot, and store the axis handles in a
# variable named 'ax'. Use the 'create_subaxes' function you wrote
# earlier, with the square root of the number of links for m
# and n (round up to make these integer values), and only as many plots
# as you have links

m = round(math.sqrt(len(link_vectors)))
n = round(math.sqrt(len(link_vectors)))
p = len(link_vectors)


fig = plt.figure()
fig.clear
ax = ['']*p
    
for idx in range (0,p):
    ax[idx]=fig.add_subplot(m,n,idx+1,projection='3d')

# Create empty cell arrays 'l', 'l2', 'l3', and 'q' to hold the handles to the
# lines and quivers that will illustrate the arm and the components of
# the Jacobians. Each cell array should be the same size as J.
l= [None]* len(J)
l2 = [None]* len(J)
l3 = [None]* len(J)
q = [None]* len(J)


# Loop over the subfigure axes, drawing the robot arm into each axis.
# Use the information in link_ends to draw a line for the arm links,
# with circles at the endpoints, and save the handle to this line into
# the corresponding element of 'l' 


#this part is done very poorly the array outputs are strange and I haven't been able to fix it yet.

x_start= ([None])*len(link_vectors)
y_start=([None])*len(link_vectors)
z_start = ([None])*len(link_vectors)
x_end=([None])*len(link_vectors)
y_end= ([None])*len(link_vectors)
z_end = ([None])*len(link_vectors)

for n in range(len(link_vectors)):

    x_start[n]=link_ends[0,n]
    y_start[n]=link_ends[1,n]
    z_start[n]=link_ends[2,n]
    x_end[n]=link_ends[0,n+1]
    y_end[n]=link_ends[1,n+1]
    z_end[n]=link_ends[2,n+1]

for n in range(0 , len(J)):    
    l[n] = ax[n].plot([x_start,x_end], [y_start,y_end], [z_start, z_end])



# Loop over the subfigure axes, adding arrows for the column of the
# corresponding Jacobian into each axis. Get the location of the end of
# the link from link_end_set, and use the draw_vectors_at_point
# function you wrote earlier to make the arrows. Save the handles
# returned by draw_vectors_at_point into the corresponding elements of
# q

for n in range(0 , len(J)):
    q[n] = draw_vectors_at_point(link_end_set[n],J[n],ax[n])


# Loop over the subfigure axes, adding a dashed line between the end of
# the link whose Jacobian is plotted in that axis and the joints
# corresponding to the columns of the Jacobian
    
    # For each subfigure axis:
    
    #   1. Make the corresponding elements of 'l2' and 'l3' empty 1xN cell
    #   arrays (where N is the number of columns in the Jacobian). This
    #   is now a nested cell array, so your command should look
    #   something like 'l2{idx} = cell(...'
    #
    #   2. Loop over the locations of the joints (the base points of
    #   the links), and draw a dotted line from each of the joints that
    #   is *before* the current link to the end of the current link
    #
    #   Save the handles to these lines into the l2{idx} cell array you
    #   created for this plot (note that because this is a nested cell
    #   array, your command should look something like 
    #   'l2{idx}{idx2} = line(...'
    
    
      
Jacobian_row_num= np.size(J,0)
Jacobian_col_num = np.size(J,1)
for idx in range(0 , len(J)):
    l2[idx] = [None]*(Jacobian_col_num)
    l3[idx] = [None]*(Jacobian_col_num)
    for idx2 in range (0 , idx+1):
        x = [link_ends[0][idx2],link_ends[0][idx+1]]
        y = [link_ends[1][idx2],link_ends[1][idx+1]]
        z = [link_ends[2][idx2],link_ends[2][idx+1]]
        l2[idx][idx2] = ax[idx].plot(x,y,z, linestyle = ':',color=link_colors[idx2])
        
       
             
    
    #   As you make these lines, set their color property to be the
    #   same as the corresponding Jacobian arrow
    #   [Use get(q{idx}{idx2},'Color') to get the color of the arrow]
    
    
    
    
    
    #   3. Loop over the locations of the joints (the base points of
    #   the links), and draw a dashed line from each of the joints that
    #   is *before* the current link to the point one unit from the
    #   joint in the direction of that joint's axis
    #
    #   Save the handles to these lines into the l3{idx} cell array you
    #   created for this plot (note that because this is a nested cell
    #   array, your command should look something like 
    #   'l3{idx}{idx2} = line(...'
    #
    #   As you make these lines, set their color property to be the
    #   same as the corresponding Jacobian arrow
    #   [Use get(q{idx}{idx2},'Color') to get the color of the arrow]
    #    x = link_ends(1,idx2), link_ends(1,idx2)+joint_axis_vectors_R[idx2,1](1)
    #    y = link_ends(2,idx2), link_ends(2,idx2)+joint_axis_vectors_R[idx2,1](2) 
    #    z = link_ends(3,idx2) , link_ends(3,idx2)+joint_axis_vectors_R[idx2,1](3) 
    #    l3[idx][idx2] = ax[idx].plot(x,y,z)

        x = [link_ends[0,idx2], link_ends[0][idx2]+joint_axis_vectors_R[idx2][0][0]]
        y = [ link_ends[1,idx2],link_ends[1][idx2]+joint_axis_vectors_R[idx2][1][0]]
        z = [link_ends[2,idx2] ,link_ends[2][idx2]+joint_axis_vectors_R[idx2][2][0]] 
        l3[idx][idx2] = ax[idx].plot(x,y,z,linestyle='--',color=link_colors[idx2])


plt.show()               