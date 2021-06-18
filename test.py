from functools import reduce

A2 = [2, 3, 8, 6, 1]

def inversion_naive( A ):
    result = [ "inversion" for i in range( len(A) - 1 ) for j in range( i + 1, len(A) ) if A[i] > A[j] ]
    return len(result)

print( inversion_naive(A2) )