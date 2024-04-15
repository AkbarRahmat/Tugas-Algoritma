def is_prime(n):
    if n <= 1:
        return False  # Mengembalikan False jika n kurang dari atau sama dengan 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Mengembalikan False jika n memiliki faktor selain 1 dan n itu sendiri
    return True  # Mengembalikan True jika n adalah bilangan prima

def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)  # Menambahkan bilangan prima ke dalam daftar primes
    return primes  # Mengembalikan daftar bilangan prima dari 2 hingga n

# Contoh penggunaan program
if __name__ == "__main__":
    n = int(input("Masukkan batas atas: "))
    
    if n < 2:
        print("Tidak ada bilangan prima dalam rentang yang diberikan.")
    else:
        prime_numbers = find_primes(n)
        print(f"Bilangan prima dari 2 hingga {n}: {prime_numbers}")
