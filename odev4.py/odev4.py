# Verilen karakter listesi
karakterler = [
    {"isim": "Aragorn", "sinif": "savasci", "seviye": 15, "hp": 220, "altin": 500},
    {"isim": "Gandalf", "sinif": "buyucu", "seviye": 20, "hp": 140, "altin": 300},
    {"isim": "Legolas", "sinif": "okcu", "seviye": 12, "hp": 160, "altin": 550},
    {"isim": "Gimli", "sinif": "savasci", "seviye": 10, "hp": 200, "altin": 600},
    {"isim": "Thranduil", "sinif": "okcu", "seviye": 14, "hp": 175, "altin": 900},
    {"isim": "Saruman", "sinif": "buyucu", "seviye": 18, "hp": 130, "altin": 800}
]

# Lambda ile sınıf kontrolü
okcu_mu = lambda k: k["sinif"] == "okcu"
guclu_mu = lambda k: k["seviye"] > 10 and k["hp"] > 150

# Test (isteğe bağlı)
okcular = list(filter(okcu_mu, karakterler))
gucluler = list(filter(guclu_mu, karakterler))

print("Okçular:", [k["isim"] for k in okcular])
print("Güçlüler:", [k["isim"] for k in gucluler])


# Comprehension ile ekip seçimi

# Seviyesi 15'ten büyük olanların isimleri
seviye_15_ustu = [k["isim"] for k in karakterler if k["seviye"] > 15]

print("Seviye 15 üstü:", seviye_15_ustu)

# Altına göre zengin/fakir etiketi
etiket_listesi = [
    (k["isim"], "zengin" if k["altin"] > 500 else "fakir")
    for k in karakterler
]

print("Etiket listesi:", etiket_listesi)