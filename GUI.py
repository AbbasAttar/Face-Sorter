import tkinter as tk
from tkinter import filedialog, Text
import os


import cv2
import face_recognition
import matplotlib.pyplot as plt


#=========================================Backend================================================================
class ImageFinder():
    def __init__(self,image_path,images_folder_path):
        self.no_img_saved=0
        self.no_img_compared=0
        self.image_path = image_path
        self.images_folder_path = images_folder_path
        
        self.image_train = face_recognition.load_image_file(self.image_path)
        self.image_train_converted = cv2.cvtColor(self.image_train,cv2.COLOR_BGR2RGB)
        
        self.encode_image_train = face_recognition.face_encodings(self.image_train_converted)
        
        

        
    def match_images(self):

        for filename in os.listdir(self.images_folder_path):
            self.no_img_compared+=1
            image_query = face_recognition.load_image_file(os.path.join(self.images_folder_path,filename))
            image_query_converted = cv2.cvtColor(image_query,cv2.COLOR_BGR2RGB)
            print(f"Image Number: {no_img_compared}")
       
            encode_image_query = face_recognition.face_encodings(image_query_converted)
       
            if encode_image_query is not None:
                for face in encode_image_query:
                    if(self.compare(self.encode_image_train[0],face)):
                        self.no_img_saved+=1
                        print(f"saving image:{no_img_saved}")
                        cv2.imwrite(f"{save_folder_path}//your_pic_{no_img_saved}.jpg",image_query_converted)
                        break
    
    def compare(self,encode_base,encode_target):
        return face_recognition.compare_faces([encode_base],encode_target)
    
#============================================================================================================


#==============================================FrontEnd======================================================
root = tk.Tk()
root.title("Face Sorter")



class MyGUI():
    
    def __init__(self):
        
        self.image_filename=""   #image file path
        self.folder_path=""      #path of folder where person's image is to be searched
        self.save_folder_path="" #path of folder where images are to be saved
        
        
    def selectPhoto(self):
        self.image_filename = filedialog.askopenfilename(
            initialdir="/", title="Select File", filetype=[('JPG file (*.jpg)', '*.jpg'),
                                                           ('JPEG file (*.jpeg)',
                                                            '*.jpeg'),
                                                           ('PNG file (*.png)', '*.png')])
        label = tk.Label(frame1, text=self.image_filename, bg="white").place(
            relwidth=0.75, relheight=0.2, x=10, y=15)


    def selectFolder(self):
        self.folder_path = filedialog.askdirectory()
        label = tk.Label(frame2, text=self.folder_path, bg="white").place(
            relwidth=0.75, relheight=0.2, x=10, y=40)


    def saveFolder(self):
        self.save_folder_path = filedialog.askdirectory()
        label = tk.Label(frame2, text=self.save_folder_path, bg="white").place(
            relwidth=0.75, relheight=0.2, x=10, y=65)
        #imgFinder = ImageFinder(image_filename,folder_path)
        #imgFinder.match_images()
        
    def runGUI(self):
        
        canvas = tk.Canvas(root, width=600, height=90, bg="#375782").grid()
        frame1 = tk.Frame(canvas, bg="white").place(
            relwidth=0.75, relheight=0.2, x=10, y=15)
        frame2 = tk.Frame(canvas, bg="white").place(
            relwidth=0.75, relheight=0.2, x=10, y=40)
        frame3 = tk.Frame(canvas, bg="white").place(
            relwidth=0.75, relheight=0.2, x=10, y=65)

        photo = tk.Button(canvas, text="Select Photo", bg="white", command=self.selectPhoto).place(
            relwidth=0.2, relheight=0.2, x=475, y=15)
        photoFolder = tk.Button(canvas, text="Select Photo Folder", bg="white", command=self.selectFolder).place(
            relwidth=0.2, relheight=0.2, x=475, y=40)
        saveFolder = tk.Button(canvas, text="Select Save Folder", bg="white", command=self.saveFolder).place(
            relwidth=0.2, relheight=0.2, x=475, y=65)


        root.mainloop()
#initializing MyGUI class
mygui = MyGUI()
mygui.runGUI()
# ========================GUI LAYOUT==========================
