import math

"""
Class form of minimum heap.
"""
class MinHeap:


    def __init__( self, list_A = [] ):

        self.heap_size = len(list_A)
        self.heap_A = list_A

        if self.heap_size > 0:
            A = MinHeap.build_min_heap( self )


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
        heap_size = self.heap_size

        #  Set sentinel
        if i >= math.ceil(heap_size / 2):
            return A

        left_index = self.left(i)
        right_index = self.right(i)

        #  Find the smallest index in i, left_index and right_index
        if left_index < heap_size and A[left_index] < A[i]:
            smallest = left_index
        else:
            smallest = i

        if right_index < heap_size and A[right_index] < A[smallest]:
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
        A = self.heap_A

        #  Build the min heap in a decreasing order.
        for i in range(math.ceil(self.heap_size / 2), -1, -1):
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
        heap_size = self.heap_size
        A = self.heap_A

        #  Exchange the smallest element with the last element in the heap.
        for i in range(heap_size - 1, 0, -1):
            A[0], A[i] = A[i], A[0]

            #  Decreasing the heap size and update.
            heap_size = heap_size - 1
            self.heap_size = heap_size

            #  Max heapify from the root.
            self.min_heapify( A, 0 )

        #  Update parameters
        self.heap_A = []
        self.heap_size = 0

        return A[-1: :-1]


    """
    Get the minimum element in heap A.
    Input @para: 
    Output @para: the minimum element in A (= the root of heap A).
    """
    def min_node( self ):

        #  Load parameters
        A = self.heap_A
        heap_size = self.heap_size

        #  Sentinel.
        assert self.heap_size > 0, "heap is empty."
        #  return the root.
        return A[0]


    """
    Change the key of one node in the min heap A.
    Input @para: heap A, index i of the node, key of the node, heap_size 
    Output @para: the new heap A after A[i] changed to key.
    """
    def change_key( self, i, key ):

        #  Load parameters.
        heap_size = self.heap_size
        A = self.heap_A

        #  Decrease key.
        if key <= A[i]:

            #  Bottom-top fixing.
            while i > 0 and A[self.parent(i)] > key:
                A[i] = A[self.parent(i)]
                #  Update the index.
                i = self.parent(i)

            A[i] = key

        else:  # Increase key

            A[i] = key
            #  Top-bottom fixing.
            A = self.min_heapify( A, i )

        return A


    """
    Insert a new element x into the min heap A.
    Input @para: heap A, element x, heap_size 
    Output @para: the new heap A after x inserted.
    """
    def insert_node( self, key ):

        #  Load parameters.
        heap_size = self.heap_size
        A = self.heap_A

        #  Add a new element in the end.
        heap_size = heap_size + 1
        A.append(float("inf"))

        #  Adjust the added element through its key.
        self.change_key( heap_size - 1, key, )

        #  Update parameters
        self.heap_A = A
        self.heap_size = heap_size

        return A


    """
    Extract the minimum element in max heap A.
    Input @para: 
    Output @para: the new heap A after extracted the max element.
    """
    def extract( self ):

        #  Load parameters.
        heap_size = self.heap_size
        A = self.heap_A

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
        self.heap_size = heap_size

        #  Screening all elements to satisfied the max heap rule.
        A = self.min_heapify( A, 0 )

        #  Update
        self.heap_A = A[:heap_size:]

        return A[:heap_size:]


    """
    Delete the ith node in the min heap A.
    Input @para: index i of the node.
    Output @para: the new heap A after deleted node A[i].
    """
    def delete( self, i ):

        #  Load parameters.
        heap_size = self.heap_size
        A = self.heap_A

        #  Sentinel.
        assert i < heap_size and i >= 0, "illegal index!"

        #  Exchange A[i] with A[heap_size - 1], then pop the last node.
        A[i], A[heap_size - 1] = A[heap_size - 1], A[i]

        #  Update heap.
        heap_size = heap_size - 1
        A = self.min_heapify( A, i )

        #  Update parameters
        self.heap_A = A[:heap_size:]
        self.heap_size = heap_size

        return A[:heap_size:]


    """
    The print function of the instance of MaxHeap class.
    """
    def __str__( self ):
        return str( self.heap_A )