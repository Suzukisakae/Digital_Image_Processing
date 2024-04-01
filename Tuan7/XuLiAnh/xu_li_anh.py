import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import Open
from tkinter.filedialog import asksaveasfilename
import cv2
import numpy as np

import chapter3 as c3

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Xử lí ảnh số")
        self.geometry("800x600")

        self.imgin = None
        self.imgout = None
        self.filename = None

        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open Image", command=self.mnu_open_image_click)
        file_menu.add_command(label="Save Image", command=self.mnu_save_image_click)

        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)
        menu.add_cascade(label="File", menu=file_menu)

        chapter_3_menu = tk.Menu(menu, tearoff=0)
        chapter_3_menu.add_command(label="Negative", command=self.mnu_c3_negative_click)
        chapter_3_menu.add_command(label="NegativeColor", command=self.mnu_c3_negative_color_click)
        chapter_3_menu.add_command(label="Logarit", command=self.mnu_c3_logarit_click)
        chapter_3_menu.add_command(label="Power", command=self.mnu_c3_power_click)
        chapter_3_menu.add_command(label="PiecewiseLinear", command=self.mnu_c3_piecewise_linear_click)
        chapter_3_menu.add_command(label="Histogram", command=self.mnu_c3_histogram_click)
        chapter_3_menu.add_command(label="Hist Equal", command=self.mnu_c3_hist_equal_click)
        chapter_3_menu.add_command(label="Local Hist", command=self.mnu_c3_local_hist_click)
        menu.add_cascade(label="Chapter 3", menu=chapter_3_menu)

        self.config(menu=menu)

    def mnu_open_image_click(self):
        ftypes = [('Image files', '*.jpg;*.jpeg;*.png;*.bmp, *.tif'), ('All files', '*')]
        dlg = Open(self, filetypes=ftypes)
        filename = dlg.show()
        if filename != '':
            self.imgin = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            cv2.imshow("Input Image", self.imgin)

    def mnu_c3_negative_click(self):
        self.imgout = c3.Negative(self.imgin)
        cv2.imshow("Output Image", self.imgout)

    def mnu_c3_negative_color_click(self):
        self.imgout = c3.NegativeColor(self.imgin)
        cv2.imshow("Output Image", self.imgout)

    def mnu_save_image_click(self):
        ftypes = [('Image files', '*.jpg;*.jpeg;*.png;*.bmp, *.tif'), ('All files', '*')]
        filenameout = asksaveasfilename(title="Save as",filetypes=ftypes, initialdir=self.filename)
        if filenameout is not None:
            cv2.imwrite(filenameout, self.imgout)

    def mnu_c3_logarit_click(self):
        self.imgout = c3.Logarit(self.imgin)
        cv2.imshow("Output Image", self.imgout)

    def mnu_c3_power_click(self):
        self.imgout = c3.Power(self.imgin)
        cv2.imshow("Output Image", self.imgout)
    
    def mnu_c3_piecewise_linear_click(self):
        self.imgout = c3.PiecewiseLinear(self.imgin)
        cv2.imshow("Output Image", self.imgout)

    def mnu_c3_histogram_click(self):
        self.imgout = c3.Histogram(self.imgin)
        cv2.imshow("Output Image", self.imgout)

    def mnu_c3_hist_equal_click(self):
        # self.imgout = c3.HistEqual(self.imgin)
        self.imgout = cv2.equalizeHist(self.imgin)
        cv2.imshow("Output Image", self.imgout)

    def mnu_c3_local_hist_click(self):
        self.imgout = c3.LocalHist(self.imgin)
        cv2.imshow("Output Image", self.imgout)

if __name__ == "__main__":
    app = App()
    app.mainloop()