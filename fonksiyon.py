def ortalama_hesapla(sayi1,sayi2):
    return sayi1*0.4+sayi2*0.6

def gectimi(ortalama):
    if ortalama>=50:
        return "Geçti"
    else:
        return "Kaldı"

sayi1 = int(input("İlk sayınızı giriniz: "))
sayi2 = int(input("İkinci sayınızı giriniz: "))
print(f"Ortalamanız = {ortalama_hesapla(sayi1,sayi2):.2f}")
print(f"geçtimi kaldımı = {gectimi(ortalama_hesapla(sayi1,sayi2))}")