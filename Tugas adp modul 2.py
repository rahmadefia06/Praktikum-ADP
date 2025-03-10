#Tampilan 1: input data diri
print('=======================================================')
print('                Pemesanan Tiket Pesawat                ')
print('=======================================================')
nama = input('Nama                  : ')
umur = input('Umur                  : ')
j_k = input('Jenis Kelamin (L/P)   : ')

#Data Maskapai
print('-------------------------------------------------------')
print('>>>>>>>>>>>>>>>>    Pilihan Maskapai   <<<<<<<<<<<<<<<<')
print('-------------------------------------------------------')
print('|kode|    tujuan    | ekonomi  | bisnis   |first class|')
print('|3012|Padang-Jakarta|Rp.800.000|Rp.850.000|Rp.900.000 |')
print('|4015|Padang-Batam  |Rp.500.000|Rp.550.000|Rp.700.000 |')
print('|4050|Padang-Bandung|Rp.700.000|Rp.750.000|Rp.850.000 |')
print('-------------------------------------------------------')

#input kode dan tujuan maskapai
kode_maskapai = input('Masukan Kode Maskapai : ')
if kode_maskapai == '3012' :
    tujuan ='Padang-Jakarta'
elif kode_maskapai == '4015' :
    tujuan ='Padang-Batam'
elif kode_maskapai == '4050' :
    tujuan ='Padang-Bandung'
else :
     tujuan ='Kode Maskapai Tidak Valid!'
print('Tujuan Penerbangan    :', tujuan)
print('-------------------------------------------------------')
jenis_maskapai = input('jenis kelas(ekonomi/bisnis/first class) : ')
if jenis_maskapai == 'ekonomi' and kode_maskapai == '3012' :
    harga =800000
elif jenis_maskapai == 'bisnis' and kode_maskapai == '3012' :
    harga =850000
elif jenis_maskapai == 'first class' and kode_maskapai == '3012' :
    harga =900000
elif jenis_maskapai == 'ekonomi' and kode_maskapai == '4015' :
    harga =500000
elif jenis_maskapai == 'bisnis' and kode_maskapai == '4015' :
    harga =550000
elif jenis_maskapai == 'first class' and kode_maskapai == '4015' :
    harga =700000
elif jenis_maskapai == 'ekonomi' and kode_maskapai == '4050' :
    harga =700000
elif jenis_maskapai == 'bisnis' and kode_maskapai == '4050' :
    harga =750000
elif jenis_maskapai == 'first class' and kode_maskapai == '4050' :
    harga =850000
else :
    harga = 0
print('Harga Tiket           :',harga)

j_t =int(input('Jumlah Tiket          : '))
#cek diskon jika membeli tiket lebih dari 3
if j_t > 3 :
    total_harga = j_t * harga * 0.2
    diskon = harga * 0.2
else :
    total_harga = j_t * harga
    diskon = 0 

print('Diskon                :', diskon)
print('Total Harga           :', total_harga)
print('                                                       ')
print('----@----@----@----@----@----@----@----@----@----@-----')
print('=======================================================')
print('>>>>>>>>>>>>>>>> STRUK PEMESANAN TIKET <<<<<<<<<<<<<<<<')
print('=======================================================')
print('Nama Penumpang        : ', nama)
print('Umur Penumpang        : ', umur)
print('Jenis Kelamin         : ',j_k)
print('-------------------------------------------------------')
print('Kode Maskapai         : ',kode_maskapai)
print('Tujuan Maskapai       : ',tujuan)
print('Jenis Maskapai        : ', jenis_maskapai)
print('Jumlah Tiket          : ',j_t)
print('Total Harga           : ',total_harga)
print('=======================================================')
print(' ^_^!TERIMA KASIH TELAH MEMESAN TIKET DENGAN KAMI!^_^  ')
print('=======================================================')
