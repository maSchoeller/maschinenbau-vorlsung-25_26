# ═══════════════════════════════════════════════
#   Anziehdrehmoment-Tabelle (trocken, verzinkt)
# ═══════════════════════════════════════════════
# Gewinde |  4.6 [Nm] |  8.8 [Nm] | 10.9 [Nm]
# ────────|───────────|───────────|──────────
#    M3   |      0.5  |      1.0  |      1.3
#    M4   |      1.2  |      2.4  |      3.0
#    M5   |      2.4  |      4.7  |      5.9
#    M6   |      3.9  |      7.8  |      9.8
#    M8   |      9.4  |     18.8  |     23.5
#    M10  |     18.3  |     36.6  |     45.8

nenndurchmesser_schrauben = [3, 4, 5, 6, 8, 10]
# (Festigkeitsklasse: Zugfestigkeit in MPa)
festigkeitsklassen = [
    {"klasse": "4.6", "rm": 400},
    {"klasse": "8.8", "rm": 800},
    {"klasse": "10.9", "rm": 1000}
]

print("═══════════════════════════════════════════════")
print(" Anziehdrehmoment-Tabelle (trocken, verzinkt)")
print("═══════════════════════════════════════════════")
print("Gewinde |  4.6 [Nm] |  8.8 [Nm] | 10.9 [Nm]")
print("────────|───────────|───────────|──────────")

for durchmesser in nenndurchmesser_schrauben:
    print(f"   M{durchmesser}   |", end="")
    for fk in festigkeitsklassen:
        # Formel: Spannungsquerschnitt As = 0.8 * π*d²/4
        import math
        spannungsquerschnitt = 0.8 * (math.pi * (durchmesser ** 2)) / 4
        # Formel: Vorspannkraft F = 0.7 * As * Rm
        vorspannkraft = 0.7 * spannungsquerschnitt * fk["rm"]
        # Formel: Anziehdrehmoment Ma = 0.2 * d * F
        anziehdrehmoment = 0.2 * durchmesser * vorspannkraft
        print(f"  {anziehdrehmoment:6.1f}  |", end="")
    print()