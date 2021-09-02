"""
The counting sort for non-negative numbers in Chapter 8 P195.
Input: list A.
Output: the sorted A.
"""
def counting_sort( A ):

    #  Get the length of A.
    n = len(A)
    #  Get the range of A.
    k = max(A)
    #  Initialize the empty auxiliary lists by size.
    C = [0] * (k + 1)
    B = [0] * n

    #  counting the times each element in A appears.
    for i in range(n):
        C[A[i]] += 1
    #  Accumulate the counting.
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    #  The value in C now represents the sorted position of its index.
    #  I know it's a bit silly and tricky, the indices of C now represents the original value in A.
    #  So now we go through A to check every element and its related sorted position.
    #  We go through A from right to left since we want the algorithm to be stable.
    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        #  Update the index.
        C[A[i]] -= 1
    return B


"""
8.2-4 in P197.
Counts how many numbers in list A are from a to b inclusive, O(n + k).
where n is the length of A and k is the largest value of element in A.
Input @para: list A, the range [a, b]
Output: the numbers of elements fall into [a, b]
"""
def num_in_range( A, a, b ):

    #  Get the length of A.
    n = len(A)
    #  Get the range of A.
    k = float("-inf")
    for j in range(n):
        if A[j] > k:
            k = A[j]

    #  Sentinels
    assert a >= 0, "a must >= 0."
    assert b <= k, "b must <= k."

    #  Initialize the empty auxiliary lists by size.
    C = [0] * (k + 1)
    B = [0] * n

    #  counting the times each element in A appears.
    for i in range(n):
        C[A[i]] += 1
    #  Accumulate the counting.
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    if a == 0:
        return C[b]
    else:
        return C[b] - C[ a - 1 ]


"""
Compute how many digits a number has.
Input: the number.
Output: the number of digits of the input number.
"""
def get_d_digits( num ):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count


"""
Transfer a list of numbers into a matrix  form by digits, 
which means each element in the matrix represent a digit of a number.
Input: the list of numbers.
Output: the digits form of the input numbers.
"""
def trans2digits( A, d ):
    n = len(A)
    #  Initialize the n * d output matrix with 0s.
    A_matrix = [ [0 for i in range(d)] for j in range(n) ]

    for i in range(n):
        j = d - 1
        key = A[i]
        while key != 0:
            A_matrix[i][j] = key % 10
            #  Update parameters.
            j -= 1
            key = key // 10
    return A_matrix


"""
The counting sort for matrix.
We compare the values in the kth column of the input matrix.
But instead of sort the values in the kth column, we sort the entire rows.
Input: matrix A and k represents the kth column.
Output: the sorted matrix.
"""
def counting_sort4mat( matrix, k ):

    #  Get the rows of matrix.
    n = len(matrix)
    #  Get the columns of matrix.
    d = len(matrix[0])

    #  set the kth digits of the matrix as list A.
    A = [matrix[i][k] for i in range(n)]

    #  Get the range of A.
    k = max(A)
    #  Initialize the empty auxiliary lists by size.
    C = [0] * (k + 1)
    B = [[0 for i in range(d)] for j in range(n)]

    #  counting the times each element in A appears.
    for i in range(n):
        C[A[i]] += 1
    #  Accumulate the counting.
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    #  The value in C now represents the sorted position of its index.
    #  I know it's a bit silly and tricky, the indices of C now represents the original value in A.
    #  So now we go through A to check every element and its related sorted position.
    #  We go through A from right to left since we want the algorithm to be stable.
    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = matrix[i]
        #  Update the index.
        C[A[i]] -= 1
    return B


"""
Transfer a matrix of digits into a list of integers. 
which means we combine the digits together.
Input: the matrix and d = the columns of the matrix.
Output: the list of integers.
"""
def trans2list( matrix, d ):
    res = []
    for i in range(len(matrix)):
        sum = 0
        factor = 1 / 10
        for j in range(d - 1, -1, -1):
            factor *= 10
            sum += int(factor) * matrix[i][j]
        res.append(sum)
    return res



"""
The classic radix sort.
Input: list A.
Output: the sorted A.
"""
def radix_sort( A ):

    #  Find the largest number of digits in A.
    d = get_d_digits( max(A) )

    #  Transfer A into matrix of digits of A.
    A_matrix = trans2digits( A, d )

    #  Sort every digit from right to left.
    for j in range(d - 1, -1, -1):
        A_matrix = counting_sort4mat( A_matrix, j )

    #  Transfer the matrix of digits to a list of integers.
    A = trans2list( A_matrix, d )

    return A


#  Drive code
if __name__ == "__main__":

    #  Data collection.
    A0 = [2, 5, 3, 0, 2, 3, 0, 3]
    A1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    A2 = [329, 457, 657, 839, 436, 720, 355]
    A3 = []

    #  Test for the classic counting sort in P195.
    print("Test for counting sort in P195: ", counting_sort(A1[:]), '\n')
    #  Test for how many of the n integers fall into a range [a, b] of 8.2-4 in P197.
    print("Test for algorithm of 8.2-4 in P197: ", num_in_range(A0, 2, 5), '\n')
    #  Test for the classic radix sort in P198.
    print("Test for the classic radix sort in P198: ", radix_sort( A2 ), '\n')


