import tkinter as tk
from tkinter import filedialog, Text, messagebox, Toplevel, ttk
import os


import PIL
import face_recognition
import matplotlib.pyplot as plt
# =========================================Backend================================================================


class ImageFinder:
    def __init__(self, image_path, images_folder_path, save_folder_path):
        self.no_img_saved = 0
        self.no_img_compared = 0
        self.image_path = image_path
        self.images_folder_path = images_folder_path
        self.save_folder_path = save_folder_path

        self.image_train = face_recognition.load_image_file(self.image_path)
        self.encode_image_train = face_recognition.face_encodings(
            self.image_train)

    def match_images(self):
        for filename in os.listdir(self.images_folder_path):
            
            
            if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.JPG'):
                
            
                self.no_img_compared += 1
                image_query = face_recognition.load_image_file(
                    os.path.join(self.images_folder_path, filename))

                print(f"Image Number: {self.no_img_compared}")

                encode_image_query = face_recognition.face_encodings(
                    image_query)
                if len(encode_image_query) == 0:
                    face_locations = face_recognition.face_locations(image_query)
                    encode_image_query = face_recognition.face_encodings(image_query,known_face_locations=face_locations)
                    
                if len(encode_image_query) != 0:
                    print(f"For image: {filename}",len(encode_image_query))
                    for face in encode_image_query:
                        result = face_recognition.compare_faces(
                             [face],self.encode_image_train[0],tolerance=0.7)
                        print(result)
                        if result[0] == True:
                            self.no_img_saved += 1
                            print(f"saving image:{self.no_img_saved}")
                            im = PIL.Image.fromarray(image_query)
                            im = im.save(self.save_folder_path,f"your_pic_{self.no_img_saved}.jpg")
                            break
                else:
                    print(f"No faces found in {filename}")
        print("end")

# ============================================================================================================


# ==============================================FrontEnd======================================================
root = tk.Tk()
root.title("Face Sorter")


class MyGUI():

    def __init__(self):

        self.image_filename = ""  # image file path
        self.folder_path = ""  # path of folder where person's image is to be searched
        self.save_folder_path = ""  # path of folder where images are to be saved
        self.canvas = tk.Canvas(
            root, width=600, height=110, bg="#375782").grid()
        self.frame1 = tk.Frame(self.canvas, bg="white").place(
            relwidth=0.75, relheight=0.15, x=10, y=15)
        self.frame2 = tk.Frame(self.canvas, bg="white").place(
            relwidth=0.75, relheight=0.15, x=10, y=40)
        self.frame3 = tk.Frame(self.canvas, bg="white").place(
            relwidth=0.75, relheight=0.15, x=10, y=65)

        photo = tk.Button(self.canvas, text="Select Photo", bg="white", command=self.selectPhoto).place(
            relwidth=0.2, relheight=0.15, x=475, y=15)
        photoFolder = tk.Button(self.canvas, text="Select Photo Folder", bg="white", command=self.selectFolder).place(
            relwidth=0.2, relheight=0.15, x=475, y=40)
        saveFolder = tk.Button(self.canvas, text="Select Save Folder", bg="white", command=self.saveFolder).place(
            relwidth=0.2, relheight=0.15, x=475, y=65)
        start = tk.Button(self.canvas, text="Start", bg="white", command=self.startFunction).place(
            relwidth=0.2, relheight=0.15, x=245, y=90)

        root.mainloop()

    def selectPhoto(self):
        self.image_filename = filedialog.askopenfilename(
            initialdir="/", title="Select File", filetypes=[('JPG file (*.jpg)', '*.jpg'),
                                                           ('JPEG file (*.jpeg)',
                                                            '*.jpeg'),
                                                           ('PNG file (*.png)', '*.png')])
        label = tk.Label(self.frame1, text=self.image_filename, bg="white").place(
            relwidth=0.75, relheight=0.15, x=10, y=15)

    def selectFolder(self):
        self.folder_path = filedialog.askdirectory()
        label = tk.Label(self.frame2, text=self.folder_path, bg="white").place(
            relwidth=0.75, relheight=0.15, x=10, y=40)

    def saveFolder(self):
        self.save_folder_path = filedialog.askdirectory()
        label = tk.Label(self.frame3, text=self.save_folder_path, bg="white").place(
            relwidth=0.75, relheight=0.15, x=10, y=65)

    def startFunction(self):
        top = Toplevel()
        my_progress = ttk.Progressbar(
            top, orient="horizontal", length=400, mode='indeterminate', maximum=100, value=10)
        my_progress.pack()
        my_progress.start(10)
        imgFinder = ImageFinder(self.image_filename,
                                self.folder_path, self.save_folder_path)
        if imgFinder.encode_image_train is None:
            messagebox.showinfo('error', "Face Not found in train image")
        else:
            imgFinder.match_images()
        my_progress.stop()
        top.destroy()


# initializing MyGUI class
mygui = MyGUI()
