import numpy as np 

def activation(X):
    return (np.maximum(X,0))

W = np.array([[1,0,-1,0],[0,1,0,-1]])
W0 = np.array([-1,-1,-1,-1])
X = np.array([3,14])
V = np.array([[1,1,1,1],[-1,-1,-1,-1]])
V = V.T
V0 = np.array([0,2])
Z = np.dot(X,W) + W0
L1 = activation(Z)
print (L1)
U = np.dot(L1,V) + V0
L2 = activation(U)
print (L2)
b =1
e_o1 = np.exp(b*L2[0])
e_o2 = np.exp(b*L2[1])
O1 = e_o1/(e_o1 + e_o2)
O2 = e_o2/(e_o1 + e_o2)

print (O1,O2)

