# İki basamaklı bir sayıyı okunuşuna çevir
# 23 -> yirmi üç
def yaziya_cevir(number):
    birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    # 42


    onlar_basamagindaki_rakam = number // 10
    birler_basamagindaki_rakam = number % 10

    okunus = onlar[onlar_basamagindaki_rakam] + birler[birler_basamagindaki_rakam]
    return okunus;

def en_kucuk_sayiyi_bul(numbers):
    en_kucuk = numbers[0]
    for num in numbers:
        if(en_kucuk > num):
            en_kucuk = num

    return en_kucuk


def en_buyuk_sayiyi_bul(sayilar):
    en_buyuk = sayilar[0]
    for num in sayilar:
        if (en_buyuk < num):
            en_buyuk = num

    return en_buyuk


if __name__ == '__main__':
    number = int(input('İki basamakli sayi girin'))
    sonuc = yaziya_cevir(number)
    print(sonuc)

    sayilar = [12,-6,25,96,4]
    kucuk = en_kucuk_sayiyi_bul(sayilar)

    buyuk = en_buyuk_sayiyi_bul(sayilar)
    print(kucuk)
    print('en büyük',buyuk)




    #senaryo: Bir listenin içindeki en küçük sayıyı bulmak istiyoruz:

    #Rastgele bir sayı seç ve ardından kullanıcının bulmasını iste.
    #Kullanıcı büyük tahmin ederse aşağı küçük ederse yukarı yönlendir



