def buat_sandwich(*bahan):
    print("\nMembuat sandwich dengan bahan berikut:")
    for item in bahan:
        print(f"- {item}")

buat_sandwich("keju")
buat_sandwich("telur", "selada", "tomat")
buat_sandwich("daging asap", "keju", "timun", "saus sambal", "mayones")
