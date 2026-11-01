def kirim_pesan(belum_terkirim, terkirim):
    while belum_terkirim:
        pesan = belum_terkirim.pop()
        print(f"Mengirim pesan: {pesan}")
        terkirim.append(pesan)

belum_terkirim = [
    "Halo, apa kabar?",
    "Jangan lupa tugas Python hari ini.",
    "Nanti malam belajar bareng, ya.",]
pesan_terkirim = []
print("\n--- 8-10. Mengirim Pesan ---")
kirim_pesan(belum_terkirim, pesan_terkirim)
print("\nBelum terkirim:", belum_terkirim)
print("Terkirim:", pesan_terkirim)