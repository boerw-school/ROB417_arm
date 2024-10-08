def vector_set_cumulative_sum(v_set):

    v_set_s = v_set
    
    for number_of_angles in range(2, len(v_set_s)):
        v_set_s[number_of_angles] = v_set_s[(number_of_angles-1)]+v_set_s[number_of_angles]
    return v_set_s