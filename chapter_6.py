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
def max_heapify( A, i, heap_size ):

    #  Set sentinel
    if i >= math.ceil( heap_size / 2 ):
        return A

    left_index = left(i)
    right_index = right(i)

    #  Find the largest index in i, left_index and right_index
    if left_index < heap_size and A[left_index] > A[i]:
        largest = left_index
    else: largest = i

    if right_index < heap_size and A[right_index] > A[largest]:
        largest = right_index

    #  Fix the node that doesn't obey to heap rule.
    if largest != i:
        #  the pythonic way is A[largest], A[i] =  A[i], A[largest]
        A[largest], A[i] = exchange( A[largest], A[i] )
        #  recursively check the nodes below.
        max_heapify(A, largest, heap_size)
        return A


"""
Make sure that all the nodes in the subtree rooted at A[i] obey the min heap rule.
Start from node A[i], check A[left(i)] and A[right(i)], 
Tha value of the parent node must be smaller than the value of its children nodes. 
Input @para: list A and node index i.
Output @para: the minimum heapified list A from A[i].
"""
def min_heapify( A, i, heap_size ):

    #  Set sentinel
    if i >= math.ceil( heap_size / 2 ):
        return A
    left_index = left(i)
    right_index = right(i)

    #  Find the smallest index in i, left_index and right_index
    if left_index < heap_size and A[left_index] < A[i]:
        smallest = left_index
    else: smallest = i

    if right_index < heap_size and A[right_index] < A[smallest]:
        smallest = right_index

    #  Fix the node that doesn't obey to heap rule.
    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        #  recursively check the nodes below.
        min_heapify( A, smallest, heap_size )
        return A


"""
The iterative version of max_heapify in 6.2-5.
Make sure that all the nodes in the subtree rooted at A[i] obey the max heap rule.
Start from node A[i], check A[left(i)] and A[right(i)], 
Tha value of the parent node must be larger than the value of its children nodes. 
Input @para: list A and node index i.
Output @para: the maximum heapified list A from A[i].
"""
def max_heapify_iter( A, i, heap_size ):

    #  while condition: it's a inner node, not a leaf.
    while i < math.ceil( heap_size / 2 ):
        left_index = left(i)
        right_index = right(i)

        #  Find the largest index in i, left_index and right_index
        if left_index < heap_size and A[left_index] > A[i]:
            largest = left_index
        else:
            largest = i

        if right_index < heap_size and A[right_index] > A[largest]:
            largest = right_index

        if largest != i:
            #  the pythonic way is A[largest], A[i] =  A[i], A[largest]
            A[largest], A[i] = exchange(A[largest], A[i])
            i = largest
        #  Break the loop if all nodes satisfied the max heap rule.
        else: break
    return A


"""
Build a max heap from list A.
Input @para: list A.
Output @para: the max heap A.
"""
def build_max_heap( A ):

    #  Build the max heap in a decreasing order.
    for i in range( math.ceil( len(A) / 2 ), -1, -1 ):
        max_heapify( A, i, len(A) )
    return A


"""
Heapsort
Input @para: list A.
Output @para: the sorted A.
"""
def heapsort( A ):

    #  Initializing
    heap_size = len( A )
    build_max_heap(A)

    #  Exchange the largest element with the last element in the heap.
    for i in range(heap_size - 1, 0 ,-1):
        A[0], A[i] = A[i], A[0]
        #  Decreasing the heap size.
        heap_size = heap_size - 1
        #  Max heapify from the root.
        max_heapify(A, 0, heap_size )

    return A


"""
Get the maximum element in heap A.
Input @para: list A.
Output @para: the maximum element in A (= the root of heap A).
"""
def heap_get_max( A ):

    #  Sentinel.
    assert len(A) > 0, "A is empty."
    #  return the root.
    return A[0]


"""
Change the key of one node in the max heap A.
Input @para: heap A, index i of the node, key of the node, heap_size 
Output @para: the new heap A after A[i] changed to key.
"""
def heap_change_key( A, i, key, heap_size ):

    #  Decrease key.
    if key <= A[i]:

        A[i] = key
        #  Top-bottom fixing.
        max_heapify(A, i, heap_size)

    else:  #  Increase key

        A[i] = key
        #  Bottom-top fixing.
        while i > 0 and A[parent(i)] < A[i]:
            A[parent(i)], A[i] = A[i], A[parent(i)]
            #  Update the index.
            i = parent(i)

    return A


"""
Insert a new element x into the max heap A.
Input @para: heap A, element x, heap_size 
Output @para: the new heap A after x inserted.
"""
def max_heap_insert( A, key, heap_size ):

    #  Add a new element in the end.
    heap_size = heap_size + 1
    A.append( float("-inf") )

    #  Adjust the added element through its key.
    heap_change_key( A, heap_size - 1, key, heap_size )

    return A


"""
Extract the maximum element in max heap A.
Input @para: heap A, heap_size 
Output @para: the new heap A after extracted the max element.
"""
def extract_max_heap( A, heap_size):

    #  Sentinel
    assert( heap_size > 0 ), "It is a empty heap."

    #  Extract the maximum element.
    max_key = A[0]

    #  Update the max heap.
    #  Exchange the maximum element with the last element in the heap,
    #  then pop the maximum element.
    A[0], A[heap_size - 1] = A[heap_size - 1], A[0]

    #  Decrease heap size by 1
    heap_size = heap_size - 1

    #  Screening all elements to satisfied the max heap rule.
    max_heapify(A, 0, heap_size)

    return A[ :heap_size: ]





if __name__ == '__main__':
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    A1 = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    A2 = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]       #  A2 is a max heap already.

    #  Test for the max_heapify in P154.
    print("Test for the max_heapify in P154:", max_heapify( A[:], 2, len(A) ))
    #  Test for the iterative max_heapify in P156.
    print("Test for the iterative max_heapify in P156:", max_heapify(A[:], 2, len(A)), '\n' )
    #  Test for build a max heap (6.3-1) in P159.
    print("Test for build a max heap (6.3-1) in P159:", build_max_heap( A1[:] ), '\n')
    #  Test for heapsort in P160.
    print("Test for heapsort in P160:", heapsort( A2[:] ), '\n')

    #  Test for extracting max heap in P162.
    print("Test for extracting max heap in P162:", extract_max_heap( A2[:], len(A2) ), '\n')
    #  Test for changing a key in a max heap  in P162.
    print("Test for changing a key in a  max heap in P162:", heap_change_key( A2[:], 1, 5, len(A2) ), '\n')
    #  Test for heap insert in P162.
    print("Test for heap insert in P162:", max_heap_insert( A2[:], 28, len(A2) ), '\n')