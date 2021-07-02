#----------------  Find the Maximum Sub-array ----------------------#
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
4.1-5  --the original Kadane's algorithm
*  The original requirement for Kadane's algorithm is that Your array must have at least one positive number.

Input @para: list A.
Output @para:
max_sum = The sum value of the maximum contiguous subarray in A;
left_index = the start index of the maximum contiguous subarray;
right_index = the end index of the maximum contiguous subarray.

See more details: https://github.com/MOMOKO606/CLRS_Code_in_Python/blob/main/Notes_Kadanes_algorithm.md
"""
def maxsubarray_kadane_ori( A ):

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


"""
The recursive Kadane's algorithm
The function aims to output the value, left-end of the max sub-array which must contains A[j].

Input @para: list A, index j, max sub-array tracker. The tracker is used to track the max sub-array throughout the whole array.
Output @para:
max_sum = The sum value of the maximum contiguous subarray in A which must have A[j];
left_index = the left-end index of the maximum contiguous subarray in A which must have A[j].
[max subarray's value, max subarray's left-end, max subarrya's right-end] is a tracker which keeps tracking the max subarray of the whole array.
"""
def maxsubarray_kadane_recur(A, j):

    #  Base case, initialize the tracker.
    if j == 0:
        max_tracker = 0
        return A[0], 0, [max_tracker, 0, 0]

    #  Recursive step
    [max_previous, i, [max_tracker, max_left, max_right]] = maxsubarray_kadane_recur(A, j - 1)
    tmp = max_previous + A[j]

    #  Check the new max sub-array, case 1
    if tmp <= A[j]:

        #  Update the tracker.
        if A[j] >= max_tracker:
            max_tracker = A[j]
            max_left = max_right = j
        return A[j], j, [max_tracker, max_left, max_right]

    else:  # case 2

        #  Update the tracker.
        if tmp >= max_tracker:
            max_tracker = tmp
            max_left = i
            max_right = j
        return tmp, i, [max_tracker, max_left, max_right]


"""
The iterative Kadane's algorithm.

Input @para: list A.
Output @para:
[max subarray's value, max subarray's left-end, max subarrya's right-end] = the max subarray of the whole array and it's indices.
"""
def maxsubarray_kadane( A ):

    #  Initialize ans as ans[i] represents the value of max sub-array that must contains A[i].
    #  left & right = left & right indices of the max sub-array that must contains A[i] for each i.
    ans = A[:]
    left = 0
    right = 0

    #  Initialize the max sub-array tracker that keeps tracking the max sub-array through the whole A.
    #  max_left & max_right = left & right indices of the max sub-array through the whole A.
    max_value = ans[0]
    max_left = 0
    max_right = 0

    for i in range( 1, len(A) ):

        #  Update ans[i], left & right according to the recurrence.
        if ans[i - 1] + ans[i] <= ans[i]:
            left = right = i
            ans[i] = ans[i]
        else:
            right = i
            ans[i] = ans[i - 1] + ans[i]

        #  Update the tracker.
        if ans[i] >  max_value:
            max_value = ans[i]
            max_left = left
            max_right = right

    return max_value, max_left, max_right


"""
The iterative Kadane's algorithm, the min version.

Input @para: list A.
Output @para:
[min subarray's value, min subarray's left-end, min subarrya's right-end] = the min subarray of the whole array and it's indices.
"""
def minsubarray_kadane( A ):

    #  Initialize ans as ans[i] represents the value of min sub-array that must contains A[i].
    #  left & right = left & right indices of the min sub-array that must contains A[i] for each i.
    ans = A[:]
    left = 0
    right = 0

    #  Initialize the min sub-array tracker that keeps tracking the min sub-array through the whole A.
    #  min_left & min_right = left & right indices of the min sub-array through the whole A.
    min_value = ans[0]
    min_left = 0
    min_right = 0

    for i in range( 1, len(A) ):

        #  Update ans[i], left & right according to the recurrence.
        if ans[i - 1] + ans[i] > ans[i]:
            left = right = i
            ans[i] = ans[i]
        else:
            right = i
            ans[i] = ans[i - 1] + ans[i]

        #  Update the tracker.
        if ans[i] < min_value:
            min_value = ans[i]
            min_left = left
            min_right = right

    return min_value, min_left, min_right
#----------------End of Find the Maximum Sub-array ----------------------#


#-----------------------  Matrix Multiplication ------------------------#
"""
The tradition point-to-point Matrix Multiplication method.
NOTICE: The number of columns in A must equals to the number of rows in B.

Input @para: Matrix A & B.
Output: Matrix C = A * B.
"""
def matrix_multip_pt( A, B ):

    #  Get the size of Matrix A.
    row_a = len( A )
    col_a = len( A[0] )

    #  Get the size of Matrix B.
    row_b = len( B )
    col_b = len( B[0] )

    #  Initialize the output matrix.
    C = [[0] * col_b for i in range(row_a)]

    #  Sentinel.
    assert col_a == row_b, "The number of columns in A must equals to the number of rows in B."

    #  The traditional method of multiply 2 matrices.
    #  point-to-point
    for i in range( row_a ):
        for j in range( col_b ):
            for k in range( col_a ):
                C[i][j] += A[i][k] * B[k][j]
    return C


"""
The tradition row  Matrix Multiplication method.
NOTICE: The number of columns in A must equals to the number of rows in B.

Input @para: Matrix A & B.
Output: Matrix C = A * B.
"""
def matrix_multip_row( A, B ):

    #  Get the size of Matrix A.
    row_a = len( A )
    col_a = len( A[0] )

    #  Get the size of Matrix B.
    row_b = len( B )
    col_b = len( B[0] )

    #  Initialize the  output matrix.
    C = []

    #  The traditional row method of multiply 2 matrices.
    for i in range( row_a ):

        #  Initialize the row in output matrix.
        row = [0] * col_b

        #  row vector * matrix B
        for j in range( col_a ):
            #  The factors (A[i][j]) * rows in Matrix B.
            tmp = [ A[i][j] * B[j][k] for k in range(col_b) ]
            #  Put the rows above together to form the rows in the result.
            row = [row[k] + tmp[k] for k in range(col_b)]
        #  Computed and added rows to the result.
        C.append(row)

    return C


"""
The tradition column Matrix Multiplication method.
NOTICE: The number of columns in A must equals to the number of rows in B.

Input @para: Matrix A & B.
Output: Matrix res = A * B.
"""
def matrix_multip_col( A, B ):

    #  Get the size of Matrix A.
    row_a = len( A )
    col_a = len( A[0] )

    #  Get the size of Matrix B.
    row_b = len( B )
    col_b = len( B[0] )

    #  Initialize the  output matrix.
    C = []
    res = []

    #  The traditional column method of multiply 2 matrices.
    for j in range(col_b):

        #  Initialize the column in output matrix.
        col = [0] * row_a

        #  matrix A * column vector
        for i in range(row_b):
            #  The factors (B[i][j]) * columns in Matrix A.
            tmp = [B[i][j] * A[k][i] for k in range(row_a)]
            #  Put the columns above together to form the columns in the result.
            col = [col[k] + tmp[k] for k in range(row_a)]
        #  Computed and added columns to the result.
        C.append(col)

    #  Exchange rows and columns.
    #  res is the transpose matrix of C.
    for j in range(col_a):
        tmp = [C[i][j] for i in range( col_b )]
        res.append(tmp)

    return res


"""
The divide-and-conquered Matrix Multiplication method.
NOTICE: 
The number of columns in A must equals to the number of rows in B.
A & B both are n * n matrices, n is divisiable by 2. 

Input @para: Matrix A & B.
Output: Matrix res = A * B.
"""
def matrix_multip_recur( A, B ):
    #  Base case, only one element.
    pass




if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    A2 = [-3, 13, 7, 28, -28, 4, 3, 2, 40]
    A3 = [-15, -3, -1, -2]
    A4 = [[0, 0, 5], [4, 2, 1], [0, -1, 2]]
    B = [[1, 2, 4, -1], [5, 3, 1, 0], [0, 0, 2, 0]]

    #  Test for the brute-force solution of finding the maximum contiguous subarray in P69 & P74 4.1-2.
    print("Test for the naive algorithm of max subarray in P69:", max_subarray_naive( A ) )

    #  Test for the recursive algo of finding the maximum contiguous subarray in P72.
    print("Test for the d & c algo of max subarray in P72:", find_maxsubarray_recur( A, 0, len(A) - 1 ))

    #  Test for a series of kadane's algorithms in P75.
    print("Test for the original kadane's algo in P75:", maxsubarray_kadane_ori( A2 ))
    print("Test for the original kadane's algo in P75:", maxsubarray_kadane_ori( A ))
    ans = maxsubarray_kadane_recur( A, len(A) - 1 )
    print("Test for the recursive kadane's algo:", ans[2])
    print("Test for the iterative kadane's algo:", maxsubarray_kadane( A3 ))
    print("Test for the min version of kadane's algo:", minsubarray_kadane(A), '\n')

    #  Test for a series of Matrix multiplications in P75.
    print("Test for the naive Matrix multiplication in P75:", matrix_multip_pt( A4, B ))
    print("Test for the row Matrix multiplication in P75:", matrix_multip_row( A4, B ))
    print("Test for the column Matrix multiplication in P75:", matrix_multip_col(A4, B))
