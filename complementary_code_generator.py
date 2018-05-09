#This file is to generate a serial of COMPLEMENTARY code, accroding to Golay's
#paper, in 1961.
from basic_func import inverse
from basic_func import string_inv
def CCG(k):
    'k decide the length of sequence in totoal'
    # length of sequence = 2**k
    A = [1]
    B = [1]
    for i in range(0,k):
        C = A
        A = A+B
        B = C+string_inv(B)
    return[A,B]


def uni(A):
    A1 = A.copy()
    A2 = A.copy()
    for i in range(len(A)):
        if A[i]==1:
            A1[i] = 1
            A2[i] = 0
        if A[i]==-1:
            A1[i] = 0
            A2[i] = 1
    return [A1,A2]
