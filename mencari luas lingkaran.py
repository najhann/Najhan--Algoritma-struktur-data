import math

# Fungsi untuk menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2

# Input dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas lingkaran
hasil = luas_lingkaran(jari_jari)

# Menampilkan hasil
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {hasil:.2f}")
