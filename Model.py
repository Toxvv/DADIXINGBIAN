import numpy as np


def Model1(L, B, P):
    NBB = np.linalg.inv(np.dot(np.dot(B.T, P), B))
    W = np.dot(np.dot(B.T, P), L)
    X1 = np.dot(NBB, W)

    # BTP = np.dot(B.T, P)
    # PB = np.dot(P, B)
    #   DModel=np.dot(DModel0,np.dot(PB,NBB))
    return X1


#   return DModel

def Model2(L, B, P):
    NBB = np.linalg.inv(np.dot(np.dot(B.T, P), B))
    W = np.dot(np.dot(B.T, P), L)
    X1 = np.dot(NBB, W)
    BTP = np.dot(B.T, P)
    PB = np.dot(P, B)
    DModel0 = np.dot(np.dot(NBB, BTP), np.linalg.inv(P))
    DModel = np.dot(DModel0, np.dot(PB, NBB))
    return DModel
