import time

def g(n):
    return 2 * n**2 + 1

n = 10000  # Contoh nilai n
start_time = time.time()
result = g(n)
end_time = time.time()

print(f"Hasil g({n}) = {result}")
print(f"Waktu eksekusi algoritma g(n): {end_time - start_time} detik")
