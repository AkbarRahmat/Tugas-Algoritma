# Input 10 nilai ke dalam array
array = []
for i in range(10):
    nilai = int(input(f"Masukkan nilai ke-{i + 1}: "))
    array.append(nilai)

# Menentukan nilai terkecil dan terbesar
nilai_terkecil = min(array)
nilai_terbesar = max(array)

# Menampilkan hasil
print(f"Nilai terkecil: {nilai_terkecil}")
print(f"Nilai terbesar: {nilai_terbesar}")
