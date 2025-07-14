# 🛡️ Text File Ownership Protection Using SHA-256 + LSB Steganography

> A beginner-friendly Python GUI tool to prove **ownership of any text file** by embedding its cryptographic fingerprint inside an image using **LSB steganography**.

---

## 🔍 What This Project Does

1. You choose a **text file** you want to protect.
2. The app generates a **SHA-256 hash** (unique digital fingerprint).
3. That hash is embedded **invisibly into a PNG/JPG image** using **Least Significant Bit (LSB)** steganography.
4. You get a stego-image — anyone can see the image, but only you can prove you owned the original text.
5. You can later extract the hash from the image to **verify** ownership.

---

## 🛠️ Technologies Used

- **Python 3**
- `hashlib` – for SHA-256 hash generation
- `PIL` (Pillow) – for image processing
- `numpy` – to handle image pixel data
- `tkinter` – to build the GUI

---

## 🖥️ How to Use

### 1️⃣ Embed Ownership

```bash
python main_gui_embed.py

