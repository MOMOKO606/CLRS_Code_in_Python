"""
Class form of Stack.
"""
class Stack:

    #  Initialize an empty Stack
    def __init__(self):
        self.top = -1
        self.S = []


    def stack_empty(self):
        if self.top == -1:
            return True
        else:
            return False


    def push(self, key):
        #  Load parameters.
        top = self.top
        S = self.S

        top += 1
        S.append(key)

        #  Update parameters.
        self.top = top
        self.S = S


    def pop(self):
        #  Set a sentinel.
        assert not self.stack_empty(), "error: underflow!"

        #  Load parameters.
        top = self.top
        S = self.S

        key = S[top]
        top -= 1

        #  Update parameters.
        self.top = top
        self.S = S

        return key


    """
    The print function of the instance of Stack class.
    """
    def __str__(self):
        top = self.top
        S = self.S
        return str(S[:top + 1])


class Queue():

    def __init__(self, n):
        self.__len = n
        self.Q = [None] * n
        self.head = 0
        self.tail = 0


    def is_underflow(self):

        #  load parameters.
        n = self.__len
        head = self.head
        tail = self.tail

        #  When the queue is empty means underflow.
        if head == tail:
            return True
        else:
            return False


    def is_overflow(self):

        #  load parameters.
        n = self.__len
        head = self.head
        tail = self.tail

        #  When the queue is full means overflow.
        if tail == n - 1 and head == 0:
            return True
        if tail + 1 == head:
            return True
        return False


    def enqueue(self, key):

        #  load parameters.
        n = self.__len
        Q = self.Q
        tail = self.tail

        assert not self.is_overflow(), "error: the queue is full / overflow!"

        Q[tail] = key
        if tail == n - 1:
            tail = 0
        else:
            tail += 1

        #  Update parameters.
        self.Q = Q
        self.tail = tail


    def dequeue(self):

        #  load parameters.
        n = self.__len
        Q = self.Q
        head = self.head

        assert not self.is_underflow(), "error: the queue is empty / underflow!"

        key = Q[head]
        if head == n - 1:
            head = 0
        else:
            head += 1

        #  Update parameters.
        self.Q = Q
        self.head = head

        return key


    """
    The print function of the instance of Queue class.
    """
    def __str__(self):

        #  load parameters.
        n = self.__len
        Q = self.Q
        head = self.head
        tail = self.tail

        if tail >= head:
            return str( Q[head : tail] )
        else:
            return str( Q[head : n] + Q[:tail] )




#  Drive code.
if __name__ == "__main__":

    #  Test for Stack in 10.1-1 in P235.
    s = Stack()
    s.push(4)
    s.push(1)
    s.push(3)
    s.pop()
    s.push(8)
    s.pop()
    print("Test for Stack in 10.1-1 in P235: ", s, '\n')

    #  Test for Queue in 10.1-3 in P235.
    q = Queue(6)
    q.enqueue(4)
    q.enqueue(1)
    q.enqueue(3)
    q.dequeue()
    q.enqueue(8)
    q.dequeue()
    print("Test for Queue in 10.1-3 in P235: ", q, '\n')



