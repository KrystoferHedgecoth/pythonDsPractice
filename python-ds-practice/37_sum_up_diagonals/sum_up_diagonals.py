def sum_up_diagonals(matrix):
    tl_br_sum = 0
    bl_tr_sum = 0
    
    for i in range(len(matrix)):
        tl_br_sum += matrix[i][i]
        bl_tr_sum += matrix[i][len(matrix) - i - 1]
    
    return tl_br_sum + bl_tr_sum