import numpy as np
def circle_x(t):
# Generate points on a unit circle in the y-z plane, wrapping in the 
# clockwise (negative) direction around the x axis, such that the
# range of t=[0 1] corresponds to one full cycle of the circle, and
# the initial point is at [0;0;1]
#
# Input:
#
#   t: 1xn or nx1 vector of times at which to generate points on the circle
#
# Output:
#
#   xyz: 3xn matrix. Each row is the x, y, or z location of points on the
#       circle, and each column corresponds to one time point from the
#       input

    # Second, use 'zeros', 'sin', and 'cos' operations to convert t into
    # xyz points. Don't forget to use a 2*pi factor so that the period of
    # the circle is 1. Save the output as variable 'xyz
    


    xyz = [[0], [np.sin(2*np.pi*t[0])], [np.cos(2*np.pi*t[0])]]

    return xyz