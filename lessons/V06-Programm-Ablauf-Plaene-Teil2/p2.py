# Anzahl der Getriebestufen: 3
# Übersetzung Stufe 1: 2.5
# Übersetzung Stufe 2: 1.8
# Übersetzung Stufe 3: 3.0
# ───────────────────────────────
# Gesamt-Übersetzung: 13.50
# Eingangsdrehzahl: 1500 U/min
# Ausgangsdrehzahl: 111.11 U/min


anzahl_getriebe_stufen = int(input("Anzahl der Getriebestufen: "))

# if getriebe_stufen >= 1:
#     stufe1 = input("Übersetzung Stufe 1: ")
#     print(stufe1)
# if getriebe_stufen >= 2:
#     stufe2 = input("Übersetzung Stufe 2: ")
#     print(stufe2)
stufen = []
for i in range(anzahl_getriebe_stufen):
    temp = float(input(f"Übersetzung Stufe {i+1}: "))
    if True:
        pass
    else:
        stufen.append(temp)
print("------------------------------------")


gesamt_uebersetzung = 1
for i in stufen:
    gesamt_uebersetzung = gesamt_uebersetzung * i


print(stufen)