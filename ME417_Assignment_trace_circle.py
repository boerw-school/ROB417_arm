import scipy
import numpy as np
import matplotlib.pyplot as plt
from threeD_robot_arm_links import *
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
from circle_x import *
from follow_trajectory import *
from threeD_update_links import *
from threeD_draw_links import *

# Make an animated plot of a robot arm tracing a circle in the yz plane

#
# Specify link vectors as a 1x3 cell array of 3x1 vectors, named
# 'link_vectors'

link_vectors = [np.array(np.reshape([1,0,0],(3,1))),np.array(np.reshape([1,0,0],(3,1))),np.array(np.reshape([0.75,0,0],(3,1)))]


#
# Specify joint axes as a cell array of the same size as link_vectors, named 'joint_axes'
joint_axes = ['z','y','y']

#
# Specify the function to be traced as a circle around the x axis with
# a half-unit radius. Use the @ syntax to create handle to an anonymous
# function named 'shape_to_draw' that takes in a time 't' and passes it
# to the 'circle_x' function, then multiplies the result by 1/2
shape_to_draw = lambda t: np.divide(circle_x(t),2)


#
# Create a function 'J' that takes in a set of joint angles and returns
# the Jacobian of the arm at those joint angles. Use the 
# '@(b) f(a,b,c)' syntax to specify the inputs to J that should be 
# passed to arm_Jacobian.
J = lambda joint_angles: arm_Jacobian(link_vectors,joint_angles,joint_axes,(len(link_vectors)-1)) 

#
# Create a function 'joint_velocity' that takes in time 't' and configuration
# 'alpha' and passes them to 'follow trajectory' along with J and shape_to_draw

joint_velocity = lambda t,alpha: follow_trajectory(t,alpha,J,shape_to_draw)


#
# Set up parameters for differential equation solver
#
# Specify the time range 'T' as being from zero to one
T = [0, 1]

# Specify the starting configuration 'a_start' as being zero for the
# first joint, pi/4 (angled down) for the second joint, and -pi/2
# (right-angle up) for the third joint
a_start = [0,np.pi/4,-np.pi/2]

#
# Run the ode45 solver with 'joint_velocity' as the function that maps
# from time and configuration to configuration velocity, 'T' as the
# timespan, and 'a_start' as the initial configuration  
# Use deval to find the joint angles at a series of 100 times spaced
# evenly along the interval from zero to one, saving the output to a
# variable 'alpha'

#sol = scipy.integrate.solve_ivp(joint_velocity,T,a_start,time_eval=1)


series_size = 100
time_linspace = np.linspace(T[0],T[1], num=series_size)


alpha = scipy.integrate.solve_ivp(joint_velocity,T,a_start,t_eval=time_linspace)



# Create figure and axes for the plot, and store the handle in a
# variable named 'ax'
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#
# Specify colors of links as a 1x3 cell array named 'link_colors'. Each
# entry can be either a standard matlab color string (e.g., 'k' or 'r')
# or a 1x3 vector of the RGB values for the color (range from 0 to 1)
link_colors = ['r','g','b']
#
# Generate a cell array named 'link_set' containing start-and-end
# points for the links
generate_link_set = lambda t: threeD_robot_arm_links(link_vectors,alpha.y[:,t],joint_axes)
    
#
# Draw a line segment for each link with threeD_draw_links, and
# save the handles into a cell array named 'l'
l3 = lambda link_set_current: threeD_draw_links(link_set_current,link_colors,ax)

#
# Draw the path that the end of the robot follows
#
# Start by creating a matrix 'p' with three rows and as many
# columns (time-points) as there are in alpha, all entries of which are zero

p = np.zeros((3,100))

# Next, loop over  the columns of alpha
for n in range(0 , 100):
    
    
    # For each column, calculate the endpoints for the links in the robot arm
    endpoints = generate_link_set(n)[0]

    #print(endpoints)
    # Save the endpoint of the last link into the corresponding column
    # of p
    
    p[0,n] = endpoints[2][1][0][0]
    p[1,n] = endpoints[2][1][1][0]
    p[2,n] = endpoints[2][1][2][0]

# Finally, make a line whose data points are the rows of p, and whose
# parent is the plotting axis, and save the handle to this line in a
# variable 'l_trace'

l_trace = ax.plot(p[0,:],p[1,:],p[2,:])
# Animate the arm

# For grading, create an empty 1xn cell array named 'link_set_history'
# to hold the the endpoints of link at each time
link_set_history = [None]*series_size

# Loop over the columns of alpha


link_set = generate_link_set(0)[0]
    
   
    
handles = l3(link_set)
    
new_lines= threeD_update_links(handles,link_set)
    





for n in range(1,series_size):

    ax.clear()    
    ax.set_aspect('equal')


    # Get the endpoints for the arm with the joint angles from
    # that column of alpha, saving them in the variable 'link_set'
   
    
 
    # Use the elements of link_set to update the illustration
    
    link_set = generate_link_set(n)[0]
    
   
    
    handles = l3(link_set)
    
    new_lines= threeD_update_links(handles,link_set)
    

    for n in range(len(link_vectors)):    
        X_Data = new_lines[n][1]
        Y_Data = new_lines[n][2]
        Z_Data = new_lines[n][3]

        
    l_trace = ax.plot(p[0,:],p[1,:],p[2,:])
    plt.draw()
    plt.pause(0.01)
    
    
    # Save the current link_set into the corresponding element
    # of link_set_history 
    link_set_history[n] = link_set