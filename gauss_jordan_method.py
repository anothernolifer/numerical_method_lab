# Gauss JORDAN method

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

    
    A[i] = A[i] / A[i, i]

    
    for j in range(n):
        if j != i:
            A[j] = A[j] - A[j, i] * A[i]

A=np.matrix(A)
print('The normal matrix is A: ')
print(A)

x=A[:,-1]
print('Solution: ')
print(x)
    
for i in range(n):
    print(f'x{i+1} = {x[i,0]}')
