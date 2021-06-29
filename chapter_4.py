"""
The brute-force algorithm for finding the maximum contiguous subarray.
Input @para: list A.
Output @para:
max = The sum value of the maximum contiguous subarray in A;
left_index = the start index of the maximum contiguous subarray;
right_index = the end index of the maximum contiguous subarray.
"""
def max_subarray_naive( A ):
    n = len( A )
    max = float("-inf")

    #  i determines the left_index.
    for i in range( n ):
        sum = 0
        #  j determines the right_index.
        for j in range( i, n - 2 ):
            sum = sum + A[j]
            if sum >= max:
                max = sum
                left_index = i
                right_index = j
    return max, left_index, right_index


"""
The function used in the "find_maxsubarray_recur" to get the maximum contiguous subarray crossing left and right parts.
The 'crossing part' must have A[mid] & A[mid + 1] at least.

Input @para: list A[low, ..., mid,..., high].
Output @para: [value, start, end]
value = The sum value of the maximum contiguous subarray in A[..., mid, mid + 1, ...];
start = the start index of the maximum contiguous subarray;
end = the end index of the maximum contiguous subarray.
"""
def getcross_maxsubarray( A, low, mid, high ):

    left_sum = float("-inf")
    sum = 0
    for i in range( mid, low - 1, -1 ):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i

    right_sum = float("-inf")
    sum = 0
    for j in range( mid + 1, high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            right_index = j

    return [left_sum + right_sum, left_index, right_index]


"""
The recursive algorithm for finding the maximum contiguous subarray.
The idea is, divide A[low, ..., high] into A[low, ..., mid] and A[mid + 1, ..., high], so the maximum contiguous subarray
is either in the left part, right part, or crossing both parts. 
So we recursively get the maximum contiguous subarray in both parts, and get max subarray from crossing part 
through function getcross_maxsubarray, then compare them to find the largest one.

Input @para: list A[low, ..., high].
Output @para: [value, start, end]
value = The sum value of the maximum contiguous subarray in A[low, ..., high];
start = the start index of the maximum contiguous subarray;
end = the end index of the maximum contiguous subarray.
"""
def find_maxsubarray_recur( A, low, high ):

    #  Base case, only one element.
    if low == high:
        return [A[low], low, high]

    mid = ( low + high ) // 2

    #  Find the max subarray in the left part.
    [left_value, left_start, left_end] = find_maxsubarray_recur( A, low, mid )
    #  Find the max subarray in the right part.
    [right_value, right_start, right_end] = find_maxsubarray_recur( A, mid + 1, high )
    #  Find the max subarray in the crossing part.
    [cross_value, cross_start, cross_end] = getcross_maxsubarray( A, low, mid, high )

    #  Compare those max subarrays above.
    if left_value >= right_value and left_value >= cross_value:
        #  The max subarray in the left part is the largest.
        return [left_value, left_start, left_end]
    elif cross_value >= right_value and cross_value >= left_value:
        #  The max subarray in the crossing part is the largest.
        return [cross_value, cross_start, cross_end]
    else:
        #  The max subarray in the right part is the largest.
        return [right_value, right_start, right_end]


"""
4.1-5  -- Kadane's algorithm
Use the following ideas to develop a nonrecursive, linear-time algorithm for the maximum-subarray problem. 
Start at the left end of the array, and progress toward the right, keeping track of the maximum subarray seen so far. 
Knowing a maximum subarray of A[1.. j] , extend the answer to ﬁnd a maximum subarray ending at index j + 1 by using 
the following observation: a maximum subarray of A[1.. j + 1] is either a maximum subarray of A[1.. j] or 
a subarray A[i .. j +1] , for some 1 <= i<= j + 1. 
Determine a maximum subarray of the form A[i... j+1] in constant time based on knowing a maximum subarray ending at index j.

* Your array must have at least one positive number.

The idea is, a maximum sub-array should be positive. Therefore, if our sum is negative, it is meaningless to consider it 
as a part of the maximum sub-array.

So, we determine i by negative or positive of the sum. 
First we need to figure out the maximum sub array ending at index j + 1 which could be just A[j + 1] or the maximum subarray in 
A[1.. j] , therefore we find the max of this two.

Input @para: list A.
Output @para:
max_sum = The sum value of the maximum contiguous subarray in A;
left_index = the start index of the maximum contiguous subarray;
right_index = the end index of the maximum contiguous subarray.
"""
def find_maxsubarray_liner( A ):

    #  Initialize
    max_sum = float("-inf")
    curr_sum = 0
    left_index = 0
    right_index = 0

    #  looking through the array
    for i in range(len(A)):
        curr_sum += A[i]

        #  Determine the right_index of the max sub-array.
        if curr_sum > max_sum:
            max_sum = curr_sum
            right_index = i

        #  Determine the left_index of the max sub-array.
        if curr_sum < 0:
            curr_sum = 0
            #  if A[i] is not the last element, we can moving it to the right.
            if i != len(A) - 1:
                left_index = i + 1

    return [max_sum, left_index, right_index]








if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    A2 = [-3, 13, 7, 28, -28, 4, 3, 2, 40]

    #  Test for the brute-force solution of finding the maximum contiguous subarray in P69 & P74 4.1-2.
    print("Test for the naive algorithm of max subarray in P69:", max_subarray_naive( A ) )
    #  Test for the recursive algo of finding the maximum contiguous subarray in P72.
    print("Test for the recursive algorithm of max subarray in P72:", find_maxsubarray_recur( A, 0, len(A) - 1 ))
    #  Test for the liner algo of finding the maximum contiguous subarray in P75.
    print("Test for the linear algorithm of max subarray in P75:", find_maxsubarray_liner( A2 ))
    print("Test for the linear algorithm of max subarray in P75:", find_maxsubarray_liner( A ), '\n')

