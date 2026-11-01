current_users = ['zaki', 'adib', 'winur', 'seto', 'robet']
new_users = ['budi', 'eko', 'winur', 'seto', 'robet']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' sudah dipakai. Masukkan username lain.")
    else:
        print(f"Username '{new_user}' tersedia.")