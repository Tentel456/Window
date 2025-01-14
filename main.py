import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Изображение справа")
root.geometry("800x600")  


image_path = "photo.jpg"  
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)


label = tk.Label(root, image=photo)
label.pack(side=tk.RIGHT, padx=10, pady=10)


root.mainloop()
