import numpy as np
import matplotlib as plt
def threeD_update_links(l,link_set):
    # Update the drawings of a set of lines for a link structure
    #
    # Inputs:
    #                                                                                                                                                                                             
    #   l: A cell array of the same size as link_set, in which each entry is a
    #       handle to a line structure for that link
    #
    #
    #   link_set: A 1xn cell array, each entry of which is a matrix whose
    #       columns are the endpoints of the lines describing one link of the
    #       system (as constructed by build_links)
    #
    # Output:
    #
    #   l: A cell array of the same size as link_set, in which each entry is a
    #       handle to a surface structure for that link


        #
        # Loop over the lines whose handles are in 'l', replacing their 'XData',
        # 'YData', and 'ZData' with the information from 'link_set'

    line_data=[None]*len(link_set)
    for n in range (len(link_set)):
        X_Data_New = link_set[0][:,0][:,0]
        Y_Data_New = link_set[1][:,0][:,0]
        Z_Data_New = link_set[2][:,0][:,0]
        
        line_data[n] = [l[n],X_Data_New,Y_Data_New,Z_Data_New]
        
            
    return line_data