#Tugas Perhitungan
#Nama  : Ratna Dewi
#Nim   : D0221110
#Kelas : Informatika H

def luas_lingkaran(r):
    return 3.14*(r*r)

def luas_segitiga(alas, tinggi):
    return 1/2 *alas*tinggi

def luas_persegi(sisi):
    return sisi*sisi

print('''1. Lingkaran
2. Segitiga
3. Persegi''')

p = int(input("Masukkan luas bangun datar yang akan dicari:"))
if p == 1:
    r = float(input("Masukkan jari - jari :"))
    hasil = luas_lingkaran(r)
    print("Luas lingkatan adalah = ", hasil,"cm")

elif p == 2:
    alas = float(input("Masukkan alas segitiga:"))
    tinggi = float(input("Masukkan tinggi segitiga:"))
    hasil = luas_segitiga(alas, tinggi)
    print("Luas segitiga adalah = ", hasil,"cm")

elif p == 3:
    sisi = float(input("Masukkan sisi persegi:"))
    hasil = luas_persegi(sisi)
    print("luas persegi adalah:",hasil,"cm")

else:
    print(p, "Tidak ada di dalam pilihan!")



