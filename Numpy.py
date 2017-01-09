import numpy as np
import matplotlib.pyplot as plt
#[0,1,2,3,4,5]
a = np.arange(5)
print(a)
#[0,2,4,6,8]
a = np.arange(0,10,2);
print(a)
a = np.array([1,2,3,4,5])
print(a)
#matrix [0,1,2]
#       [3,4,5]
#       [6,7,8]
a = np.arange(9).reshape(3,3)
print(a)
matrix = np.array([(1,2,3),(4,5,6)]);
print(matrix)
matrix = np.zeros((3,8))
print(matrix)
matrix = np.ones((3,8))
print(matrix)
#get dim,size,dtype,itemsize
print(a.shape),print(a.size),print(a.dtype),print(a.itemsize)
#complex
coplex = np.array([[1, 2], [3, 4]], dtype=complex)
print(coplex)


#linspace 10 numbers in [0,1]
a = np.linspace(0,1,10)
print(a)
#--------------------Operations---------------------
# v-u,v+u,v^2
v = np.array( [20,30,40,50] )
u = np.arange( 4 )
print(v-u)
print(v+u)
print(u**2)
#sin(x)
x = np.linspace( 0, 2*np.pi, 5 )
f = np.sin(x)
print(10*f);
print(10*f < 0)
#matrix operations
A = np.array([[1,1],[0,1]])
B = np.array( [[2,0],[3,4]])
print(A*3)
print(A*B)
print(A.dot(B))
#   sum             sum on c        sum on r                cumulative sum axis=?
print(A.sum()),print(A.sum(axis=0)),print(A.sum(axis=1)),print(A.cumsum())
print(A.min())
print(A.max())

a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a.transpose())
#linear algorithms
print(np.linalg.inv(a))
print(np.eye(2))
print(np.trace(a))
y = np.array([[5.], [7.]])
print(np.linalg.solve(a,y))
print(np.linalg.eig(a))
#ploting
x = np.linspace( 0, 20*np.pi, 1000 )
f = np.sin(x)
plt.plot(f)
plt.show()

mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
plt.hist(v, bins=50, normed=1)
plt.show()


