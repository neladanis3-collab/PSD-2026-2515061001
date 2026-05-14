JUDUL >> Sistem Riwayat Aktivitas Belajar Mahasiswa

DESKRIPSI SINGKAT >> ini adalah program penerapan Stack untuk mencatat aktivitas belajar mahasiswa.
Setiap aktivitas terbaru yang dilakukan seperti membuka materi, membaca, atau menonton video pembelajaran, akan disimpan di bagian paling atas stack.
Fitur pop digunakan untuk menghapus aktivitas terakhir yang dilakukan, misal kalau kita salah mencatat aktivitasnya. 

SOURCE CODE >>
<img width="767" height="880" alt="Screenshot 2026-05-12 214127" src="https://github.com/user-attachments/assets/a266c4c0-ecff-4524-a220-757893475e69" />
<img width="762" height="787" alt="Screenshot 2026-05-12 214154" src="https://github.com/user-attachments/assets/7262feef-1579-4ba3-aed3-2435c1645189" />
<img width="640" height="331" alt="Screenshot 2026-05-12 214205" src="https://github.com/user-attachments/assets/3b1315d2-d83a-4c14-9d43-ab8a8f388f30" />

PENJELASAN CODE >>
1. class ini seperti rumus agar bisa menjalankan banyak aktivitas. Lalu mencetak bernama StackActivitas.
2. __init__ fungsi khusus yang otomatis jalan kalo kita buat aktivitas baru. max_size=100 kalau kita tidak isi sendiri nilainya, maka otomatis akan diisi default-nya 100.
3. Menyimpan batas maksimal tumpukan. self berarti untuk milik objek ini sendiri
4. Membuat list (array) sebanyak 100 slot, isinya None (kosong). anggap seperti wadah/rak nya buat nyimpan aktivitas.
5. top_idx penunjuk posisi tumpukan paling atas. Nilai -1 artinya tumpukan masih kosong (belum ada isinya).
6. -
7. mengecek apakah tumpukan kosong
8. Kalau top_idx masih -1, berarti belum ada isi maka return True.
9. -
10. mengecek apakah tumpukan sudah penuh
11. Kalau top_idx sudah di posisi 99 (MAX-1), berarti penuh maka return True.
12. -
13. Menambahkan aktivitas ke stack
14. kalau stack penuh
15. print "Riwayat Aktivitas Penuh"
16. dan langsung stop
17. geser penunjuk ke atas satu posisi misal dari -1 ke 0, dari 0 ke 1
18. menempatkan aktivitas di posisi yang baru
19. f-string adalah cara menulis variabel di dalam teks, pakai {}.
20. -
21 - 24. Pop digunakan untuk mengambil atau menghapus item paling atas. Kalau kosong, langsung stop.
25 - 26. Menampilkan terlebih dahulu aktivitas yang dihapus, terus turunin penunjuknya satu posisi. Data lamanya masih disimpan di list, tapi dianggap udah ngga ada karena penunjuknya turun.
27. -
28 - 32. Peek digunakan untuk ngintip/ngeliat aja aktivitas paling atas, tapi ngga dihapus. Bedanya sama pop, top_idx nggak diubah.
33. -
34. buat fungsi bernama tampilkan_riwayat. self berarti fungsi ini punya class StackAktivitas, jadi dia bisa akses data data yang ada di dalamnya.
35 - 36. Sebelum nampilin apapun, cek dulu tumpukannya kosong atau ngga. kalau True print "kosong!" terus return maka fungsi langsung berhenti, ngga lanjut ke bawah. kalau False berati skip bagian ini, dan lanjut terus.
37. return tidak mengirim nilai apapun, tugasnya cuma stop, dan keluar dari fungsi
38. -
39. \n artinya baris baru (enter), jadi sebelum tulisannya ada jarak kosong satu baris supaya rapi.
40. looping untuk nampilin satu-satu aktivitasnya. range(self.top_idx, -1, -1) maksudnya range buat bikin urutan angka. pertama self.top_idx , mulai dari angka ini. kedua -1 berhenti sebelum angka ini. ketiga -1 tiap langkah mundur 1.
41. nampilin aktivitas satu per satu sesuai posisi i. self.st[i] artinya seperti ambil isi di nomor i.
42. -
43. -
44. deklarasi fungsi utama
45. buat objek dari class StackAktivitas.
46. buat variabel pilih dan isi dengan angka 0.
47. -
48. terus looping selama pilihan bukan 5 (keluar)
49 - 54. print yang akan ditampilkan. user akan diinstruksikan untuk memilih
55. -
56 - 60. try dan except untuk mengantisipasi error. Kalau user ketik huruf, int() akan error dan ditangkap except ValueError dan langsung minta input lagi pakai continue.
61. -
62 - 79. akan memanggil fungsi sesuai pilihan menu. Kalau inputnya di luar 1-5, masuk ke else yaitu pilihan tidak valid.
80. -
81. -
82 - 83. name variabel otomatis, kalau filenya dijalanin langsung, baru panggil fungsi main()
Kalau file ini diimport dari file lain maka fungsi main() ngga ikut berjalan.

OUTPUT >> 
<img width="410" height="871" alt="Screenshot 2026-05-14 213608" src="https://github.com/user-attachments/assets/1708a778-0961-41a2-b8b1-23f0bce64585" />
<img width="360" height="857" alt="Screenshot 2026-05-14 213630" src="https://github.com/user-attachments/assets/66936b2f-58b8-444c-a659-c7f251355dad" />
<img width="322" height="317" alt="Screenshot 2026-05-14 213639" src="https://github.com/user-attachments/assets/e11b728b-e9ae-425b-98fb-686601fcfe94" />
Pertama user milih menu 1 (Push) sebanyak 4 kali buat masukin aktivitas satu-satu, yaitu "membaca", "mengaji", "menulis", sama "menonton". Setiap kali dimasukin, program langsung konfirmasi kalau aktivitasnya berhasil ditambahkan. setelah  itu user milih menu 4 buat lihat semua riwayat. Hasilnya nampilin dari atas ke bawah, jadi "menonton" muncul paling duluan, terus "menulis", "mengaji", dan "membaca" paling bawah. Urutannya kebalik dari urutan masukinnya karena konsep stack.
lalu user milih menu 2 (Pop) buat hapus aktivitas teratas. Yang kehapus otomatis "menonton" karena dia lagi di posisi paling atas tumpukan. Ini namanya LIFO yaitu yang terakhir masuk, yang pertama keluar. Setelah "menonton" dihapus, user milih menu 3 (Peek) buat ngintip aktivitas teratas sekarang. Hasilnya "menulis" karena setelah "menonton" dihapus, "menulis" jadi yang paling atas. Peek cuma ngintip aja, nggak menghapus apapun.  User milih menu 4 lagi buat mastiin. Sekarang tinggal 3 aktivitas "menulis", "mengaji", sama "membaca". "menonton" udah beneran hilang dari stack.
Terakhir user milih menu 5 dan program nampilin "Program selesai." dan berhenti.

LINK YOUTUBE >> 
