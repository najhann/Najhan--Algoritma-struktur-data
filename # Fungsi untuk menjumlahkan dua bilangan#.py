# Fungsi untuk menjumlahkan dua bilangan
def jumlahkan_bilangan(bilangan1, bilangan2):
    return bilangan1 + bilangan2

# Input dari pengguna
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Menghitung jumlah
hasil = jumlahkan_bilangan(bilangan1, bilangan2)

# Menampilkan hasil
print(f"Jumlah dari {bilangan1} dan {bilangan2} adalah {hasil}.")
