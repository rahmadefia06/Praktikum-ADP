# Program pengolahan nilai akhir mahasiswa
print('===========================================')
print('=========NILAI AKHIR PRAKTIKUM ADP=========')
print('===========================================')
jumlah = int(input("Masukkan Jumlah Mahasiswa: "))
nama_mahasiswa = []
nilai_akhir = []

for i in range(jumlah):
    print(f"\n>> Mahasiswa ke-{i+1}")
    nama = input("Nama          : ")
    pretest = float(input("Nilai pretest : "))
    posttest = float(input("Nilai posttest: "))
    makalah = float(input("Nilai makalah : "))

    nilai = 0.4 * pretest + 0.4 * posttest + 0.2 * makalah
    nama_mahasiswa.append(nama)
    nilai_akhir.append(nilai)

# Menampilkan nama dan nilai akhir dalam bentuk tabel
print("\n>> Daftar Nilai Akhir Mahasiswa:")
print("---------------------------------------")
print("| Nama Mahasiswa       | Nilai Akhir  |")
print("---------------------------------------")
for i in range(jumlah):
    print(f"| {nama_mahasiswa[i]:<20} | {nilai_akhir[i]:^12.2f} |")
print("---------------------------------------")

# Menghitung rata-rata nilai akhir
total = sum(nilai_akhir)
rata2 = total / jumlah
print(f"\n>> Rata-rata nilai akhir: {rata2:.2f}")

# Menampilkan Nilai tertinggi dan Nilai terendah
nilai_tertinggi = max(nilai_akhir)
nilai_terendah = min(nilai_akhir)

print("\n>> Mahasiswa dengan nilai tertinggi:")
for i in range(jumlah):
    if nilai_akhir[i] == nilai_tertinggi:
        print(f"=> {nama_mahasiswa[i]} - {nilai_akhir[i]:.2f}")

print("\n>> Mahasiswa dengan nilai terendah:")
for i in range(jumlah):
    if nilai_akhir[i] == nilai_terendah:
        print(f"=> {nama_mahasiswa[i]} - {nilai_akhir[i]:.2f}")

print("\n>> Mahasiswa dengan nilai di atas rata-rata:")
for i in range(jumlah):
    if nilai_akhir[i] > rata2:
        print(f"=> {nama_mahasiswa[i]} - {nilai_akhir[i]:.2f}")
print()
print('===========================================')
print()