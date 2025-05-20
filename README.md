# DasarAlgoritmaDanPemrograman-BisDig1)
1) Studi Kasus: Anda diminta membuat fungsi untuk menghitung faktorial dari suatu bilangan menggunakan metode rekursif. Pertanyaan: Jelaskan manfaat penggunaan fungsi dan bagaimana rekursi bekerja dalam menghitung faktorial. Buatlah program Python yang menggunakan fungsi rekursif untuk menghitung faktorial dari angka yang dimasukkan.

Manfaat Penggunaan Fungsi:
- Modularitas: Memecah program menjadi bagian-bagian kecil yang lebih mudah dikelola
- Reusability: Dapat digunakan kembali tanpa menulis ulang kode
- Abstraksi: Menyembunyikan kompleksitas implementasi
- Readability: Membuat kode lebih mudah dibaca dan dipahami
  
Cara Kerja Rekursi:
Rekursi adalah teknik di mana fungsi memanggil dirinya sendiri. 
Dalam menghitung faktorial:
- Fungsi akan memanggil dirinya sendiri dengan nilai yang lebih kecil
- Proses berlanjut hingga mencapai base case (n = 0 atau 1)
- Kemudian hasilnya dihitung mundur melalui tumpukan pemanggilan

2) Studi Kasus: Seorang guru ingin membuat sistem input nilai 5 siswa dan mencari nilai tertinggi. Pertanyaan: Jelaskan penggunaan perulangan dan array dalam kasus ini. Buat program Python untuk menerima input nilai ke dalam list dan menampilkan nilai tertinggi serta siswa ke berapa yang mendapatkannya.

Pemjelasan penggunaan perulangan dan array
- Menggunakan array list : Digunakan untuk menyimpan nilai siswa secara terstruktur
- Selanjutnya Perulangan menggunakan foor loop ( Jumlah yang diketahui ) dan while loop ( Validasi ) untuk menginput nilai secara otomatis.
- Selanjutnya mencari nilai tertinggi menggunakan max() dan index ()
- Terakhir output hasil untuk menghasilkan nilai tertinggi siswa yang mendapatkannya.

3) Studi Kasus: Dalam sistem e-commerce, pelanggan mendapatkan diskon 10% jika belanja di atas Rp500.000. Pertanyaan: Jelaskan bagaimana struktur kontrol percabangan digunakan untuk logika pemberian diskon. Buatlah program yang menghitung total bayar setelah diskon jika syarat terpenuhi.
sistem diskon e-commerce menggunakan percabangan (if-else), dilengkapi analogi, contoh kode Python, dan ilustrasi proses Sistem ini memberikan diskon 10% jika total belanja pelanggan melebihi Rp500.000.

Komponen utama:
- Input: Total belanja (angka)
- Proses: Cek kondisi belanja > Rp500.000
- Output: Total akhir setelah diskon (jika ada)
Real Life Example Belanja Rp500.000 → Dapet diskon Rp50.000 → Bayar Rp450.000 Kasus 2: Belanja Rp450.000 → Gak dapet diskon → Bayar Rp450.000 
jadi, jika total belanja nya besar dapat potongan dan jika totalnya kecil dapat potongannya normal.

5) Studi Kasus: Seorang kasir toko ingin sistem sederhana untuk menghitung total harga pembelian 3 barang dan menampilkan totalnya. Pertanyaan: Jelaskan langkah-langkah algoritma untuk menyelesaikan masalah tersebut. Buatlah program Python sederhana yang membaca harga 3 barang dan menampilkan total pembayaran.

Program Kasir Sederhana
Program Python untuk menghitung total harga pembelian 3 barang.

Deskripsi Program
Program ini memungkinkan kasir untuk:
- Memasukkan harga 3 barang berbeda
- Menghitung total harga secara otomatis
- Menampilkan total dalam format mata uang Rupiah

Mulai program
- Input harga barang pertama (disimpan di variabel harga1)
- Input harga barang kedua (disimpan di variabel harga2)
- Input harga barang ketiga (disimpan di variabel harga3)
- Hitung total = harga1 + harga2 + harga3
- Tampilkan total harga dalam format Rp X.XXX,XX Program selesai

5) Seorang siswa ingin mengetahui apakah nilai ujiannya memenuhi syarat lulus berdasarkan rata-rata nilai dari 3 mata pelajaran. Pertanyaan: Jelaskan peran tipe data dan operator dalam menyelesaikan perhitungan tersebut. Buatlah program Python yang menghitung rata-rata dan menampilkan status kelulusan (lulus jika rata-rata ≥ 75).

Program 1: Kasir Sederhana
Fungsi: Menghitung total harga dari 3 barang yang dibeli.
Fitur:
- Input harga untuk 3 barang
- Validasi input (harus angka positif)
- Perhitungan total otomatis
- Tampilan hasil dengan format mata uang

Program 2: Penentuan Kelulusan
Fungsi: Menentukan kelulusan siswa berdasarkan rata-rata 3 nilai mata pelajaran.
Fitur:
Input 3 nilai ujian : 
- Validasi input (harus antara 0-100)
- Perhitungan rata-rata
- Penentuan status kelulusan (≥75 lulus)
- Tampilan rata-rata dan status

Konsep yang Digunakan : 
- Tipe data dasar (float, string, boolean)
- Operator (aritmatika, perbandingan)
- Struktur kontrol (kondisional)
- Input/output dasar
- Validasi input
