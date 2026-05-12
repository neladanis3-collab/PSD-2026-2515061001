class StackAktivitas:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push_aktivitas(self, aktivitas):
        if self.is_full():
            print("Riwayat aktivitas penuh!")
            return
        self.top_idx += 1
        self.st[self.top_idx] = aktivitas
        print(f"Aktivitas '{aktivitas}' berhasil ditambahkan")

    def pop_aktivitas_terakhir(self):
        if self.is_empty():
            print("Tidak ada aktivitas!")
            return
        print(f"Aktivitas '{self.st[self.top_idx]}' berhasil dihapus")
        self.top_idx -= 1

    def peek_aktivitas_terbaru(self):
        if self.is_empty():
            print("Tidak ada aktivitas!")
            return
        print(f"Aktivitas terbaru: {self.st[self.top_idx]}")

    def tampilkan_riwayat(self):
        if self.is_empty():
            print("Riwayat aktivitas kosong!")
            return

        print("\n Riwayat Aktivitas Belajar")
        for i in range(self.top_idx, -1, -1):
            print(f"- {self.st[i]}")


def main():
    aktivitas = StackAktivitas()
    pilih = 0

    while pilih != 5:
        print("\n SISTEM RIWAYAT AKTIVITAS BELAJAR")
        print("1. Push Aktivitas")
        print("2. Pop Aktivitas Terakhir")
        print("3. Peek Aktivitas Terbaru")
        print("4. Tampilkan Semua Riwayat")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            aktivitas_baru = input("Masukkan aktivitas belajar: ")
            aktivitas.push_aktivitas(aktivitas_baru)

        elif pilih == 2:
            aktivitas.pop_aktivitas_terakhir()

        elif pilih == 3:
            aktivitas.peek_aktivitas_terbaru()

        elif pilih == 4:
            aktivitas.tampilkan_riwayat()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
