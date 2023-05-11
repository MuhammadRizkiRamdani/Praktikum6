import numpy as np                              # Mengimport library numpy
import imageio.v2 as imageio                     # Mengimport library imageio v2
import matplotlib.pyplot as plt                  # Mengimport library matplotlib untuk plot gambar

img = imageio.imread("image/riram.jpg")            # Membaca gambar dengan menggunakan imageio
img_height = img.shape[0]                         # Mendapatkan tinggi gambar
img_width = img.shape[1]                          # Mendapatkan lebar gambar
img_channel = img.shape[2]                        # Mendapatkan jumlah channel pada gambar (RGB/RGBA)

img_grayscale = np.zeros(img.shape, dtype=np.uint8)    # Membuat array kosong dengan tipe data uint8 dengan ukuran sama dengan gambar yang dibaca

for y in range(0, img_height):                    # Looping sebanyak tinggi gambar
    for x in range(0, img_width):                 # Looping sebanyak lebar gambar
        red = img[y][x][0]                       # Menyimpan nilai channel merah pada titik (y, x)
        green = img[y][x][1]                     # Menyimpan nilai channel hijau pada titik (y, x)
        blue = img[y][x][2]                      # Menyimpan nilai channel biru pada titik (y, x)
        gray = (int(red) + int(green) + int(blue)) / 3  # Menentukan nilai grayscale pada titik (y, x)
        img_grayscale[y][x] = (gray, gray, gray)  # Menyimpan nilai grayscale ke dalam array img_grayscale pada titik (y, x)

plt.imshow(img_grayscale)                         # Menampilkan gambar grayscale dengan menggunakan matplotlib
plt.title("Grayscale")                            # Memberikan judul pada gambar
plt.show()                                        # Menampilkan gambar pada layar


#Menampilkan Histogram Gambar Grayscale
hg = np.zeros((256))

#Menghitung nilai frekuensi kemunculan setiap nilai grayscale pada gambar
for x in range(0, 256):
    hg[x] = 0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hg[gray] += 1

#Menampilkan histogram gambar
bins = np.linspace(0, 256, 100)
plt.hist(hg, bins, color="black", alpha=0.5)
plt.title("Histogram")
plt.show()

#Menampilkan Histogram Gambar RGB
#Membuat variabel untuk menyimpan data gambar
hgr = np.zeros((256))
hgg = np.zeros((256))
hgb = np.zeros((256))
hgrgb = np.zeros((768))

#Mengisi histogram dengan nilai awal 0
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0

for x in range(0, 768):
    hgrgb[x] = 0

for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0

for x in range(0, 768):
    hgrgb[x] = 0

temp = [0]

#Melakukan iterasi pada setiap piksel gambar untuk menghitung histogram
for y in range(0, img.shape[0]):
    for x in range(0, img.shape[1]):
        red = int(img[y][x][0])
        green = int(img[y][x][1])
        blue = int(img[y][x][2])
#Menambahkan offset untuk green dan blue agar bisa dimasukkan ke dalam histogram gabungan
        green = green + 256
        blue = blue + 512
#Menghitung histogram untuk masing-masing channel dan gabungan
        hgrgb[red] += 1
        hgrgb[green] += 1
        hgrgb[blue] += 1

#Membuat bins untuk histogram gabungan
binsrgb = np.linspace(0, 768, 100)

#Menampilkan histogram gabungan
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)
plt.title("Histogram Red Green Blue")
plt.show()

#menghitung nilai histogram untuk masing-masing kanal warna
for y in range(0, img_height):
    for x in range(0, img_width):
        red = img[y][x][0]
        green = img[y][x][1]
        blue = img[y][x][2]
        hgr[red] += 1
        hgg[green] += 1
        hgb[blue] += 1

#menentukan batasan-batasan (bins) untuk histogram
bins = np.linspace(0, 256, 100)

#menampilkan histogram untuk kanal warna merah
plt.hist(hgr, bins, color="red", alpha=0.5)
plt.title("Histogram Red")
plt.show()

#menampilkan histogram untuk kanal warna hijau
plt.hist(hgg, bins, color="green", alpha=0.5)
plt.title("Histogram Green")
plt.show()

#menampilkan histogram untuk kanal warna biru
plt.hist(hgb, bins, color="blue", alpha=0.5)
plt.title("Histogram Blue")
plt.show()

#Inisialisasi array histogram dan kumulatif
hgk = np.zeros((256))
c = np.zeros((256))

#Mengisi array histogram dan kumulatif dengan nilai awal 0
for x in range(0, 256):
    hgk[x] = 0
    c[x] = 0

#Menghitung histogram gambar grayscale
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgk[gray] += 1

#Menghitung array kumulatif
c[0] = hgk[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgk[x]

#Menormalisasi array kumulatif dan menghitung nilai maksimum kumulatif
hmaxk = c[255]
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

#Menampilkan histogram kumulatif gambar grayscale
bins = np.linspace(0, 256, 100)
plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Kumulatif")
plt.show()

#Menampilkan Histogram Hequalisasi¶
#Inisialisasi array histogram
hgh = np.zeros((256))
h = np.zeros((256))
c = np.zeros((256))

#Set nilai awal histogram menjadi 0
for x in range(0, 256):
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

#Menghitung histogram gambar grayscale
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgh[gray] += 1

#Menghitung nilai kumulatif histogram
h[0] = hgh[0]
for x in range(1, 256):
     h[x] = h[x-1] + hgh[x]

#Normalisasi histogram
for x in range(0, 256):
     h[x] = h[x] / img_height / img_width

#Set nilai awal histogram menjadi 0 kembali
for x in range(0, 256):
    hgh[x] = 0

#Melakukan ekualisasi histogram
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

#Menghitung nilai kumulatif histogram yang telah di-ekualisasi
c[0] = hgh[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgh[x]

hmaxk = c[255] #Menghitung nilai maksimum histogram setelah di-ekualisasi

#Normalisasi histogram yang telah di-ekualisasi dan mengalikan dengan 190
for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

#Menampilkan histogram hasil ekualisasi
plt.hist(c, bins, color="black", alpha=0.5)
plt.title("Histogram Grayscale Hequalisasi")
plt.show()