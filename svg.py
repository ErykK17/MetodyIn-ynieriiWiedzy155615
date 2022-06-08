from cmath import sqrt
import numpy as np

matrix = np.array([[1,-2,0],
        [0,-2,1]])
        
matrixtest =np.array([[1,1],[1,1]])

def left_side(matrix):
    matrix_trasnposed = np.transpose(matrix)
    q_matrix = matrix @ matrix_trasnposed
    wartosci_wlasne = np.linalg.eig(q_matrix)
    return wartosci_wlasne[0], wartosci_wlasne[1]

def right_side(matrix):
    matrix_transposed = np.transpose(matrix)
    v_matrix = matrix_transposed @ matrix
    wartosci_wlasne = np.linalg.eig(v_matrix) 
    return wartosci_wlasne[0], wartosci_wlasne[1]
    
singulars_from_q, q_values = left_side(matrix)
singulars_from_v, v_values = right_side(matrix)

if len(singulars_from_q) >len(singulars_from_v) :
    lambdas = singulars_from_q
else:
    lambdas = singulars_from_v

singular = []

for lam in lambdas:
    lam = float (lam)
    sing_val = sqrt(lam)
    singular.append(sing_val)

# print(singular)

sigma = np.zeros((2,3))

print(singular[0])


if int(sigma.shape[0])> int(sigma.shape[1]):
    for i in range (int(sigma.shape[1])):
        sigma[i][i] += singular[i]
        print(singular[i])
else:
    for i in range (int(sigma.shape[0])):
        sigma[i][i] += singular[i]

v_values_transposed = np.transpose(v_values)

print (f'Q : \n {q_values}')
print (f'SIGMA: \n {sigma}')
print(f'V: \n {v_values_transposed}')

