def topla_yaz(a, b):
    print(a + b)          # ekrana yazar, hiçbir şey döndürmez


def topla(a, b):
    return a + b          # sonucu çağırana geri verir


x = topla_yaz(2, 3)
y = topla(2, 3)
print("x =", x)
print("y =", y)