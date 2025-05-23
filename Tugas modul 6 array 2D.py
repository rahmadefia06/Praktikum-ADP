print('---------------------------------------------------------')
print('------------->>>>> KALKULATOR MATRIKS <<<<<--------------')
print('---------------------------------------------------------')
# Input ukuran matriks A
barisA = int(input("Masukkan jumlah baris matriks A  : "))
kolomA = int(input("Masukkan jumlah kolom matriks A  : "))

# Input elemen matriks A
print("Masukkan elemen-elemen matriks A :")
A = []
for i in range(barisA):
    baris = []
    for j in range(kolomA):
        elemen = int(input(f"A[{i}][{j}]: "))
        baris.append(elemen)
    A.append(baris)

# Input ukuran matriks B
barisB = int(input("\nMasukkan jumlah baris matriks B  : "))
kolomB = int(input("Masukkan jumlah kolom matriks B  : "))

# Input elemen matriks B
print("Masukkan elemen-elemen matriks B :")
B = []
for i in range(barisB):
    baris = []
    for j in range(kolomB):
        elemen = int(input(f"B[{i}][{j}]: "))
        baris.append(elemen)
    B.append(baris)

while True:
    print("\n-->> Menu Operasi Matriks : ")
    print("1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Determinan Matriks (2x2)")
    print("5. Invers Matriks (2x2)")
    print("6. Transpose Matriks")
    print("7. Keluar")
    print('---------------------------------------------------------')
    pilihan = input("Pilih operasi (1-7) : ")

    if pilihan == '1':
        if barisA == barisB and kolomA == kolomB:
            print("Hasil Penjumlahan   :")
            for i in range(barisA):
                hasil = []
                for j in range(kolomA):
                    hasil.append(A[i][j] + B[i][j])
                print(hasil)
        else:
            print("Ukuran matriks tidak cocok untuk penjumlahan.")

    elif pilihan == '2':
        if barisA == barisB and kolomA == kolomB:
            print("Hasil Pengurangan   :")
            for i in range(barisA):
                hasil = []
                for j in range(kolomA):
                    hasil.append(A[i][j] - B[i][j])
                print(hasil)
        else:
            print("Ukuran matriks tidak cocok untuk pengurangan.")

    elif pilihan == '3':
        if kolomA == barisB:
            print("Hasil Perkalian Matriks A x B:")
            for i in range(barisA):
                hasil = []
                for j in range(kolomB):
                    total = 0
                    for k in range(kolomA):
                        total += A[i][k] * B[k][j]
                    hasil.append(total)
                print(hasil)
        else:
            print("Jumlah kolom A harus sama dengan jumlah baris B.")

    elif pilihan == '4':
        print("Determinan Matriks (hanya untuk 2x2):")
        if barisA == 2 and kolomA == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            print("Determinan Matriks A:", detA)
        else:
            print("Matriks A bukan 2x2.")
        if barisB == 2 and kolomB == 2:
            detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            print("Determinan Matriks B:", detB)
        else:
            print("Matriks B bukan 2x2.")

    

    elif pilihan == '5':
        print("Invers Matriks (hanya untuk 2x2):")
        if barisA == 2 and kolomA == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            if detA != 0:
                print("-> Invers Matriks A:")
                invA = [
                    [A[1][1]/detA, -A[0][1]/detA],
                    [-A[1][0]/detA, A[0][0]/detA]
                ]
                for baris in invA:
                    print("[", end="")
                    for i in range(len(baris)):
                        print(f"{baris[i]:.2f}", end="")
                        if i != len(baris) - 1:
                            print(" ", end="") 
                    print("]")
            else:
                print("Matriks A tidak memiliki invers (determinan = 0)")
        else:
            print("Matriks A bukan 2x2.")

        if barisB == 2 and kolomB == 2:
            detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            if detB != 0:
                print(" -> Invers Matriks B:")
                invB = [
                    [B[1][1]/detB, -B[0][1]/detB],
                    [-B[1][0]/detB, B[0][0]/detB]
                ]
                for baris in invB:
                    print("[", end="")
                    for i in range(len(baris)):
                        print(f"{baris[i]:.2f}", end="")
                        if i != len(baris) - 1:
                            print(" ", end="") 
                    print("]")
            else:
                print("Matriks B tidak memiliki invers (determinan = 0)")
        else:
            print("Matriks B bukan 2x2.")

    elif pilihan == '6':
        print("-> Transpose Matriks A:")
        for j in range(kolomA):
            baris = []
            for i in range(barisA):
                baris.append(A[i][j])
            print(baris)

        print("-> Transpose Matriks B:")
        for j in range(kolomB):
            baris = []
            for i in range(barisB):
                baris.append(B[i][j])
            print(baris)

    elif pilihan == '7':
        print('^-^!Terima kasih telah menggunakan kalkulator matriks!^-^')
        print()
        break
    else:
        print("Pilihan tidak valid.")

print('=========================================================')
print('======================== SELESAI ========================')
print('=========================================================')
print()