JUDUL PROGRAM >>  PROGRAM CATATAN PENGELUARAN HARIAN

DESKRIPSI SINGKAT >> Dari kodingan yang saya buat, struktur data yang digunakan adalah list1D pada Python yang termasuk dalam struktur data linear.
List ini digunakan untuk menyimpan data pengeluaran selama 5 hari dengan pengeluaran = [0] * 5, sehingga setiap elemen dapat diakses menggunakan index.
Program ini menerapkan algoritma dasar seperti perulangan (while untuk menjalankan program dan for untuk mengakses data) serta percabangan (if-elif-else)
untuk menentukan pilihan menu. Selain itu, digunakan proses traversal untuk menampilkan dan menjumlahkan data dengan sum(), serta validasi input menggunakan try-except agar program tidak error.
Program ini berfungsi sebagai aplikasi sederhana pencatat pengeluaran, di mana pengguna dapat menginput data selama 5 hari, melihat data, menghitung total pengeluaran,
serta melihat address memori data menggunakan id(), dan program akan berhenti ketika pengguna memilih keluar.

SOURCE CODE >>
<img width="538" height="210" alt="Screenshot 2026-04-28 171238" src="https://github.com/user-attachments/assets/d7e9e82c-3a35-4651-9c55-e3cf6be462e5" />

1. untuk mendeklarasikan fungsi bernama menu, supaya tampilan menu bisa dipanggil berulang tanpa nulis ulang.
2. menampilkan judul menu, \n : untuk pindah baris biar rapi

3-7. pilihan menu ke user. menu ini menjadi petunjuk utama program.
8.
9. 

<img width="830" height="757" alt="Screenshot 2026-04-28 172019" src="https://github.com/user-attachments/assets/f85385ea-7f61-4d35-99e3-25110bc31b2b" />

10. fungsi utama program.
11. membuat list berisi 5 angka 0. fungsinya untuk menyimpan data pengeluaran 5 hari. kenapa [0] * 5 ? karena ini cara cepat buat list yang ukurannya tetap.
12. variabel kontrol loop. selama True maka program terus berjalan.
13. 
14. loop utama program. program akan terus berjalan sampai user memilih keluar.
15. untuk memanggil fungsi menu agar menu tampil setiap loop.
16-17. untuk meminta input dari user. int() untuk mengubah ke angka. try untuk mengantisipasi error.
18-20. kalau user menginputkan bukan angka maka program tidak crash dan akan ke continue  untuk mengulang ke awal loop.

22. kalau user pilih 1
23. judul outputnya
24. loop dari index 0-4 karena data ada 5
25. menampilkan data. i+1  agar menampilkan mulai dari hari ke 1. f-string merupakan format string modern phyton.

26. 
27-29. menampilkan alamat list di memori. id() = fungsi untuk melihat lokasi object di RAM.
30-31. menampilkan alamat tiap elemen, berguna untuk belajar konsep memori.
32. 
33-34. mengecek apakah user memilih menu nomor 3, kalau iya, program akan menjalankan perintah dibawahnya, yaitu meminta pengguna untuk memasukan data pengeluaran.
35. input sebanyak 5 data.
36. loop sampai input valid.
37-39. menyimpan input dan disimpan ke list, break untuk keluar dari loop kalau berhasil.
40-41. untuk memvalidasi input.

<img width="592" height="338" alt="Screenshot 2026-04-27 221431" src="https://github.com/user-attachments/assets/96cb024b-653b-454f-b60c-956242901d6a" />
43. jika user memilih 4
44. menjumlahkan semua list. sum() merupakan fungsi bawaan phyton. 
45. untuk menampilkan hasil total pengeluaran ke layar.
46. 
47. jika user memilih 5
48. untuk menghentikan loop
49. program selesai dijalankan
50. 
51-52. jika pilihan tidak valid, fungsi ini berguna untuk mengantisipasi input selain 1-5
53.
54.
55. artinya jalankan main() hanya kalau file ini dijalankan langsung
56. untuk memanggil fungsi utama kembali.


OUTPUT>>
<img width="465" height="906" alt="Screenshot 2026-04-29 071634" src="https://github.com/user-attachments/assets/74505277-56b1-4483-9649-d1c0dd236087" />
<img width="368" height="581" alt="Screenshot 2026-04-29 071648" src="https://github.com/user-attachments/assets/7d0ac197-219f-4a53-be23-46a8152ece98" />

Program ini saya buat sebagai aplikasi sederhana untuk mencatat pengeluaran selama 5 hari dengan menggunakan List1D di Python. 
Jadi, ketika program dijalankan, pertama akan muncul menu utama yang berisi beberapa pilihan, seperti menampilkan semua pengeluaran, 
menampilkan address setiap data, menambah atau mengubah pengeluaran, menghitung total pengeluaran, dan keluar dari program. Jika user memilih opsi 3,
program akan meminta saya memasukkan pengeluaran selama 5 hari, lalu data tersebut disimpan ke dalam list. Setelah itu, jika user memilih opsi 4, 
program akan menghitung total dari semua pengeluaran yang sudah dimasukkan dengan menjumlahkan isi list tersebut. Kemudian, jika user memilih opsi 1,
program akan menampilkan kembali semua data pengeluaran per hari yang sudah diinput sebelumnya. Selain itu, di opsi 2, 
program menampilkan address atau alamat memori dari list dan tiap elemennya menggunakan fungsi id(), supaya user bisa melihat bagaimana data itu disimpan di memori. 
Terakhir, jika user memilih opsi 5, program akan berhenti dan menampilkan pesan bahwa program sudah selesai.


LINK YOUTUBE https://youtu.be/-BoTQ9glcco?si=-l82_kcJyETHyUNp
