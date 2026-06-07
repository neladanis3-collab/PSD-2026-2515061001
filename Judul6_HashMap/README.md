JUDUL >> Sistem Manajemen Nilai Mahasiswa

DESKRIPSI SINGKAT >> Program ini merupakan sistem sederhana untuk mengelola data nilai mahasiswa dengan memanfaatkan struktur data HashMap dengan teknik
Separate Chaining untuk menangani collision (tabrakan indeks). Pada sistem ini, NIM (Nomor Induk Mahasiswa) digunakan sebagai key dan nilai
mahasiswa digunakan sebagai value. Pengguna dapat melakukan beberapa operasi, seperti menambahkan data mahasiswa, mencari nilai berdasarkan NIM, 
menghapus data mahasiswa, serta menampilkan seluruh data yang tersimpan.

KODE >>
<img width="532" height="786" alt="Screenshot 2026-06-07 235001" src="https://github.com/user-attachments/assets/ffa02c73-70ee-42c4-b310-68805410b009" />
<img width="703" height="636" alt="Screenshot 2026-06-07 235023" src="https://github.com/user-attachments/assets/5ec89aad-c1fb-462e-ad1a-1beb509aaac9" />
<img width="588" height="832" alt="Screenshot 2026-06-07 235055" src="https://github.com/user-attachments/assets/9b32a2c5-86af-448f-a075-1589c8d98a28" />
<img width="400" height="222" alt="Screenshot 2026-06-07 235107" src="https://github.com/user-attachments/assets/6dc43308-b4b9-4a04-b767-6896c2d9b381" />

OUTPUT >>
<img width="295" height="726" alt="Screenshot 2026-06-07 235705" src="https://github.com/user-attachments/assets/4bd0954e-2947-41ce-bdde-7aebb7ece961" />
<img width="362" height="603" alt="Screenshot 2026-06-07 235717" src="https://github.com/user-attachments/assets/795ed9da-d008-4890-b5c8-4ad5a24b2078" />

PENJELASAN >>
Fungsi __init__() pada Class Node. Fungsi ini digunakan untuk membuat sebuah node baru yang akan menyimpan data mahasiswa. Setiap node memiliki tiga atribut,
yaitu key sebagai NIM mahasiswa, value sebagai nilai mahasiswa, dan next sebagai penghubung ke node berikutnya. Atribut next diperlukan karena metode Separate
Chaining menggunakan linked list untuk menyimpan data yang memiliki indeks hash yang sama.

Fungsi __init__() pada Class HashMapSeparateChaining. Fungsi ini digunakan untuk membuat Hash Table dengan ukuran tertentu. Pada program ini ukuran default yang 
digunakan adalah 10 indeks. Semua indeks awalnya berisi None, yang menandakan bahwa belum ada data yang tersimpan.

Fungsi hash_function(). Fungsi ini bertugas menentukan lokasi penyimpanan data pada Hash Table. Program akan mengubah NIM menjadi nomor indeks menggunakan 
operasi modulo (%). Fungsi ini membuat proses pencarian menjadi lebih cepat karena program dapat langsung menuju lokasi data yang dicari.

Fungsi insert(). Fungsi ini digunakan untuk menambahkan data mahasiswa ke dalam Hash Table. Program akan menghitung indeks terlebih dahulu menggunakan fungsi hash.
Jika NIM sudah ada, maka nilai mahasiswa akan diperbarui. Jika belum ada, program akan membuat node baru dan menyimpannya pada indeks yang sesuai.

Fungsi search(). Fungsi ini digunakan untuk mencari data mahasiswa berdasarkan NIM. Program akan menghitung indeks terlebih dahulu kemudian memeriksa linked list
pada indeks tersebut. Jika data ditemukan, fungsi akan mengembalikan node yang berisi data mahasiswa. Jika tidak ditemukan, fungsi akan mengembalikan nilai None.

Fungsi remove_key(). Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan NIM. Program akan mencari data terlebih dahulu. Jika data ditemukan,
node akan dihapus dari linked list. Jika data berhasil dihapus maka fungsi mengembalikan nilai True, sedangkan jika data tidak ditemukan maka mengembalikan False.

Fungsi display(). Fungsi ini digunakan untuk menampilkan seluruh data mahasiswa yang tersimpan dalam Hash Table. Program akan memeriksa setiap indeks dan 
menampilkan semua node yang ada pada indeks tersebut. Fungsi ini juga memperlihatkan bagaimana metode Separate Chaining bekerja ketika beberapa data tersimpan 
pada indeks yang sama.

Fungsi main(). Fungsi main() merupakan pusat jalannya program. Semua interaksi antara pengguna dan sistem dilakukan di dalam fungsi ini. Pengguna dapat memilih
menu untuk menambah data, mencari data, menghapus data, menampilkan seluruh data, atau keluar dari program. Fungsi ini menggunakan perulangan while True sehingga
program akan terus berjalan sampai pengguna memilih menu keluar.

KESIMPULAN >> Program Sistem Manajemen Nilai Mahasiswa menerapkan struktur data HashMap dengan metode Separate Chaining untuk menyimpan dan mengelola data nilai
mahasiswa. Program menyediakan fitur menambah, mencari, menghapus, dan menampilkan data mahasiswa berdasarkan NIM. Penggunaan HashMap membuat proses pengelolaan 
data menjadi lebih cepat dan efisien, terutama ketika jumlah data yang disimpan semakin banyak.

LINK YOUTUBE >> 
