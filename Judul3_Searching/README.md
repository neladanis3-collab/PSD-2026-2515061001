JUDUL >> SISTEM PENCARIAN BUKU DI PERPUSTAKAAN MENGGUNAKAN BINARY SEARCH

DESKRIPSI SINGKAT >>  Program pencarian buku perpustakaan ini dibuat buat mempermudah pengguna mencari judul buku
dengan cepat dari daftar buku yang sudah diurutkan sesuai alfabet. Program ini menggunakan metode Binary Search,
yaitu pencarian dengan membagi data jadi dua bagian sampai buku yang dicari ketemu. Program ini dibuat menggunakan
bahasa pemrograman phyton supaya proses pencarian buku jadi lebih cepat dan efisien. 

SOURCE CODE >>
<img width="592" height="880" alt="Screenshot 2026-05-07 174323" src="https://github.com/user-attachments/assets/6626ccdb-8d6a-4f40-802f-ee549908d465" />
<img width="665" height="470" alt="Screenshot 2026-05-07 174343" src="https://github.com/user-attachments/assets/0c10c028-b03c-4775-9e33-ac762d7066b2" />

PENJELASAN KODE >>
1. Mendefinisikan fungsi dengan 2 parameter yaitu buku (list nama buku) dan target yaitu buku yang akan dicari. 
2. L = Left. Batas kiri pencarian dan indeks dimulai dari 0
3. R = Right. Batas kanan pencarian dan indeks terakhir
4. menunjukkan posisi hasil, -1 artinya nilai tidak ditemukan
5. -
6. Loop terus berjalan selama batas kiri tidak melewati batas kanan.
7. Untuk menghitung indeks tengah atau mediannya dari rentang pencarian yang sedang dilakukan
8. -
9. print() berfungsi untuk menampilkan teks ke layar. f untuk menyisipkan variabel langsung ke teks. \n untuk menampilkan baris baru sebelum teks ditampilkan.
   {buku[m]} untuk menampilkan nilai buku pada indeks m atau posisi tengah saat ini
10. -
11. if merupakan percabangan, kode di bawahnya hanya akan berjalan jika kondisi benar. buku[m] menunjukkan elemen buku di posisi tengah (indeks m).
    .lower() untuk mengubah teks menjadi huruf kecil semua agar perbandingannya tidak berantakan. == untuk mengecek apakah dua nilai sama.
    target.lower() menampilkan nama buku yang dicari dan juga diubah ke huruf kecil
12. menyimpan posisi nilai tengah sebagai hasil yang ditemukan.
13. menghentikan looping
14. -
15. elif berjalan jika if di atas tidak terpenuhi. buku[m].lower() < target.lower() jika buku tengah lebih awal secara alfabet dari target.
16. memberi tahu user arah pencarian ke sebelah kanan.
17. geser batas kiri ke satu posisi setelah tengah
18. -
19. jika semua kondisi diatas tidak terpenuhi
20. memberi tahu arah pencarian ke sebelah kiri
21. geser batas kanan ke satu posisi sebelum tengah
22. return untuk mengembalikan nilai dari fungsi ke pemanggilnya. pos untuk mengembalikan indeks posisi buku ditemukan
23. -
24. -
25. deklarasikan fungsi utama program
26. untuk mencetak judul program ke layar
27. -
28. mencoba menjalankan kode
29. input("..") untuk menampilkan teks dan menunggu user memasukkan inputan, hasilnya selalu berupa teks
int(...) untuk mengubah teks hasil input menjadi bilangan bulat.
30. menangkap error kalau user memasukkan bukan angka
31. memberi tahu user kalau input harus angka
32. keluar dari fungsi main kalau terjadi error
33. -
34. variabel berupa list kosong yang nantinya akan diisi nama buku yang akan diinputkan
35. -
36. memerintahkan user untuk menginputkan buku secara urut alfabet
37. -
38. loop sebanyak n kali, dan i dimulai dari 0 sampai n-1
39. {i+1} agar menampilkan 1,2,3... bukan 0,1,2..
40. untuk menambahkan elemen baru ke akhir list
41. -
42. {buku} = menampilkan seluruh isi list buku
43. -
44. \n di dalam input() menampilkan baris baru, Hasil input() langsung disimpan ke target tanpa konversi karena sudah berupa teks
45. -
46. memanggil fungsi dengan mengirim list buku dan target
47. -
48. mengecek apakah hasil bukan -1 ("tidak ditemukan")
49. {hasil} untuk menampilkan nilai indeks posisi buku ditemukan
50. menampilkan nama buku pada indeks tersebut
51. jika hasil tetap -1, berarti buku tidak ada di daftar
52. cetak buku tidak ditemukan
53. -
54. -
55. __name__ untuk menyimpan nama file saat ini
56. memanggil fungsi main untuk memulai program

OUTPUT >> 
<img width="618" height="581" alt="Screenshot 2026-05-07 195651" src="https://github.com/user-attachments/assets/ddc9d987-98db-492a-b88b-f87a5e550e9c" />

Binary Search cara kerjanya dengan cara membagi data jadi dua bagian. Di program ini ada 5 buku yang sudah diurutkan berdasarkan alfabet,yaitu alpro, kalkulus, matdis, pemrograman, dan rpl dengan indeks 0 sampai 4. Buku yang dicari adalah “rpl”.Di pengecekan pertama, program mencari indeks tengah dari 0 sampai 4, hasilnya indeks 2 yaitu “matdis”. Karena secara alfabet “matdis” masih lebih kecil dari “rpl”, maka pencarian lanjut ke bagian kanan dengan mengubah batas kiri jadi indeks 3. Di pengecekan kedua, program hitung lagi titik tengah dari indeks 3 sampai 4, hasilnya indeks 3 yaitu “pemrograman”. Karena “pemrograman” juga masih lebih kecil dari “rpl”, maka pencarian lanjut lagi ke kanan dan batas kiri pindah ke indeks 4.Di pengecekan ketiga, batas kiri dan kanan sama-sama ada di indeks 4, jadi titik tengahnya juga indeks 4 yaitu “rpl”. Karena data yang dicari sudah ketemu, program langsung berhenti dan menyimpan posisi buku tersebut. Hasil akhirnya, program menampilkan kalau buku ditemukan di indeks ke-4 dengan judul “rpl”. Program hanya perlu 3 kali pengecekan untuk menemukan buku, jadi lebih cepat dan efisien dibanding Sequential Search yang harus ngecek data satu-satu dari awal.

LINK YOUTUBE >>
https://youtu.be/IWD2EOLX_KE

