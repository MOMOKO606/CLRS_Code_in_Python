from functools import reduce

"""
The classic iterative insertion sort(in place).
Input @para:list A, order represents increasing or decreasing order of the output.
            the default order = "increasing".
Output: the sorted list A.
"""
def insertion_sort( A, order = "increasing" ):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while(j >= 0 and key < A[j]):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    if order == "increasing":
        return A
    elif order == "decreasing":
        return A[-1: :-1]
    else:
        print("order = either 'increasing' or 'decreasing'.")


"""
The recursive insertion sort.
Input @para:list A.
Output: the sorted list A.
"""
def insertionsort_recur_aux( A ):

    """
    The subfunction insertion used in insertion_sort_recur.
    Input @para: list A and index end, meaning insert A[end] into the sorted A[0, ... ,end - 1]
    Output: the sorted A[0, ... ,end]
    """
    def insertion( A, end ):
        key = A[end]
        j = end - 1
        while( key < A[j] and j >= 0):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
        return A


    """
    The recursive insertion sort.
    The idea is, to sort A[0, ... ,end] means insert A[end] into the sorted A[0, ... ,end - 1]
    Input @para: list A and index end.
    Output: the sorted A[0, ... ,end]
    """
    def insertion_sort_recur(A, end):
        if end == 0:
            return
        insertion_sort_recur(A, end - 1)
        insertion(A, end)
        return A

    return insertion_sort_recur( A, len(A) - 1 )


"""
The classic selection sort(in place).
Input @para:list A
Output: the sorted list A.
"""
def selection_sort( A ):
    n = len(A)
    # The outer loop which determines one min element at a time.
    for i in range( n - 1 ):
        #  Initialize the minimum value and its index.
        minimum = A[i]
        k = i
        #  The inner loop for searching the min element.
        for j in range(i + 1, n):
            if A[j] < minimum:
                minimum = A[j]
                k = j
        A[k] = A[i]
        A[i] = minimum
    return A


"""
Exchange the value of x and y.
Input @para: x & y of a single number respectively. 
Output: the exchanged x and y.
"""
def exchange(x, y):
    x = x + y  # put the sum of x and y in x.
    y = x - y  # sum - y = x - y = the original x, and put it in y.
    x = x - y  # now x = sum, y = the original x, so sum - y = x - y = the original y, and put it in x.
    return x, y


"""
Bubble sort from problems 2-2 in P40.
Input @para: list A.
Output: the sorted A.
"""
def bubble_sort( A ):
    n = len(A)
    #  Outer loop determines the min elements in the A[0], A[1], ..., A[n - 1] order.
    for i in range(n - 1):
        #  Inner loop, the bubble processing.
        for j in range( n - 1, i, -1):
            if A[j] < A[j - 1]:
                #  Swap A[j - 1] and A[j].
                A[j - 1], A[j] = exchange(A[j - 1], A[j])
                #  Pythonic way for swapping.
                # (A[j - 1], A[j]) = (A[j], A[j - 1])
    return A


"""
The classic mergesort.
Input @para: list A.
Output: A in sorted order.
"""
def mergesort_aux(A):

    """
    The merge function  with sentinels used in mergesort.
    Input @param: list A, index low, mid and high to form A[low,..., mid] & A[mid + 1,..., high].
    Output: the sorted A[low,..., high]
    """
    def merge(A, low, mid, high):

        #  Construct L and R lists.
        L = [A[i] for i in range(low, mid + 1)]
        R = [A[i] for i in range(mid + 1, high + 1)]

        #  Set sentinels to L & R.
        L.append(float("inf"))
        R.append(float("inf"))

        #  Merging.
        i = j = 0
        for k in range(low, high + 1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
        return A

    """
        Exercise 2.3-2 in P37.
        The merge function  without sentinels used in mergesort.
        Input @param: list A, index low, mid and high to form A[low,..., mid] & A[mid + 1,..., high].
        Output: the sorted A[low,..., high]
        """
    def merge_beta(A, low, mid, high):

        #  Construct L and R lists.
        L = [A[i] for i in range(low, mid + 1)]
        R = [A[i] for i in range(mid + 1, high + 1)]

        #  Get n1 & n2.
        n1 = len(L)
        n2 = len(R)

        #  Merging.
        i = j = 0
        for k in range(low, high + 1):
            #  Run out of L.
            if i > n1 - 1 and j < n2:
                A[k] = R[j]
                j = j + 1
            #  Run out of R.
            elif i < n1 and j > n2 - 1:
                A[k] = L[i]
                i = i + 1
            #  Find the smaller element in l & R and put it in A.
            elif L[i] <= R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
        return A

    """
    The recursive mergesort.
    Input @param: list A, index low and high.
    Output: the sorted A[low,..., high] 
    """
    def mergesort(A, low, high):
        #  Base case means low >= high
        if low < high:
            mid = (low + high) // 2
            #  Divide.
            mergesort(A, low, mid)
            mergesort(A, mid + 1, high)
            #  Conquer.
            merge(A, low, mid, high)
            return A

    """
    Problems 2-1, P39.
    Mergesort with k minimum length of the divided segments.
    Input @param: list A, index low and high, k = the minimum length of the divided segments.
                  the default k = 5
    Output: the sorted A[low,..., high] 
    """
    def mergesort_beta( A, low, high, k = 5 ):

        #  Base case
        #  When high - low + 1 <= k stopping divide A[low,...,high]
        if high - low + 1 <= k:
            #  Using insertion sort to sort A[low,...,high] instead.
            tmp = A[low : high + 1]
            tmp = insertion_sort(tmp)
            #  Put the sorted part back to A.
            for i in range(low, high + 1):
                A[i] = tmp[i - low]
            return A
        mid = (low + high) // 2
        #  Divide.
        mergesort_beta( A, low, mid )
        mergesort_beta( A, mid + 1, high )
        #  Conquer.
        merge(A, low, mid, high)
        return A

    # return mergesort( A, 0, len(A) - 1 )
    return mergesort_beta( A, 0, len(A) - 1 )


"""
The classic linear search.
Input @para:list A, 
            the element "key" which wants to be found in A.
Output: index of key in A or None if there isn't any key in A.
"""
def linear_search( A, key ):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return None
    #  Pythonic version code
    # return [i  for i in range(len(A)) if A[i] == key ]


"""
The recursive binary search.
Input @para:the sorted list A and its indices low and high, A[low, ..., high].
            the element "key" which wants to be found in A.
Output: index of key in A or None if there isn't any key in A.
"""
def binary_search_recur( A, key, low, high ):

    #  Base case 1, cannot find the key in list A.
    if low > high:
        return None
    mid = (low + high) // 2

    #  Base case 2, find the key and return its index.
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binary_search_recur(A, key, low, mid - 1)
    else:
        return binary_search_recur(A, key, mid + 1, high)


"""
The iterative binary search.
Input @para:the sorted list A,
            the element "key" which wants to be found in A.
Output: index of key in A or None if there isn't any key in A.
"""
def binary_search_iter( A, key ):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


"""
Add two binary numbers in list form.
Input @para:list x, list y represent two binary numbers, they can be different in length.
Output: x + y in binary in list form.
"""
def binary_add( x, y ):

    #  Supplement 0 to the short binary number from the left.
    n1 = len(x)
    n2 = len(y)
    delta = abs(n1 - n2)
    if n1 > n2:
        y = [0 for i in range(delta)] + y
        n = n1
    elif n1 < n2:
        x = [0 for i in range(delta)] + x
        n = n2

    #  Initialize carry and the output list.
    carry = 0
    result = [0] * (n + 1)
    #  Computing
    for i in range(n, 0, -1):
        tmp = x[i - 1] + y[i - 1] + carry
        if tmp > 1:
            carry = 1
        else:
            carry = 0
        result[i] = tmp % 2
    # Don't forget the carry.
    result[0] = carry
    return result


"""
Compute the polynomial equation: 
para[0] + para[1] * x + para[2] * x^2 + ... + para[n - 1] * x^n-1
Input @para: list para and x
Output: the result of the polynomial equation.
"""
def polynomial( para, x ):
    sum = 0
    x_iter = 1 / x
    for i in range( len(para) ):
        x_iter = x_iter * x
        sum = sum + para[i] * x_iter
    return sum


"""
Horner's rule for computing the polynomial equation: 
a[0] + a[1] * x + a[2] * x^2 + ... + a[n - 1] * x^n-1
Input @para: list a and x
Output: the result of the polynomial equation.
"""
def polynomial_Horner( a, x ):
    sum = a[-1]  # a[n - 1]
    for i in range( len(a) - 1, 0, -1 ):
        # a[n - 2] + a[n - 1] * x
        sum = a[i - 1] + sum * x
    return sum


"""
Closure form code of Horner's rule for computing the polynomial equation.
Input @para: a single number x.
Output: function para_of which requires the coefficient list a as its put.
"""
def poly_equa(x):
    """
    Input @para: the coefficient list a of the polynomial equation.
    Output: the result of the polynomial equation.
    """

    def para_of(a):
        sum = a[-1]
        for i in range(len(a) - 1, 0, -1):
            # a[n - 2] + a[n - 1] * x
            sum = a[i - 1] + sum * x
        return sum

    #  When you return a function, don't write () after the function name.
    return para_of


"""
A Pythonic with closure code of Horner's rule for computing the polynomial equation.
Input @para: a single number x.
Output: function para_of which requires the two coefficients  as its put.
"""
def poly_equa_beta(x):

    """
    Input @para: two coefficients a2 and a1.
    Output: the result of the equation a1 + a2 * x.
    """
    def para_of(a2, a1):
        return a1 + a2 * x

    #  When you return a function, don't write () after the function name.
    return para_of

if __name__ == '__main__':
    A = [5, 9, 8, 2, 13, 4, 6, 7, 10, 1, 3, 0, 11, 12]
    A1 = [0, 1, 2, 3]
    binaryX = [1, 1, 1]
    binaryY = [1]

    #  Test for insertion sort in P18.
    print("Test for insertion sort in P18:", insertion_sort(A[:]), '\n')  # Copy A for not changing the origin A list.

    #  Test for linear search in P22.
    print("Test for linear search in P22:", linear_search(A, 1), '\n')

    #  Test for binary addition in P22.
    print("Test for binary addition in P22:", binary_add( binaryY, binaryX ), '\n')

    #  Test for selection sort in P29.
    print("Test for selection sort in P29:", selection_sort( A[:] ), '\n')

    #  Test for mergesort in P34.
    print("Test for mergesort in P34:", mergesort_aux( A[:] ), '\n')

    #  Test for recursive insertion sort in P39.
    print("Test for recursive insertion sort in P39:", insertionsort_recur_aux( A[:] ), '\n')

    #  Test for recursive binary search in P39.
    B = mergesort_aux( A[:] )
    print("Test for recursive binary search in P39:", binary_search_recur( B, 13, 0, len(B) - 1 ))
    #  Test for iterative binary search in P39.
    print("Test for iterative binary search in P39:", binary_search_iter( B, 13 ), '\n')

    #  Test for bubble sort in P40.
    print("Test for bubble sort in P40:", bubble_sort( A[:]), '\n')

    #  Test for polynomial equation in P41.
    print("Test for polynomial equation in P41:", polynomial( A1, 2 ), '\n')

    #  Test for polynomial equation(Horner's rule) in P41.
    print("Test for polynomial equation(Horner's rule) in P41:", polynomial_Horner( A1, 2 ))

    #  The Pythonic way of Horner's rule.
    print("The pythonic way: ", reduce(lambda a2, a1, x=2: a1 + a2 * x, A1[-1:: -1]))

    #  The closure way of Horner's rule.
    polynomial_equation = poly_equa(2)  # Set x = 2
    print("The closure way of Horner's rule:", polynomial_equation( A1 ))

    #  A more Pythonic way with closure of Horner's rule.
    polynomial_equation = poly_equa_beta(2)  # Set x = 2.
    print( "A more Pythonic way with closure of Horner's rule:", reduce( polynomial_equation, A1[-1:: -1] ), '\n' )
