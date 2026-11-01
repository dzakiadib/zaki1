

guest_list = ['zaki', 'adib', 'winur', 'seto', 'adam', 'messi', 'ronaldo']

print("Maaf, kursi yang baru tidak datang tepat waktu.")
print("Saya hanya bisa mengundang dua orang untuk makan malam.\n")

removed = guest_list.pop(6)
print(f"Maaf {removed}, saya tidak bisa mengundang Anda makan malam.")
removed = guest_list.pop(2)
print(f"Maaf {removed}, saya tidak bisa mengundang Anda untuk makan malam.")
removed = guest_list.pop(3)
print(f"Maaf {removed}, saya tidak bisa mengundang Anda untuk makan malam.")
removed = guest_list.pop()
print(f"Maaf {removed}, saya tidak bisa mengundang Anda untuk makan malam.")
removed = guest_list.pop()
print(f"Maaf {removed}, saya tidak bisa mengundang Anda untuk makan malam.")

print(f"\n{guest_list[0]}, Anda masih diundang untuk makan malam.")
print(f"{guest_list[1]}, Anda masih diundang untuk makan malam.")

del guest_list[0]
del guest_list[0]

print(f"\nIsi list sekarang: {guest_list}")