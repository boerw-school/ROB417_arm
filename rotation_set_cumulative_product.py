def rotation_set_cumulative_product(R_set):

    R_set_c = R_set
    
    for number_of_angles in range(2, len(R_set_c)):
        R_set_c[number_of_angles] = R_set_c[(number_of_angles-1)]+R_set_c[number_of_angles]
    return R_set_c