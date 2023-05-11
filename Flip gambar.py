# Mengimport library
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

# Membaca gambar menggunakan imageio
img = imageio.imread("image/riram.jpg")

# Mendapatkan resolusi, channel, dan tipe dari gambar
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

# Membuat variabel kosong untuk menyimpan hasil flip horizontal dan vertical
img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)

# Melakukan flipping secara horizontal
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]

# Melakukan flipping secara vertical
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]

# Menampilkan hasil flipping secara horizontal
plt.imshow(img_flip_horizontal)
plt.title("Flip Horizontal")
plt.show()

# Menampilkan hasil flipping secara vertical
plt.imshow(img_flip_vertical)
plt.title("Flip Vertical")
plt.show()