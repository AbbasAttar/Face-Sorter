import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Face Sorter")

# ========================FUNCTION==========================


def selectPhoto():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetype=[('JPG file (*.jpg)', '*.jpg'),
                                                       ('JPEG file (*.jpeg)',
                                                        '*.jpeg'),
                                                       ('PNG file (*.png)', '*.png')])
    label = tk.Label(frame1, text=filename, bg="white").place(
        relwidth=0.75, relheight=0.2, x=10, y=15)


def selectFolder():
    filename = filedialog.askdirectory()
    label = tk.Label(frame2, text=filename, bg="white").place(
        relwidth=0.75, relheight=0.2, x=10, y=40)


def saveFolder():
    filename = filedialog.askdirectory()
    label = tk.Label(frame2, text=filename, bg="white").place(
        relwidth=0.75, relheight=0.2, x=10, y=65)


# ========================GUI LAYOUT==========================

canvas = tk.Canvas(root, width=600, height=90, bg="#375782").grid()
frame1 = tk.Frame(canvas, bg="white").place(
    relwidth=0.75, relheight=0.2, x=10, y=15)
frame2 = tk.Frame(canvas, bg="white").place(
    relwidth=0.75, relheight=0.2, x=10, y=40)
frame3 = tk.Frame(canvas, bg="white").place(
    relwidth=0.75, relheight=0.2, x=10, y=65)

photo = tk.Button(canvas, text="Select Photo", bg="white", command=selectPhoto).place(
    relwidth=0.2, relheight=0.2, x=475, y=15)
photoFolder = tk.Button(canvas, text="Select Photo Folder", bg="white", command=selectFolder).place(
    relwidth=0.2, relheight=0.2, x=475, y=40)
saveFolder = tk.Button(canvas, text="Select Save Folder", bg="white", command=saveFolder).place(
    relwidth=0.2, relheight=0.2, x=475, y=65)


root.mainloop()
