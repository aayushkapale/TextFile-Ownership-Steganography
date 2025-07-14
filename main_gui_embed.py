import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import hashlib
import numpy as np

# This is the main mbedding function 
def embed_ownership_proof():
    if not user_text_file.get() or not input_image_path.get():
        messagebox.showerror("Missing Input", "Please select both a text file and an image.")
        return

    try:
        #Reading user's text file and generating SHA-256 hash
        with open(user_text_file.get(), 'r') as f:
            data = f.read()
        hash_result = hashlib.sha256(data.encode()).hexdigest()
        binary_hash = bin(int(hash_result, 16))[2:].zfill(256)

        #Opening and preparing the image
        image = Image.open(input_image_path.get()).convert('RGB')
        pixel_data = np.array(image)
        flat_data = pixel_data.flatten().astype(int)

        #Embedding binary hash into the  image
        if len(binary_hash) > len(flat_data):
            messagebox.showerror("Image Too Small", "Selected image does not have enough space to store the hash.")
            return

        for i in range(256):
            flat_data[i] = (flat_data[i] & ~1) | int(binary_hash[i])

        flat_data = flat_data.astype(np.uint8)
        modified_pixels = flat_data.reshape(pixel_data.shape)
        stego_image = Image.fromarray(modified_pixels)

        #Saving the image with a custom name
        stego_image.save("Aayush_stego_image.png")
        messagebox.showinfo("Success", "Hash embedded successfully!\nSaved as Aayush_stego_image.png")

    except Exception as err:
        messagebox.showerror("Error", str(err))

# This is the  GUI Setup
window = tk.Tk()
window.title("Aayush's File Ownership Locker 🔐")
window.geometry("430x300")

user_text_file = tk.StringVar()
input_image_path = tk.StringVar()

#GUI Header
tk.Label(window, text="Secure Your Files with Hash-Lock", font=("Arial", 12, "bold")).pack(pady=10)

#Browsing text file
tk.Label(window, text="Text File:").pack()
tk.Entry(window, textvariable=user_text_file, width=45).pack()
tk.Button(window, text="Browse Text File", command=lambda: user_text_file.set(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]))).pack(pady=5)

#Browsing image
tk.Label(window, text="Cover Image:").pack()
tk.Entry(window, textvariable=input_image_path, width=45).pack()
tk.Button(window, text="Browse Cover Image", command=lambda: input_image_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")]))).pack(pady=5)

#Embed button
tk.Button(window, text="🔐 Embed Ownership Hash", command=embed_ownership_proof, bg="purple", fg="white").pack(pady=15)

window.mainloop()
