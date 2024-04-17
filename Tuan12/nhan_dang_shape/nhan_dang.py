import	tkinter	as	tk
from tkinter.filedialog import Open
from PIL import Image, ImageTk
import numpy as np
import cv2

class App(tk.Tk):
    def	__init__(self):
        super().__init__()
        self.filename = None
        self.title('Nhận dạng shape')
        self.cvs_image = tk.Canvas(self, width = 640, height = 480, 
                       relief = tk.SUNKEN, border = 1)
        lbl_frm_menu = tk.LabelFrame(self)
        btn_open_image = tk.Button(lbl_frm_menu, text = 'Open Image', width = 10,
                                   command = self.btn_open_image_click)
        btn_predict = tk.Button(lbl_frm_menu, text = 'Predict', width = 10,
                                   command = self.btn_predict_click)
        btn_open_image.grid(row = 0, column = 0, padx = 5, pady = 5)
        btn_predict.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.cvs_image.grid(row = 0, column = 0, padx = 5, pady = 5)
        lbl_frm_menu.grid(row = 0, column = 1, padx = 5, pady = 7, sticky = tk.NW)

    def btn_open_image_click(self):
        ftypes = [('Images', '*.jpg *.tif *.bmp *.gif *.png')]
        dlg = Open(self, filetypes = ftypes)
        self.filename = dlg.show()
        if self.filename != '':
            image = Image.open(self.filename)
            self.image_tk = ImageTk.PhotoImage(image)
            self.cvs_image.create_image(0, 0, anchor = tk.NW, image = self.image_tk)

    def btn_predict_click(self):
        imgin = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
        moments = cv2.moments(imgin)
        hu = cv2.HuMoments(moments)
        if 0.000623 <= hu[0] <= 0.000629:
            shape = 'Circle'
        elif 0.000646 <= hu[0] <= 0.000743:
            shape = 'Elip, Vuong, ChuNhat'
        elif 0.000762 <= hu[0] <= 0.000808:
            shape = 'Triangle'
        elif 0.000908 <= hu[0] <= 0.000992:
            shape = 'Right Triangle'        
        else:
            shape = 'Unknown shape'
        self.cvs_image.create_text(100, 10, text = shape, fill="white", justify=tk.CENTER, font=("Arial", 16))


if	__name__	==	"__main__":
    app	= App()
    app.mainloop()
