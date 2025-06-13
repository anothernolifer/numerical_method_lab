# Gauss elimination method

import numpy as np


n = int(input('No of variables: '))
A =[]


for i in range(n):
    A.append(list(map(float,input( ).split())))
    
A = np.matrix(A)
   
    
print(f'THE AUGMENTED MATRIX IS A = ')
print(A)


for i in range(n):
    
    p_row = np.argmax(np.abs(A[i:, i])) + i
    A[[i, p_row]] = A[[p_row, i]]
    
    for j in range(i + 1, n):
        factor = A[j, i] / A[i, i]
        A[j] = A[j] - factor * A[i]

print('\nUpper Triangular Matrix:')
print(A)


x = np.zeros((n, 1))

for i in range(n - 1, -1, -1):
    x[i] = A[i, -1] - np.sum(A[i, i+1:n] * x[i+1:n]) 
    x[i] = x[i] / A[i, i]

print('\nSolution:')
for i in range(n):
    print(f'x{i+1} = {x[i,0]}')
