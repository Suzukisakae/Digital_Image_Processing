import cv2
import numpy as np
import os

path = './dataset/HinhElip/'
lst_dir = os.listdir(path)
f = open('./parameter/para_a_b_elip.txt', 'w')

text = ''
data = []
for filename in lst_dir:
    fullname = path + filename
    print(fullname)
    img = cv2.imread(fullname, cv2.IMREAD_GRAYSCALE)
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, 
                                cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    para = cv2.fitEllipse(cnt)
    xc = int(para[0][0])
    yc = int(para[0][1])
    a = int(para[1][0])/2
    b = int(para[1][1])/2
    d = abs(a - b)
    goc_quay = para[2]
    text = text + '%5d %5d %5d \n' % (a, b, d)

f.write(text)
f.close()
