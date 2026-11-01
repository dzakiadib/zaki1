guest_list = ['zaki', 'adib', 'winur', 'seto']

print(f"Yang terhormat {guest_list[0]}, saya mengundang Anda untuk makan malam.")
print(f"Yang terhormat {guest_list[1]}, saya mengundang Anda untuk makan malam.")
print(f"Yang terhormat {guest_list[2]}, saya mengundang Anda untuk makan malam.")
print(f"Yang terhormat {guest_list[3]}, saya mengundang Anda untuk makan malam.")

cannot_come = guest_list[1]
print(f"\nSayang sekali, {cannot_come} tidak bisa hadir.\n")

guest_list[1] = 'robet'

print(f"Yang terhormat {guest_list[0]}, saya mengundang Anda untuk makan malam.")
print(f"Yang terhormat {guest_list[1]}, saya mengundang Anda untuk makan malam.")
print(f"Yang terhormat {guest_list[2]}, saya mengundang Anda untuk makan malam.")
print(f"Yang terhormat {guest_list[3]}, saya mengundang Anda untuk makan malam.")