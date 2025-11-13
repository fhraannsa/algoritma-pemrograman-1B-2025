# Data tuple
t1 = (12, 3, 0)
t2 = (1, 5, 9)


gabungan = t1 + t2


unik = []
for angka in gabungan:
    if angka not in unik:
        unik.append(angka)


for i in range(len(unik)):
    for j in range(i + 1, len(unik)):
        if unik[i] < unik[j]:
            unik[i], unik[j] = unik[j], unik[i]


hasil = tuple(unik) 
print("Hasil akhir:", hasil)
