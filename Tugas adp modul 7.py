print('=============================================================================')
print('====================== MENGHITUNG DATA NILAI MAHASISWA ======================')
print('=============================================================================')
# Fungsi untuk input data mahasiswa
def input_data():
    banyak = int(input("\nMasukkan Jumlah Mahasiswa : "))
    data = []
    for i in range(banyak):
        print(f"\nData Mahasiswa ke-{i+1}")
        nama  = input("Nama        : ")
        nim   = input("NIM         : ")
        uts   = float(input("Nilai UTS   : "))
        uas   = float(input("Nilai UAS   : "))
        tugas = float(input("Nilai Tugas : "))
        data.append([nama, nim, uts, uas, tugas])
    return data

# Fungsi menghitung nilai akhir mahasiswa
def hitung_nilai_akhir(data):
    for i in range(len(data)):
        uts   = data[i][2]
        uas   = data[i][3]
        tugas = data[i][4]
        nilai_akhir = 0.35 * uas + 0.35 * uts + 0.30 * tugas
        data[i].append(nilai_akhir)
    return data

# Fungsi menghitung rata-rata dari kolom tertentu
def hitung_rata_rata(data, indeks):
    total = 0
    for i in range(len(data)):
        total += data[i][indeks]
    return total / len(data)

# Fungsi mengurutkan data secara manual berdasarkan nilai akhir
def urutkan_data(data):
    n = len(data)
    for i in range(n):
        for j in range(i+1, n):
            if data[i][5] < data[j][5]:
                sementara = data[i]
                data[i] = data[j]
                data[j] = sementara
    return data

# Fungsi memberi peringkat ke mahasiswa
def beri_peringkat(data):
    for i in range(len(data)):
        data[i].append(i + 1)
    return data

# Fungsi untuk menampilkan tabel dengan garis "="
def tampilkan_tabel(data):
    garis = "=" * 91
    print("\n" + garis)
    print("| {:^10} | {:^10} | {:^8} | {:^8} | {:^10} | {:^15} | {:^10} |".format(
        "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Ranking"
    ))
    print(garis)

    for i in range(len(data)):
        print("| {:<10} | {:<10} | {:>8.2f} | {:>8.2f} | {:>10.2f} | {:>15.2f} | {:^10} |".format(
            data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]
        ))
    print(garis)

    # Hitung rata-rata
    rata_uts   = hitung_rata_rata(data, 2)
    rata_uas   = hitung_rata_rata(data, 3)
    rata_tugas = hitung_rata_rata(data, 4)
    rata_akhir = hitung_rata_rata(data, 5)

    print("| {:<10} | {:<10} | {:>8.2f} | {:>8.2f} | {:>10.2f} | {:>15.2f} | {:^10} |".format(
        "Rata-rata", "", rata_uts, rata_uas, rata_tugas, rata_akhir, ""
    ))
    print(garis)

# Fungsi utama
def main():
    data = input_data()
    data = hitung_nilai_akhir(data)
    data = urutkan_data(data)
    data = beri_peringkat(data)
    tampilkan_tabel(data)

# Jalankan program
main()
