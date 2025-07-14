from PIL import Image
import numpy as np
 #Loading the stego image
img = Image.open('stego_image.png')
img = img.convert('RGB')
pixels = np.array(img)
flat_pixels = pixels.flatten()

#Extracting LSB (first 256 bits)
binary_hash = ''
for i in range(256):
    binary_hash += str(flat_pixels[i] & 1)

print("Binary hash extracted:")
print(binary_hash)

#Converting binary to hex hash
hex_hash = ''
for i in range(0, 256, 4):
    nibble = binary_hash[i:i+4]
    hex_char = hex(int(nibble, 2))[2:]  # Remove '0x'
    hex_hash += hex_char

print("Reconstructed SHA-256 hash:")
print(hex_hash)