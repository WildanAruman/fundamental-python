print('\nPop -1')
daftar_buku = ['Seven Habits', 'How to influence People', 'First Thing first', '4dx']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How to influence People', 'First Thing first', '4dx']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Seven Habits', 'How to influence People', 'First Thing first', '4dx']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan comprehension')
daftar_buku = ['1 Seven Habits', '2 How to influence People', '3 First Thing first', '4 4dx']
daftar_buku_baru = daftar_buku[1:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])