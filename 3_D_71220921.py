#test care
milk = int(input("Masukkan tahun: "))

if milk% 400 == 0:
    print("{} merupakan tahun kabisat".format(milk))
elif milk % 100 == 0:
    print("{} bukan tahun kabisat".format(milk))
elif milk % 4 == 0:
    print("{} merupakan tahun kabisat".format(milk))
else:
    print("{} bukan tahun kabisat".format(milk))