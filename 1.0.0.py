import math
import time

def toplama(x, y):
    return x + y
tekrar1=1
def çıkartma(x, y):
    return x - y
tekrar2=1
def üshesapla(x,y):
    return x ** y
tekrar5=1
def çarpma(x,y):
    return x * y
tekrar3=1
def bölme(x,y):
    return x / y
tekrar4=1
def piçarpma(x,y):
    return x * y
tekrar6=1
def pibölme(x,y):
    return x / y
tekrar7=1
def pitoplama(x,y):
    return x + y
tekrar8=1
def piçıkartma(x,y):
    return x - y
tekrar9=1
def karekök(x):
    return math.sqrt(x)
tekrar10=1
def sin(x):
    return math.sin(x)
tekrar11=1
def cos(x):
    return math.cos(x)
tekrar12=1
def tan(x):
    return math.tan(x)
tekrar13=1
def log10(x):
    return math.log(x, 10)
tekrar14=1
def log2(x):
    return math.log2(x)
tekrar15=1
def faktöriyel(x):
    return math.factorial(x)
tekrar16=1
def mutlakdeğer(x):
    return math.fabs(x)
tekrar17=1
def radyanderece(x):
    return math.degrees(x)
tekrar18=1
def dereceradyan(x):
    return math.radians(x)
tekrar19=1
def sayınınkaresi(x):
    return x ** 2
tekrar21=1
def sayınınküpü(x):
     return x ** 3
tekrar22=1
def modalma(x,y):
    return x % y
tekrar20=1

a="Bu işlemi daha önce iki kez yaptınız, devam etmek istiyor musunuz?(evet/hayır): "
b="işlem seçim paneline yönlendiriliyorsunuz..."
c="programın doğru çalışması için lütfen 'evet' veya 'hayır' şeklinde cevap veriniz. "



print("""
Lütfen Bir İşlem Seçiniz:
1-Toplama '+'
2-Çıkartma '-'
3-Çarpma '*'
4-Bölme '/'
5-Üs Alma 'xʸ'
6-PI ile Çarpma-Bölme-Toplama-Çıkartma 
7-Karekök Hesaplama '√x'
8-Sin
9-Cos
10-Tan
11-LOG 10 
12-LOG 2
13-Faktöriyel 'x!'
14-Mutlak Değer '|x|'
15-Radyanı Dereceye Çevirme 'xπ'
16-Dereceyi Radyana Çevirme 'x°'
17-Mod Alma 'x%'
18-Sayının Karesi 'x²'
19-Sayının Küpü 'x³'
        """)

while True:
    selection = input("Seçtiğiniz İşlemi Yazınız (1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19) İşlem yapmak istemiyorsanız 'Çıkış' yazınız:")

    if selection == '1':
        if tekrar1<=2:
            number1 = float(input("Bir sayı girin: "))
            number2 = float(input("Bir sayı girin: "))
            sonuc = toplama(number1, number2)
            print("{} + {} = {}".format(number1, number2, sonuc))
            tekrar1 += 1
            time.sleep(2)
        elif tekrar1 > 2:
            question=str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                number2 = float(input("Bir sayı girin: "))
                sonuc = toplama(number1, number2)
                print("{} + {} = {}".format(number1, number2, sonuc))
                tekrar1 += 1
                time.sleep(2)
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '2':
        if tekrar2<=2:
            number1 = float(input("Bir sayı girin: "))
            number2 = float(input("Bir sayı girin: "))
            sonuc = çıkartma(number1, number2)
            print("{} - {} = {}".format(number1, number2, sonuc))
            tekrar2 += 1
            time.sleep(2)
        elif tekrar2>2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                number2 = float(input("Bir sayı girin: "))
                sonuc = çıkartma(number1, number2)
                print("{} - {} = {}".format(number1, number2, sonuc))
                tekrar2+=1
                time.sleep(2)
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '3':
        if tekrar5<=2:
            number1 = float(input("Bir sayı girin: "))
            number2 = float(input("Bir sayı girin: "))
            sonuc = çarpma(number1, number2)
            print("{} * {} = {}".format(number1, number2, sonuc))
            tekrar5+=1
            time.sleep(2)
        elif tekrar5>2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                number2 = float(input("Bir sayı girin: "))
                sonuc = çarpma(number1, number2)
                print("{} * {} = {}".format(number1, number2, sonuc))
                tekrar5 += 1
                time.sleep(2)
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '4':
        if tekrar4<=2:
            number1 = float(input("Bir sayı girin: "))
            number2 = int(input("Bir sayı girin: "))
            sonuc = bölme(number1, number2)
            print("{} / {} = {}".format(number1, number2, sonuc))
            tekrar4+=1
            time.sleep(2)
        elif tekrar4>2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                number2 = int(input("Bir sayı girin: "))
                sonuc = bölme(number1, number2)
                print("{} / {} = {}".format(number1, number2, sonuc))
                tekrar4 += 1
                time.sleep(2)
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)


    elif selection == '5':
        if tekrar3<=2:
            number1 = float(input("Bir sayı girin: "))
            number2 = int(input("Bir sayı girin: "))
            sonuc = üshesapla(number1, number2)
            print("{} ** {} = {}".format(number1, number2, sonuc))
            tekrar3+=1
            time.sleep(2)
        elif tekrar3>2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                number2 = int(input("Bir sayı girin: "))
                sonuc = üshesapla(number1, number2)
                print("{} ** {} = {}".format(number1, number2, sonuc))
                tekrar3+=1
                time.sleep(2)
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '6':
        number1 = float(input("Bir sayı girin: "))
        number2 = float(3.14)
        operation= input("Hangi işlemi yapmak istersin? (Çarp-Böl-Topla-Çıkar): ")

        if operation == 'çarp' or operation == 'Çarp':
            if tekrar6<=2:
                sonuc = piçarpma(number1,number2)
                print("{} * {} = {}".format(number1, number2, sonuc))
                time.sleep(2)
                tekrar6+=1
            elif tekrar6>2:
                question = str(input(a))
                if question == "evet":
                    sonuc = piçarpma(number1, number2)
                    print("{} * {} = {}".format(number1, number2, sonuc))
                    time.sleep(2)
                    tekrar6 += 1
                elif question == "hayır":
                    print(b)
                    time.sleep(2)
                else:
                    print(c)
                    time.sleep(2)
                    print(b)
                    time.sleep(2)

        elif operation == 'böl' or operation == 'Böl':
            if tekrar7 <= 2:
                sonuc = pibölme(number1, number2)
                print("{} / {} = {}".format(number1, number2, sonuc))
                time.sleep(2)
                tekrar7 += 1
            elif tekrar7 > 2:
                question = str(input(a))
                if question == "evet":
                    sonuc = piçarpma(number1, number2)
                    print("{} * {} = {}".format(number1, number2, sonuc))
                    time.sleep(2)
                    tekrar6 += 1
                elif question == "hayır":
                    print(b)
                    time.sleep(2)
                else:
                    print(c)
                    time.sleep(2)
                    print(b)
                    time.sleep(2)

        elif operation == 'topla' or operation == 'Topla':
            if tekrar8 <= 2:
                sonuc = pitoplama(number1, number2)
                print("{} + {} = {}".format(number1, number2, sonuc))
                time.sleep(2)
                tekrar8 += 1
            elif tekrar8 > 2:
                question = str(input(a))
                if question == "evet":
                    sonuc = pitoplama(number1, number2)
                    print("{} + {} = {}".format(number1, number2, sonuc))
                    time.sleep(2)
                    tekrar8 += 1
                elif question == "hayır":
                    print(b)
                    time.sleep(2)
                else:
                    print(c)
                    time.sleep(2)
                    print(b)
                    time.sleep(2)

        elif operation == 'çıkar' or operation == 'Çıkar':
            if tekrar9 <= 2:
                sonuc = piçıkartma(number1, number2)
                print("{} - {} = {}".format(number1, number2, sonuc))
                time.sleep(2)
                tekrar9 += 1
            elif tekrar9 > 3:
                question = str(input(a))
                if question == "evet":
                    sonuc = piçıkartma(number1, number2)
                    print("{} - {} = {}".format(number1, number2, sonuc))
                    time.sleep(2)
                    tekrar9 += 1
                elif question == "hayır":
                    print(b)
                    time.sleep(2)
                else:
                    print(c)
                    time.sleep(2)
                    print(b)
                    time.sleep(2)

    elif selection == '7':
        if tekrar10 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = karekök(number1)
            print("√{} = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar10 += 1
        elif tekrar10 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = karekök(number1)
                print("√{} = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar10 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '8':
        if tekrar11 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = sin(number1)
            print("{} = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar11 += 1
        elif tekrar12 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = sin(number1)
                print("{} = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar11 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '9':
        if tekrar12 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = cos(number1)
            print("{}cos = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar12+=1
        elif tekrar12 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = cos(number1)
                print("{}cos = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar12 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '10':
        if tekrar13 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = tan(number1)
            print("{}tan = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar13+=1
        elif tekrar13 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = tan(number1)
                print("{}tan = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar13 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '11':
        if tekrar14 <=2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = log10(number1)
            print("{}log10 = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar14+=1
        elif tekrar14 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = log10(number1)
                print("{}log10 = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar14 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '12':
        if tekrar15 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = log2(number1)
            print("{}log2 = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar15+=1
        elif tekrar15 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = log2(number1)
                print("{}log2 = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar15 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '13':
        if tekrar16 <= 2:
            number1 = int(input("Bir sayı girin: "))
            sonuc = faktöriyel(number1)
            print("{}! = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar16+=1
        elif tekrar16 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = faktöriyel(number1)
                print("{}! = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar16 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '14':
        if tekrar17 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = mutlakdeğer(number1)
            print("|{}| = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar17+=1
        elif tekrar17 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = mutlakdeğer(number1)
                print("|{}| = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar17 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '15':
        if tekrar18 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = radyanderece(number1)
            print("{}π = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar18+=1
        elif tekrar18 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = radyanderece(number1)
                print("{}π = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar18 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '16':
        if tekrar19 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = dereceradyan(number1)
            print("{}° = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar19+=1
        elif tekrar19 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = dereceradyan(number1)
                print("{}° = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar19 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '17':
        if tekrar20 <= 2:
            number1 = float(input("Bir sayı girin: "))
            number2 = int(input("Bir sayı girin: "))
            sonuc = modalma(number1,number2)
            print("{} % {}  = {}".format(number1,number2, sonuc))
            time.sleep(2)
            tekrar20+=1
        elif tekrar20 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                number2 = int(input("Bir sayı girin: "))
                sonuc = modalma(number1, number2)
                print("{} % {}  = {}".format(number1, number2, sonuc))
                time.sleep(2)
                tekrar20 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '18':
        if tekrar21 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = sayınınkaresi(number1)
            print("{}² = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar21+=1
        elif tekrar21 <= 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = sayınınkaresi(number1)
                print("{}² = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar21 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == '19':
        if tekrar22 <= 2:
            number1 = float(input("Bir sayı girin: "))
            sonuc = sayınınküpü(number1)
            print("{}³ = {}".format(number1, sonuc))
            time.sleep(2)
            tekrar22+=1
        elif tekrar22 > 2:
            question = str(input(a))
            if question == "evet":
                number1 = float(input("Bir sayı girin: "))
                sonuc = sayınınküpü(number1)
                print("{}³ = {}".format(number1, sonuc))
                time.sleep(2)
                tekrar22 += 1
            elif question == "hayır":
                print(b)
                time.sleep(2)
            else:
                print(c)
                time.sleep(2)
                print(b)
                time.sleep(2)

    elif selection == "çıkış" or "Çıkış":
        print("işleminiz sonlandırılıyor...")
        time.sleep(2)
        print("Tekrar bekleriz ... ")
        time.sleep(1)
        break
