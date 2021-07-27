import math

"""
Min heap for list of key-value tuples.
e.g. list A = [(key1, value1), (key2, value2), ...]
"""
class MinHeap4dict:

    def __init__( self, list_A = [] ):

        self.__heap_size = len(list_A)
        self.__heap_A = list_A

        if self.__heap_size > 0:
            A = MinHeap4dict.build_min_heap( self )


    """
    Get the parent index of index i in a heap.
    Input @para: index i.
    Output i's parent index.
    """
    def parent( self, i ):
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
    def left( self, i ):
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
    def right(self, i):
        #  i << 1 equals to i * 2
        #  << is bit operation which means move x digit(s) to the left.
        #  i << 1 will first transfer i to binary format, then move one digit to the left.
        # "move one digit to the left" means "i * 2".
        # "move n digits to the right" means "i * 2 ^ n", e.g. 1 << 10 is 1024.
        return i + 1 << 1


    """
    The recursive version of min_heapify.
    Make sure that all the nodes in the subtree rooted at A[i] obey the min heap rule.
    Start from node A[i], check A[left(i)] and A[right(i)], 
    Tha value of the parent node must be smaller than the value of its children nodes. 
    Input @para: list A and node index i.
    Output @para: the maximum heapified list A from A[i].
    """
    def min_heapify( self, A, i ):

        #  Get the initialized heap size.
        heap_size = self.__heap_size

        #  Set sentinel
        if i >= math.ceil(heap_size / 2):
            return A

        left_index = self.left(i)
        right_index = self.right(i)

        #  Find the smallest index in i, left_index and right_index
        if left_index < heap_size and A[left_index][0] < A[i][0]:
            smallest = left_index
        else:
            smallest = i

        if right_index < heap_size and A[right_index][0] < A[smallest][0]:
            smallest = right_index

        #  Fix the node that doesn't obey to heap rule.
        if smallest != i:
            A[smallest], A[i] =  A[i], A[smallest]

            #  recursively check the nodes below.
            self.min_heapify( A, smallest )

        return A


    """
    Build a min heap from list A.
    Input @para: 
    Output @para: the min heap A.
    """
    def build_min_heap( self ):

        #  Get the initialized heap A.
        A = self.__heap_A

        #  Build the min heap in a decreasing order.
        for i in range(math.ceil(self.__heap_size / 2), -1, -1):
            A = self.min_heapify( A, i )

        #  Return the new heap.
        return A


    """
    Heapsort
    Input @para:
    Output @para: the sorted A.
    """
    def heapsort( self ):

        #  Initializing
        heap_size = self.__heap_size
        A = self.__heap_A

        #  Exchange the smallest element with the last element in the heap.
        for i in range(heap_size - 1, 0, -1):
            A[0], A[i] = A[i], A[0]

            #  Decreasing the heap size and update.
            heap_size = heap_size - 1
            self.__heap_size = heap_size

            #  Max heapify from the root.
            self.min_heapify( A, 0 )

        #  Update parameters
        self.__heap_A = []
        self.__heap_size = 0

        return A[-1: :-1]


    """
    Get the minimum element in heap A.
    Input @para: 
    Output @para: the minimum element in A (= the root of heap A).
    """
    def min_node( self ):

        #  Load parameters
        A = self.__heap_A
        heap_size = self.__heap_size

        #  Sentinel.
        assert self.__heap_size > 0, "heap is empty."
        #  return the root.
        return A[0]


    """
    Change the key of one node in the min heap A.
    Input @para: heap A, index i of the node, key of the node, heap_size 
    Output @para: the new heap A after A[i] changed to key.
    """
    def change_key( self, i, key ):

        #  Load parameters.
        heap_size = self.__heap_size
        A = self.__heap_A
        value = A[i][1]

        #  Decrease key.
        if key <= A[i][0]:

            #  Bottom-top fixing.
            while i > 0 and A[self.parent(i)][0] > key:
                A[i] = A[self.parent(i)]
                #  Update the index.
                i = self.parent(i)

            #  We replace A[i] since tuple is unchangeable.
            A[i] = (key, value)

        else:  # Increase key

            A[i] = (key, value)
            #  Top-bottom fixing.
            A = self.min_heapify( A, i )

        return A


    """
    Insert a new element x into the min heap A.
    Input @para: heap A, element x, heap_size 
    Output @para: the new heap A after x inserted.
    """
    def insert_node( self, key, value ):

        #  Load parameters.
        heap_size = self.__heap_size
        A = self.__heap_A

        #  Add a new element in the end.
        heap_size = heap_size + 1
        A.append((float("inf"), value))

        #  Adjust the added element through its key.
        self.change_key( heap_size - 1, key )

        #  Update parameters
        self.__heap_A = A
        self.__heap_size = heap_size

        return A


    """
    Extract the minimum element in max heap A.
    Input @para: 
    Output @para: the new heap A after extracted the max element.
    """
    def extract( self ):

        #  Load parameters.
        heap_size = self.__heap_size
        A = self.__heap_A

        #  Sentinel
        assert (heap_size > 0), "It is a empty heap."

        #  Extract the minimum element.
        min_key = A[0]

        #  Update the min heap.
        #  Exchange the minimum element with the last element in the heap,
        #  then pop the minimum element.
        A[0], A[heap_size - 1] = A[heap_size - 1], A[0]

        #  Decrease heap size by 1
        heap_size = heap_size - 1
        #  Update heap size
        self.__heap_size = heap_size

        #  Screening all elements to satisfied the max heap rule.
        A = self.min_heapify( A, 0 )

        #  Update
        self.__heap_A = A[:heap_size:]

        return A[:heap_size:]


    """
    Delete the ith node in the min heap A.
    Input @para: index i of the node.
    Output @para: the new heap A after deleted node A[i].
    """
    def delete( self, i ):

        #  Load parameters.
        heap_size = self.__heap_size
        A = self.__heap_A

        #  Sentinel.
        assert i < heap_size and i >= 0, "illegal index!"

        #  Exchange A[i] with A[heap_size - 1], then pop the last node.
        A[i], A[heap_size - 1] = A[heap_size - 1], A[i]

        #  Update heap.
        heap_size = heap_size - 1
        self.__heap_size = heap_size
        A = self.min_heapify( A, i )

        #  Update parameters
        self.__heap_A = A[:heap_size:]


        return A[:heap_size:]


    """
    The print function of the instance of MaxHeap class.
    """
    def __str__( self ):
        return str( self.__heap_A )


"""
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
    A = MinHeap4dict()
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
        result.append( tmp )

        #  Update the heap.
        A.extract()  #  Extract the min node.
        #  If the i list does not meet the sentinel, insert the next node in i list.
        if j + 1 <= max_cols -1 and matrix[i][j][0] < float("inf"):
            A.insert_node(matrix[i][j + 1][0], matrix[i][j + 1][1])

    return result


if __name__ == '__main__':

    matrix = [[3, 9, 11], [7], [5, 8], [1, 4, 6, 10]]

    print(sort_klists(matrix, 10))







