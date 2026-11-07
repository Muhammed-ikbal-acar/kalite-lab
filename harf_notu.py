puan = 72

if puan >= 85:
    harf = "AA"
elif puan >= 70:
    harf = "BB"
elif puan >= 50:
    harf = "CC"
else:
    harf = "FF"

print(f"{puan} puan: {harf}")