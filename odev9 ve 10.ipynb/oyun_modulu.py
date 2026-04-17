import random
import csv
import os

def sayi_tahmin():
    hedef = random.randint(1, 100)
    hak = 7
    print("\n--- Sayı Tahmin Oyunu (1-100) ---")

    for i in range(hak):
        try:
            tahmin = int(input(f"{i+1}. Tahmininizi girin: "))
            if tahmin == hedef:
                print(f"Tebrikler! {hedef} sayısını bildiniz.")
                return 50
            elif tahmin < hedef:
                print("Daha büyük bir sayı girin.")
            else:
                print("Daha küçük bir sayı girin.")
        except ValueError:
            print("Hata: Lütfen sadece sayı giriniz! Bir hakkınız boşa gitti.")

    print(f"Üzgünüm, hakkınız bitti. Sayı: {hedef}")
    return 0

def yazi_tura():
    print("\n--- Yazı-Tura Oyunu ---")
    secim = input("Yazı mı Tura mı? ").capitalize()
    sonuc = random.choice(["Yazı", "Tura"])

    if secim == sonuc:
        print(f"Kazandınız! Sonuç: {sonuc}")
        return 20
    else:
        print(f"Kaybettiniz. Sonuç: {sonuc}")
        return 0

def skor_kaydet(oyuncu, oyun, puan):
    dosya_adi = 'skorlar.csv'
    dosya_var_mi = os.path.exists(dosya_adi)

    with open(dosya_adi, mode='a', newline='', encoding='utf-8') as f:
        yazici = csv.writer(f)
        if not dosya_var_mi:
            yazici.writerow(['Oyuncu', 'Oyun', 'Puan'])
        yazici.writerow([oyuncu, oyun, puan])

def skor_goster():
    print("\n--- Tüm Skorlar ---")
    try:
        with open('skorlar.csv', mode='r', encoding='utf-8') as f:
            okuyucu = csv.reader(f)
            for satir in okuyucu:
                print(f"{satir[0]:<15} | {satir[1]:<15} | {satir[2]}")
    except FileNotFoundError:
        print("Hata: skorlar.csv dosyası bulunamadı. Önce oyun oynamalısınız!")
