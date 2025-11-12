# Membuat set nomor unik
nomor = {1, 2, 3, 4, 2, 3, 5}

# Set secara otomatis menghilangkan duplikat
print(f"Set nomor: {nomor}") # Output: {1, 2, 3, 4, 5}

# Menambah item baru
nomor.add(6)
print(f"Setelah ditambah: {nomor}")

# Mengecek apakah item ada di dalam set
print(f"Apakah 3 ada di set? {3 in nomor}")
print(f"Apakah 10 ada di set? {10 in nomor}")