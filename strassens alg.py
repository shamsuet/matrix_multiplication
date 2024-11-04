import numpy as np

def strausen(A,B):
    m,n = A.shape
    assert(m==n,'should be a square matrix')
    
    if(not np.log2(n)%1==0):
        print('matrix dimension should be a power of 2')
        return


    n = int(n)
    if n == 1:
        return A[0,0]*B[0,0]
    
    A00 = A[0:n//2,0:n//2]
    A01 = A[0:n//2,n//2:n]
    A10 = A[n//2:n,0:n//2]
    A11 = A[n//2:n,n//2:n]

    B00 = B[0:n//2,0:n//2]
    B01 = B[0:n//2,n//2:n]
    B10 = B[n//2:n,0:n//2]
    B11 = B[n//2:n,n//2:n]
    
    M1 = strausen(A00+A11,B00+B11)
    M2 = strausen(A10+A11,B00)
    M3 = strausen(A00,B01-B11)
    M4 = strausen(A11,B10-B00)
    M5 = strausen(A00+A01,B11)
    M6 = strausen(A10-A00,B00+B01)
    M7 = strausen(A01-A11,B10+B11)

    C = np.zeros(A.shape)
    C[0:n//2,0:n//2] = M1+M4-M5+M7
    C[0:n//2,n//2:n] = M3+M5
    C[n//2:n,0:n//2] = M2+M4
    C[n//2:n,n//2:n] = M1+M3-M2+M6

    return C
n = 8


A = np.floor(100*np.random.rand(n,n))
B = np.floor(100*np.random.rand(n,n))
print(A.shape)

C1 = np.matmul(A,B)
print("Using NP Library")
print(C1)

C2 = strausen(A,B)
print("Using strausen")
print(C2)

if np.sum(C1-C2,axis=None) == 0:
    print("Strausen implementation is correct")