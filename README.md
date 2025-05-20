# DasarAlgoritmaDanPemrograman-BisDig1)
Studi Kasus: Anda diminta membuat fungsi untuk menghitung faktorial dari suatu bilangan menggunakan metode rekursif. Pertanyaan: Jelaskan manfaat penggunaan fungsi dan bagaimana rekursi bekerja dalam menghitung faktorial. Buatlah program Python yang menggunakan fungsi rekursif untuk menghitung faktorial dari angka yang dimasukkan.

Manfaat Penggunaan Fungsi:

Modularitas: Memecah program menjadi bagian-bagian kecil yang lebih mudah dikelola
Reusability: Dapat digunakan kembali tanpa menulis ulang kode
Abstraksi: Menyembunyikan kompleksitas implementasi
Readability: Membuat kode lebih mudah dibaca dan dipahami
Cara Kerja Rekursi:

Rekursi adalah teknik di mana fungsi memanggil dirinya sendiri. Dalam menghitung faktorial:

Fungsi akan memanggil dirinya sendiri dengan nilai yang lebih kecil
Proses berlanjut hingga mencapai base case (n = 0 atau 1)
Kemudian hasilnya dihitung mundur melalui tumpukan pemanggilan
2) Studi Kasus: Seorang guru ingin membuat sistem input nilai 5 siswa dan mencari nilai tertinggi. Pertanyaan: Jelaskan penggunaan perulangan dan array dalam kasus ini. Buat program Python untuk menerima input nilai ke dalam list dan menampilkan nilai tertinggi serta siswa ke berapa yang mendapatkannya.

Pemjelasan penggunaan perulangan dan array

1) Menggunakan array list : Digunakan untuk menyimpan nilai siswa secara terstruktur 2) Selanjutnya Perulangan menggunakan foor loop ( Jumlah yang diketahui ) dan while loop ( Validasi ) untuk menginput nilai secara otomatis. 3) Selanjutnya mencari nilai tertinggi menggunakan max() dan index () 4) Terakhir output hasil untuk menghasilkan nilai tertinggi siswa yang mendapatkannya.

3) Studi Kasus: Dalam sistem e-commerce, pelanggan mendapatkan diskon 10% jika belanja di atas Rp500.000. Pertanyaan: Jelaskan bagaimana struktur kontrol percabangan digunakan untuk logika pemberian diskon. Buatlah program yang menghitung total bayar setelah diskon jika syarat terpenuhi.

sistem diskon e-commerce menggunakan percabangan (if-else), dilengkapi analogi, contoh kode Python, dan ilustrasi proses Sistem ini memberikan diskon 10% jika total belanja pelanggan melebihi Rp500.000. Komponen utama:

Input: Total belanja (angka)
Proses: Cek kondisi belanja > Rp500.000
Output: Total akhir setelah diskon (jika ada)
Real Life Example Belanja Rp500.000 → Dapet diskon Rp50.000 → Bayar Rp450.000 Kasus 2: Belanja Rp450.000 → Gak dapet diskon → Bayar Rp450.000 jadi, jika total belanja nya besar dapat potongan dan jika totalnya kecil dapat potongannya normal.
