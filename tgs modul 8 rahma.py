# 1. Buat Data Awal
def buat_data_awal():
    data = [
        "9780001,Matematika Dasar,Andi,10,50000,70000",
        "9780002,Fisika Umum,Budi,8,60000,85000",
        "9780003,Kimia Dasar,Citra,3,55000,80000",
        "9780004,Biologi Modern,Dina,4,52000,75000",
        "9780005,Algoritma,Eka,12,48000,70000",
        "9780006,Basis Data,Fajar,2,65000,95000",
        "9780007,Statistika,Gilang,7,60000,82000",
        "9780008,Aljabar Linear,Hana,5,53000,76000",
        "9780009,Analisis Real,Irfan,6,58000,84000",
        "9780010,Matdis,Joko,1,47000,69000"
    ]
    with open("inventaris_buku.txt", "w") as f:
        for item in data:
            f.write(item + "\n")

# 2. Baca & Simpan Data
def baca_dan_simpan_data():
    inventaris = {}
    with open("inventaris_buku.txt", "r") as f:
        for line in f:
            isbn, judul, penulis, stok, beli, jual = line.strip().split(",")
            inventaris[isbn] = {
                "Judul": judul,
                "Penulis": penulis,
                "Stok": int(stok),
                "Harga Beli": int(beli),
                "Harga Jual": int(jual)
            }
    return inventaris

# 3. Hitung Potensi Keuntungan & Update Data
def hitung_potensi_keuntungan(inventaris):
    with open("laporan_inventaris.txt", "w") as f:
        for isbn, data in inventaris.items():
            keuntungan = (data["Harga Jual"] - data["Harga Beli"]) * data["Stok"]
            data["Potensi Keuntungan"] = keuntungan
            f.write(f"{isbn},{data['Judul']},{data['Penulis']},{data['Stok']},{data['Harga Beli']},{data['Harga Jual']},{keuntungan}\n")

# 4. Analisis Inventaris
def analisis_inventaris(inventaris):
    keuntungan_tertinggi = max(inventaris.items(), key=lambda x: x[1]["Potensi Keuntungan"])
    keuntungan_terendah = min(inventaris.items(), key=lambda x: x[1]["Potensi Keuntungan"])

    print("\n>>> Buku dengan potensi keuntungan tertinggi :")
    print(f"ISBN           : {keuntungan_tertinggi[0]}")
    print(f"Judul          : {keuntungan_tertinggi[1]['Judul']}")
    print(f"Penulis        : {keuntungan_tertinggi[1]['Penulis']}")
    print(f"Stok           : {keuntungan_tertinggi[1]['Stok']}")
    print(f"Harga Beli     : Rp{keuntungan_tertinggi[1]['Harga Beli']}")
    print(f"Harga Jual     : Rp{keuntungan_tertinggi[1]['Harga Jual']}")
    print(f"Keuntungan     : Rp{keuntungan_tertinggi[1]['Potensi Keuntungan']}")

    print("\n>>> Buku dengan potensi keuntungan terendah :")
    print(f"ISBN           : {keuntungan_terendah[0]}")
    print(f"Judul          : {keuntungan_terendah[1]['Judul']}")
    print(f"Penulis        : {keuntungan_terendah[1]['Penulis']}")
    print(f"Stok           : {keuntungan_terendah[1]['Stok']}")
    print(f"Harga Beli     : Rp{keuntungan_terendah[1]['Harga Beli']}")
    print(f"Harga Jual     : Rp{keuntungan_terendah[1]['Harga Jual']}")
    print(f"Keuntungan     : Rp{keuntungan_terendah[1]['Potensi Keuntungan']}")

    total_nilai = 0
    for data in inventaris.values():
        stok = data.get("Stok", 0)
        harga_beli = data.get("Harga Beli", 0)
        total_nilai += stok * harga_beli
    print(f"\n>>> Total nilai inventaris (berdasarkan harga beli): Rp{total_nilai}")

    print("\n>>> Buku yang stoknya kurang dari 5 (perlu di-restock):")
    for isbn, data in inventaris.items():
        if data["Stok"] < 5:
            print(f"- {data['Judul']} (Stok: {data['Stok']})")

# Main Program
buat_data_awal()
data = baca_dan_simpan_data()
hitung_potensi_keuntungan(data)
analisis_inventaris(data)