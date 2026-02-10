
# Einfache Ausgabe, um das Programm zu erklaeren.
print("Der tolle Taschenrechner!")
print("Lass uns zwei Zahlen addieren")

# Zeige die moeglichen Operatoren an.
print("Operatoren:")
print("- addition/a")
print("- subtraktion/s")
print("- multiplikation/m")
print("- division/d")
print("- exit/e")
# Hier wird die Nutzereingabe fuer den Operator gespeichert.
operator = ""
# while True bedeutet: Schleife laeuft endlos, bis ein break kommt.
while True:
    # Wiederhole den gesamten Ablauf, bis der Nutzer beendet.
    operator = input("Gib deine Rechenoperation an:")
    # if prueft eine Bedingung; wenn sie stimmt, wird der Block ausgefuehrt.
    if operator == "exit" or operator == "e":
        break
    # if/elif/else waehlen genau einen der drei Zweige.
    if operator  == "multiplikation" or operator ==  "m":
        # Multiplikation startet bei 1, damit das Ergebnis korrekt bleibt.
        ergebnis = 1
    # elif ist der zweite Zweig, falls das if nicht passt.
    elif operator == "division" or operator == "d":
        # Bei Division brauchen wir zuerst den Zaehler.
        ergebnis = float(input("Gib den Zähler der Division an:"))
    # else gilt, wenn weder if noch elif zutreffen.
    else:
        # Addition und Subtraktion starten bei 0.
        ergebnis = 0
    # Zaehler fuer die Eingaben (1. Zahl, 2. Zahl, ...).
    i = 1
    # while True bedeutet: Zahlen werden so lange abgefragt, bis abgebrochen wird.
    while True:    
        # Frage fortlaufend Zahlen ab.
        zahl = float(input(f"Gib die {i} Zahl ein:"))
        # 0 ist hier das Abbruchsignal fuer die Zahlenliste.
        # if prueft hier, ob die Eingabe das Abbruchsignal ist.
        if zahl == 0:
            break
        # if prueft hier den gewaehlten Operator.
        if operator == "addition" or operator == "a" :
            # Addiere die eingegebene Zahl.
            ergebnis += zahl
        # if prueft hier den gewaehlten Operator.
        if operator == "subtraktion" or operator ==  "s":
            # Subtrahiere die eingegebene Zahl.
            ergebnis -= zahl
        # if prueft hier den gewaehlten Operator.
        if operator == "multiplikation" or operator ==  "m":
            # Multipliziere mit der eingegebenen Zahl.
            ergebnis *= zahl
        # if prueft hier den gewaehlten Operator.
        if operator == "division" or operator == "d":
            # Teile durch die eingegebene Zahl.
            ergebnis /= zahl
        i+=1
    # Ausgabe des berechneten Ergebnisses.
    print(f"Das Ergebnis ist: {ergebnis}")
    print()
