# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 13:17:20 2022

@author: Rere
"""

import cv2
import pytesseract
import imutils
import csv
import pytesseract as pt

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-ORC/tesseract'

# membaca file gambar
image = cv2.imread('D:/Kuliah S4/PCD/1.jpg, cv2.IMREAD_COLOR)

# mengubah lebar gambar menjadi 500px
image = imutils.resize(image, width=500)

# menampilkan gambar asli
cv2.imshow("Gambar Asli", image)
cv2.waitKey(0)

# konversi gambar RGB ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("1. Gambar Grayscale", gray)
cv2.waitKey(0)

# mengurangi noise dengan filter bilateral
gray = cv2.bilateralFilter(gray, 11, 17, 17)
cv2.imshow("2. Filter Bilateral(Reduksi Noise)", gray)
cv2.waitKey(0)

# deteksi tepi dari gambar grayscale
edge = cv2.Canny(gray, 30, 200)
cv2.imshow("3. Deteksi Tepi", edge)
cv2.waitKey(0)

# mencari kontur dari hasil deteksi tepi
contours, new = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1 = image.copy()
cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
cv2.imshow("4. Contours", img1)
cv2.waitKey(0)

# slices plat nomer yang telah terdeteksi
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
img1 = image.copy()
cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
cv2.imshow("5. Sorted", img1)
cv2.waitKey(0)

# inisialisasi kontur dan koordinat x,yx
NumberPlate = None
license_plate = None
x = None
y = None
w = None
h = None

count = 0
hasil = 7
# mencari kontur yang memiliki 4 sudut yang kemungkinan adalah plat nomor
for c in cnts:
    peri = cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        NumberPlateCnt = approx

        # Menyimpan Hasil Crop Plat
        x, y, w, h = cv.boundingRect(c)
        new_img = gray[y:y + h, x:x + w]
        cv.imwrite('D:\data/images/' + str("hasil") + '.png', new_img)

# menampilkan posisi plat nomor yang terdeteksi
cv2.drawContours(image, [NumberPlate], -1, (0, 255, 0), 3)
cv2.imshow("posisi plat nomor kendaraan yang terdeteksi", image)
cv2.waitKey(0)

break
cv.drawContours(image, [NumberPlateCnt], -1, (0, 255, 0), 3)
cv.imshow("Plat Nomer Yang Terdeteksi", image)

Cropped_img = "D:\data\images\hasil.png"
cv.imshow("Plat Nomer", cv.imread(Cropped_img))

#konversi gambar plat
plat = pytesseract.image_to_string(Cropped_img)
print('Number is:' + plat)

cv.waitKey(0)
