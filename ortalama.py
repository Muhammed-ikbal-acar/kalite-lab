# Bu bir açıklama satırıdır. Başındaki diyez (#) sayesinde bilgisayar burayı okumaz.

# 'def' kelimesi yeni bir işlem/komut (fonksiyon) yarattığımızı söyler.
def ortalama_hesapla(sayi1, sayi2):
    # İki sayıyı toplayıp 'toplam' adında bir kutuya (değişkene) koyuyoruz.
    toplam = sayi1 + sayi2
    
    # Kutudaki değeri ikiye bölüp 'sonuc' kutusuna aktarıyoruz.
    sonuc = toplam / 2
    
    # 'return' komutu, işlemi bitirip bulduğu bu sonucu bize teslim eder.
    return sonuc

# Kodu test edelim: Ekrana yazı yazdırmak için 'print' kullanılır.
print("Notların ortalaması:", ortalama_hesapla(80, 90))