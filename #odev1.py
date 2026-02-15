# Kullanıcı Bilgileri
ad = "Emirhan"
soyad = "Karaaslan"
yas = 22
sehir = "İstanbul"
meslek = "Büyük Veri Analistliği"

# Hesaplamalar
bes_yil_sonraki_yas = yas + 5
# Ad ve soyadın toplam harf sayısı (boşluksuz)
toplam_harf_sayisi = len(ad) + len(soyad)

# f-string ile Çıktı Formatı
print("-" * 35)
print("KİŞİSEL BİLGİ YÖNETİM SİSTEMİ")
print("-" * 35)
print(f"Ad Soyad: {ad} {soyad}")
print(f"Yaş: {yas}")
print(f"Şehir: {sehir}")
print(f"Meslek: {meslek}")
print("-" * 35)
print(f"Bilgi: 5 yıl sonra {bes_yil_sonraki_yas} yaşında olacaksınız.")
print(f"Bilgi: Adınız ve soyadınız toplam {toplam_harf_sayisi} harften oluşuyor.")
print("-" * 35)