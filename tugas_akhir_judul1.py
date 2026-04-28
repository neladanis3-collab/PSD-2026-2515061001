def menu():
    print("\n=== MENU CATATAN PENGELUARAN ===")
    print("1. Tampilkan semua pengeluaran")
    print("2. Tampilkan address setiap data")
    print("3. Tambah / ubah pengeluaran")
    print("4. Hitung total pengeluaran")
    print("5. Keluar")


def main():
    pengeluaran = [0] * 5  # menyimpan 5 data pengeluaran
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print("\nDaftar Pengeluaran:")
            for i in range(5):
                print(f"Hari ke-{i+1}: Rp {pengeluaran[i]}")

        elif choice == 2:
            print("\nAddress List dan Isinya:")
            print(f"Address list: {id(pengeluaran)}")
            for i in range(5):
                print(f"Address pengeluaran[{i}]: {id(pengeluaran[i])}")

        elif choice == 3:
            print("\nMasukkan pengeluaran selama 5 hari:")
            for i in range(5):
                while True:
                    try:
                        pengeluaran[i] = int(input(f"Hari ke-{i+1}: Rp "))
                        break
                    except ValueError:
                        print("Masukkan angka yang valid!")

        elif choice == 4:
            total = sum(pengeluaran)
            print(f"\nTotal pengeluaran: Rp {total}")

        elif choice == 5:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
