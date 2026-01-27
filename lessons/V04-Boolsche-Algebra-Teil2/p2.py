# Beispiel: Notenbewertung
punkte = int(input("Erreichte Punktzahl (0-100): "))

if punkte >= 90:
    note = "Sehr gut (1)"
else:
    if punkte >= 80:
        note = "Gut (2)"
    else:
        if punkte >= 70:
            note = "Befriedigend (3)"
        else:
            if punkte >= 60:
                note = "Ausreichend (4)"
            else:
                note = "Nicht bestanden (5)"

print(f"Deine Note: {note}")


# Beispiel: Notenbewertung
punkte = int(input("Erreichte Punktzahl (0-100): "))

if punkte >= 90:
    note = "Sehr gut (1)"
elif punkte >= 80:
    note = "Gut (2)"
elif punkte >= 70:
    note = "Befriedigend (3)"
elif punkte >= 60:
    note = "Ausreichend (4)"
else:
    note = "Nicht bestanden (5)"

print(f"Deine Note: {note}")