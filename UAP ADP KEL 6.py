import os
import time
from termcolor import colored, cprint
from datetime import datetime

# Fungsi untuk membersihkan layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi tampilkan logo toko
def tampilkan_logo():
    clear()
    baris1 = colored("╔════════════════════════════════╗", "black", "on_cyan")
    baris2 = colored("║     (^_^) SELAMAT DATANG!      ║", "black", "on_cyan", attrs=["bold"])
    baris3 = colored("║  ~~~~~ DI KANTIN EATERY ~~~~~  ║", "black", "on_cyan", attrs=["bold"])
    baris4 = colored("╚════════════════════════════════╝", "black", "on_cyan")
    
    print(baris1)
    print(baris2)
    print(baris3)
    print(baris4)
    time.sleep(1)

# Daftar produk awal
produk = {
    "1": {"nama": "Nasi Goreng", "harga": 12000, "stok": 10},
    "2": {"nama": "Mie Ayam", "harga": 13000, "stok": 8},
    "3": {"nama": "Martabak Mesir", "harga": 20000, "stok": 25},
    "4": {"nama": "Bakso", "harga": 15000, "stok": 30},
    "5": {"nama": "Ayam Geprek", "harga": 15000, "stok": 50},
    "6": {"nama": "Nasi Soto", "harga": 10000, "stok": 40},
    "7": {"nama": "Lotek", "harga": 8000, "stok": 15},
    "8": {"nama": "Batagor", "harga": 10000, "stok": 30},
    "9": {"nama": "Nasi Sup", "harga": 15000, "stok": 20},
    "10": {"nama": "Ayam Crispy", "harga": 17000, "stok": 35},
    "11": {"nama": "Jus Naga", "harga": 10000, "stok": 15},
    "12": {"nama": "Jus Mangga", "harga": 10000, "stok": 20},
    "13": {"nama": "Air Mineral", "harga": 3000, "stok": 55},
    "14": {"nama": "Es Teh", "harga": 5000, "stok": 20},
    "15": {"nama": "Es Jeruk", "harga": 10000, "stok": 20},
}


# Denah kursi 4x4
denah = [[str(i * 4 + j + 1) for j in range(4)] for i in range(4)]

# Tampilkan daftar produk
def tampilkan_produk():
    cprint("📋 Daftar Menu Kantin Eatery 📋", "cyan", "on_green", attrs=["bold"])
    print("=" * 55)
    print(f"|{' Kode':^5} | {'Nama Menu':<20} | {'Harga':<10} | {'Stok':<5}    |")
    print("-" * 55)
    for kode, item in produk.items():
        print(f"|{kode:^5} | {item['nama']:<20} | Rp{item['harga']:<8} | {item['stok']:<5}    |")
    print("=" * 55)

# Tampilkan denah kursi
def tampilkan_denah():
    print("")
    cprint("Denah Kursi (4x4) : \n", "cyan", "on_green", attrs=["bold"]) 
    for i in range(4):
        for j in range(4):
            kursi = denah[i] [j]
            warna = "yellow" if kursi != "X" else "red" 
            teks = kursi if kursi == "X " else kursi.rjust(2)
            cprint(teks, warna, "on_white", end=" ", attrs=["bold"])
            time.sleep(0.05)
        print()
        time.sleep(0.05)

# Fungsi belanja pelanggan
def belanja(nama):
    keranjang = []
    tampilkan_produk()

    while True:
        kode = input("Masukkan kode produk (0 untuk selesai): ")
        if kode == "0":
            break
        if kode in produk:
            try:
                jumlah = int(input("Jumlah: "))
                if jumlah <= produk[kode]["stok"]:
                    produk[kode]["stok"] -= jumlah
                    keranjang.append({
                        "nama": produk[kode]["nama"],
                        "harga": produk[kode]["harga"],
                        "jumlah": jumlah
                    })
                else:
                    print("Stok tidak cukup.")
            except ValueError:
                print("Input jumlah harus angka.")
        else:
            print("Kode tidak ditemukan.")
    time.sleep(0.5)
    os.system("cls")
    if keranjang:
        while True:
            tampilkan_denah()
            pilih = input("Pilih kursi (1-16), atau 0 untuk skip: ")
            if pilih == "0":
                break
            try:
                pilih = int(pilih)
                if 1 <= pilih <= 16:
                    baris = (pilih - 1) // 4
                    kolom = (pilih - 1) % 4
                    if denah[baris][kolom] == "X":
                        print("Kursi sudah ditempati.")
                    else:
                        denah[baris][kolom] = "X"
                        lanjut = input("Pilih kursi lain? (y/t): ").lower()
                        if lanjut != "y":
                            break
                else:
                    print("Nomor kursi tidak valid.")
            except ValueError:
                print("Masukkan angka yang benar.")
        tampilkan_denah()
        print(f"kursi yang dipilih telah terpesan!")
        time.sleep(3)
        os.system("cls")
        cetak_struk(nama, keranjang)
    else:
        print("Tidak ada pembelian.")

# Fungsi cetak struk dengan animasi total
def cetak_struk(nama, keranjang):
    print("\n")
    total = 0
    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    cprint("🧾 STRUK PEMESANAN KANTIN EATERY🧾", "yellow", "on_grey", attrs=["bold"])
    print(f"Nama Pembeli : {nama}")
    print(f"Waktu        : {waktu}")
    print("=" * 66)
    print(f"| {'Nama Produk':<20} | {'Jumlah':^6} | {'Harga':>10} | {'Subtotal':>12}      |")
    print("-" * 66)

    for item in keranjang:
        nama_produk = item["nama"]
        jumlah = item["jumlah"]
        harga = item["harga"]
        subtotal = jumlah * harga
        total += subtotal
        print(f"| {nama_produk:<20} | {jumlah:^6} | Rp{harga:>8} | Rp{subtotal:>10}      |")
        time.sleep(0.1)

    print("=" * 66)
    teks = "Menghitung total"
    print(teks, end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\r" + " " * (len(teks) + 3), end="\r")

    cprint(f"{'TOTAL BAYAR':>54} : Rp{total:,}", "green", "on_black", attrs=["bold"])
    print("=" * 66)

    # Simpan ke file log
    with open("transaksi.txt", "a", encoding="utf-8") as file:
        file.write(f"Nama: {nama}\nWaktu: {waktu}\n")
        for item in keranjang:
            file.write(f"{item['nama']} x {item['jumlah']} = Rp{item['harga'] * item['jumlah']}\n")
        file.write(f"Total: Rp{total}\n")
        file.write("=" * 66 + "\n")


# Menu admin
def menu_admin():
    while True:
        cprint("\n=== MENU ADMIN ===", "blue", "on_grey", attrs=["bold"])
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Ubah Stok")
        print("4. Hapus Produk")
        print("0. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_produk()
        elif pilih == "2":
            kode = input("Kode baru: ")
            nama = input("Nama produk: ")
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok: "))
                produk[kode] = {"nama": nama, "harga": harga, "stok": stok}
                print("Produk ditambahkan.")
            except ValueError:
                print("Harga dan stok harus angka.")
        elif pilih == "3":
            kode = input("Kode produk: ")
            if kode in produk:
                try:
                    stok_baru = int(input("Stok baru: "))
                    produk[kode]["stok"] = stok_baru
                    print("Stok diperbarui.")
                except ValueError:
                    print("Input harus angka.")
            else:
                print("Produk tidak ditemukan.")
        elif pilih == "4":
            kode = input("Kode produk yang dihapus: ")
            if kode in produk:
                del produk[kode]
                print("Produk dihapus.")
            else:
                print("Produk tidak ditemukan.")
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")

# Menu utama
def main():
    tampilkan_logo()
    time.sleep(1.5)
    os.system("cls")
    while True:
        cprint("\n=== SELAMAT DATANG DI KANTIN EATERY ===", "cyan", "on_green", attrs=["bold"])
        print("1. Masuk sebagai ADMIN")
        print("2. Masuk sebagai PEMBELI")
        print("0. Keluar")
        pilih = input("Pilih menu: ")
        time.sleep(0.5)
        os.system("cls")
        if pilih == "1":
            sandi = input("Masukkan kata sandi admin: ")
            if sandi == "admin123":
                menu_admin()
            else:
                print("Sandi salah.")
        elif pilih == "2":
            nama = input("Masukkan nama Anda: ")
            print(" ")
            belanja(nama)
            break
        elif pilih == "0":
            cprint("Terima kasih telah menggunakan Kantin Eatery!", "cyan", attrs=["bold"])
            break
        else:
            print("Pilihan tidak tersedia.")

# Jalankan program
main()