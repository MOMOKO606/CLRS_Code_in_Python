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

    def __init__(self):
        self.Q = [None]
        self.head = 0
        self.tail = 0





    def __str__(self):
        Q = self.Q
        head = self.head
        tail = self.tail

        return str( Q[head : tail] )




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
    print("Test for Stack in 10.1-1 in P235.: ", s, '\n')

