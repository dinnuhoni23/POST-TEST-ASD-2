# Algoritma Binary

# Mengembalikan nilai index x, apabila x ditemukan. Jika index x tidak ditemukan maka akan mengembalikan nilai -1
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        # Jika elemen ditemukan ditengah elemen itu sendiri
        if isinstance(arr[mid], list):
            inner_index = binary_search(arr[mid], 0, len(arr[mid])-1, x)
            if inner_index != -1:
                return (mid, inner_index)
            
        elif arr[mid] == x:
        # Jika elemen x ditemukan maka akan mengembalikan nilai mid
            return mid

        # Jika elemen lebih kecil dari nilai mid, maka akan ditampilkan di bagian kiri subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Elemen akan ditampilkan di bagian kanan subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Elemen tidak ditemukan di array
        return None

# Percobaan array
arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Perulangan
for i in range(5):     
    x = input("Masukkan nama yang ingin dicari: ").capitalize()

    # Fungsi untuk melakukan searching binary pada array
    result = binary_search(arr, 0, len(arr)-1, x)

    if result is None:
        print("{} tidak ditemukan di dalam array".format(x))
    elif isinstance(result, tuple):
        print("{} ditemukan di index {} dan di kolum {}".format(x, result[0], result[1]))
    else:
        print("{} ditemukan di index {}".format(x, result))