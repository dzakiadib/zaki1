usernames = ['zaki', 'adib', 'winur', 'seto', 'admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, mau lihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih sudah login lagi.")
else:
    print("Kita perlu mencari beberapa pengguna!")