"""
The counting sort for non-negative numbers in Chapter 8 P195.
Input: list A.
Output: the sorted A.
"""
def counting_sort( A ):

    #  Get the length of A.
    n = len(A)
    #  Get the range of A.
    k = float("-inf")
    for j in range(n):
        if A[j] > k:
            k = A[j]

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
        return C[b] - C[a -1]





#  Drive code
if __name__ == "__main__":

    #  Data collection.
    A0 = [2, 5, 3, 0, 2, 3, 0, 3]
    A1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]

    #  Test for the classic counting sort in P195.
    print("Test for counting sort in P195: ", counting_sort(A1[:]), '\n')
    #  Test for how many of the n integers fall into a range [a, b] of 8.2-4 in P197.
    print("Test for algorithm of 8.2-4 in P197: ", num_in_range(A0, 2, 5))


