import numpy as np
import cv2
m=3
n=3
w = np.zeros((m,n), np.float32)
sigma = 1.0

a = m // 2
b = n // 2

for s in range(-a, a + 1):
    for t in range(-b, b + 1):
        w[s + a, t + b] = np.exp(-(s**2 + t**2)/(2*sigma**2))

for x in range(0, m):
    for y in range(0, n):
        print('%10.8f' % w[x,y], end = '')
    print()

K = np.sum(w)
w = w/K
for x in range(0, m):
    for y in range(0, n):
        print('%10.8f' % w[x,y], end = '')
    print()
K = np.sum(w)
print(K)

v = cv2.getGaussianKernel(3, 1.0)
print(v)
u = np.transpose(v)
print(u)
w = np.matmul(v, u)
print(w)