
def vector_set_difference(v,v_set):

    # Start by copying v_set into a new variable v_diff;
    v_diff = v_set

    # Loop over v_diff, subtracting each vector from v 
    for n in range(0 , len(v_set)):
        v_diff[n] = v- v_set[n]
    return v_diff