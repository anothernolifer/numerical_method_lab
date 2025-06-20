# Gauss Seidal Method

import numpy as np
import pandas as pd


n = int(input('No of variables: '))
A =[]
T =[]


for i in range(n):
    A.append(list(map(float,input( ).split())))
    
A = np.array(A)

print(f'THE AUGMENTED MATRIX IS A = ')
print(A)

X =[]


for i in range(n):
    X.append(list(map(float,input( ).split())))
    
X = np.array(X)

print(f'THE INITIAL GUESS MATRIX IS X = ')
print(X)

e = float(input("Enter tolerable error: "))
N = int(input("Enter maximum number of iterations: "))

itr = 1

while itr <= N:
    x_old = np.copy(X)
    
    for i in range(n):
        s = 0
        
        for j in range(n):
            if j != i:
                s += A[i,j]*X[j]
                
        X[i] = (A[i,-1]-s) / A[i,i]
    
    err = np.abs(X - x_old)
    T.append([itr] + [X[i] for i in range(n)])
    
    
    if np.all(err < e):
        columns = ['iterations'] + [f'X{i+1}' for i in range(n)]
        T = pd.DataFrame(T, columns=columns)
        print(T)
        break

    itr += 1
    
if itr > N:
        print(f"Solution does not reach in {N} iterations")

else:
    print('Solution: ')
    
    for i in range(n):
        print(f'X{i+1} = {X[i,0]}')
        
        
            
    
    
        
