def negative(x):
    if x <= 0:
        return x
    else:
        return -1 * x 

def ind_plus_1_lap(alist,ind):
    if ind == len(alist) - 1:
        ind = 0
    else:
        ind += 1

    return ind 