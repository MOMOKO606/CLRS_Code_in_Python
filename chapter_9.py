"""
The median-selection algorithm is generally not used in practice, as he overhead of pivot computation is significant.
But this technique is of theoretical interest in relating selection and sorting algorithms.
-- https://www.geeksforgeeks.org/selection-algorithms/
"""
import random
import math

"""
Get the minimum and the maximum elements of A simultaneously.
First we compare each elements in pairs, 
then we search the possible minimum in the smaller elements in all pairs,
search the possible maximum in the larger elements in all pairs.

Input: list A.
Output: the minimum & maximum elements in A.
"""
def min_max(A):
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


#  The classic partition in Quicksort.
def partition(A, p, r):
    j = p - 1
    for i in range(p, r):
        if A[i] <= A[r]:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[j + 1], A[r] = A[r], A[j + 1]
    return j + 1


#  Randomized partition in Quicksort.
def random_partition(A, p, r):
    #  Choosing the pivot randomly.
    j = random.randint(p, r)
    A[j], A[r] = A[r], A[j]
    return partition(A, p, r)


"""
Select the ith largest element in array A recursively.
Input @para: list A, start index p and end index r, i means ith largest element.
Output: the ith largest element in array A[p,...,r] and its index.
"""
def select_recur(A, p, r, i):
    #  Partition list A randomly, then search ith element in which subarray of A.
    q = random_partition(A, p, r)
    #  Transfer index q to kth.
    k = q - p + 1

    #  Base case.
    if k == i:
        #  Notice, return the value not index.
        return A[q], q
    #  ith element must be in the left subarray.
    if i < k:
        return select_recur(A, p, q - 1, i)
    #  when i > k, ith element must be in the right subarray.
    #  Notice, when go to the right subarray, i need to do some computation.
    else:
        return select_recur(A, q + 1, r, i - k)


"""
Select the ith largest element in array A iteratively.
Input @para: list A, i means ith largest element.
Output: the ith largest element in array A[p,...,r]
"""
def select_iter(A, i):
    n = len(A)
    p = 0
    r = n - 1

    #  Set a sentinel.
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


"""
The kth quantiles of an n-element set are the k - 1 order statistics that 
divide the sorted set into k equal-sized sets (to within 1).

Input @para: list A, p & r are indices of A that A[p,...,r], k means split the array into k segments.
Output @para: the k - 1 quantiles.
"""
def kquantiles(A, p, r, k):
    #  Set sentinel.
    assert k > 1, "It's meaningless otherwise."

    n = r - p + 1
    #  Base case 1: just return the median.
    if k == 2:
        ans = select_recur(A, p, r, math.ceil(n / 2))
        return ans[0]
    #  Base case 2: return the three equal points.
    if k == 3:
        ans1 = select_recur(A, p, r, round(n / 3))
        ans2 = select_recur(A, p, r, round(n / 3) * 2)
        return [ans1[0], ans2[0]]

    #  When k is an even number.
    if k % 2 == 0:
        #  We find the median and its index first.
        q_value, q = select_recur(A, p, r, math.ceil(n / 2))

        #  Then we go to the subarray to find k / 2 quantiles recursively.
        #  k / 2 must be an integer as n is an even number.
        t1 = kquantiles(A, p, q - 1, k / 2)
        t2 = kquantiles(A, q + 1, r, k / 2)
        return [t1, q_value, t2]

    #  When k is an odd number.
    else:
        #  We find the middle two quantiles and their indices first.
        pivot = k - 1 / 2
        pivot = n / k
        q1_value, q1 = select_recur(A, p, r, pivot * n / k)
        q2_value, q2 = select_recur(A, p, r, (pivot + 1) * n / k)

        #  Then we go to the subarray to find k - 1 / 2 quantiles recursively.
        #  k - 1 / 2 must be an integer as n is an even number.
        t1 = kquantiles(A, p, q1 - 1, (k - 1) / 2)
        t2 = kquantiles(A, q2 + 1, r, (k - 1) / 2)
        return [t1, q1_value, q2_value, t2]


"""
Find the closest k elements around median inclusively of array A.
Input @para: array A and parameter k.
Output: the closest k elements.
"""
def kclosest( A, k ):

    #  Find the median in A first.
    n = len(A)
    median, q = select_recur(A, 0, n - 1, math.ceil( n / 2))  # index q is useless here.

    #  Get the delta of each elements with median.
    delta = [A[i] - median for i in range(n)]
    #  We find the first k minimum elements in delta.
    q_left, index = select_recur(delta, 0, n - 1, max(math.ceil( n / 2 ) - k // 2, 1) )  # index is useless here.
    q_right, index = select_recur(delta, 0, n - 1, min(math.ceil( n / 2 ) + k // 2, n - 1) )  # index is useless here.

    #  Search the first k minimum elements in A and return.
    res = [ A[i] for i in range(n) if A[i] >= q_left + median and A[i] <= q_right + median ]
    return res


"""
Get the median of array X and array y, X & Y are already sorted.
Input @para: the sorted array X[xp, ..., xr], the sorted array Y[yp, ..., yr]
Output: the median of X and Y.
"""
def get_median( X, xp, xr, Y, yp, yr ):

    #  Base case1: if the total length of X & Y == 2, we find the median of the two.
    xn = xr - xp + 1
    yn = yr - yp + 1
    if xn + yn == 2:
        return min( X[xp], Y[yp] )

    #  The index / position of median in X.
    xq = (xp + xr) // 2
    #  The index / position of median in Y.
    yq = (yp + yr) // 2

    #  Divide:
    #  We move to the right part of X & left part of Y.
    if X[xq] < Y[yq]:
        #  When X & Y has even numbers of elements each,
        #  The X median is not inclusive, the Y median is inclusive.
        #  The idea is simple, the median of X must belong to the left part of the total median.
        #  Therefore, X median is not inclusive, since it never will be the possible total median.
        #  The Y median is inclusive because we use lower median.
        if xn % 2 == 0:
            return get_median( X, xq + 1, xr, Y, yp, yq )
        #  When X & Y has odd numbers of elements each,
        #  Both median in X & Y are inclusive.
        else:
            return get_median( X, xq, xr, Y, yp, yq )
    #  Y[yq] < X[xq]
    #  vise versa.
    else:
        if xn % 2 == 0:
            return get_median( X, xp, xq, Y, yq + 1, yr )
        else:
            return get_median( X, xp, xq, Y, yq, yr )


"""
Compute the weighted median of array A.
Input @para: A[p,...,r], the original leftkey and rightkey are both 0.5 according to the definition.
Output: the weighted median of A.
"""
def weighted_median( A, p, r, leftkey, rightkey ):

    #  We find the median and its index first.
    median, mindex = select_recur( A, p, r, math.ceil( (r - p + 1)/2 ) )

    #  Get the sum of left & right weight.
    left = sum( A[p:mindex])
    right = sum( A[mindex + 1:r + 1] )

    #  Base case: the median is the weighted median.
    if left < leftkey and right <= rightkey:
        return median
    #  Divide
    #  if the weighted median is in the right part.
    #  NOTICE: remember to update the left key in the recursive call.
    if left < leftkey and right > rightkey:
        return weighted_median(A, mindex + 1, r, leftkey - left - median, rightkey)
    #  if the weighted median is in the left part.
    #  NOTICE: remember to update the right key in the recursive call.
    else:
        return weighted_median(A, p, mindex - 1, leftkey, rightkey - right - median)




#  Drive code
if __name__ == "__main__":
    #  Test data collection.
    A0 = [2, 5, 3, 0, 2, 3, 0, 3]
    A1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    A2 = [329, 457, 657, 839, 436, 720, 355]
    A3 = [10000, 329, 9923, 457, 12, 657, 68, 839, 54921, 436, 2849, 720, 3, 355]
    A5 = [4321, 399, 28, 5]
    A6 = [5, 10, 7, 2, 3, 1, 4, 9, 8, 6]
    A7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    A8 = [2, 4, 6, 8, 10, 12]
    A9 = [1, 3, 5, 7, 9, 11]
    A10 = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]

    #  Test for the simultaneous minimum and maximum algorithm in P214.
    print("Test for the simultaneous minimum and maximum algorithm in P214: ", min_max(A3), '\n')
    #  Test for recursive select in P216.
    print("Test for recursive select in P216: ", select_recur(A2[:], 0, len(A2) - 1, 5))
    #  Test for iterative select in 9.2-3 P219.
    print("Test for iterative select in 9.2-3 P219: ", select_iter(A2[:], 5), '\n')
    #  Test for the k-quantiles in 9.3-6 P223.
    print("Test for the k-quantiles in 9.3-6 P223: ", kquantiles(A7[:], 0, len(A7) - 1, 5), '\n')
    #  Test for the k closest elements to median in 9.3-7 P223.
    print("Test for the k closest to median func in 9.3-7 P223: ", kclosest(A6[:], 4), '\n')
    #  Test for find the median in X & Y in 9.3-8 P223.
    print("Test for find the median in X & Y in 9.3-8 P223: ", get_median( A8, 0, len(A8) - 1, A9, 0, len(A9) - 1 ), '\n')
    #  Test for the weighted median in problems 9-2 P225.
    print("Test for the weighted median in problems 9-2 P225: ", weighted_median(A10, 0, len(A10) - 1, 0.5, 0.5), '\n')