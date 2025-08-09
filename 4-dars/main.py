# Ma’lumotlar
yillar = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
ish_orinlari = [85000, 87000, 89000, 91000, 92000, 94000, 95000, 96000, 97000, 98000]
bitiruvchilar = [90000, 94000, 98000, 101000, 104000, 108000, 112000, 115000, 118000, 121000]

# Har yil ishsiz qolganlar sonini hisoblash
ishsizlar_soni = []
ishsizlik_foizi = []

for i in range(len(yillar)):
    ishsiz = bitiruvchilar[i] - ish_orinlari[i]
    foiz = (ishsiz / bitiruvchilar[i]) * 100
    ishsizlar_soni.append(ishsiz)
    ishsizlik_foizi.append(round(foiz, 2))

# Natijalarni chiqarish
print("Yil | Bitiruvchilar | Ish o‘rinlari | Ishsizlar soni | Ishsizlik foizi (%)")
print("-"*65)
for i in range(len(yillar)):
    print(f"{yillar[i]} | {bitiruvchilar[i]} | {ish_orinlari[i]} | {ishsizlar_soni[i]} | {ishsizlik_foizi[i]}")

# Eng yuqori ishsizlik bo‘lgan yilni topish
max_foiz = max(ishsizlik_foizi)
indeks = ishsizlik_foizi.index(max_foiz)
print("\n📌 Eng yuqori ishsizlik bo‘lgan yil:", yillar[indeks], "-", max_foiz, "%")
