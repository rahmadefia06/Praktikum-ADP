print('===========================================================')
print('==================PEMESANAN TIKET BIOSKOP==================')
print('===========================================================')
print()
#Meminta input jumlah baris dan kolom kursi bioskop
while True:
    r =int(input('Masukkan Jumlah Baris Kursi (minimal 4) : '))
    c =int(input('Masukkan Jumlah Kolom Kursi (minimal 4) : '))

    if r>=4 and c>=4 :
        break
    else :
        print('Ukuran minimal bioskop adalah 4x4! Silakan masukkan ulang.')
        print('\n-----------------------------------------------------------')
#Membuat daftar kursi
kursi_dipesan = []
kursi = r * c

while True:
    #Menampilkan layout kursi
    print('\nLayout Kursi Bioskop : ')
    nomor_kursi = 1 
    for i in range(1, r + 1) :
        print('|', end='')
        for j in range(c) :
            if str(nomor_kursi) in kursi_dipesan :
                print('  X|', end='')
            else :
                print(f'{nomor_kursi:3}|', end='')

            nomor_kursi += 1
        print()
    #Meminta input pemesanan kursi
    pilihan=input('\nMasukan nomor kursi yang ingin dipesan (atau 0 untuk selesai) : ')

    if pilihan == '0':
        print('Terima kasih telah memesan tiket!')
        break
    #jika kursi sudah dipesan, beri peringatan
    elif pilihan in kursi_dipesan :
        print(f'kursi {pilihan} sudah dipesan! Pilih kursi lain.')
    elif 1 <= int(pilihan) <= kursi :
        kursi_dipesan.append(pilihan)
        print(f'Kursi {pilihan} berhasil dipesan!')
    #jika nomor tidak valid, beri peringatan
    else :
        print('Nomor kursi tidak valid! Masukkan nomor kursi yang tersedia.')
print()
print('===========================================================')
print('              ^-^THANK YOU FOR YOUR ORDER^-^               ')
print('===========================================================')
            