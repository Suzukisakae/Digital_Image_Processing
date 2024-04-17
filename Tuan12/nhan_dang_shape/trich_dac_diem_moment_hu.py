import os
import cv2
import numpy as np

path = './dataset/HinhTamGiacVuong/'
# path = './dataset/HinhChuNhat/'
lst_dir = os.listdir(path)
f = open('./feature/hu_moment_tam_giac_vuong.txt', 'w')
# f = open('./feature/hu_moment_chu_nhat.txt', 'w')
text = ''
data = []
for filename in lst_dir:
    fullname = path + filename
    print(fullname)
    image = cv2.imread(fullname, cv2.IMREAD_GRAYSCALE)
    moments = cv2.moments(image)
    # có 7 đặc điểm Hu là hu[0], hu[1], ..., hu[6]
    # do hình của ta đã lý tưởng nên ta chỉ lấy hu[0]
    hu = cv2.HuMoments(moments)
    s = '%10.6f' % hu[0]
    text = text + s + '\n'
    data.append(hu[0])
avg = sum(data)/len(data)
min = min(data)
max = max(data)
thong_ke = 'avg = %.6f, min = %.6f, max = %.6f' % (avg, min, max)
text = text + thong_ke + '\n'

f.write(text)
f.close()