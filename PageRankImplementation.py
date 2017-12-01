'''
Name: Tejaswi Ginuga
Submitting as part of my Assignment 2, Information retrieval
'''
import numpy as np
from scipy.sparse import csc_matrix
import numpy as np
import pandas as pd
from fractions import Fraction
import scipy.sparse as sps
import numpy.matlib as npm
def pageRankImplementation(path):
    beta = 0.85
    epsilon = 0.0001
    M = helper(path)
    no_of_nodes = M[0].size
    E = np.matlib.ones((no_of_nodes,1) ,dtype=np.int)

    # v' = beta * M * v + (1-beta) * e / N

    x = ((1-beta) * E / no_of_nodes)
    A = beta * M 
    p = 1/no_of_nodes
    r = np.full((no_of_nodes, 1), p)
    orginial_rank_vector = r
    prev_r = r
    count = 0

    while(True):
        count = count + 1
        r = (A * r) + x
        #print(roundFloat(r,6))
        #check for convergence
        if ((abs(prev_r - r)) < epsilon).all():
            break
        prev_r = r
 
    #print ("sum", np.sum(r))

    print("Outputs")
    print("Matrix M: \n" , np.round(M,4))
    print("Original rank vector rj: \n" , orginial_rank_vector)
    print("Converged rank vector (R): \n" , roundFloat(r,6))
    print("Number of iterations took to converge: \n",count)


def roundFloat(x, decimal):
    return np.round((x).astype(np.float), decimals=decimal)


def helper(path):
	#read input Adj text file into A
    A = np.genfromtxt(path, delimiter=' ',skip_header=0,dtype = int)
    i,j,k = A[:,0], A[:,1], A[:,2]   
    dim = (set(np.concatenate((i,j),axis=0)))
    len_dim = len(dim)
    # B is Sparse Matrix
    B = sps.lil_matrix((len_dim, len_dim))
    for i,j,k in zip(i,j,k):
        B[i-1,j-1] = k
        C = B.todense()
    sum = np.sum(C, axis=1)
    for x in range(C[0].size):
        for y in range(C[0].size):
            if C[x,y] == 1.:
                C[x,y] = 1 / sum[x,0] 
    return C.transpose()


print("Enter the path of Adj Matrix. Acceptable input format: Three columns of ints or floats")
path = input()
pageRankImplementation(path)