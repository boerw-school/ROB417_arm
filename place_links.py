import numpy as np
import copy
def place_links(links_in_world,link_end_set_with_base):
    link_set = copy.deepcopy(links_in_world)
    
    for n in range(0 , len(link_set)):
        link_set[n] = link_end_set_with_base[n]+link_set[n]
    return link_set
