import numpy as np

def build_links(link_vectors):

    link_set = np.empty(np.size(link_vectors, 0),np.size(link_vectors, 1))
    


    for number_of_links in range(1,len(link_set)):
        #link_set[number_of_links] = [np.zeros(len(link_vectors[1,number_of_links]),1) , link_vectors[:,number_of_links]]
    return link_set