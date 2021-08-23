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
    i = p
    j = r
    pivot = A[p]

    while i < j:
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
    print("Test for Quicksort using Hoare-partition in P185: ", hoare_quicksort( A[:], 0, len(A) - 1), '\n')








