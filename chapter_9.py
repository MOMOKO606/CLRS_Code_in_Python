import random


"""
Get the minimum and the maximum elements of A simultaneously.
First we compare each elements in pairs, 
then we search the possible minimum in the smaller elements in all pairs,
search the possible maximum in the larger elements in all pairs.

Input: list A.
Output: the minimum & maximum elements in A.
"""
def min_max( A ):
    n = len(A)

    #  Comparing in pairs.
    for i in range(0, n - 1, 2):
        if A[i] >= A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]

    #  Get the minimum.
    Amin = float("inf")
    for i in range(0, n, 2):
        if A[i] < Amin:
            Amin = A[i]

    #  Get the maximum.
    Amax = float("-inf")
    for i in range(1, n, 2):
        if A[i] > Amax:
            Amax = A[i]

    return Amin, Amax


#  Randomized partition in Quicksort.
def random_partition(A, p, r):

    #  The classic partition in Quicksort.
    def partition(A, p, r):
        j = p - 1
        for i in range(p, r):
            if A[i] <= A[r]:
                j += 1
                A[j], A[i] = A[i], A[j]
        A[j + 1], A[r] = A[r], A[j + 1]
        return j + 1
    #  Choosing the pivot randomly.
    j = random.randint( p, r )
    A[j], A[r] = A[r], A[j]
    return partition(A, p, r)


"""
Select the ith largest element in array A.
Input @para: list A, start index p and end index r, i means ith largest element.
Output: the ith largest element in array A[p,...,r]
"""
def select_recur( A, p, r, i ):

    #  Partition list A randomly, then search ith element in which subarray of A.
    q = random_partition(A, p, r)
    #  Transfer index q to kth.
    k = q - p + 1

    #  Base case.
    if k == i:
        return A[q]
    #  ith element must be in the left subarray.
    if i < k:
        return select_recur( A, p, q - 1, i)
    #  when i > k, ith element must be in the right subarray.
    #  Notice, when go to the right subarray, i need to do some computation.
    else:
        return select_recur( A, q + 1, r, i - k)


def select_iter(A, i):
    n = len(A)
    p = 0
    r = n - 1
    assert i <= n, "i must be less than or equal to n."
    while True:
        #  Partition list A randomly, then search ith element in which subarray of A.
        q = random_partition(A, p, r)
        #  Transfer index q to kth.
        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            r = q - 1
        else:
            p = q + 1
            i = i - k




#  Drive code
if __name__ == "__main__":

    #  Test data collection.
    A0 = [2, 5, 3, 0, 2, 3, 0, 3]
    A1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    A2 = [329, 457, 657, 839, 436, 720, 355]
    A3 = [10000, 329, 9923, 457, 12, 657, 68, 839, 54921, 436, 2849, 720, 3, 355]
    A5 = [4321, 399, 28, 5]
    A6 = [5, 10, 7, 2, 3, 1, 4, 9, 8, 6]


    #  Test for the simultaneous minimum and maximum algorithm in P214.
    print("Test for the simultaneous minimum and maximum algorithm in P214: ", min_max( A3 ), '\n')
    #  Test for recursive select in P216.
    print("Test for recursive select in P216: ", select_recur( A2[:], 0, len(A2) - 1, 3 ), '\n')
    #  Test for iterative select in 9.2-3 P219.
    print("Test for iterative select in 9.2-3 P219: ", select_iter(A2[:], 3), '\n')
