notlar = [70, 45, 90, 60, 85]

gecenler = []
for n in notlar:
    if n >= 60:
        gecenler.append(n)

print("Geçenler:", gecenler)
print("Toplam:", sum(notlar))
print("En düşük:", min(notlar), "En yüksek:", max(notlar))
print("Ortalama:", sum(notlar) / len(notlar))
print("Sıralı:", sorted(notlar))