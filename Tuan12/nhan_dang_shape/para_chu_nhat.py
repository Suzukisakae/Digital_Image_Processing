import cv2
import numpy as np
img = cv2.imread('./dataset/HinhElip/001.bmp', cv2.IMREAD_GRAYSCALE)
img_save = cv2.imread('./dataset/HinhElip/001.bmp', cv2.IMREAD_COLOR)
contours, _ = cv2.findContours(img, cv2.RETR_TREE, 
                               cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

L, _, _ = cnt.shape 
for i in range(0, L-1):
    cv2.line(img_save, 
             (cnt[i,0,0], cnt[i,0,1]), 
             (cnt[i+1,0,0], cnt[i+1,0,1]), 
             (0, 0, 255))

para = cv2.fitEllipse(cnt)
xc = int(para[0][0])
yc = int(para[0][1])
a = int(para[1][0])/2
b = int(para[1][1])/2
goc_quay = para[2]

n = 21
theta = np.linspace(0, 2*np.pi, n)
x = a*np.cos(theta)
y = b*np.sin(theta)

x1 = np.zeros(n, np.float64)
y1 = np.zeros(n, np.float64)
for i in range(0, n):
    x1[i] = x[i]*np.cos(goc_quay) - y[i]*np.sin(goc_quay)
    y1[i] = x[i]*np.sin(goc_quay) + y[i]*np.cos(goc_quay)
goc_quay = goc_quay*np.pi/180

x1 = x1 + xc
y1 = y1 + yc

for i in range(0, n-1):
    cv2.line(img_save, 
             (int(x1[i]), int(y1[i])), 
             (int(x1[i+1]), int(y1[i+1])), 
             (0, 255, 0))

cv2.imshow('Image', img_save)
cv2.waitKey(0)