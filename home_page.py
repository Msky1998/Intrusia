import customtkinter as ctk
from PIL import Image
import os
class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        image_path = os.path.join(os.path.dirname(__file__), 'images', 'cadenas.png')
        image_light = Image.open(image_path)
        my_image = ctk.CTkImage(light_image=image_light,size=(450,256))


        self.title_label = ctk.CTkLabel(self, text="Intrusia App", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.description_label = ctk.CTkLabel(self, text="Bienvenue dans notre système de détection d'intrusion réseau.", font=("Helvetica", 22))
        self.description_label.pack(pady=10)

        self.image_label = ctk.CTkLabel(self, image=my_image,text="")
        self.image_label.pack(pady=20)
