import numpy as np
import numpy.linalg as la

def SVD(A):
    At = np.transpose(A)
    B = np.matmul(At, A)
    ew, ev = la.eig(B)
    # V = Orthonormale Basis aus den Eigenvektoren ev zu den Eigenwerten ew
    Vt = np.transpose(V)
    sv = np.sqrt(ew)
    Sigma = np.diag(sv)
    # U = ui = (1/sqrt(ewi)) * A * evi ergaenzt zu ON-Basis des Rm
    return U, Sigma, Vt

def PseudoInverse(A):
    # Berechne A+ mit Hilfe der SVD
    pass

def LinearSolve(A,b):
    # Loese lineares Gleichungssystem, behandle es dazu als lineares
    # Ausgleichsproblem ||A*x-b||2 -> min
    pass
