import numpy as np

def draw_vectors_at_point(p,V,ax):
# Draw the columns of V as arrows based at point p, in axis ax
#
# Inputs:
#
#   p: a 3x1 vector designating the location of the vectors
#   V: a 3xn matrix, each column of which is a 3x1 vector that should be
#       drawn at point p
#   ax: the axis in which to draw the vectors
#
# Output:
#
#   q: a cell array of handles to the quiver objects for the drawn arrows

    # First use hold(ax,'on') so that when we call quiver, it does not
    # delete the plot
    # Now create an empty cell array named 'q' with one row and as many columns as V
    
    V_row_amount = np.size(V,0)
    V_column_amount  = np.size(V,1)
    q = [None] * V_column_amount
    

    # Loop over the columns of V
       
        # Use quiver3 to plot an arrow at p, with vector components taken
        # as the first three rows of the (idx)th column of V. Store the
        # output as the (idx)th element of q

   
    for n in range(0 , V_column_amount):
        q[n] = ax.quiver(p[0],p[1],p[2], V[0,n],V[1,n],V[2,n] )

    
      
            
              
    
    # Use hold(ax,'off') to return the axis to its normal behavior
    return q

