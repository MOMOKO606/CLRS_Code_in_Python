import math
import MaxHeap as maxh
import MinHeap as minh
import MinHeap4dict as mh4d

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
Input @para: list A, node index i and heap size.
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
Input @para: list A, node index i and heap size.
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
Input @para: list A，node index i and heap size.
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
Change the key of one node in the max heap A.
Input @para: heap A, index i of the node, key of the node, heap_size 
Output @para: the new heap A after A[i] changed to key.
"""
def heap_change_key_beta( A, i, key, heap_size ):

    #  Decrease key.
    if key <= A[i]:

        A[i] = key
        #  Top-bottom fixing.
        max_heapify(A, i, heap_size)

    else:  #  Increase key

        while i > 0 and A[parent(i)] < key:
            A[i] = A[parent(i)]
            #  Update the index.
            i = parent(i)

        A[i] = key

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


"""
Delete the ith node in the max heap A.
Input @para: heap A, index i of the node, heap_size 
Output @para: the new heap A after deleted node A[i].
"""
def delete_max_heap( A, i, heap_size):

    #  Sentinel.
    assert i < heap_size and i >=0, "illegal index!"

    #  Exchange A[i] with A[heap_size - 1], then pop the last node.
    A[i], A[heap_size - 1] = A[heap_size - 1], A[i]

    #  Update heap.
    heap_size = heap_size - 1
    max_heapify(A, i, heap_size)

    return A[ :heap_size: ]


"""
Merge k sorted lists using a minimum heap.
Input @para: matrix = 2-D lists of the k sorted lists, n = number of elements in the k sorted lists.
Output @para: the sorted list of the n elements.
"""
def sort_klists( matrix, n ):

    #  Get the k (= number of lists).
    k = len( matrix )
    #  Get the maximum columns.
    max_cols = max([len(matrix[i]) for i in range(k)])

    #  Change the matrix into a k * max_cols matrix.
    #  Each element changes from key to (key, 10*indexi + indexj).
    #  fill the empty element with (infinite, 10*indexi + indexj).
    for i in range(k):
        for j in range( max_cols ):
            if j >= len(matrix[i]):
                matrix[i].append( (float("inf"), 10 * i + j) )
            else:
                matrix[i][j] = (matrix[i][j], 10 * i + j)

    #  Initializing the heap by creating an empty maximum heap.
    A = mh4d.MinHeap4dict()
    for i in range(k):
        A.insert_node( matrix[i][0][0], matrix[i][0][1])

    #  Get the smallest element from the heap once a time.
    result = []
    for k in range(n):

        #  Get the pointer.
        tmp = A.min_node()
        i = tmp[1] // 10
        j = tmp[1] - i * 10

        #  Put the smallest node into the result.
        result.append( tmp[0] )

        #  Update the heap.
        A.extract()  #  Extract the min node.
        #  If the i list does not meet the sentinel, insert the next node in i list.
        if j + 1 <= max_cols -1 and matrix[i][j][0] < float("inf"):
            A.insert_node(matrix[i][j + 1][0], matrix[i][j + 1][1])

    return result


"""
Start youngify from Y[i][j] in a young tableau. 
From left-top to right-bottom.
(The value of Y[i][j] maybe changed, so we want to make sure all the elements in Y obey young tableau's rule.)
Input @para: young tableau Y, start position i & j.
Output @para: the new young tableau after youngify starts from Y[i][j].
"""
def youngify_iter( Y, i, j ):

    #  Get the size of Y.
    m = len(Y)
    n = len(Y[0])

    while i < m - 1 or j < n - 1:

        if i + 1 < m and Y[i + 1][j] < Y[i][j]:
            smallesti = i + 1
            smallestj = j
        else:
            smallesti = i
            smallestj = j

        if j + 1 < n and Y[i][j + 1] < Y[smallesti][smallestj]:
            smallesti = i
            smallestj = j + 1

        if smallestj != j or smallesti != i:
            Y[smallesti][smallestj], Y[i][j] = Y[i][j], Y[smallesti][smallestj]
            i = smallesti
            j = smallestj
        else: return Y

    return Y


"""
Start youngify recursively from Y[i][j] in a young tableau. 
From left-top to right-bottom.
(The value of Y[i][j] maybe changed, so we want to make sure all the elements in Y obey young tableau's rule.)
Input @para: young tableau Y, start position i & j, m * n is the size of Y.
Output @para: the new young tableau after youngify starts from Y[i][j].
"""
def youngify( Y, i, j, m, n ):

    #  Base case, reach the end of Y.
    if i == m and j == n:
        return Y

    if i + 1 < m and Y[i + 1][j] < Y[i][j]:
        smallesti = i + 1
        smallestj = j
    else:
        smallesti = i
        smallestj = j

    if j + 1 < n and Y[i][j + 1] < Y[smallesti][smallestj]:
        smallesti = i
        smallestj = j + 1

    if smallestj != j or smallesti != i:
        Y[smallesti][smallestj], Y[i][j] = Y[i][j], Y[smallesti][smallestj]
        Y = youngify( Y, smallesti, smallestj, m, n )

    return Y


"""
Start youngify reversely, recursively from Y[i][j] in a young tableau. 
From right-bottom to left-top.
(The value of Y[i][j] maybe changed, so we want to make sure all the elements in Y obey young tableau's rule.)
Input @para: young tableau Y, start position i & j, m * n is the size of Y.
Output @para: the new young tableau after youngify starts from Y[i][j].
"""
def youngify_reverse( Y, i, j ):

    #  Base case, reach the start of Y.
    if i == 0 and j == 0:
        return Y

    if i - 1 >= 0 and Y[i - 1][j] > Y[i][j]:
        largesti = i - 1
        largestj = j
    else:
        largesti = i
        largestj = j

    if j - 1 >= 0 and Y[i][j - 1] > Y[largesti][largestj]:
        largesti = i
        largestj = j - 1

    if largestj != j or largesti != i:
        Y[largesti][largestj], Y[i][j] = Y[i][j], Y[largesti][largestj]
        Y = youngify_reverse( Y, largesti, largestj )

    return Y


"""
Extract the minimum element from a young tableau Y, then replace the minimum element of inf and fix Y.
Input @para: young tableau Y.
Output @para: the minimum element of Y.
"""
def extract_min_yt( Y ):

    #  Get the size of Y.
    m = len(Y)
    n = len(Y[0])

    #  Get the minimum element in Y.
    min_element = Y[0][0]
    Y[0][0] = float("inf")

    #  Fix the young tableau Y.
    # Y = youngify_iter( Y, 0, 0 )
    Y = youngify(Y, 0, 0, m, n)

    return min_element


"""
Insert a element with the value of key into the right-bottom end position.
Input @para: young tableau Y, key value.
Output @para: young tableau Y after inserted key.
"""
def insert_yt( Y, key ):

    #  Get the size of Y.
    m = len(Y)
    n = len(Y[0])

    #  Insert key to the last element of the young tableau Y.
    Y[m - 1][n - 1] = key

    #  Fix the young tableau Y.
    Y = youngify_reverse( Y, m - 1, n - 1 )

    return Y






if __name__ == '__main__':
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    A1 = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    A2 = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]       #  A2 is a max heap.
    A3 = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]  #  A3 is a max heap.
    A4 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    A5 = [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]  # A5 is a min heap.
    matrix = [[3, 9, 11], [7], [5, 8], [1, 4, 6, 10]]  #  matrix contains k sorted lists.
    #  young tableau
    Y1 = [[2, 8, 10, 12], [7, 9, 11, 13], [16, float("inf"), float("inf"), float("inf")]]
    Y2 = [[2, 4, 9, float("inf")], [3, 8, 16, float("inf")], [5, 14, float("inf"), float("inf")], [12, float("inf"), float("inf"), float("inf")]]


    #  Test for the max_heapify in P154.
    print("Test for the max_heapify in P154:", max_heapify( A[:], 2, len(A) ))

    #  Test for the iterative max_heapify in P156.
    print("Test for the iterative max_heapify in P156:", max_heapify(A[:], 2, len(A)), '\n' )

    #  Test for build a max heap (6.3-1) in P159.
    print("Test for build a max heap (6.3-1) in P159:", build_max_heap( A1[:] ), '\n')

    #  Test for heapsort in P160.
    print("Test for heapsort in P160:", heapsort( A2[:] ), '\n')

    #  Test for extracting max heap in P162.
    print("Test for extracting max heap in P162:", extract_max_heap( A3[:], len(A3) ), '\n')

    #  Test for changing a key in a max heap in P162.
    print("Test for changing a key in a max heap in P162:", heap_change_key( A2[:], 1, 5, len(A2) ), '\n')

    #  Test for changing a key in a max heap in 6.5-6 P166.
    print("Test for changing a key in a max heap in 6.5-6 P166:", heap_change_key_beta(A2[:], 1, 5, len(A2)), '\n')

    #  Test for heap insert in P162.
    print("Test for heap insert in P162:", max_heap_insert( A3[:], 10, len(A3) ), '\n')

    #  Test for deleting a key in a max heap in 6.5-8 P166.
    print("Test for deleting a key in a max heap in 6.5-8 P166:", delete_max_heap( A3[:], 0, len(A3)), '\n')

    #  Test for the MaxHeap class.
    #  Create a instance of class MaxHeap
    #  equals to transfer list A into a max heap
    heap_x = maxh.MaxHeap(A4)
    heap_y = maxh.MaxHeap(A2)
    heap_z = maxh.MaxHeap(A3)

    #  Test for printing the max heap A.
    print("Test for printing the max heap A4: ", heap_x, '\n')
    print("Test for getting the max node in the max heap A4: ", heap_x.max_node(), '\n')

    #  Test for heapsort function.
    print("Test for heapsort: ", heap_x.heapsort(), '\n')

    #  Test for changing a key in the max heap A2
    print("Test for changing a key in the max heap A2: ", heap_y.change_key(1, 5), '\n')

    #  Test for deleting a key in a max heap in 6.5-8 P166.
    print("Test for deleting a key in a max heap in 6.5-8 P166:", heap_z.delete(0), '\n')

    #  Test for the MinHeap class.
    #  Create a instance of class MinHeap
    #  equals to transfer list A into a min heap
    heap_q = minh.MinHeap(A5)

    #  Test for changing a key in the min heap A5.
    print("Test for changing a key in the min heap A5: ", heap_q.change_key(1, 5), '\n')

    #  Test for deleting a key in the min heap A5.
    print("Test for deleting a key in the min heap A5:", heap_q.delete(0), '\n')

    #   Test for sorting k sorted lists 6.5-9 P166.
    print("Test for sorting k sorted lists  6.5-9 P166:", sort_klists(matrix, 10), '\n')

    #   Test for young tableau in problems 6-3 P168.
    print("Test for extract function in young tableau in problems 6-3 P168:", extract_min_yt( Y1 ))
    print("Test for young tableau in problems 6-3 P168:", Y1, '\n')
    print("Test for insert function in young tableau in problems 6-3 P168:", insert_yt( Y2, 10 ), '\n' )


