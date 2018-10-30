import numpy as np
import numpy.linalg as la

def gram_schmidt_cofficient(v1, v2):
    return np.dot(v2, v1) / np.dot(v1, v1)


def multiply(cofficient, v):
    return map((lambda x : x * cofficient), v)


def project(v1, v2):
    return multiply(gram_schmidt_cofficient(v1, v2) , v1)


def gram_schmidt(X):
    B = []
    for i in range(len(X)):
        temp_vec = X[i]
        for v in B :
            proj_vec = project(v, X[i])
            temp_vec = map(lambda x, y : x - y, temp_vec, proj_vec)
        B.append(temp_vec)
    return B

def svd(A):
    B = np.matmul(A.T, A)
    ew, ev = la.eig(B)
    V = gram_schmidt(ev)
    Vt = np.transpose(V)
    sv = np.sqrt(ew)
    Sigma = np.diag(sv)
    # U = ui = (1/sqrt(ewi)) * A * evi ergaenzt zu ON-Basis des Rm
    return U, Sigma, Vt

def pseudo_inverse(A):
    A_ = la.inv(np.matmul(A.T, A))
    A_pseu = np.matmul(A_, A.T)
    return A_pseu

def lin_solve(A,b):
    return np.matmul(pseudo_inverse(A), b)
