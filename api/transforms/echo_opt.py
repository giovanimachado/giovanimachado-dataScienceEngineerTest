import numpy as np

def diff_matrix(a):
    '''
    This function returns a two-dimensional (broadcasted) numpy array 
    which contains the differences between all possible combinations 
    of a list or numpy array a. 
    For example, diff[3,2] would contain the result of a[3] - a[2] 
    and so on.
    '''
    x = np.reshape(a, (len(a), 1))
    return x - x.transpose()


def the_good_func(my_list, tol=1e-2):
    #Calculate the difference between all elements
    elements_dif = diff_matrix(my_list)
    
    #Compare the diff with the threshold (tolerance)
    boolArr = abs(elements_dif) > tol
    
    #Create an upper triangular matrix containing the diffs
    tri = np.triu(boolArr, k=1)*(1)
    np.fill_diagonal(tri, 1)

    #Count the "non_zeros" elements diffs
    non_zeros_counter = np.count_nonzero(tri, axis=0)
    
    #Create a numpy array with the index range of the original list 
    idx = np.arange(len(my_list))+1
    
    #Create a mask to apply to the repeated elements
    mask = (idx-non_zeros_counter) == 0
    
    #Sum the elements and 
    out_sum = np.cumsum(my_list) 
    
    #Divide the elements by their position and apply the mask 
    #to remove repeated elements
    #result = out_sum/(np.arange(len(my_list))+1)*mask
    result = out_sum / (idx) * mask 
  
    return result.tolist()