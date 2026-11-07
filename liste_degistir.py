dersler = ["Matematik", "Fizik"]
dersler.append("Yazılım Testi")    # sona ekle
print(dersler)

dersler.remove("Fizik")            # değere göre sil
print(dersler)

dersler[0] = "Lineer Cebir"        # bir elemanı değiştir
print(dersler)

print("Fizik" in dersler)          # içinde var mı?