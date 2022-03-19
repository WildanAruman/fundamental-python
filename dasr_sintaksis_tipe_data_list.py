daftar_buku = ['Seven Habits', 'How to influence people', 'First thing first ']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\n tampil daftar_buku dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji vol 2', 313, 3.14]
print('\n tampil daftar_buku dengan for in rangedengan data tiap elemen berbeda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to influence people', 'First thing first ']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia mtk kelas 5')

for i in range(0, len(daftar_buku)):
        print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti element pertama')
daftar_buku = ['Seven Habits', 'How to influence people', 'First thing first ']
daftar_buku[0] = 'Eight gabits11'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n Buku yang diambil tadi ' )
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['Seven Habits', 'How to influence People', 'First Thing first', '4dx']
daftar_buku.pop(-3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

