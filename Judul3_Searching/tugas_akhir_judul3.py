def binary_search_buku(buku, target):
    l = 0
    r = len(buku) - 1
    pos = -1

    while l <= r:
        m = l + (r - l) // 2

        print(f"\nPengecekan tengah -> {buku[m]}")

        if buku[m].lower() == target.lower():
            pos = m
            break

        elif buku[m].lower() < target.lower():
            print("Mencari buku di sebelah kanan")
            l = m + 1

        else:
            print("Mencari buku di sebelah kiri")
            r = m - 1
    return pos


def main():
    print("Program Pencarian Buku Perpustakaan")

    try:
        n = int(input("Masukkan jumlah buku: "))
    except ValueError:
        print("Input harus angka!")
        return

    buku = []

    print("\nMasukkan nama buku secara urut alfabet:")

    for i in range(n):
        nama_buku = input(f"Buku ke-{i+1}: ")
        buku.append(nama_buku)

    print(f"\nDaftar buku: {buku}")

    target = input("\nMasukkan nama buku yang dicari: ")

    hasil = binary_search_buku(buku, target)

    if hasil != -1:
        print(f"\nBuku ditemukan pada indeks ke-{hasil}")
        print(f"Judul buku: {buku[hasil]}")
    else:
        print("\nBuku tidak ditemukan")


if __name__ == "__main__":
    main()
