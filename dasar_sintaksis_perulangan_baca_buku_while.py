"""
Program perulangan baca buku dengan while

"""

jumlah_buku = 100
print('Ibu berkata, "Baca semua bukumu!')

jumlah_buku_dibaca = 0

print(f'Buku yang sudah dibaca {jumlah_buku_dibaca} buku')

while jumlah_buku_dibaca < jumlah_buku:
    jumlah_buku_dibaca = jumlah_buku_dibaca + 1
    print(f'buku ke{jumlah_buku_dibaca} sudah dibaca')

print(f'Jumlah buku yang sudah dibaca  {jumlah_buku_dibaca}')
