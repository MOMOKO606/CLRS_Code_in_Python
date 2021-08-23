import random


"""
The exquisite & classic function used in Quicksort.
Input @para: list A, the start & end index of A.
Output @para: j + 1 = the index of the pivot, the list satisfies A[...j] <= pivot, A[j + 1] == pivot, A[j + 2, ...] > pivot.

"""
def partition( A, low, high ):

    #  Define A[high] as pivot.
    #  pivot can be any element in A[low, ..., high], it's your choice.
    pivot = A[high]
    #  Initialize index j
    j = low - 1

    for i in range(low, high):
        #  A[...j] <= pivot
        if A[i] <= pivot:
            j = j + 1
            A[i], A[j] = A[j], A[i]

    #  A[...j] <= pivot, A[j + 1] == pivot, A[j + 2, ...] > pivot.
    A[high], A[j + 1] = A[j + 1], A[high]

    #  Return the index of pivot in A after partition.
    return j + 1


"""
The classic Quicksort.
Input @para: list A, the start & end index of A.
Output @para: the sorted A[low, ..., high].
"""
def quicksort( A, low, high ):

    #  Base case: one or 0 element.
    if low >= high:
        return A

    #  Divide A into 2 parts.
    mid = partition( A, low, high )
    #  Recursively sort the 2 parts.
    quicksort( A, low, mid - 1 )
    quicksort( A, mid + 1, high )

    return A


"""
The randomized Quicksort.
We choose the pivot randomly to avoid the worst case in which the list is already sorted.

Input @para: list A, p & r = the start & end index of A.
Output @para: the sorted A[p, ..., r].
"""
def randomized_quicksort(A, p, r):
    #  Implicit the base case: if p >= r: return A.
    if p < r:
        #  Get a random index j from p to r.
        j = random.randrange( p, r )
        #  Exchange A[j] and A[r]
        A[j], A[r] = A[r], A[j]

        #  Implemented quick sort.
        q = partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)

    return A


"""
The old fashion hoare partition.
Input @para: list A, the start & end index of A.
Output @para: j + 1 = the index of the pivot, the list satisfies A[...j] <= pivot, A[j + 1] == pivot, A[j + 2, ...] > pivot.

The secrete of Hoare partition is that, 
unlike the classic partition algorithm which can make sure that A[p,...,q - 1] <= A[q] < A[q + 1, ..., r]
The hoare partition cannot locate the index of pivot, which means A[i] = pivot can be within either part.
so we have to process A[p,...,q] and A[q + 1, ..., r] then.

Note: 
Using do-while is better than while in this algorithm.
We can use while True + break to replace do-while in Python.
"""
def hoare_partition(A, p, r):

    #  Initialize i & j
    i = p - 1
    j = r + 1
    pivot = A[p]

    while i < j:
        #  Start from left,
        #  Moving to the right if A[i] < pivot.
        while True:
            i += 1
            if A[i] >= pivot: break

        #  Start from right,
        #  Moving to the left if A[i] > pivot.
        while True:
            j -= 1
            if A[j] <= pivot: break

        # #  The while version.
        # while i <= r and A[i] < pivot:
        #     i += 1
        # while j >= p and A[j] > pivot:
        #     j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]
    return j


"""
The classic Quicksort using Hoare partition.
Input @para: list A, the start & end index of A.
Output @para: the sorted A[p, ..., r].
"""
def hoare_quicksort(A, p, r):
    #  Base case: one or 0 element.
    if p >= r:
        return A

    #  Divide A into 2 parts.
    q = hoare_partition( A, p, r )
    #  Recursively sort the 2 parts.
    hoare_quicksort( A, p, q )
    hoare_quicksort( A, q + 1, r )

    return A


if __name__ == "__main__":

    A = [2, 8, 7, 1, 3, 5, 6, 4]

    #  Test for Quicksort in P171.
    print("Test for Quicksort in P171: ", quicksort( A[:], 0, len(A) - 1) , '\n')
    #  Test for Randomized Quicksort in P179.
    print("Test for Randomized Quicksort in P179: ", randomized_quicksort( A[:], 0, len(A) - 1) , '\n')
    #  Test for Quicksort using Hoare-partition in P185.
    print("Test for Quicksort using Hoare-partition in P185: ", hoare_quicksort( A[:], 0, len(A) - 1), '\n')

