### 3.3.4 Thống kê Histogram

- Ta chỉ dùng 2 đại lượng thống kê là mean (trung bình) và standard Deviation (độ lệch chuẩn)
- Code thống kê histogram: chapter3.py

```python
def HistStat(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8) + 255
    # sum = 0.0
    # for x in range(0,M):
    #     for y in range(0, N):
    #         r = imgin[x,y]
    #         sum = sum + r
    # mean = sum/(M*N)

    # variance = 0.0
    # for x in range(0,M):
    #     for y in range(0, N):
    #         r = imgin[x,y]
    #         variance = variance + (r - mean)**2
    # variance = variance/(M*N)

    # sigma = np.sqrt(variance)
    # print("mean = ", mean)
    # print("sigma = ", sigma)

    mean, stdDev = cv2.meanStdDev(imgin)
    # print("mean = ", mean)
    # print("stdDev = ", stdDev)
    mG = mean[0,0]
    sigmaG = stdDev[0,0]

    m = 3
    n = 3
    a = m // 2
    b = n // 2
    w = np.zeros((m,n), np.uint8)
    C = 22.8
    k0 = 0.0
    k1 = 0.1
    k2 = 0.0
    k3 = 0.1

    for x in range(a, M - a):
        for y in range(b, N - b):
            w = imgin[x - a:x + a + 1, y - b:y + b + 1]
            mean, stdDev = cv2.meanStdDev(w)
            msxy = mean[0,0]
            sigmasxy = stdDev[0,0]
            if (k0*mG <= msxy <= k1*mG) and (k2*sigmaG <= sigmasxy <= k3*sigmaG):
                r = imgin[x,y]
                imgout[x,y] = np.uint8(C*r)
            else:
                imgout[x,y] = imgin[x,y]

    return imgout

```

### 3.4 Cơ bản về lọc trong không gian (trang 226 - Sách DigitalImageProcessing2018_LocalVersion.pdf)

- NGười ta dùng một cửa sổ nhỏ w để lọc trong không gian. Cửa sổ nhỏ có kích thước lẻ để có phần tử trung tâm
  VD: Kích thước của của sổ nhỏ sẽ là 3x3 hay 5x5
- Cửa sổ có kích thước mxn. Giá trị của n người ta sẽ cho tùy vào yêu cầu cụ thể.
- Cửa sổ w còn được gọi là bộ lọc (filter), mặt nạ (mask), kernel (nhân) hay template (mẫu)

Lọc trong không gian được cho bằng phương trình ở Figure 3.34 (trang 226)
Ta viết trong hàm MyFilter2D của chapter3.py

```python
def MyFilter2D(imgin):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8) + 255
    m = 11
    n = 11
    w = np.zeros((m,n), np.float32) + 1.0/(m*n)
    a = m // 2
    b = n // 2
    for x in range(a, M - a):
        for y in range(b, M - b):
            r = 0.0
            for s in range(-a, a + 1):
                for t in range(-b, b + 1):
                    x_moi = (x + s)%M
                    y_moi = (y + t)%N
                    r = r + w[s + a, t + b]*imgin[x_moi, y_moi]
            if r < 0:
                r = 0
            if r > L - 1:
                r = L - 1
            imgout[x, y] = np.uint8(r)

    return imgout
```

Nhưng ta cũng có thể dùng hàm có sẵn mà không cần phải lập trình như trên

```python
def MySmooth(imgin):
    m = 11
    n = 11
    w = np.zeros((m,n), np.float32) + 1.0/(m*n)
    imgout = cv2.filter2D(imgin, cv2.CV_8UC1, w)
    return imgout
```

### 3.5 Lọc làm trơn trong không gian

- Lọc làm trơn sẽ làm nhòe ảnh, đây là điều ta không mong muốn nhưng nó là chức năng cơ bản của Xử lí ảnh và là bước tiền xử lí cho các thuật toán xử lý ảnh khác như phát hiện chạnh Canny
- Có 2 phương pháp làm trơn cơ bản là lọc Box và lọc Gaussian

#### 3.5.1 Lọc Box

#### 3.5.2 Lọc Gaussian

#### 3.5.3 Lọc medium (Lọc trung vị)

- Lọc trung vị dùng để xóa nhiễu xung. Nhiễu xung là đốm sáng hoặc đốm tối xuất hiện ngẫu nhiên trên ảnh 
- Nhiễu xung còn gọi là nhiễu muối tiêu (salt noise) và nhiễu ớt (pepper noise)
- Và trong cv2, cũng có hàm dùng để lọc trung vị