tempat = ['surakarta', 'sukoharjo', 'klaten', 'karanganyar', 'boyolali', 'wonogiri']

print("Urutan asli:")
print(tempat)

print("\nsorted() alfabetis:")
print(sorted(tempat))
print("Urutan asli masih sama:")
print(tempat)

print("\nsorted() alfabetis terbalik:")
print(sorted(tempat, reverse=True))
print("Urutan asli masih sama:")
print(tempat)

tempat.reverse()
print("\nSetelah reverse():")
print(tempat)

tempat.reverse()
print("\nSetelah reverse() lagi (kembali ke urutan asli):")
print(tempat)

tempat.sort()
print("\nSetelah sort():")
print(tempat)

tempat.sort(reverse=True)
print("\nSetelah sort(reverse=True):")
print(tempat)