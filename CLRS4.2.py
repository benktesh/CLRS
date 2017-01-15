import numpy as np;  
import time; 
import random; 

def maxtrixmultiply (A, B):
    m = A.shape[0]
    n = A.shape[1]
    o = B.shape[0]
    p = B.shape[1]

    #print "m={}, n={}, o={}, p={} ".format(m, n, o, p)

    C = np.zeros((m,p), dtype=float ) 

    if(o != n):
        return "Error"

    for i in range(m):        
        for j in range(p):            
            for k in range(n):
                C[i,j] = C[i,j] + A[i,k] * B[k, j]
    
    if (np.dot(A,B).sum() != C.sum()):
        print "Algorithhm is Incorrect"
    else:
        return C
def main():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[1, 2, 3], [4, 5, 6]])
    print "A:\n", A
    print "B:\n", B
    print "Result:\n", maxtrixmultiply(A, B)
    return;

  

if __name__ == "__main__":
    main();