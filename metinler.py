ad = "Ayşe"
soyad = "Yılmaz"
not_ = 87.456

tam_ad = ad + " " + soyad             # + ile birleştirme
print(tam_ad)
print(f"{tam_ad} dersten {not_} aldı")  # f-string
print(f"Yuvarlanmış: {not_:.1f}")       # virgülden sonra 1 basamak ":" ise değişken üzerinde değişiklik yaptırır 

print(len(tam_ad))       # karakter sayısı (boşluk dahil)
print(tam_ad.upper())    #Bütün karakterleri büyük yapar
print(tam_ad.lower())    #Bütün karakterleri küçük yapar
print(tam_ad[0])         # ilk karakter: sayma 0'dan başlar
print("Ay" in tam_ad)    # içinde geçiyor mu?