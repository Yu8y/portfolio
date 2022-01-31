import numpy as np
from numpy import linalg as ln
#F(x)=2x^3-x+5
A=np.array([[-1,0],[2,2]])
B=2*ln.matrix_power(A,3)
C=B-A
D=C+5
print(B)
print(C)
print(D)


#Another equation example

import numpy as np
A=np.array([[-3,0],[2,-1],[1,1],[0,3]])
print(A)
B=np.array([[-3,2,1,-4],[1,1,-3,0]])
print(B)
#(A-2Bтр)*(С+3D)
C=np.array([[4,0,-3],[2,5,-1]])
print(C)
D=np.array([[10,5,-1],[-2,3,-3]])
print(D)
G=np.dot(A-2*B.transpose(),C+3*D)
print(G)


M1 = np.array([[2,3],[5,2],[1,4]])
M2 = np.array([30,50])

print(M1, M2)
M3 = np.dot(M1, M2)
print("M3: ")
print(M3)