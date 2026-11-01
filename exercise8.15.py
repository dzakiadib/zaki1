"Fungsi untuk mencetak model 3D."

def cetak_desain(desain_belum_dicetak, model_selesai):
    """Cetak setiap desain, lalu pindahkan ke daftar model selesai."""
    while desain_belum_dicetak:
        desain_sekarang = desain_belum_dicetak.pop()
        print(f"Mencetak model: {desain_sekarang}")
        model_selesai.append(desain_sekarang)


def tampilkan_model_selesai(model_selesai):
    """Tampilkan semua model yang sudah dicetak."""
    print("\nModel berikut sudah selesai dicetak:")
    for model in model_selesai:
        print(model)
from fungsi_cetak import cetak_desain, tampilkan_model_selesai

desain_belum_dicetak = ["casing ponsel", "liontin robot", "dodekahedron"]
model_selesai = []

cetak_desain(desain_belum_dicetak, model_selesai)
tampilkan_model_selesai(model_selesai)