"""Transformation function 'Echo'"""

def bad_func(inp_vals, tol=1e-2):
    """Takes a list of floats and transforms them
    A new list of values of the same length is returned
    """
    new_vals = []
    i_p = 0
    while i_p < len(inp_vals):
        val = inp_vals[i_p]
        # Calculate the sum and count of all values up to this value
        sum_vals = 0
        j_p = 0
        while j_p < len(inp_vals):
            s_val = inp_vals[j_p]
            sum_vals += s_val
            counter = j_p + 1
            if j_p == i_p:
                break
            j_p += 1
        # Find if this value already occurred in the input list within tol
        seen = False
        j_p = 0
        while j_p < len(inp_vals):
            if j_p == i_p:
                break
            s_val = inp_vals[j_p]
            if abs(val - s_val) < tol:
                seen = True
            j_p += 1
        # If we've seen the value before we set a zero, otherwise
        # we set the sum divided by a counter.
        if seen:
            new = 0
        else:
            new = sum_vals / counter
        new_vals.append(new)
        i_p += 1
    return new_vals
