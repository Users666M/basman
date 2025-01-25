#gunakan import random agar bisa menggunakan fitur memilih acak
import random
#selamat datang di game
print("HALO, SELAMAT DATAMG DI GAME YANGE TELAH SAYA BUAT")
print("SILAHKAN MASUKKAN NAMA")
nama = input()
print("SELAMAT DATANG " + nama)
print("AKU TELAH MEMILIH ANGKA DARI 1 HINGGA 100")
print("Jika berhasil,maka akan mendapat hadiah 5k dari diriku")
print("coba tebak yaa!")

#angka rahasia 
angka_rahasia = random.randint(1, 100)

#batas tebakan
batas_tebakan = 7

#gunakan for loop
for percobaan in range(1, batas_tebakan + 1):

    #input dari pemain
    tebakan = int(input(f"tebakan #{percobaan}:"))

    if tebakan < angka_rahasia:
        print("terlalu kecil")
    elif tebakan > angka_rahasia:
        print("terlalu besar")
    else:
        print(f"selamat, kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan")
        break

else:
    print(f"yah kamu kehabisan kesempatan. Angka rahasianya adalah {angka_rahasia} .terimakasih telah bermain")
