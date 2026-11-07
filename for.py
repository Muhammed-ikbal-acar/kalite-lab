sayi = int(input("Lütfen bir sayı giriniz: "))
for i in range(1,sayi):
    print(f"{i} Sayısının karesi = {i*i}")
toplam = 0
for a in range(1,sayi):
    toplam=toplam+a
print(f"Yazdığınız sayıya kadar toplamı = {toplam}")