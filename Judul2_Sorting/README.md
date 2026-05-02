JUDUL >> SISTEM PENGURUTAN NAMA OBAT BERDASARKAN ABJAD DARI A-Z

DESKRIPSI >> Program ini saya buat untuk mengurutkan nama obat sesuai abjad (A–Z) menggunakan metode Bubble Sort.
Jadi alurnya, pertama user akan memasukkan jumlah obat, lalu memasukkan nama-nama obatnya satu per satu ke dalam list. 
Setelah itu, data yang sudah diterima akan diurutkan menggunakan fungsi bubble_sort, yang cara kerjanya membandingin
data yang bersebelahan, jika urutannya salah maka akan langsung ditukar. Proses ini diulang terus sampai semua data urut. 
Dalam fungsinya, saya menggunakan .lower() supaya huruf besar dan kecil tidak berpengaruh ke hasil urutan. Terakhir, 
program akan menampilkan daftar obat sebelum dan sesudah diurutkan.

SOURCE CODE >>
<img width="673" height="856" alt="Screenshot 2026-05-02 212716" src="https://github.com/user-attachments/assets/ed443af8-fbff-4e5f-a4b5-81d166834d20" />
<img width="347" height="76" alt="Screenshot 2026-05-02 212734" src="https://github.com/user-attachments/assets/576a7d27-a62f-48ad-873d-7b1671a288d7" />
PENJELASAN PER BARIS:
1. Mendefinisikan fungsi bernama tukar yang menerima 3 input: array, dan dua variabel i & j 
2. Menyimpan nilai arr[i] ke variabel sementara yaitu temp supaya tidak hilang saat ditukar 
3. lalu mengisi posisi i dengan nilai dari posisi j 
4. Mengisi posisi j dengan nilai asli i yang udah disimpan di temp. 
5. -
6. -
7. Mendefinisikan fungsi sorting yaitu bubble sort dengan array dan banyaknya data
8. Looping diulang sebanyak n-1 kali (jumlah putaran). intinya mengatur berapa kali proses pengurutan diulang. kenapa n-1? karena elemen terakhir otomatis sudah benar sendiri 
9. Looping buat ngebandingin elemen yang sebelahan, makin ke kanan makin pendek karena elemen yang besar sudah tergeser ke akhir.
10. ngebandingin dua nama obat yang sebelahan, pakai .lower() biar huruf besar/kecil tidak mempengaruhi perbandingan 
11. Kalau urutan salah, panggil fungsi tukar buat menukar posisinya 
12. -
13. -
14. Fungsi utama program 
15. Mulai menjalankan kode 
16. Meminta user memasukkan jumlah obat, dikonversi ke integer 
17. Jika input bukan angka, maka akan menangkap error
18. menampilkan pesan error 
19. menghentikan fungsi jika input salah 
20. -
21. Buat list kosong untuk menyimpan nama obat 
22. Menampilkan instruksi ke user untuk menginputkan nama obat
23. Loop sebanyak n kali (sesuai jumlah obat) 
24. Meminta user memasukkan nama obat satu per satu 
25. Tambahkan nama obat ke dalam list arr 
26. -
27. menampilkan isi list sebelum diurutkan, \n biar ada jarak baris, f"..." biar isi variabel bisa langsung ditampilkan di dalam kalimat  
28. -
29. Memanggil fungsi bubble sort untuk mengurutkan array 
30. -
31. \n memberi jarak baris kosong sebelum teks, biar output keliatan lebih rapi. end="" kebalikan dari \n. Normalnya setelah print() akan otomatis pindah baris setelah selesai cetak. Tapi kalau dikasih end="", tidak akan pindah baris, jadi teks selanjutnya nyambung di baris yang sama.
32. Looping untuk mencetak setiap elemen 
33. Cetak nama obat dipisah koma, semua dalam satu baris 
34. Cetak baris kosong sebagai penutup 
35. -
36. -
37. Mengecek apakah file ini dijalankan langsung, bukan di-import oleh file lain
38. Jika ya, panggil fungsi main() untuk memulai program


OUTPUT >>
Output program menjalankan proses input 5 nama obat yaitu Paracetamol, Citrizine, Amoxilin, Promag, dan Ibu Profen. 
Setelah semua nama dimasukkan, program menampilkan daftar obat sebelum diurutkan sesuai urutan input aslinya. 
Kemudian bubble sort bekerja dan menghasilkan urutan alfabetis A-Z yaitu Amoxilin, Citrizine, Ibu Profen, Paracetamol, Promag
dan sudah sesuai dengan alfabet hal ini membuktikan program berjalan dengan benar.

LINK YOUTUBE >> https://youtu.be/axhQhAgD5Jo
