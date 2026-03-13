def uzunluk_kontrol(sifre):
    """Şifrenin en az 8 karakter olup olmadığını kontrol eder."""
    return len(sifre) >= 8


def buyuk_harf_kontrol(sifre):
    """Şifrede en az bir büyük harf olup olmadığını kontrol eder."""
    for harf in sifre:
        if harf.isupper():
            return True
    return False


def kucuk_harf_kontrol(sifre):
    """Şifrede en az bir küçük harf olup olmadığını kontrol eder."""
    for harf in sifre:
        if harf.islower():
            return True
    return False


def rakam_kontrol(sifre):
    """Şifrede en az bir rakam olup olmadığını kontrol eder."""
    for harf in sifre:
        if harf.isdigit():
            return True
    return False


def sifre_kontrol(sifre):
    """
    Şifrenin tüm kurallara uygun olup olmadığını kontrol eder.
    Eksik olan kuralları liste olarak döndürür.
    """
    eksikler = []

    if not uzunluk_kontrol(sifre):
        eksikler.append("En az 8 karakter olmalı")

    if not buyuk_harf_kontrol(sifre):
        eksikler.append("En az 1 büyük harf olmalı")

    if not kucuk_harf_kontrol(sifre):
        eksikler.append("En az 1 küçük harf olmalı")

    if not rakam_kontrol(sifre):
        eksikler.append("En az 1 rakam olmalı")

    return eksikler


# Kullanıcıdan şifre alma
sifre = input("Şifre giriniz: ")

sonuc = sifre_kontrol(sifre)

if len(sonuc) == 0:
    print("Şifre Geçerli")
else:
    print("Geçerli Değil")
    print("Eksik kurallar:")
    for kural in sonuc:
        print("-", kural)