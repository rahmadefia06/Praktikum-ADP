print('================================================')
print('         💥PERMAINAN TEBAK ANGKA BOM💥         ')
print('================================================')
print('Menyiapkan Permainan.....')
print('\n')
print('------------------------------------------------')

#pemain 1 menetukan batas angka dan angka BOM nya
a = int(input('>>>>> Pemain 1 <<<<<\nPilih Angka Positif Sampai Berapa : '))
b = int(input('Angka BOM : '))
print('------------------------------------------------')

#menampilkan angka dari 1 sampai a, mengganti kelipatan bom dengan 'BOM'
print('\nDeretan Angka BOM : ')
for i in range(1, a + 1):
    if i % b == 0:
        print('BOM', end =' ')
    else :
        print(i, end =' ')
print('\n')
print('------------------------------------------------')

#pemain ke-2 menebak angka 
while True :
    t = int(input(f'>>>>> Pemain 2 <<<<<\nMenebak angka dari 1 - {a} : '))
    if t < 1 or t > a:
        print('       UPSSS!!!       \nAngka diluar batas! Ayo Coba Lagi.')
        continue
    if t % b == 0 :
        print('Angka',t,'adalah Angka BOM, Anda Kalah!')
        break
    else :
        print('Angka',t,'bukanlah angka BOM, Selamat Anda Menang!!^_^')
        break

