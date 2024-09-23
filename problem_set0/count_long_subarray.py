def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    record_dict = {}
    i = 0
    j = 1
    length = 1
    max_key = 0
    def record(length):
        if length in record_dict:
            record_dict[length] += 1
        else:
            record_dict[length] = 1

    while j <= len(A) - 1:
        if A[i] < A[j]:
            length += 1
            i += 1
            j += 1
            record(length)
        else:
            i += 1
            j += 1
            length = 1

    for key in record_dict.keys():
        if key > max_key:
            max_key = key
    
    count = record_dict[max_key]

    return count
