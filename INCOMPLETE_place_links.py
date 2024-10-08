import numpy as np

def place_links(links_in_world,link_end_set_with_base):
    
    link_set = links_in_world
    for n in range(1 , np.size(link_set, 1)):
        link_set[n] = np.add(link_end_set_with_base[n],link_set[n])
    #rows in each array are supposed to be columns
    return link_set


a = np.array([[[0,0],[0,1]],[[0,0],[2,1]]])
print (a.shape)
b = np.array([[0,0],[0,1],[2,2]])
print (b.shape)
print(place_links(a,b))