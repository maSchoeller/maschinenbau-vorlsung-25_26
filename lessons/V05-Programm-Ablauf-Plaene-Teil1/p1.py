# Dein Code hier
drehzahl = int(input("Aktuelle Spindeldrehzahl (U/min): "))

if drehzahl > 5000:
    print("⚠️ Error: Viel zu Hohe Drehzahl!!!!! Abbruch.")
else:
    if drehzahl > 3000:
        print("⚠️ WARNUNG: Hohe Drehzahl! Werkzeugverschleiß prüfen.")
    else:
        print("alles Super")
