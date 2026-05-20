JUDUL >> Sistem Penyimpanan Nilai Siswa

DESKRIPSI SINGKAT >> Program ini dibuat untuk mengelola data nilai siswa. Program memiliki fitur untuk menambahkan nilai, mencari nilai tertentu,
menampilkan data menggunakan traversal inorder, preorder, dan postorder, serta mencari nilai tertinggi, nilai terendah, jumlah data, dan total seluruh nilai siswa.
Data disusun secara otomatis mengikuti aturan BST, yaitu nilai yang lebih kecil berada di kiri dan nilai yang lebih besar berada di kanan sehingga proses 
pengolahan data menjadi lebih cepat dan terstruktur. 

SOURCE CODE >> 
<img width="792" height="872" alt="Screenshot 2026-05-21 002039" src="https://github.com/user-attachments/assets/bb74fcb3-ec58-432b-a445-b04204bd75b0" />
<img width="581" height="762" alt="Screenshot 2026-05-21 002101" src="https://github.com/user-attachments/assets/ac8ee0c3-2e5b-476d-97ab-8dde4d91f0c7" />
<img width="832" height="756" alt="Screenshot 2026-05-21 002123" src="https://github.com/user-attachments/assets/54c44293-542b-49f6-a6d7-2a45953adf2d" />
<img width="681" height="803" alt="Screenshot 2026-05-21 002146" src="https://github.com/user-attachments/assets/8f37f2a2-a855-4826-b5f0-24156b3889f5" />
<img width="823" height="836" alt="Screenshot 2026-05-21 002205" src="https://github.com/user-attachments/assets/bddf984a-ba1e-465c-821f-99da4d8536ae" />
<img width="810" height="335" alt="Screenshot 2026-05-21 002223" src="https://github.com/user-attachments/assets/a8c1b74a-c200-4d84-aa18-dea6d98f6c1f" />

PENJELASAN >>
__init__(self, nilai) pada class Siswa
Fungsi ini digunakan sebagai constructor untuk membuat node baru pada Binary Search Tree (BST). Setiap node menyimpan satu data nilai siswa pada atribut nilai, lalu memiliki dua cabang yaitu kiri dan kanan yang awalnya bernilai None. Cabang kiri nantinya digunakan untuk menyimpan nilai yang lebih kecil, sedangkan cabang kanan untuk nilai yang lebih besar.

__init__(self) pada class DataNilaiSiswa
Fungsi ini digunakan untuk menginisialisasi BST. Variabel root diatur menjadi None karena pada awal program pohon masih kosong dan belum memiliki data nilai siswa.

tambah_nilai_node(self, root, nilai)
Fungsi ini digunakan untuk menambahkan data nilai siswa ke dalam BST secara rekursif. Jika posisi node masih kosong (None), maka fungsi akan membuat node baru menggunakan class Siswa. Jika nilai yang dimasukkan lebih kecil dari node saat ini, data akan ditempatkan ke cabang kiri. Jika lebih besar, data ditempatkan ke cabang kanan. Fungsi ini menjaga aturan BST agar data tetap terurut.

tambah_nilai(self, nilai)
Fungsi ini merupakan fungsi utama untuk menambahkan nilai siswa. Fungsi ini memanggil tambah_nilai_node() dengan root utama pohon sehingga pengguna cukup memasukkan nilai tanpa perlu mengatur node secara manual.

cari_nilai_node(self, root, nilai)
Fungsi ini digunakan untuk mencari apakah suatu nilai siswa ada di dalam BST. Pencarian dilakukan secara rekursif. Jika node kosong, berarti nilai tidak ditemukan. Jika nilai sama dengan node saat ini, fungsi mengembalikan True. Jika nilai lebih kecil, pencarian dilanjutkan ke kiri, sedangkan jika lebih besar maka dilanjutkan ke kanan.

cari_nilai(self, nilai)
Fungsi ini digunakan sebagai fungsi utama untuk mencari nilai siswa. Fungsi ini memanggil cari_nilai_node() dimulai dari root utama agar proses pencarian lebih mudah digunakan.

inorder(self, root)
Fungsi ini digunakan untuk melakukan traversal inorder pada BST. Proses traversal dilakukan dengan urutan kiri → root → kanan. Karena mengikuti aturan BST, hasil traversal inorder akan menampilkan nilai siswa secara urut dari terkecil ke terbesar.

preorder(self, root)
Fungsi ini digunakan untuk traversal preorder dengan urutan root → kiri → kanan. Traversal ini biasanya digunakan untuk melihat struktur pohon dimulai dari akar terlebih dahulu sebelum menuju cabang lainnya

postorder(self, root)
Fungsi ini digunakan untuk traversal postorder dengan urutan kiri → kanan → root. Traversal ini sering digunakan ketika ingin memproses seluruh anak node terlebih dahulu sebelum node induknya.

nilai_terendah(self, root)
Fungsi ini digunakan untuk mencari nilai siswa paling kecil pada BST. Karena BST menyimpan nilai lebih kecil di sebelah kiri, fungsi akan terus bergerak ke node kiri hingga mencapai node paling kiri. Nilai pada node tersebut adalah nilai terendah.

nilai_tertinggi(self, root)
Fungsi ini digunakan untuk mencari nilai siswa paling besar pada BST. Fungsi akan terus bergerak ke cabang kanan hingga mencapai node paling kanan karena nilai terbesar selalu berada di sisi kanan BST.

jumlah_siswa(self, root)
Fungsi ini digunakan untuk menghitung jumlah seluruh node atau jumlah siswa yang tersimpan di BST. Perhitungan dilakukan secara rekursif dengan menjumlahkan node saat ini ditambah jumlah node di subtree kiri dan subtree kanan.

total_nilai(self, root)
Fungsi ini digunakan untuk menghitung total seluruh nilai siswa dalam BST. Fungsi bekerja secara rekursif dengan menjumlahkan nilai node saat ini dengan total nilai pada cabang kiri dan kanan.

main()
Fungsi main() merupakan pusat jalannya program. Fungsi ini membuat objek BST bernama sekolah, lalu menampilkan menu interaktif kepada pengguna. Pengguna dapat memilih menu untuk menambah nilai, mencari nilai, menampilkan traversal, mencari nilai minimum dan maksimum, menghitung jumlah siswa, menghitung total nilai, hingga keluar dari program. Fungsi ini juga menangani kesalahan input menggunakan try-except agar program tidak error ketika pengguna memasukkan data yang bukan angka.

if __name__ == "__main__":
Bagian ini digunakan agar fungsi main() hanya dijalankan ketika file Python dieksekusi secara langsung. Jika file ini di-import ke program lain, maka fungsi main() tidak otomatis berjalan.

OUTPUT >>
Pada awal program, ditampilkan menu utama yang berisi beberapa pilihan operasi seperti insert, search, traversal, mencari nilai minimum dan maksimum, menghitung jumlah node, hingga keluar dari program. Pengguna kemudian memilih menu insert dan memasukkan nilai 87. Karena BST masih kosong, nilai 87 menjadi root atau akar utama dari pohon. Setelah itu pengguna kembali memilih menu insert dan memasukkan nilai 67. Program membandingkan nilai 67 dengan root 87, dan karena 67 lebih kecil dari 87 maka data ditempatkan di cabang kiri. Selanjutnya pengguna memasukkan nilai 97. Karena 97 lebih besar dari 87, maka nilai tersebut ditempatkan di cabang kanan pohon.

Setelah tiga data dimasukkan, pengguna memilih menu Count Nodes. Output “Jumlah siswa: 3” menunjukkan bahwa BST memiliki tiga node, yaitu 87, 67, dan 97. Kemudian pengguna memilih menu Sum Nodes untuk menjumlahkan seluruh nilai siswa yang tersimpan dalam BST. Hasilnya adalah 251, yang diperoleh dari penjumlahan 87 + 67 + 97. Setelah itu pengguna memilih menu preorder. Traversal preorder bekerja dengan urutan root, kiri, lalu kanan. Oleh karena itu output yang dihasilkan adalah “87 67 97”, dimulai dari akar pohon terlebih dahulu kemudian dilanjutkan ke cabang kiri dan kanan. Terakhir, pengguna memilih menu keluar sehingga program menampilkan pesan “Program selesai” sebagai tanda bahwa eksekusi program telah berakhir.
