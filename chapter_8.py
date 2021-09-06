import random
import chapter_7
import chapter_6

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
The counting sort for matrix of letters.
We compare the values in the rth column of the input matrix.
But instead of sort the values in the rth column, we sort the entire rows.
Input: matrix A and r represents the rth column.
Output: the sorted matrix of letters.
"""
def counting_sort4letters( letter_matrix, r ):
    #  Get the rows of matrix.
    n = len(letter_matrix)
    #  Get the columns of matrix.
    d = len(letter_matrix[0])

    #  set the kth digits of the matrix as list A.
    A = [letter_matrix[i][r] for i in range(n)]

    #  Create dictionaries of ALPHABET & ALPHABET_REVERSE.
    ALPHABET = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", \
                7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", \
                14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", \
                20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z" }
    ALPHABET_REVERSE = {value:key for key, value in ALPHABET.items()}
    #  Initialize the empty auxiliary lists by size.
    C = [0] * 26
    B = [[0 for i in range(d)] for j in range(n)]

    #  counting the times each element in A appears.
    for i in range(n):
        C[ALPHABET_REVERSE[A[i]]] += 1
    #  Accumulate the counting.
    for i in range(1, 25):
        C[i] += C[i - 1]
    #  The value in C now represents the sorted position of its index.
    #  I know it's a bit silly and tricky, the indices of C now represents the original value in A.
    #  So now we go through A to check every element and its related sorted position.
    #  We go through A from right to left since we want the algorithm to be stable.
    for i in range(n - 1, -1, -1):
        B[C[ALPHABET_REVERSE[A[i]]] - 1] = letter_matrix[i]
        #  Update the index.
        C[ALPHABET_REVERSE[A[i]]] -= 1
    return B


"""
Radix sort for words of the same length.
Input: list of words of the same length d.
Output: the sorted A.
"""
def radix_sort4words( words, d ):

    #  Transfer words into matrix of letters of A.
    letter_matrix = [ list(words[i]) for i in range(len(words))]

    #  Sort every letter from right to left.
    for j in range(d - 1, -1, -1):
        letter_matrix = counting_sort4letters( letter_matrix, j )

    #  Transfer the matrix of letters into a list of strings.
    words = [''.join([letter_matrix[i][j] for j in range(d)]) for i in range(len(letter_matrix))]

    return words


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
We compare the values in the rth column of the input matrix.
But instead of sort the values in the rth column, we sort the entire rows.
Input: matrix A and r represents the rth column.
Output: the sorted matrix.
"""
def counting_sort4mat( matrix, r ):

    #  Get the rows of matrix.
    n = len(matrix)
    #  Get the columns of matrix.
    d = len(matrix[0])

    #  set the kth digits of the matrix as list A.
    A = [matrix[i][r] for i in range(n)]

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
The counting sort for matrix.
We compare the values in the rth column of the input matrix.
But instead of sort the values in the rth column, we sort the entire rows.
Input: matrix A and r represents the rth column.
Output: the sorted matrix.
"""
def counting_sort4mat_range( matrix, low, high, r ):

    n = high - low + 1
    #  Get the columns of matrix.
    d = len(matrix[0])

    #  set the kth digits of the matrix as list A.
    A = [matrix[i][r] for i in range(low, high + 1)]

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
    for i in range(high, low - 1, -1):
        B[C[A[i - low]] - 1] = matrix[i]
        #  Update the index.
        C[A[i - low]] -= 1
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


"""
Rearrange the matrix by exchanging rows with dmax digits to matrix[start, ... ,j].
matrix[j + 1, ... ,end] has smaller digits.
Input @para: 
matrix stored the number in matrix form split by digits 
The rows of the matrix are from index start to index end, so we have (end - start + 1) numbers.
dmax digits 
Output: rearranged matrix and index j.
"""
def partition_matrix( matrix, start, end, dmax ):
    #  Number of columns.
    col = len(matrix[0])
    j = start - 1
    for i in range(start, end + 1):
        if matrix[i][col - dmax] != 0:
            j += 1
            matrix[j], matrix[i] = matrix[i], matrix[j]
    return matrix, j


"""
The recursive radix sort.
Input @para: 
matrix stored the number in matrix form split by digits 
The rows of the matrix are from index start to index end, so we have (end - start + 1) numbers.
The numbers can be divided into dmax digits maximum and dmin digits minimum.
Output: matrix in decreasing order.
"""
def radix_sort_recur( matrix, start, end, dmin, dmax ):
    #  We sort the matrix from large digits to small digits.
    #  Implicit that the base case is dmin > dmax which means the end of the loop and return None
    if dmin <= dmax:
        #  Find the rows indices of number of digits dmax, and rearrange the matrix.
        #  matrix[start,...,mid] have dmax digits.
        matrix, mid = partition_matrix( matrix, start, end, dmax )
        #  Sort the matrix[start,...,mid] with dmax digits by counting sort.
        tmp1 = []
        for j in range( len(matrix[0]) - 1, len(matrix[0]) - dmax - 1, -1):
            tmp1 = counting_sort4mat_range(matrix, start, mid, j)
        #  Recursively sort the matrix[mid + 1, ... , end] with smaller digits.
        tmp2 = radix_sort_recur(matrix, mid + 1, end, dmin, dmax - 1)

        #  Change the order, put tmp1 & tmp2 together and return.
        tmp1.reverse()
        if tmp2 is None:
            return tmp1
        else:
            return tmp1 + tmp2


"""
Optimized radix sort.
Reduce the number of loops by rearrange the numbers. 
Number with the same digits should be put together.
Numbers with less digits are smaller than those with more digits.
Input: list A.
Output: the sorted A.
"""
def radix_sort_opt( A ):

    #  Find the smallest and the largest number of digits in A.
    dmin = get_d_digits(min(A))
    dmax = get_d_digits(max(A))

    #  Transfer A into matrix of digits of A.
    A_matrix = trans2digits(A, dmax)

    #  Recursively sort A_matrix from low to high digits.
    A_matrix = radix_sort_recur( A_matrix, 0, len(A_matrix) - 1, dmin, dmax )

    #  Transfer the matrix of digits to a list of integers.
    A = trans2list(A_matrix, dmax)
    A.reverse()

    return A


"""
The partition algorithm with given pivot.
Input @para: list A, the start & end index of A, the pivot.
Output @para: q & t, the list satisfies A[p, ..., q - 1] < A[q, .., t] = pivot < A[ t + 1, ..., r].
"""
def partition_by_pivot( A, p, r, pivot):
    q = p - 1
    t = p - 1
    for i in range(p, r + 1):
        if A[i] < pivot:
            q += 1
            t += 1
            A[q], A[i] = A[i], A[q]
            if q != t:
                A[t], A[i] = A[i], A[t]
        elif A[i] == pivot:
            t += 1
            A[t], A[i] = A[i], A[t]
    return q, t


"""
Problems 8-4 in P207
Suppose that you are given n red and n blue water jugs, all of different shapes and sizes. 
All red jugs hold different amounts of water, as do the blue ones. 
Moreover, for every red jug, there is a blue jug that holds the same amount of water, and vice versa.
Your task is to find a grouping of the jugs into pairs of red and blue jugs that hold the same amount of water. 
To do so, you may perform the following operation: pick a pair of jugs in which one is red and one is blue, 
fill the red jug with water, and then pour the water into the blue jug. 
This operation will tell you whether the red or the blue jug can hold more water, or that they have the same volume. 
Assume that such a comparison takes one time unit. 
Your goal is to find an algorithm that makes a minimum number of comparisons to determine the grouping. 
Remember that you may not directly compare two red jugs or two blue jugs.

Input @para: list R, its start index red_p and end index red_r. list B, its start index blue_p and end index blue_r. 
Output: the identical R & B represent the matched water jugs.
"""
def waterjugs( R, B, red_p, red_r, blue_p, blue_r ):

    #  Base case: when R & B both have 0 or 1 element we just return them.
    if red_p >= red_r:
        return R, B

    #  Randomly choose a pivot from R.
    k = random.randint(red_p, red_r)
    #  Using the pivot of R to partition the jugs in B.
    blue_q, blue_t = partition_by_pivot(B, blue_p, blue_r, R[k])
    #  Using the pivot of B to partition the jugs in R.
    red_q, red_t = partition_by_pivot(R, red_p, red_r, B[blue_t])

    #  Divide-and-conquer.
    #  Now we have matched the R[k] and B[blue_t].
    #  Then, solve the left and right subparts of R & B.
    R, B = waterjugs(R, B, red_p, red_q, blue_p, blue_q)
    R, B = waterjugs(R, B, red_t + 1, red_r, blue_t + 1, blue_r)

    return R, B


"""
K-sort in problems 8-5 in P207.
Every element satisfied A[i] <= A[i + k], O(nlg(n/k)).
Input @para: list A and k.
Output: the k-sorted A.
"""
def k_sort( A, k ):

    #  Outer loop represents k sub-arrays need to be sorted.
    for i in range(k):
        #  Get each sub-array (A[i], A[i + k], ...) and quicksort it.
        tmp = []
        for j in range(i, len(A), k):
            tmp.append(A[j])
        tmp = chapter_7.quicksort(tmp, 0, len(tmp) - 1)
        #  Put them back to their original positions in A
        for j in range(len(tmp)):
            A[i + j * k] = tmp[j]

    return A


"""
Sort a k-sorted array.
Input @para: array A that already is a k-sorted array.
Output: the sorted A.
"""
def sort_ksorted( A, k ):
    #  Rearrange k-sorted A into k lists of matrix form.
    matrix = []
    for i in range( k ):
        tmp = []
        for j in range(i, len( A ), k):
            tmp.append( A[j] )
        matrix.append( tmp )
    #  Use max-heap to merge k lists.
    A = chapter_6.sort_klists( matrix, len(A) )
    return A






#  Drive code
if __name__ == "__main__":

    #  Test data collection.
    A0 = [2, 5, 3, 0, 2, 3, 0, 3]
    A1 = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    A2 = [329, 457, 657, 839, 436, 720, 355]
    A3 = [10000, 329, 9923, 457, 12, 657, 68, 839, 54921, 436, 2849, 720, 3, 355]
    A4 = ["COW", "DOG", "SEA", "RUG","ROW", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"]
    A5 = [4321, 399, 28, 5]
    A6 = [5, 10, 7, 2, 3, 1, 4, 9, 8, 6]
    R = [7, 6, 0, 4, 8, 3, 2, 1, 5]
    B = [4, 6, 1, 2, 0, 5, 8, 3, 7]

    #  Test for the classic counting sort in P195.
    print("Test for counting sort in P195: ", counting_sort(A1[:]), '\n')
    #  Test for how many of the n integers fall into a range [a, b] of 8.2-4 in P197.
    print("Test for algorithm of 8.2-4 in P197: ", num_in_range(A0, 2, 5), '\n')
    #  Test for the classic radix sort in P198.
    print("Test for the classic radix sort in P198: ", radix_sort( A3 ), '\n')
    #  Test for the radix sort of strings in P199.
    print("Test for the radix sort of strings in P199: ", radix_sort4words( A4, 3 ), '\n')
    #  Test for the optimized radix sort.
    print("Test for the optimized radix sort: ", radix_sort_opt( A3[:] ), '\n')
    #  Test for the problems 8-4 water jugs in P206.
    print("Test for the problems 8-4 water jugs in P206: ", waterjugs( R, B, 0, len(R) - 1 , 0, len(B) - 1 ), '\n')
    #  Test for k-sort in P207.
    print("Test for k-sort in P207: ", k_sort( A6[:], 2 ), '\n')
    #  Test for sorting a k-sorted array in P207.
    print("Test for sorting a k-sorted array in P207: ", sort_ksorted( k_sort( A6[:], 2 ), 2 ), '\n')

