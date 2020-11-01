#-*-coding:utf-8-*-
import random

oyunAlani = [[],[]]
hamleSayisi = 0
gemi1 = []
gemi2 = []
gemi3 = []
gemi4 = []

def oyunAlaniOlustur(x):
    global oyunAlani
    oyunAlani = [['?' for i in range(x)] for j in range(x)]
    print("Oyun alanı başarıyla oluşturuldu..")

def oyunAlaniGöster(x):
    global oyunAlani
    for i in range(x):
        print(oyunAlani[i])

def gemileriYerlestirAcikMod(x):
    global oyunAlani
    global gemi1,gemi2,gemi3,gemi4
    gemiSayisi = 0
    for i in range(4):
        yon = random.randint(0, 1)
        if yon == 0:
            if gemiSayisi == 0:
                a, b = random.randint(0, x-1), random.randint(0, x-1)
                oyunAlani[a][b] = '+'
                gemiSayisi += 1
                k1 = [a,b]
                gemi1.append(k1)
            elif gemiSayisi == 1:
                a, b = random.randint(0, x-1), random.randint(0, x-2)
                if oyunAlani[a][b] == '+':
                    continue
                oyunAlani[a][b] = '+'
                oyunAlani[a][b + 1] = '+'
                gemiSayisi += 1
                k1 = [a,b]
                k2 = [a,b+1]
                gemi2.append(k1)
                gemi2.append(k2)
            elif gemiSayisi == 2:
                a, b = random.randint(0, x-1), random.randint(0, x-3)
                if oyunAlani[a][b] == '+':
                    continue
                oyunAlani[a][b] = '+'
                oyunAlani[a][b + 1] = '+'
                oyunAlani[a][b + 2] = '+'
                gemiSayisi += 1
                k1 = [a,b]
                k2 = [a,b+1]
                k3 = [a,b+2]
                gemi3.append(k1)
                gemi3.append(k2)
                gemi3.append(k3)
            elif gemiSayisi == 3:
                a, b = random.randint(0, x-1), random.randint(0, x-4)
                if oyunAlani[a][b] == '+':
                    continue
                oyunAlani[a][b] = '+'
                oyunAlani[a][b + 1] = '+'
                oyunAlani[a][b + 2] = '+'
                oyunAlani[a][b + 3] = '+'
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                k3 = [a, b + 2]
                k4 = [a,b+3]
                gemi4.append(k1)
                gemi4.append(k2)
                gemi4.append(k3)
                gemi4.append(k4)
        elif yon == 1:
            if gemiSayisi == 0:
                a, b = random.randint(0, x-1), random.randint(0, x-1)
                oyunAlani[a][b] = '+'
                gemiSayisi += 1
                k1 = [a, b]
                gemi1.append(k1)
            elif gemiSayisi == 1:
                a, b = random.randint(0, x-2), random.randint(0, x-1)
                if oyunAlani[a][b] == '+':
                    continue
                oyunAlani[a][b] = '+'
                oyunAlani[a + 1][b] = '+'
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                gemi2.append(k1)
                gemi2.append(k2)
            elif gemiSayisi == 2:
                a, b = random.randint(0, x-3), random.randint(0, x-1)
                if oyunAlani[a][b] == '+':
                    continue
                oyunAlani[a][b] = '+'
                oyunAlani[a + 1][b] = '+'
                oyunAlani[a + 2][b] = '+'
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                k3 = [a, b + 2]
                gemi3.append(k1)
                gemi3.append(k2)
                gemi3.append(k3)
            elif gemiSayisi == 3:
                a, b = random.randint(0, x-4), random.randint(0, x-1)
                if oyunAlani[a][b] == '+':
                    continue
                oyunAlani[a][b] = '+'
                oyunAlani[a + 1][b] = '+'
                oyunAlani[a + 2][b] = '+'
                oyunAlani[a + 3][b] = '+'
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                k3 = [a, b + 2]
                k4 = [a, b + 3]
                gemi4.append(k1)
                gemi4.append(k2)
                gemi4.append(k3)
                gemi4.append(k4)

def gemileriYerlestirGizliMod(x):
    global gemi1,gemi2,gemi3,gemi4
    gemiSayisi = 0
    for i in range(4):
        yon = random.randint(0, 1)

        if yon == 0:
            if gemiSayisi == 0:
                a, b = random.randint(0, x - 1), random.randint(0, x - 1)
                gemiSayisi += 1
                k1 = [a, b]
                gemi1.append(k1)
            elif gemiSayisi == 1:
                a, b = random.randint(0, x - 1), random.randint(0, x - 2)
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                gemi2.append(k1)
                gemi2.append(k2)
            elif gemiSayisi == 2:
                a, b = random.randint(0, x - 1), random.randint(0, x - 3)
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                k3 = [a, b + 2]
                gemi3.append(k1)
                gemi3.append(k2)
                gemi3.append(k3)
            elif gemiSayisi == 3:
                a, b = random.randint(0, x - 1), random.randint(0, x - 4)
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                k3 = [a, b + 2]
                k4 = [a, b + 3]
                gemi4.append(k1)
                gemi4.append(k2)
                gemi4.append(k3)
                gemi4.append(k4)
        elif yon == 1:
            if gemiSayisi == 0:
                a, b = random.randint(0, x - 1), random.randint(0, x - 1)
                gemiSayisi += 1
                k1 = [a, b]
                gemi1.append(k1)
            elif gemiSayisi == 1:
                a, b = random.randint(0, x - 2), random.randint(0, x - 1)
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                gemi2.append(k1)
                gemi2.append(k2)
            elif gemiSayisi == 2:
                a, b = random.randint(0, x - 3), random.randint(0, x - 1)
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                k3 = [a, b + 2]
                gemi3.append(k1)
                gemi3.append(k2)
                gemi3.append(k3)
            elif gemiSayisi == 3:
                a, b = random.randint(0, x - 4), random.randint(0, x - 1)
                gemiSayisi += 1
                k1 = [a, b]
                k2 = [a, b + 1]
                k3 = [a, b + 2]
                k4 = [a, b + 3]
                gemi4.append(k1)
                gemi4.append(k2)
                gemi4.append(k3)
                gemi4.append(k4)


def saldir():
    global oyunAlani
    global hamleSayisi
    global gemi1, gemi2, gemi3, gemi4
    x = int(input("Saldırı hedefi(satir):"))
    y = int(input("Saldiri hedefi(sütun):"))
    [x,y] = x-1,y-1
    hamleSayisi -= 1
    if [x,y] in gemi1:
        print("Hedef başarıyla vuruldu..")
        gemi1.remove([x,y])
        oyunAlani[x][y] = 'X'
        print("gemi1 başarıyla imha edildi")
    elif [x,y] in gemi2:
        print("Hedef başarıyla vuruldu..")
        gemi2.remove([x,y])
        oyunAlani[x][y] = 'X'
        if len(gemi2) == 0:
            print("gemi2 başarıyla imha edildi..")
    elif [x,y] in gemi3:
        print("Hedef başarıyla vuruldu..")
        gemi3.remove([x,y])
        oyunAlani[x][y] = 'X'
        if len(gemi3) == 0:
            print("gemi3 başarıyla imha edildi..")
    elif [x,y] in gemi4:
        print("Hedef başarıyla vuruldu..")
        gemi4.remove([x,y])
        oyunAlani[x][y] = 'X'
        if len(gemi4) == 0:
            print("gemi4 başarıyla imha edildi..")
    else:
        oyunAlani[x][y] = '*'
        print("Herhangi bir gemiye isabet etmedi..")


while True:
    print("*************** AMİRAL BATTI ***************")
    kare = int(input("Oyun alanı boyutunu giriniz(Minimum 10):"))
    if kare<10:
        print("Girilebilecek minimum değer 10'dur..")
        continue
    hamleSayisi = int((kare**2)/3)
    print("Hamle sayısı:" + str(hamleSayisi))
    oyunAlaniOlustur(kare)
    print("1)Gizli mod")
    print("2)Açık mod")
    m =int(input("Oyun modunu seçiniz:"))
    if m == 1:
        gemileriYerlestirGizliMod(kare)
        while True:
            oyunAlaniGöster(kare)
            saldir()
            if len(gemi1) == 0:
                if len(gemi2) == 0:
                    if len(gemi3) == 0:
                        if len(gemi4) == 0:
                            print("TEBRİKLER!Bütün gemiler imha edildi.. ")
                            print("Puanınız:" + str(hamleSayisi))
                            break
            if hamleSayisi == 0:
                print("Hamleniz bitmiştir..")
                break

    elif m == 2:
        gemileriYerlestirAcikMod(kare)
        while True:
            oyunAlaniGöster(kare)
            saldir()
            if len(gemi1) == 0:
                if len(gemi2) == 0:
                    if len(gemi3) == 0:
                        if len(gemi4) == 0:
                            print("TEBRİKLER!Bütün gemiler imha edildi.. ")
                            print("Puanınız:" + str(hamleSayisi))
                            break

            if hamleSayisi == 0:
                print("Hamleniz bitmiştir..")
                break

    else:
        print("Uygun olmayan seçim..")
        continue

    print("1) Yeni Oyun")
    print("2) Çıkış")
    s = int(input("Seçim:"))
    if s == 1:
        continue
    else:
        break
