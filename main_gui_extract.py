import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import hashlib

def extract_and_verify():
    try:
        #Getting the  stego image path
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if not image_path:
            return

        img = Image.open(image_path)
        img = img.convert("RGB")
        pixels = np.array(img)
        flat_pixels = pixels.flatten()

        #Extracting the LSB bits
        binary_hash = ""
        for i in range(256):
            binary_hash += str(flat_pixels[i] & 1)

        #Converting to hex SHA-256 hash
        extracted_hash = hex(int(binary_hash, 2))[2:].zfill(64)

        #Optional comparison
        compare = messagebox.askyesno("Compare", "Do you want to verify this hash with a text file?")
        if compare:
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    file_hash = hashlib.sha256(content.encode()).hexdigest()

                if extracted_hash == file_hash:
                    messagebox.showinfo("✅ Verified", "Hash matches. Ownership verified!")
                else:
                    messagebox.showerror("❌ Not Verified", "Hash does not match. This is not the original file.")
        else:
            messagebox.showinfo("Extracted Hash", f"SHA-256 Hash:\n{extracted_hash}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
window = tk.Tk()
window.title("Aayush's Ownership Verifier 🕵️‍♂️")
window.geometry("380x180")

tk.Label(window, text="Extract & Verify Ownership from Image", font=("Arial", 12, "bold")).pack(pady=15)
tk.Button(window, text="🖼️ Select Stego Image", command=extract_and_verify, bg="green", fg="white").pack(pady=10)

window.mainloop()
