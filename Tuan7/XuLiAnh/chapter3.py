import cv2
import numpy as np
import matplotlib.pyplot as plt
L = 256
def Negative(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    for x in range(M):
        for y in range(0, N):
            r = imgin[x, y]
            s = L - 1 - r
            imgout[x, y] = np.uint8(s)
    return imgout

def NegativeColor(imgin):
    M, N, C = imgin.shape
    imgout = np.zeros((M, N, C), np.uint8) + 255
    for x in range(0,M):
        for y in range(0, N):
            b = imgin[x,y,0]
            g = imgin[x,y,1]
            r = imgin[x,y,2]

            b = L - 1 - b
            g = L - 1 - g
            r = L - 1 - r

            imgout[x,y,0] = np.uint8(b)
            imgout[x,y,1] = np.uint8(g)
            imgout[x,y,2] = np.uint8(r)
    
    return imgout

def Logarit(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8) + 255
    c = (L-1)/np.log(1.0*L)
    for x in range(0,M):
        for y in range(0, N):
            r = imgin[x,y]
            s = c*np.log(1.0 + r)
            imgout[x,y] = np.uint8(s)
    return imgout

def Power(imgin):
    gamma = 5.0
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8) + 255
    c = np.power(L-1.0,1.0 - gamma)
    for x in range(0,M):
        for y in range(0, N):
            r = imgin[x,y]
            s = c*np.power(1.0*r,gamma)
            imgout[x,y] = np.uint8(s)
    return imgout

def PiecewiseLinear(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8) + 255
    rmin, rmax, _, _ = cv2.minMaxLoc(imgin)
    r1 = rmin
    s1 = 0
    r2 = rmax
    s2 = L - 1
    for x in range(0,M):
        for y in range(0, N):
            r = imgin[x,y]
            # Giai doan 1
            if r < r1:
                s = s1*r/r1
            elif r < r2:
                s = (s2 - s1)*(r - r1)/(r2 - r1) + s1
            # Giai doan 2
            else:
                s = (L-1 - s2)*(r - r2)/(L-1 - r2) + s2
            imgout[x,y] = np.uint8(s)
    return imgout

def Histogram(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, L), np.uint8) + 255
    h = np.zeros(L, np.uint)
    for x in range(0,M):
        for y in range(0, N):
            r = imgin[x,y]
            h[r] = h[r] + 1
    p = h/(M*N)
    scale = 3000
    for r in range(0,L):
        cv2.line(imgout, (r, M -1), (r,M -1 - int(scale*p[r])), (0, 0, 0))
    return imgout

def HistEqual(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8) + 255
    h = np.zeros(L, np.int32)
    for x in range(0,M):
        for y in range(0, N):
            r = imgin[x,y]
            h[r] = h[r] + 1
    p = h/(M*N) 
    s = np.zeros(L, np.float64)
    for k in range(0,L):
        for j in range(0, k +1):
            s[k] = s[k] + p[j]
        s[k] = (L-1)*s[k]
    for x in range(0,M):
        for y in range(0, N):
            r = imgin[x,y]
            imgout[x,y] = np.uint8(s[r])
    return imgout

def LocalHist(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8) + 255

    m = 3
    n = 3
    a = m // 2
    b = n // 2
    w = np.zeros((m,n), np.uint8)

    for x in range(a, M - a):
        for y in range(b, N - b):
            w = imgin[x - a:x + a + 1, y - b:y + b + 1]
            # for s in range(-a, a + 1):
            #     for t in range(-b, b + 1):
            #         w[s + a, t + b] = imgin[x + s, y + t]
            w = cv2.equalizeHist(w)
            imgout[x, y] = w[a, b]
    return imgout
