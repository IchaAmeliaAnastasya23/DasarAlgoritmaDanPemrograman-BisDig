# -*- coding: utf-8 -*-
"""UTS ICHA AMELIA ANASTASYA 24110310040

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11NOhLc2lxHOjpcBelGAy1EoHbyKXJock

Nama : Icha Amelia Anastasya
NIM 24110310040
2B Bisnis digital
ALGORITMA DAN PEMORGRAMAN

1) Studi Kasus:
Anda diminta membuat fungsi untuk menghitung faktorial dari suatu bilangan menggunakan metode rekursif.
Pertanyaan:
Jelaskan manfaat penggunaan fungsi dan bagaimana rekursi bekerja dalam menghitung faktorial. Buatlah program Python yang menggunakan fungsi rekursif untuk menghitung faktorial dari angka yang dimasukkan.

# Manfaat Penggunaan Fungsi:

1. Modularitas: Memecah program menjadi bagian-bagian kecil yang lebih mudah dikelola
2. Reusability: Dapat digunakan kembali tanpa menulis ulang kode
3. Abstraksi: Menyembunyikan kompleksitas implementasi
4. Readability: Membuat kode lebih mudah dibaca dan dipahami

# Cara Kerja Rekursi:

Rekursi adalah teknik di mana fungsi memanggil dirinya sendiri. Dalam menghitung faktorial:

1. Fungsi akan memanggil dirinya sendiri dengan nilai yang lebih kecil
2. Proses berlanjut hingga mencapai base case (n = 0 atau 1)
3. Kemudian hasilnya dihitung mundur melalui tumpukan pemanggilan

2) Studi Kasus:
Seorang guru ingin membuat sistem input nilai 5 siswa dan mencari nilai tertinggi.
Pertanyaan:
Jelaskan penggunaan perulangan dan array dalam kasus ini. Buat program Python untuk menerima input nilai ke dalam list dan menampilkan nilai tertinggi serta siswa ke berapa yang mendapatkannya.

# Pemjelasan penggunaan perulangan dan array
1) Menggunakan array list : Digunakan untuk menyimpan nilai siswa secara terstruktur
2) Selanjutnya Perulangan menggunakan foor loop ( Jumlah yang diketahui )  dan while loop ( Validasi ) untuk menginput nilai secara otomatis.
3) Selanjutnya mencari nilai tertinggi menggunakan max() dan index ()
4) Terakhir output hasil untuk menghasilkan nilai tertinggi siswa yang mendapatkannya.

3) Studi Kasus:
Dalam sistem e-commerce, pelanggan mendapatkan diskon 10% jika belanja di atas Rp500.000.
Pertanyaan:
Jelaskan bagaimana struktur kontrol percabangan digunakan untuk logika pemberian diskon. Buatlah program yang menghitung total bayar setelah diskon jika syarat terpenuhi.

sistem diskon e-commerce menggunakan percabangan (if-else), dilengkapi analogi, contoh kode Python, dan ilustrasi proses
Sistem ini memberikan diskon 10% jika total belanja pelanggan melebihi Rp500.000.
Komponen utama:
1. Input: Total belanja (angka)
2. Proses: Cek kondisi belanja > Rp500.000
3. Output: Total akhir setelah diskon (jika ada)

Real Life Example
Belanja Rp500.000 → Dapet diskon Rp50.000 → Bayar Rp450.000
Kasus 2:
Belanja Rp450.000 → Gak dapet diskon → Bayar Rp450.000
jadi, jika total belanja nya besar dapat potongan dan jika totalnya kecil dapat potongannya normal.

4) Studi Kasus:
Seorang kasir toko ingin sistem sederhana untuk menghitung total harga pembelian 3 barang dan menampilkan totalnya.
Pertanyaan:
Jelaskan langkah-langkah algoritma untuk menyelesaikan masalah tersebut. Buatlah program Python sederhana yang membaca harga 3 barang dan menampilkan total pembayaran.

# Program Kasir Sederhana

Program Python untuk menghitung total harga pembelian 3 barang.

## Deskripsi Program
Program ini memungkinkan kasir untuk:
1. Memasukkan harga 3 barang berbeda
2. Menghitung total harga secara otomatis
3. Menampilkan total dalam format mata uang Rupiah

## Algoritma Program
1. Mulai program
2. Input harga barang pertama (disimpan di variabel `harga1`)
3. Input harga barang kedua (disimpan di variabel `harga2`)
4. Input harga barang ketiga (disimpan di variabel `harga3`)
5. Hitung total = harga1 + harga2 + harga3
6. Tampilkan total harga dalam format Rp X.XXX,XX
7. Program selesai

## Cara Menggunakan
1. Pastikan Python 3 terinstall di komputer Anda
2. Clone repository ini atau download file `kasir_sederhana.py`
3. Buka terminal/command prompt
4. Navigasi ke direktori file
5. Jalankan program dengan perintah:

5) Seorang siswa ingin mengetahui apakah nilai ujiannya memenuhi syarat lulus berdasarkan rata-rata nilai dari 3 mata pelajaran.
Pertanyaan:
Jelaskan peran tipe data dan operator dalam menyelesaikan perhitungan tersebut. Buatlah program Python yang menghitung rata-rata dan menampilkan status kelulusan (lulus jika rata-rata ≥ 75).

## Program 1: Kasir Sederhana

**Fungsi**: Menghitung total harga dari 3 barang yang dibeli.

**Fitur**:
- Input harga untuk 3 barang
- Validasi input (harus angka positif)
- Perhitungan total otomatis
- Tampilan hasil dengan format mata uang

**Cara Menjalankan**:

## Program 2: Penentuan Kelulusan

**Fungsi**: Menentukan kelulusan siswa berdasarkan rata-rata 3 nilai mata pelajaran.

**Fitur**:
- Input 3 nilai ujian
- Validasi input (harus antara 0-100)
- Perhitungan rata-rata
- Penentuan status kelulusan (≥75 lulus)
- Tampilan rata-rata dan status

**Cara Menjalankan**:

## Konsep yang Digunakan

- Tipe data dasar (float, string, boolean)
- Operator (aritmatika, perbandingan)
- Struktur kontrol (kondisional)
- Input/output dasar
- Validasi input
"""

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

# Input dari user
angka = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))
print(f"Faktorial dari {angka} adalah {faktorial(angka)}")

nilai_siswa = []

# Input nilai 5 siswa
for i in range(5):
    nilai = float(input(f"Masukkan nilai siswa ke-{i+1}: "))
    nilai_siswa.append(nilai)

# Mencari nilai tertinggi
nilai_tertinggi = max(nilai_siswa)
index_siswa = nilai_siswa.index(nilai_tertinggi) + 1

print(f"Nilai tertinggi adalah {nilai_tertinggi} diperoleh oleh siswa ke-{index_siswa}")

# Input total belanja dengan validasi
while True:
    try:
        total_belanja = float(input("Total belanja: Rp"))
        if total_belanja >= 0:
            break
        else:
            print("Total tidak boleh negatif!")
    except ValueError:
        print("Masukkan angka yang valid!")

# Logika diskon
if total_belanja > 500000:
    diskon = total_belanja * 0.1
    total_bayar = total_belanja - diskon
    print(f"\nSelamat! Anda dapat diskon 10%")
    print(f"Diskon: Rp{diskon:,.2f}")
else:
    total_bayar = total_belanja
    print("\nBelanja kembali untuk dapat diskon 10%!")

# Format output dengan separator ribuan
print(f"Total belanja: Rp{total_belanja:,.2f}")
print(f"Total bayar: Rp{total_bayar:,.2f}")

nilai_siswa = []

# Input nilai menggunakan perulangan
for i in range(5):
    while True:
        try:
            nilai = float(input(f"Nilai siswa ke-{i+1}: "))
            if 0 <= nilai <= 100:  # Validasi nilai
                nilai_siswa.append(nilai)
                break
            else:
                print("Nilai harus antara 0-100!")
        except ValueError:
            print("Masukkan angka yang valid!")

# Mencari nilai tertinggi dan indeksnya
nilai_tertinggi = -1
indeks_tertinggi = -1

for indeks, nilai in enumerate(nilai_siswa):
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai
        indeks_tertinggi = indeks

# Output hasil
print(f"\nNilai tertinggi: {nilai_tertinggi}")
print(f"Diraih oleh siswa ke-{indeks_tertinggi + 1}")

# Program menghitung total harga 3 barang
print("Program Kasir Sederhana")
print("-----------------------")

# Input harga barang dengan validasi
try:
    harga1 = float(input("Masukkan harga barang pertama: "))
    harga2 = float(input("Masukkan harga barang kedua: "))
    harga3 = float(input("Masukkan harga barang ketiga: "))

    # Validasi input tidak negatif
    if harga1 < 0 or harga2 < 0 or harga3 < 0:
        raise ValueError("Harga tidak boleh negatif")

    # Menghitung total
    total = harga1 + harga2 + harga3

    # Menampilkan hasil dengan format mata uang
    print(f"Total harga pembelian adalah: Rp {total:,.2f}")

except ValueError as e:
    print(f"Error: {e}. Masukkan angka yang valid.")

# Program penentuan kelulusan berdasarkan rata-rata nilai
print("Program Penentuan Kelulusan")
print("--------------------------")

# Input nilai dengan validasi
try:
    nilai1 = float(input("Masukkan nilai mata pelajaran pertama (0-100): "))
    nilai2 = float(input("Masukkan nilai mata pelajaran kedua (0-100): "))
    nilai3 = float(input("Masukkan nilai mata pelajaran ketiga (0-100): "))

    # Validasi range nilai
    if not (0 <= nilai1 <= 100) or not (0 <= nilai2 <= 100) or not (0 <= nilai3 <= 100):
        raise ValueError("Nilai harus antara 0 sampai 100")

    # Menghitung rata-rata
    rata_rata = (nilai1 + nilai2 + nilai3) / 3

    # Menentukan kelulusan
    status = "Lulus" if rata_rata >= 75 else "Tidak Lulus"

    # Menampilkan hasil
    print(f"Rata-rata nilai: {rata_rata:.2f}")
    print(f"Status: {status}")

except ValueError as e:
    print(f"Error: {e}. Masukkan nilai yang valid.")