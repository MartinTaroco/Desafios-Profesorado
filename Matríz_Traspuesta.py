import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(A)



def transpuesta(matriz):
    M_T = matriz.T

    return M_T


A_T = transpuesta(A)

print(A_T)