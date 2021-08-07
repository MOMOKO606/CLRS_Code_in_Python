import chapter_2 as algo



#  Drive code.
if __name__ == '__main__':

    #  Read data from file.
    A = []
    with open('data.txt', 'r') as f:
        for line in f:
            A.append(int(line))
    f.close()



    print( algo.inversion_recur( A, 0, len(A) - 1) )
    print(algo.inversion_naive( A ))







