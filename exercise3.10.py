gunung = ['lawu', 'merapi', 'merbabu', 'andong']
print(f"Awal: {gunung}")

gunung.append('Kerinci')
print(f"Setelah append('Kerinci'): {gunung}")

gunung.insert(0, 'Slamet')
print(f"Setelah insert(0, 'Slamet'): {gunung}")

gunung.remove('andong')
print(f"Setelah remove('andong'): {gunung}")

terakhir = gunung.pop()
print(f"Setelah pop() (mengeluarkan {terakhir}): {gunung}")

del gunung[1]
print(f"Setelah del gunung[1]: {gunung}")

print(f"sorted() (list asli tidak berubah): {sorted(gunung)}")
print(f"List asli: {gunung}")

gunung.sort()
print(f"Setelah sort(): {gunung}")

gunung.reverse()
print(f"Setelah reverse(): {gunung}")

print(f"Jumlah gunung dalam list: {len(gunung)}")