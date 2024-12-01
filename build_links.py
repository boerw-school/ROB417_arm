import numpy as np

def build_links(link_vectors):

    
    link_set = [None]*len(link_vectors)
    
    
    
    for number_of_links in range(0,len(link_vectors)):
        
        link_set[number_of_links] = np.reshape([0,0,0],(3,1)),link_vectors[number_of_links]
        
        
        #link_set[number_of_links] = np.matrix(np.reshape(np.append(np.zeros(len(link_vectors[number_of_links])) , link_vectors[number_of_links]),(len(link_vectors[number_of_links]),2)))

    return link_set
