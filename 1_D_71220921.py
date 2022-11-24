print ("ketik 1 untuk menghitung penjumlahan")
print ("ketik 2 untuk menghitung pegurangan")
print ("ketik 3 untuk menghitung perkalian")
print ("ketik 4 untuk menghitung pembagian")
print ("ketik 5 untuk menghitung sisa hasil bagi")
print ("ketik 6 untuk menghitung pemangkatan")
a = int(input("masukan pilihan anda:"))
c = int(input("masukan bilangan pertama:"))
b = int(input("masukan bilangan kedua:"))
if a== 1 :
    jumlah = c+b
    print ("hasil dari",c,"dijumlahkan dengan",b,"adalah",jumlah)
elif a== 2 :
    jumlah = c-b
    print ("hasil dari",c,"dikurangi dengan",b,"adalah",jumlah)
elif a== 3 :
    jumlah = c*b
    print ("hasil dari",c,"dikali dengan",b,"adalah",jumlah)
elif a== 4 :
    jumlah = c/b
    print ("hasil dari",c,"dibagi dengan",b,"adalah",jumlah)
elif a== 5 :
    jumlah = c%b
    print ("hasil dari",c,"sisa bagi dengan",b,"adalah",jumlah)
elif a== 6 :
    jumlah = c**b
    print ("hasil dari",c,"dipangkatkan dengan",b,"adalah",jumlah)
else :
    print ("terserah")