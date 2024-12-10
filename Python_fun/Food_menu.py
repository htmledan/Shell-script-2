menu = {
    "Telur Ceplok": 5000,
    "Telur Dadar": 2000,
    "Telur Bacem": 3000,
    "Telur Balado": 4000,
    "Telur Asin": 4000
}


print("##=== Selamat Datang di Rumah Makan Telor ===##")
print("================ Daftar Menu ==================")

for i in menu :
    print("Daftar Menu : ", i, "\t Harga : ",menu [i])
print("===============================================")

# Input pesanan
nama_pelanggan = input("nama pelanggan:")
pesanan = input("Pesanan Anda (pisahkan dengan koma): ")
jumlah_pesanan = int(input("Jumlah pesanan: "))

# Hitung total harga
total_harga = 0
for item in pesanan.split(','):
    item = item.strip()
    if item in menu:
        total_harga += menu[item] * jumlah_pesanan
    else:
        print(f"menu {item} ")

# Tampilkan struk
print("\n=============== Struk Pembayaran ===============")
print("Nama:", nama_pelanggan)
print("Pesanan:", pesanan)
print("Jumlah:", jumlah_pesanan)
print("Total Bayar: Rp", total_harga )

print("\n#= Terimakasih sudah mampir di Rumah Makan Telor =#")
