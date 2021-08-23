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


def randomized_quick_sort(A, p, r):

    if p < r:
        #  Get a random index j from p to r.
        j = random.randrange( p, r )
        #  Exchange A[j] and A[r]
        A[j], A[r] = A[r], A[j]

        #  Implemented quick sort.
        q = partition(A, p, r)
        randomized_quick_sort(A, p, q - 1)
        randomized_quick_sort(A, q + 1, r)

    return A






if __name__ == "__main__":

    A = [2, 8, 7, 1, 3, 5, 6, 4]

    #  Test for Quicksort in P171.
    print("Test for Quicksort in P171: ", quicksort( A, 0, len(A) - 1) , '\n')
    #  Test for Randomized Quicksort in P179.
    print("Test for Randomized Quicksort in P179: ", randomized_quick_sort( A, 0, len(A) - 1) , '\n')

