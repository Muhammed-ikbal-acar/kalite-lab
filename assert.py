def gectimi(ortalama):
    return ortalama >= 60

assert gectimi(75) == True
assert gectimi(60) == True
assert gectimi(59) ==False