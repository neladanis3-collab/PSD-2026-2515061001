def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah obat: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan nama obat:")
    for i in range(n):
        nama = input(f"Obat ke-{i+1}: ")
        arr.append(nama)

    print(f"\nDaftar obat sebelum diurutkan: {arr}")

    bubble_sort(arr, n)

    print("\nDaftar obat setelah diurutkan (A-Z): ", end="")
    for i in range(n):
        print(arr[i], end=", ")
    print()


if __name__ == "__main__":
    main()
