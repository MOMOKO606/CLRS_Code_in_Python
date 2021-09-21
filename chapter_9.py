import random

def min_max( A ):
    pass



#  Drive code
if __name__ == "__main__":

    #  Test data collection.
    A0 = [2, 5, 3, 0, 2, 3, 0, 3]
    A1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    A2 = [329, 457, 657, 839, 436, 720, 355]
    A3 = [10000, 329, 9923, 457, 12, 657, 68, 839, 54921, 436, 2849, 720, 3, 355]
    A5 = [4321, 399, 28, 5]
    A6 = [5, 10, 7, 2, 3, 1, 4, 9, 8, 6]


    #  Test for the classic counting sort in P195.
    print("Test for counting sort in P195: ", counting_sort(A1[:]), '\n')
    #  Test for how many of the n integers fall into a range [a, b] of 8.2-4 in P197.
