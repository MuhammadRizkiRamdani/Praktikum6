#Import library
import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

img = imageio.imread("image/riram.jpg")        #Baca gambar dengan Imageio
img_height = img.shape[0]                     #Dapatkan nilai tinggi gambar
img_width = img.shape[1]                      #Dapatkan nilai lebar gambar
img_channel = img.shape[2]                    #Dapatkan nilai channel gambar

img_inversi = np.zeros(img.shape, dtype=np.uint8)     #Membuat variabel kosong dengan ukuran sama dengan gambar

def inversi_grayscale(nilai):                          #Definisikan fungsi inversi grayscale dengan satu parameter
    for y in range(0, img_height):                      #Looping setiap pixel di gambar untuk sumbu y
        for x in range(0, img_width):                   #Looping setiap pixel di gambar untuk sumbu x
            red = img[y][x][0]                          #Dapatkan nilai warna merah pada pixel tersebut
            green = img[y][x][1]                        #Dapatkan nilai warna hijau pada pixel tersebut
            blue = img[y][x][2]                         #Dapatkan nilai warna biru pada pixel tersebut
            gray = (int(red) + int(green) + int(blue)) / 3   #Hitung nilai rata-rata grayscale
            gray = nilai - gray                              #Lakukan inversi grayscale
            img_inversi[y][x] = (gray, gray, gray)           #Set nilai pada gambar inversi dengan gray

def inversi_rgb(nilai):                                 #Definisikan fungsi inversi RGB dengan satu parameter
    for y in range(0, img_height):                      #Looping setiap pixel di gambar untuk sumbu y
        for x in range(0, img_width):                   #Looping setiap pixel di gambar untuk sumbu x
            red = img[y][x][0]                          #Dapatkan nilai warna merah pada pixel tersebut
            red = nilai - red                           #Lakukan inversi warna merah
            green = img[y][x][1]                        #Dapatkan nilai warna hijau pada pixel tersebut
            green = nilai - green                       #Lakukan inversi warna hijau
            blue = img[y][x][2]                         #Dapatkan nilai warna biru pada pixel tersebut
            blue = nilai - blue                         #Lakukan inversi warna biru
            img_inversi[y][x] = (red, green, blue)      #Set nilai pada gambar inversi dengan nilai RGB yang baru

inversi_grayscale(255)                                 #Panggil fungsi inversi grayscale dengan parameter 255
plt.imshow(img_inversi)                                #Tampilkan gambar inversi grayscale
plt.title("Inversi Grayscale")                         #Tambahkan judul "Inversi Grayscale"
plt.show()                                             #Tampilkan gambar

inversi_rgb(255)                                       #Panggil fungsi inversi RGB dengan parameter 255
plt.imshow(img_inversi)                                #Tampilkan gambar inversi RGB
plt.title("Inversi RGB")                               #Tambahkan judul "Inversi RGB"
plt.show()                                             #Tampilkan gambar


#Log
#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8)

def log(c): #membuat fungsi log dengan parameter c
    for y in range(0, img_height): #looping untuk setiap baris citra
        for x in range(0, img_width): #looping untuk setiap kolom citra
            red = img[y][x][0] #mengambil nilai pixel warna merah di posisi y,x
            green = img[y][x][1] #mengambil nilai pixel warna hijau di posisi y,x
            blue = img[y][x][2] #mengambil nilai pixel warna biru di posisi y,x
            gray = (int(red) + int(green) + int(blue)) / 3 #menghitung rata-rata nilai dari tiga warna merah, hijau, biru
            gray = int(c * np.log(gray + 1)) #melakukan transformasi log terhadap nilai rata-rata tadi, kemudian dikalikan dengan parameter c, dan diubah ke tipe data integer
#jika nilai hasil transformasi log lebih dari 255, maka diatur menjadi 255
            if gray > 255:
                gray = 255
#jika nilai hasil transformasi log kurang dari 0, maka diatur menjadi 0
            if gray < 0:
                gray = 0
            img_log[y][x] = (gray, gray, gray) #memasukkan nilai gray ke variabel img_log pada posisi y,x, dengan nilai r,g,b yang sama

log(30) #memanggil fungsi log dengan parameter 30
#menampilkan citra hasil transformasi log
plt.imshow(img_log)
plt.title("Log")
plt.show()

#Inversi & Log
#Membuat variabel img_inlog untuk menampung hasil
img_inlog = np.zeros(img.shape, dtype=np.uint8)

#Mendefinisikan fungsi untuk inversi log
def inlog(c):

    #Looping untuk setiap pixel pada gambar
    for y in range(0, img_height):
        for x in range(0, img_width):
            #Mendapatkan nilai red, green, blue pada pixel (x,y)
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]

            #Menghitung nilai grayscale pada pixel (x,y)
            gray = (int(red) + int(green) + int(blue)) / 3

            #Transformasi inlog pada grayscale
            gray = int(c * np.log(255 - gray + 1))

            #Mengecek dan menyesuaikan nilai grayscale agar tidak melebihi atau kurang dari 0-255
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0

            #Memasukkan nilai grayscale baru ke dalam pixel (x,y) pada gambar hasil transformasi
            img_inlog[y][x] = (gray, gray, gray)


log(30)  #memanggil fungsi log dengan parameter 30
# menampilkan citra hasil iversi log
plt.imshow(img_inlog)
plt.title("Inversi & Log")
plt.show()

#Nth Power
#Membuat variabel img_nthpower untuk menampung hasil
img_nthpower = np.zeros(img.shape, dtype=np.uint8)

#Mendefinisikan fungsi untuk nth power
def nthpower(c, y):
#Menghitung variabel thc dan thy
    thc = c / 100
    thy = y / 100
    # Iterasi setiap piksel pada citra
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Mendapatkan nilai warna merah, hijau, dan biru dari piksel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]

            #Menghitung nilai keabuan
            gray = (int(red) + int(green) + int(blue)) / 3

            #Menghitung nilai keabuan hasil transformasi nth power
            gray = int(thc * pow(gray, thy))

            #Membatasi nilai keabuan di antara 0 dan 255
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0

            #Menyimpan nilai keabuan yang telah diubah ke dalam citra hasil transformasi
            img_nthpower[y][x] = (gray, gray, gray)


#Menampilkan hasil citra nth power
nthpower(50, 100)
plt.imshow(img_nthpower)
plt.title("Nth Power")
plt.show()

#Nth Root Power
#Membuat variabel img_nthrootpower
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)

#Membuat fungsi untuk nth root power
def nthrootpower(c, y):
#Menghitung variabel thc dan thy
    thc = c / 100
    thy = y / 100

#Looping setiap pixel gambar untuk menghitung gray scale dan mengaplikasikan formula nth root power
    for y in range(0, img_height):
        for x in range(0, img_width):
#Mendapatkan nilai Red, Green, dan Blue dari setiap pixel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]

        #Menghitung nilai rata-rata dari Red, Green, dan Blue untuk mendapatkan gray scale
        gray = (int(red) + int(green) + int(blue)) / 3

        #Menghitung nilai gray scale dengan formula nth root power dan mengubahnya menjadi integer
        gray = int(thc * pow(gray, 1. / thy))

        #Membatasi nilai gray scale agar tidak melebihi 255 atau kurang dari 0
        if gray > 255:
            gray = 255
        if gray < 0:
            gray = 0

        #Menetapkan nilai gray scale ke setiap pixel pada img_nthpower
        img_nthpower[y][x] = (gray, gray, gray)

#Menampilkan hasil citra nth root power
nthrootpower(50, 100)
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()