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
    print("Test for the simultaneous minimum and maximum algorithm in P214: ",min_max( A3 ), '\n')
    #  Test for how many of the n integers fall into a range [a, b] of 8.2-4 in P197.
