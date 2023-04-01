from MethodBurjo import *

def tidak_ada_uang(jenis):
    return("Maaf kamu tidak memiliki uang yang cukup untuk memesan " + jenis)

def sisa_uang():
    return("sisa uang mu adalah Rp." + str(uang))

# Inisialisasi Nilai Awal Saat Pemesanan
pesan_makanan = False
pesan_minuman = False
pesan_tambahan = False
jenis_pesan = True
pesanan1 = False
pesanan2 = False
pesanan3 = False


print("----------- BURJO DKP UHUY -----------")
# variabel untuk menyimpan nilai uang, menu makanan, menu minuman, dan menu tambahan
uang = int (input('Masukan jumlah uang anda : '))
makanan = ["Orak-arik Ayam",14000], ["Magelangan",13000], ["MIE Dok-dok", 12000], ["Nasi Goreng", 13000]
minuman = ["ES Tea Manis", 6000], ["Air Mineral", 3000], ["Teh Anget", 5000], ["Jus Jeruk", 9000]
tambahan = ['Gorengan', 2000], ['Kerupuk', 1000]

makananlen = len(makanan)
minumanlen = len(minuman)
tambahanlen = len(tambahan)

pesan = Pesanan()

#Print List Makanan
print("---------------------------------")
for i in range (makananlen):
    print(str(i+1) + ". " + makanan[i][0] + " (Rp." + str(makanan[i][1]) + ")")
    
#Mengecek apabila cukup uang untuk membeli menu    
for j in range(makananlen):
    if(uang >= makanan[j][1]):
        pesan_makanan = True

if(pesan_makanan == False):
    print("\n" + tidak_ada_uang("makanan") + " di menu")

while (pesan_makanan == True):
    choice1 = int(input("Pilih menu makanan yang diinginkan: "))
    if(choice1 > len(makanan)):
        print("Harap masukkan nomor orderan yang benar")
    else:
        totalchoice1 = int(input("Berapa banyak porsi yang ingin kamu beli? "))
        if(totalchoice1 >= 50):
            print("Maaf burjo kami tidak menyediakan porsi sebanyak itu")
        elif(uang >= (totalchoice1 * makanan[choice1-1][1])):
            uang = uang - (totalchoice1 * makanan[choice1-1][1])
            print("Kamu telah membeli menu " + makanan[choice1-1][0] + " sebanyak " + str(totalchoice1) + " porsi dan " + sisa_uang())
            pesan.tambah_pesanan(makanan[choice1-1][0])
            pesan.tambah_total(totalchoice1)
            pesanan1 = True
            pesan_makanan = False
        else:
            print(tidak_ada_uang("makanan") + " coba pesan menu lain")

#Print List Minuman
print("---------------------------------")
for i in range (minumanlen):
    print(str(i+1) + ". " + minuman[i][0] + " (Rp." + str(minuman[i][1]) + ")")
   
#Mengecek apabila cukup uang untuk membeli menu
for j in range(minumanlen):
    if(uang >= minuman[j][1]):
        pesan_minuman = True

if(pesan_minuman == False):
    print("\n" + tidak_ada_uang("minuman") + " di menu")

while (pesan_minuman == True):
    choice2 = int(input("Pilih menu minuman yang diinginkan: "))
    if(choice2 > len(minuman)):
        print("Harap masukkan nomor orderan yang benar")
    else:
        totalchoice2 = int(input("Berapa banyak porsi yang ingin kamu beli? "))
        if(totalchoice2 >= 50):
            print("Mohon maaf burjo kami tidak mempunyai minuman sebanyak itu")
        elif(uang >= (totalchoice2 * minuman[choice2-1][1])):
            uang = uang - (totalchoice2 * minuman[choice2-1][1])
            print("Kamu telah membeli menu " + minuman[choice2-1][0] + " sebanyak " + str(totalchoice2) + " buah dan " + sisa_uang())
            pesan_minuman = False
            pesan.tambah_pesanan(minuman[choice2-1][0])
            pesan.tambah_total(totalchoice2)
            pesanan2 = True
        else:
           print(tidak_ada_uang("minuman") + " coba pesan menu lain")

#Print list Tambahan
print("---------------------------------")
for i in range (tambahanlen):
    print(str(i+1) + ". " + tambahan[i][0] + " (Rp." + str(tambahan[i][1]) + ")")

#Mengecek apabila cukup uang untuk membeli menu
for j in range(tambahanlen):
    if(uang >= tambahan[j][1]):
        pesan_tambahan = True

if(pesan_tambahan == False):
    print("\n" + tidak_ada_uang("tambahan") + " di menu")

while (pesan_tambahan == True):
    choice3 = int(input("Pilih menu tambahan yang diinginkan: "))
    if(choice3 > len(tambahan)):
        print("Harap masukkan nomor orderan yang benar")
    else:
        totalchoice3 = int(input("Berapa banyak yang ingin kamu beli? "))
        if(totalchoice3 >= 50):
            print("Mohon maaf warteg kami tidak mempunyai minuman sebanyak itu")
        elif(uang >= (totalchoice3 * tambahan[choice3-1][1])):
            uang = uang - (totalchoice3 * tambahan[choice3-1][1])
            print("Kamu telah membeli menu " + tambahan[choice3-1][0] + " sebanyak " + str(totalchoice3) + " buah dan kamu memiliki sisa uang Rp." + str(uang))
            pesan_tambahan = False
            pesan.tambah_pesanan(tambahan[choice3-1][0])
            pesan.tambah_total(totalchoice3)
            pesanan3 = True
        else:
            print(tidak_ada_uang("tambahan") + " coba pesan menu lain")

# Ingin dibawa pulang / makan di tempat
print("---------------------------------")
if(pesanan1 == True or pesanan2 == True or pesanan3 == True):
    print("1. Dibungkus \n2. Makan di tempat")
    while(jenis_pesan == True):
        choice4 = int(input("Ingin dibungkus atau makan di tempat?"))
        if(choice4 == 1):
            bungkus = True
            jenis_pesan = False
        elif(choice4 == 2):
            bungkus = False
            jenis_pesan = False
        else:
            print("Mohon masukkan format yang benar")

    print("\nBerikut adalah pesananmu: ")
    pesan.total_pesanan()
    if(bungkus == True):
        print("\nMohon tunggu sebentar, kami akan membungkus pesananmu")
    else:
        print("\nMohon tunggu sebentar.... \nSelamat Menikmati!")

    print(sisa_uang())
else:
    print("Kamu tidak memesan apapun")
