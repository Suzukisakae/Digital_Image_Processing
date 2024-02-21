import os
import cv2
import numpy as np

path = 'D:/SPKT/NamBa/Ki2/DIPR430685_23_2_03/Tuan4/TraiCayScratch/ThanhLong/'
path_new = 'D:/SPKT/NamBa/Ki2/DIPR430685_23_2_03/Tuan4/trai_cay_640x640/thanh_long/'
lst_trai_cay = os.listdir(path)
dem = 0

for filename in lst_trai_cay:
    fullname = path + filename
    imgin = cv2.imread(fullname, cv2.IMREAD_COLOR)
    # cv2.imshow('ImageIn', imgin)
    # key = cv2.waitKey(0)
    # # ASCII cua ESC la 27
    # if key == 27:
    #     break
    M, N, C = imgin.shape
    if M < N:
        imgout = np.zeros((N, N, C), np.uint8) + 255
        imgout[0:M, :, :] = imgin[:, :, :]
    elif M > N:
        imgout = np.zeros((M, M, C), np.uint8) + 255
        imgout[:, 0:N, :] = imgin[:, :, :]
    else: 
        imgout = imgin.copy()
    imgout = cv2.resize(imgout, (640, 640))
    fullname_new = path_new + 'thanh_long_%04d.jpg' % dem
    print(fullname_new)
    dem = dem + 1
    cv2.imwrite(fullname_new, imgout)