def quick_sort(arr):
    # Base case: Jika larik hanya memiliki 1 elemen atau kosong, langsung kembalikan larik tersebut.
    if len(arr) <= 1:
        return arr

    # Langkah 1: Pilih elemen pivot. Dalam kasus ini, kita hanya memilih elemen pertama.
    pivot = arr[0]

    # Langkah 2: Pisahkan elemen-elemen ke dalam dua sublarik, satu yang lebih kecil dan satu yang lebih besar dari pivot.
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    # Langkah 3: Gabungkan hasil pengurutan rekursif dari sublarik kiri, pivot, dan sublarik kanan.
    return quick_sort(left) + [pivot] + quick_sort(right)

# Contoh penggunaan algoritma Quick Sort
input_array = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_array = quick_sort(input_array)
print(sorted_array)
