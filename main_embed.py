from PIL import Image
import hashlib
import numpy as np

file_path = 'file.txt'  
with open(file_path, 'r') as file:
    content = file.read()

print("File content read successfully:")
print(content)

#Generating SHA hash of the content
hash_value = hashlib.sha256(content.encode()).hexdigest()
print("SHA-256 Hash generated:")
print(hash_value)
#Converting hash to binary
binary_hash = ''
for char in hash_value:
    binary_hash += format(int(char, 16), '04b')

print("Binary Hash:")
print(binary_hash)
print(f"Total bits: {len(binary_hash)}")  

#Loading and flattening the image
img = Image.open('cover_image.png')
img = img.convert('RGB')  
pixels = np.array(img)
flat_pixels = pixels.flatten()

print(f"Total available bits in image: {len(flat_pixels)}")
if len(binary_hash) > len(flat_pixels):
    print("❌ Error: Image too small to embed the hash!")
    exit()

# Embedding binary hash in the LSB of pixel data
flat_pixels = flat_pixels.astype(int)
for i in range(len(binary_hash)):
    flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_hash[i])

print("Hash successfully embedded in image pixels.")

#Reshaping and Saving the image 
flat_pixels = flat_pixels.astype(np.uint8)
new_pixels = flat_pixels.reshape(pixels.shape)

stego_img = Image.fromarray(new_pixels)
stego_img.save('stego_image.png')
print("Stego image saved as 'stego_image.png'.")
