# Sekuensial
print('Ibu berkata , "pergi ke toko "')
print('Budi menjawab, "Baik apa yang harus saya lakukan ditoko"')
print('Ibu menjawab, Beli satu botol susu"')
print('Maka budi berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan
jumlah_botol_susu = 173
jumlah_telor = 7
print(f'Jumlah botol susu {jumlah_botol_susu} botol')
print(f'Jumlah telur {jumlah_telor} butir')

if jumlah_botol_susu > 0:
    print("Budi menegecek harganya dan uangnya cukup")
    if jumlah_telor >= 6:
        print("Budi beli 1 botol susu dan 6 butir telur ")
    elif jumlah_telor >= 1 and jumlah_telor <= 6:
        print(f'budi membeli 1 botol susu  dan {jumlah_telor} butir telur')
    else:
        print('Budi beli 1 botol susu tanpa telur')
else:
    print('Budi tidak jadi beli 1 botol susu')

print('Budi pulang kerumah')
print('menyerahkan hasilnya pada ibu')







