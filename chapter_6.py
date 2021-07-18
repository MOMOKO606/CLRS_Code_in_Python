import math

"""
Get the parent index of index i in a heap.
Input @para: index i.
Output i's parent index.
"""
def parent( i ):
    #  i >> 1 equals to i // 2
    #  >> is bit operation which means move x digit(s) to the right.
    #  i >> 1 will first transfer i to binary format, then move one digit to the right.
    # "move one digit to the right" means "i // 2".
    # "move n digits to the right" means "i // 2 ^ n", e.g. 1024 >> 10 is 1.
    return i - 1 >> 1

"""
Get the left child index of index i in a heap.
Input @para: index i.
Output i's left index.
"""
def left( i ):
    #  i << 1 equals to i * 2
    #  << is bit operation which means move x digit(s) to the left.
    #  i << 1 will first transfer i to binary format, then move one digit to the left.
    # "move one digit to the left" means "i * 2".
    # "move n digits to the right" means "i * 2 ^ n", e.g. 1 << 10 is 1024.
    return (i << 1) + 1

"""
Get the right child index of index i in a heap.
Input @para: index i.
Output i's right index.
"""
def right( i ):
    #  i << 1 equals to i * 2
    #  << is bit operation which means move x digit(s) to the left.
    #  i << 1 will first transfer i to binary format, then move one digit to the left.
    # "move one digit to the left" means "i * 2".
    # "move n digits to the right" means "i * 2 ^ n", e.g. 1 << 10 is 1024.
    return i + 1 << 1

"""
Exchange the value of x and y without using additional variables.
Input @para: x, y.
Output @para: the exchanged x, y.
"""
def exchange( x, y ):
    x = x + y  # now x = the sum of x & y
    y = x - y  # now y = sum - y = the original x
    x = x - y  # now x = sum - y = sum - the original x = the original y
    return x, y


"""
The recursive version of max_heapify.
Make sure that all the nodes in the subtree rooted at A[i] obey the max heap rule.
Start from node A[i], check A[left(i)] and A[right(i)], 
Tha value of the parent node must be larger than the value of its children nodes. 
Input @para: list A and node index i.
Output @para: the maximum heapified list A from A[i].
"""
def max_heapify( A, i ):

    n = len(A)
    #  Set sentinel
    if i >= math.ceil(n / 2):
        return A

    left_index = left(i)
    right_index = right(i)

    #  Find the largest index in i, left_index and right_index
    if left_index < n and A[left_index] > A[i]:
        largest = left_index
    else: largest = i

    if right_index < n and A[right_index] > A[largest]:
        largest = right_index

    #  Fix the node that doesn't obey to heap rule.
    if largest != i:
        #  the pythonic way is A[largest], A[i] =  A[i], A[largest]
        A[largest], A[i] = exchange( A[largest], A[i] )
        #  recursively check the nodes below.
        max_heapify(A, largest)
        return A


"""
Make sure that all the nodes in the subtree rooted at A[i] obey the min heap rule.
Start from node A[i], check A[left(i)] and A[right(i)], 
Tha value of the parent node must be smaller than the value of its children nodes. 
Input @para: list A and node index i.
Output @para: the minimum heapified list A from A[i].
"""
def min_heapify( A, i ):

    n = len(A)
    #  Set sentinel
    if i >= math.ceil(n / 2):
        return A
    left_index = left(i)
    right_index = right(i)

    #  Find the smallest index in i, left_index and right_index
    if left_index < n and A[left_index] < A[i]:
        smallest = left_index
    else: smallest = i

    if right_index < n and A[right_index] < A[smallest]:
        smallest = right_index

    #  Fix the node that doesn't obey to heap rule.
    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        #  recursively check the nodes below.
        min_heapify( A, smallest )
        return A


"""
The iterative version of max_heapify in 6.2-5.
Make sure that all the nodes in the subtree rooted at A[i] obey the max heap rule.
Start from node A[i], check A[left(i)] and A[right(i)], 
Tha value of the parent node must be larger than the value of its children nodes. 
Input @para: list A and node index i.
Output @para: the maximum heapified list A from A[i].
"""
def max_heapify_iter( A, i ):

    n = len(A)

    #  while condition: it's a inner node, not a leaf.
    while i < math.ceil(n / 2):
        left_index = left(i)
        right_index = right(i)

        #  Find the largest index in i, left_index and right_index
        if left_index < n and A[left_index] > A[i]:
            largest = left_index
        else:
            largest = i

        if right_index < n and A[right_index] > A[largest]:
            largest = right_index

        if largest != i:
            #  the pythonic way is A[largest], A[i] =  A[i], A[largest]
            A[largest], A[i] = exchange(A[largest], A[i])
            i = largest
        #  Break the loop if all nodes satisfied the max heap rule.
        else: break
    return A



if __name__ == '__main__':
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

    #  Test for the max_heapify in P154.
    print("Test for the max_heapify in P154:", max_heapify( A[:], 2 ) )
    #  Test for the iterative max_heapify in P156.
    print("Test for the iterative max_heapify in P156:", max_heapify(A[:], 2), '\n' )