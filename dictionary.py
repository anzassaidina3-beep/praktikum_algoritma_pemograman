# Membuat dictionary data mahasiswa
mahasiswa = {
    "nama": "anjas",
    "nim": "2404030016",
    "prodi": "Informatika",
    "semester": 3
}

# Menampilkan dictionary
print(f"Data mahasiswa: {mahasiswa}")

# Mengakses nilai menggunakan key
print(f"Nama: {mahasiswa['nama']}")
print(f"Jurusan: {mahasiswa['prodi']}")

# Menambah pasangan key:value baru
mahasiswa["ipk"] = 3.75
print(f"Setelah ditambah IPK: {mahasiswa}")

# Mengubah nilai
mahasiswa["semester"] = 4
print(f"Setelah diubah semester: {mahasiswa}")