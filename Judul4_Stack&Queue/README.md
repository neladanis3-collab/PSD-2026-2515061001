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
21. 
