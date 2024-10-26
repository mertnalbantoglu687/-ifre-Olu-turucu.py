import random

karakterler = "é!'£^#+$%½&/=?\*_-@¨¨~~æß´`,;<>.:qQwWeErRtTyYuUIoOpPğĞüÜaAsSdDfFgGhHjJkKlLşŞiİzZxXcCvVbBnNmMöÖçÇ1234567890"

sifre_uzunlugu = int(input("Bir şifre uzunluğu giriniz: "))

sifre = ""

for a in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)

print("Şifre:",sifre)
