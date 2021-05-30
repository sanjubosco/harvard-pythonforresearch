import numpy as np 

w1 = 0.01
w2 = -5
b= -1
x = 3
t = 1

z1 = w1*x
a1 = np.maximum(z1,0)
z2 = w2*a1 + b
y = 1/(1 + np.exp(-z2))
loss = ((y-t)**2)/2

derivative1 = (y-t)*(np.exp(-z2)/((1+np.exp(-z2))**2))

d_w2 = a1*derivative1
print (d_w2)
print (derivative1)
d_w1 = x * d_w2
print (d_w1)