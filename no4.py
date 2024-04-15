import time

def f(n):
    return 400 * n + 23

n = 10000  # Contoh nilai n
start_time = time.time()
result = f(n)
end_time = time.time()

print(f"Hasil f({n}) = {result}")
print(f"Waktu eksekusi algoritma f(n): {end_time - start_time} detik")
