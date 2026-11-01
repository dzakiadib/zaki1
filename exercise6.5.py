sungai_negara = {"nil": "mesir","amazon": "brasil","yangtze": "tiongkok",}

for sungai, negara in sungai_negara.items():
    print(f"Sungai {sungai.title()} mengalir melalui {negara.title()}.")

print("\nSungai yang ada di dictionary:")
for sungai in sungai_negara.keys():
    print(f"- {sungai.title()}")

print("\nNegara yang ada di dictionary:")
for negara in sungai_negara.values():
    print(f"- {negara.title()}")