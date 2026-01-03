# V07: Übungsaufgaben - Software Engineering & Schleifen Teil 2

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V07.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Software-Prinzipien identifizieren (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten

Analysiere die folgenden Code-Snippets und identifiziere, welches Software-Engineering-Prinzip (KISS, DRY, SRP) jeweils verletzt wird. Begründe deine Antwort kurz und schlage eine Verbesserung vor.

**Snippet 1:**
```python
def verarbeite_kundendaten(kunde_id):
    # Kundendaten aus Datenbank laden
    kunde = db.query(f"SELECT * FROM kunden WHERE id = {kunde_id}")
    
    # Berechne Alter
    geburtsjahr = int(kunde.geburtsdatum.split("-")[0])
    aktuelles_jahr = 2026
    alter = aktuelles_jahr - geburtsjahr
    
    # Berechne Rabatt basierend auf Alter
    if alter >= 65:
        rabatt = 0.15
    elif alter >= 18:
        rabatt = 0.05
    else:
        rabatt = 0.0
    
    # Sende Werbe-Email
    email_text = f"Hallo {kunde.name}, Sie erhalten {rabatt * 100}% Rabatt!"
    smtp_server.send(kunde.email, email_text)
    
    # Logge die Aktion
    with open("logs.txt", "a") as log:
        log.write(f"{kunde_id} verarbeitet am {datetime.now()}\n")
    
    # Aktualisiere Statistik
    stats = db.query("SELECT count FROM statistik WHERE typ = 'verarbeitungen'")
    neue_anzahl = stats.count + 1
    db.execute(f"UPDATE statistik SET count = {neue_anzahl} WHERE typ = 'verarbeitungen'")
```

**Snippet 2:**
```python
def berechne_flaeche_rechteck(laenge, breite):
    flaeche = laenge * breite
    return flaeche

def berechne_flaeche_quadrat(seite):
    flaeche = seite * seite
    return flaeche

def berechne_flaeche_dreieck(basis, hoehe):
    flaeche = (basis * hoehe) / 2
    return flaeche

def berechne_flaeche_kreis(radius):
    pi = 3.14159
    flaeche = pi * radius * radius
    return flaeche

def berechne_flaeche_trapez(a, b, hoehe):
    flaeche = ((a + b) / 2) * hoehe
    return flaeche
```

**Snippet 3:**
```python
def verarbeite_bestellung(bestellung_id, kunde_name, kunde_email, artikel_liste, anzahl_liste, preis_liste, versand_adresse, zahlungsmethode, rabatt_code, notizen):
    # Validiere alle Eingaben
    if not bestellung_id or not kunde_name or not kunde_email:
        if not bestellung_id:
            if not kunde_name:
                if not kunde_email:
                    return {"fehler": "Email fehlt"}
                else:
                    return {"fehler": "Name fehlt"}
            else:
                return {"fehler": "Bestellung-ID fehlt"}
    
    # Berechne Gesamtpreis
    gesamt = 0
    for i in range(len(artikel_liste)):
        if anzahl_liste[i] > 0:
            if preis_liste[i] > 0:
                gesamt = gesamt + (anzahl_liste[i] * preis_liste[i])
    
    # Wende Rabattcode an
    if rabatt_code == "SOMMER2026":
        gesamt = gesamt - (gesamt * 0.10)
    elif rabatt_code == "WINTER2026":
        gesamt = gesamt - (gesamt * 0.15)
    elif rabatt_code == "NEUKUNDE":
        gesamt = gesamt - (gesamt * 0.20)
    
    # Weitere Berechnungen...
    return {"gesamt": gesamt}
```

**Hinweise**:
- Jedes Snippet verletzt primär eines der drei Prinzipien
- Überlege, wie der Code vereinfacht, entstaubt oder aufgeteilt werden könnte
- Achte auf Code-Duplikation, Komplexität und Verantwortlichkeiten

---

### Aufgabe T2: Refactoring-Strategien (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 15-20 Minuten

Gegeben ist folgende Funktion, die mehrere Software-Engineering-Prinzipien verletzt:

```python
def verarbeite_studentendaten(daten_liste):
    ergebnis = []
    for student in daten_liste:
        name = student[0]
        alter = student[1]
        noten = student[2]
        
        # Berechne Durchschnitt
        summe = 0
        for note in noten:
            summe = summe + note
        durchschnitt = summe / len(noten)
        
        # Bestimme Status
        if durchschnitt >= 4.0:
            status = "Bestanden"
        else:
            status = "Nicht bestanden"
        
        # Bestimme Altersgruppe
        if alter < 20:
            gruppe = "Jung"
        elif alter >= 20 and alter < 25:
            gruppe = "Mittel"
        else:
            gruppe = "Älter"
        
        # Erstelle Ergebniszeile
        zeile = name + " | Alter: " + str(alter) + " | Gruppe: " + gruppe + " | Durchschnitt: " + str(durchschnitt) + " | Status: " + status
        ergebnis.append(zeile)
    
    return ergebnis
```

**Aufgabenstellung:**

1. Identifiziere **mindestens 5 konkrete Verstöße** gegen die Prinzipien KISS, DRY oder SRP
2. Entwirf einen **Refactoring-Plan** mit klaren Schritten zur Verbesserung
3. Skizziere die verbesserte Struktur mit Funktionsnamen und Signaturen (ohne vollständigen Code)
4. Erkläre, welche Vorteile die refaktorisierte Version gegenüber der ursprünglichen Version hat

**Hinweise**:
- Achte auf wiederholte Berechnungen und Logik
- Überlege, welche Teile in separate Funktionen ausgelagert werden könnten
- Berücksichtige moderne Python-Features (z.B. f-Strings, List Comprehensions)

---

### Aufgabe T3: Code Review und Design-Entscheidungen (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 20-30 Minuten

Ein Teammitglied hat folgende Implementierung für ein Passwort-Validierungssystem vorgeschlagen:

```python
def validiere_passwort(passwort):
    """Validiert ein Passwort nach Sicherheitsrichtlinien."""
    # Mindestlänge 8
    if len(passwort) < 8:
        return False
    
    # Maximal 64 Zeichen
    if len(passwort) > 64:
        return False
    
    # Mindestens ein Großbuchstabe
    hat_gross = False
    for zeichen in passwort:
        if zeichen.isupper():
            hat_gross = True
    if not hat_gross:
        return False
    
    # Mindestens ein Kleinbuchstabe
    hat_klein = False
    for zeichen in passwort:
        if zeichen.islower():
            hat_klein = True
    if not hat_klein:
        return False
    
    # Mindestens eine Ziffer
    hat_ziffer = False
    for zeichen in passwort:
        if zeichen.isdigit():
            hat_ziffer = True
    if not hat_ziffer:
        return False
    
    # Mindestens ein Sonderzeichen
    sonderzeichen = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    hat_sonderzeichen = False
    for zeichen in passwort:
        if zeichen in sonderzeichen:
            hat_sonderzeichen = True
    if not hat_sonderzeichen:
        return False
    
    # Keine aufeinanderfolgenden identischen Zeichen (z.B. "aaa")
    for i in range(len(passwort) - 2):
        if passwort[i] == passwort[i+1] == passwort[i+2]:
            return False
    
    # Keine häufigen Muster (z.B. "123", "abc")
    verbotene_muster = ["123", "abc", "qwe", "password", "admin"]
    passwort_lower = passwort.lower()
    for muster in verbotene_muster:
        if muster in passwort_lower:
            return False
    
    return True
```

**Aufgabenstellung:**

1. **Funktionale Analyse**: Teste die Funktion gedanklich mit verschiedenen Eingaben. Welche Passwörter würden akzeptiert/abgelehnt? Gibt es Grenzfälle, die problematisch sein könnten?

2. **Prinzipienverletzungen**: Identifiziere konkrete Verstöße gegen KISS, DRY und SRP. Welches Prinzip wird am stärksten verletzt?

3. **Alternative Implementierungen**: Schlage **zwei verschiedene Refactoring-Ansätze** vor:
   - **Ansatz A**: Fokus auf DRY und Modularität
   - **Ansatz B**: Fokus auf KISS und Lesbarkeit
   
   Skizziere die Struktur beider Ansätze (Funktionsnamen, grobe Logik, keine vollständige Implementierung)

4. **Design-Diskussion**: Welcher Ansatz ist besser? Argumentiere aus Sicht von:
   - Wartbarkeit
   - Testbarkeit
   - Erweiterbarkeit (z.B. neue Validierungsregeln hinzufügen)
   - Performance

5. **Fehler-Reporting**: Die aktuelle Funktion gibt nur `True` oder `False` zurück. Diskutiere, ob und wie ein besseres Fehler-Reporting implementiert werden sollte, ohne gegen KISS zu verstoßen.

**Hinweise**:
- Es gibt keine einzig "richtige" Antwort – verschiedene Ansätze haben unterschiedliche Vor- und Nachteile
- Berücksichtige reale Anforderungen: Die Funktion sollte dem Benutzer mitteilen, *warum* sein Passwort abgelehnt wurde
- Überlege, wie die Funktion in einem größeren System eingebettet wäre
- Diskutiere Trade-offs zwischen verschiedenen Qualitätszielen

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Primzahlen-Finder mit break (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Schleifen, `break`, Modulo-Operator

Schreibe ein Programm, das alle Primzahlen bis zu einer vom Benutzer eingegebenen Obergrenze findet und ausgibt.

**Anforderungen**:
- Fordere den Benutzer auf, eine Obergrenze einzugeben (z.B. 50)
- Für jede Zahl von 2 bis zur Obergrenze prüfe, ob sie eine Primzahl ist
- Eine Zahl ist eine Primzahl, wenn sie nur durch 1 und sich selbst teilbar ist
- Verwende `break`, um die Prüfung vorzeitig zu beenden, sobald ein Teiler gefunden wurde
- Nutze die `else`-Klausel der Schleife, um Primzahlen zu identifizieren
- Gib alle gefundenen Primzahlen aus

**Beispiel Ein-/Ausgabe**:
```
Obergrenze eingeben: 20
Primzahlen bis 20:
2 3 5 7 11 13 17 19
```

**Hinweise**:
- Eine Zahl n ist keine Primzahl, wenn sie durch irgendeine Zahl von 2 bis n-1 teilbar ist
- Optimierung: Es genügt, bis zur Quadratwurzel von n zu testen
- Die `else`-Klausel nach der Schleife wird nur ausgeführt, wenn kein `break` aufgerufen wurde

---

### Aufgabe P2: Zahlenrate-Spiel mit continue (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 20-25 Minuten  
**Vorkenntnisse**: Schleifen, `break`, `continue`, Eingabevalidierung

Erstelle ein interaktives Zahlenrate-Spiel, bei dem der Computer eine Zufallszahl zwischen 1 und 100 wählt und der Spieler sie erraten muss.

**Anforderungen**:
- Verwende `import random` und `random.randint(1, 100)`, um eine Zufallszahl zu generieren
- Verwende eine `while`-Schleife für die Spiellogik
- Fordere den Spieler auf, eine Zahl einzugeben
- Validiere die Eingabe:
  - Wenn die Eingabe keine gültige Zahl ist, gib eine Fehlermeldung aus und verwende `continue`
  - Wenn die Zahl außerhalb des Bereichs 1-100 liegt, gib eine Fehlermeldung aus und verwende `continue`
- Gib Hinweise: "Zu hoch!", "Zu niedrig!" oder "Richtig!"
- Beende das Spiel mit `break`, wenn die richtige Zahl erraten wurde
- Zähle die Anzahl der Versuche und gib sie am Ende aus

**Beispiel Spielablauf**:
```
Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.
Dein Tipp: abc
Das ist keine gültige Zahl! Versuche es nochmal.
Dein Tipp: 150
Die Zahl muss zwischen 1 und 100 liegen!
Dein Tipp: 50
Zu niedrig!
Dein Tipp: 75
Zu hoch!
Dein Tipp: 63
Richtig! Du hast die Zahl in 5 Versuchen erraten.
```

**Hinweise**:
- Verwende `input().strip()`, um Leerzeichen zu entfernen
- Verwende `.isdigit()` zur Validierung
- Denke an den Fall, dass der Benutzer negative Zahlen eingibt (z.B. "-5")

---

### Aufgabe P3: Multiplikationstabelle mit verschachtelten Schleifen (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25-30 Minuten  
**Vorkenntnisse**: Verschachtelte Schleifen, String-Formatierung

Erstelle ein Programm, das eine formatierte Multiplikationstabelle ausgibt.

**Anforderungen**:
- Fordere den Benutzer auf, die Größe der Tabelle einzugeben (z.B. 10 für 1×1 bis 10×10)
- Erstelle eine Tabelle mit Überschriften für Zeilen und Spalten
- Formatiere die Zahlen rechtsbündig, sodass die Spalten ausgerichtet sind
- Füge eine horizontale Trennlinie nach der Kopfzeile ein
- Verwende verschachtelte `for`-Schleifen

**Beispiel Ausgabe** (für Größe 5):
```
     |    1    2    3    4    5
-----|----------------------------
   1 |    1    2    3    4    5
   2 |    2    4    6    8   10
   3 |    3    6    9   12   15
   4 |    4    8   12   16   20
   5 |    5   10   15   20   25
```

**Erweiterte Anforderungen** (optional):
- Färbe oder markiere die Quadratzahlen (1, 4, 9, 16, 25, ...) in der Diagonale
- Füge eine zusätzliche Summenzeile am Ende hinzu

**Hinweise**:
- Verwende f-Strings mit Breitenangabe: `f"{zahl:4d}"` für rechtsbündige Ganzzahlen mit Breite 4
- Die Trennlinie kann mit `"-" * laenge` erzeugt werden
- Überlege, wie breit die Spalten sein müssen (abhängig von der maximalen Zahl)

---

### Aufgabe P4: Passwort-Generator mit List Comprehension (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: List Comprehensions, String-Methoden, `random`-Modul

Erstelle einen sicheren Passwort-Generator, der Passwörter nach verschiedenen Kriterien erzeugt.

**Anforderungen**:
- Der Benutzer kann die gewünschte Passwortlänge eingeben (mindestens 8 Zeichen)
- Der Benutzer kann wählen, welche Zeichentypen enthalten sein sollen:
  - Großbuchstaben (A-Z)
  - Kleinbuchstaben (a-z)
  - Ziffern (0-9)
  - Sonderzeichen (!@#$%^&*()_+-=[]{}|;:,.<>?)
- Generiere ein Passwort, das mindestens ein Zeichen von jedem ausgewählten Typ enthält
- Fülle den Rest zufällig auf
- Verwende List Comprehensions, wo sinnvoll
- Gib mehrere Passwörter zur Auswahl aus (z.B. 5 Stück)

**Beispiel Interaktion**:
```
Willkommen beim Passwort-Generator!

Passwortlänge (min. 8): 12

Welche Zeichentypen sollen enthalten sein?
Großbuchstaben (J/N): J
Kleinbuchstaben (J/N): J
Ziffern (J/N): J
Sonderzeichen (J/N): J

Generierte Passwörter:
1. K9#mPq2@xLz4
2. Tr5$aBw@9Yc!
3. Xs2&Nj7#Pq9L
4. Mz4@Lk8$Rt3B
5. Qw7#Hv2!Xn6C

Weiteres Passwort generieren? (J/N): N
```

**Hinweise**:
- Verwende `import random` und `random.choice()` für zufällige Auswahl
- Verwende `import string` für vordefinierte Zeichensets: `string.ascii_uppercase`, `string.ascii_lowercase`, `string.digits`
- Um sicherzustellen, dass mindestens ein Zeichen jedes Typs enthalten ist, wähle zunächst je ein Zeichen aus jedem Set und fülle dann auf
- Verwende `random.shuffle()`, um die Zeichen zu mischen
- Nutze List Comprehensions für kompakte Listen-Generierung

---

### Aufgabe P5: Text-Analyse-Tool (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: Alle bisherigen Schleifen-Konzepte, List Comprehensions, Dictionaries (Vorgriff auf V08)

Erstelle ein umfassendes Text-Analyse-Tool, das verschiedene Statistiken über einen eingegebenen Text berechnet.

**Anforderungen**:

1. **Eingabe**: Fordere den Benutzer auf, einen Text einzugeben (kann auch mehrzeilig sein, beendet durch eine Zeile mit nur "END")

2. **Grundlegende Statistiken**:
   - Anzahl der Zeichen (mit und ohne Leerzeichen)
   - Anzahl der Wörter
   - Anzahl der Sätze (Zähle '.', '!', '?')
   - Durchschnittliche Wortlänge
   - Durchschnittliche Satzlänge (in Wörtern)

3. **Zeichenanalyse**:
   - Anzahl Großbuchstaben
   - Anzahl Kleinbuchstaben
   - Anzahl Ziffern
   - Anzahl Sonderzeichen
   - Prozentuale Verteilung der obigen Kategorien

4. **Wortanalyse**:
   - Längstes Wort
   - Kürzestes Wort (ignoriere Wörter mit nur 1 Zeichen)
   - Die 5 häufigsten Wörter (case-insensitive)

5. **Erweiterte Analyse**:
   - Alle Wörter, die mit Großbuchstaben beginnen (potenzielle Eigennamen)
   - Alle Zahlen, die im Text vorkommen
   - Wörter mit mehr als 10 Buchstaben

6. **Ausgabe**: Präsentiere alle Statistiken übersichtlich formatiert

**Beispiel Ausgabe**:
```
=== TEXT-ANALYSE ===

Text eingeben (beende mit 'END' auf einer neuen Zeile):
> Python ist eine vielseitige Programmiersprache.
> Sie wurde 1991 von Guido van Rossum entwickelt.
> Heute nutzen über 8 Millionen Entwickler Python.
> END

--- GRUNDSTATISTIKEN ---
Zeichen (gesamt):        153
Zeichen (ohne Leerz.):   128
Wörter:                   18
Sätze:                     3
Ø Wortlänge:             7.1
Ø Satzlänge:             6.0

--- ZEICHENANALYSE ---
Großbuchstaben:          5 (3.3%)
Kleinbuchstaben:       112 (73.2%)
Ziffern:                 4 (2.6%)
Sonderzeichen:           7 (4.6%)
Leerzeichen:            25 (16.3%)

--- WORTANALYSE ---
Längstes Wort:           "Programmiersprache" (18 Buchstaben)
Kürzestes Wort:          "ist" (3 Buchstaben)

Top 5 häufigste Wörter:
  1. Python (2×)
  2. eine (1×)
  3. vielseitige (1×)
  4. Programmiersprache (1×)
  5. Sie (1×)

--- ERWEITERTE ANALYSE ---
Potenzielle Eigennamen: Python, Sie, Guido, Rossum, Heute, Python
Zahlen im Text: 1991, 8
Lange Wörter (>10): Programmiersprache, Entwickler
```

**Hinweise**:
- Verwende List Comprehensions für Filteroperationen
- Verwende ein Dictionary, um Worthäufigkeiten zu zählen (wird in V08 detailliert erklärt, aber hier kann es als Vorschau verwendet werden)
- Verwende `str.split()` zum Zerlegen in Wörter
- Verwende `str.strip(".,!?")`, um Satzzeichen von Wörtern zu entfernen
- Für das Zählen von Zeichentypen kannst du `str.isupper()`, `str.islower()`, `str.isdigit()` verwenden
- Strukturiere dein Programm mit Funktionen (Vorgriff auf V10), um es übersichtlich zu halten

**Bonus-Challenge** (optional):
- Berechne den "Flesch Reading Ease Score" (Lesbarkeitsindex)
- Erkenne und zähle E-Mail-Adressen und URLs im Text
- Erstelle ein einfaches Histogramm der Wortlängen-Verteilung mit ASCII-Art

