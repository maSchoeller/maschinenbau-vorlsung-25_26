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

### Aufgabe P1: CNC-Werkzeugwechsel-Sequenz optimieren (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Schleifen, `break`, List/Array-Verarbeitung  
**Maschinenbau-Kontext**: Optimierung von CNC-Werkzeugmagazin-Sequenzen

Schreibe ein Programm zur Suche nach **optimalen Werkzeugpositionen** in einem CNC-Werkzeugmagazin.

> [!NOTE]
> **CNC-Werkzeugmagazin**: Speichersystem für Fräs- und Drehwerkzeuge mit typisch 12-60 Positionen. Werkzeugwechsel kostet Zeit (2-10 Sekunden). Häufig genutzte Werkzeuge sollten an bevorzugten Positionen liegen.

**Aufgabe**:
Erstelle ein Programm, das ein **Werkzeug in einem Magazin sucht** und bei Fund die Schleife sofort beendet.

**Anforderungen**:
- Gegeben: Liste mit Werkzeug-IDs im Magazin (z.B. `[101, 205, 310, 405, 210, 115, 320]`)
- Eingabe: Gesuchte Werkzeug-ID
- Durchsuche das Magazin Position für Position
- Bei Fund: Gib Position aus und beende Suche mit `break`
- Verwende `else`-Klausel, um "Werkzeug nicht gefunden" anzuzeigen
- Zähle die Anzahl der geprüften Positionen (Suchaufwand)

**Beispiel Ein-/Ausgabe**:
```
Werkzeugmagazin: [101, 205, 310, 405, 210, 115, 320]
Gesuchte Werkzeug-ID: 210
─────────────────────────────────
Suche Werkzeug 210...
Position 1: 101 ❌
Position 2: 205 ❌
Position 3: 310 ❌
Position 4: 405 ❌
Position 5: 210 ✅ GEFUNDEN!
─────────────────────────────────
Werkzeug 210 gefunden auf Position 5
Suchaufwand: 5 Positionen geprüft
```

**Beispiel (nicht gefunden)**:
```
Gesuchte Werkzeug-ID: 999
─────────────────────────────────
...
❌ Werkzeug 999 nicht im Magazin!
Empfehlung: Werkzeug nachladen oder Programm anpassen.
```

**Hinweise**:
- Verwende `for i, werkzeug_id in enumerate(magazin, start=1):` für Position und ID
- `break` beendet die Suche sofort nach Fund (Effizienz!)
- Die `else`-Klausel der Schleife wird nur ausgeführt, wenn kein `break` erfolgte

---

### Aufgabe P2: Hydraulikdruck-Überwachung mit Eingabevalidierung (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 20-25 Minuten  
**Vorkenntnisse**: Schleifen, `break`, `continue`, Eingabevalidierung  
**Maschinenbau-Kontext**: Echtzeit-Überwachung von Hydrauliksystemen mit Fehlertoleranz

Erstelle ein **Hydraulikdruck-Überwachungssystem** mit robuster Eingabevalidierung.

> [!NOTE]
> **Hydraulik-Überwachung**: Kontinuierliche Druckmessung in hydraulischen Systemen (Pressen, Bagger, Industriemaschinen). Kritische Werte: Unterdruck < 50 bar (Leckage), Überdruck > 250 bar (Berstgefahr). Sensoren liefern manchmal fehlerhafte Werte durch elektromagnetische Störungen.

**Aufgabe**:
Simuliere eine **kontinuierliche Drucküberwachung** mit Eingabevalidierung und Alarmfunktion.

**Anforderungen**:
- Fordere den Benutzer wiederholt auf, Druckwerte einzugeben (simuliert Sensor-Readings)
- Validiere jede Eingabe:
  - Wenn keine gültige Zahl: Fehlermeldung + `continue` (Messung wiederholen)
  - Wenn negativer Wert: Fehlermeldung + `continue` (Sensor defekt)
  - Wenn Wert > 300 bar: Fehlermeldung + `continue` (unrealistisch)
- Bewerte gültige Druckwerte:
  - **< 50 bar**: 🔴 ALARM - Unterdruck! Leckage möglich!
  - **50-180 bar**: 🟢 OK - Normaler Betriebsbereich
  - **180-250 bar**: 🟡 WARNUNG - Hoher Druck!
  - **> 250 bar**: 🔴 ALARM - Überdruck! System abschalten!
- Bei ALARM: Beende Überwachung mit `break`
- Zähle gültige Messungen
- Eingabe "STOP" beendet die Überwachung manuell

**Beispiel Ablauf**:
```
═══════════════════════════════════
  Hydraulikdruck-Überwachung
═══════════════════════════════════
Normbereich: 50-180 bar
Warnung: 180-250 bar
Alarm: <50 bar oder >250 bar

Messung eingeben (oder 'STOP'): abc
⚠️  Fehler: Ungültiger Wert! Sensor prüfen.

Messung eingeben (oder 'STOP'): -5
⚠️  Fehler: Negativer Wert nicht möglich! Sensor defekt.

Messung eingeben (oder 'STOP'): 120
🟢 OK - Druck: 120.0 bar (Normal)

Messung eingeben (oder 'STOP'): 195
🟡 WARNUNG - Druck: 195.0 bar (Erhöht)

Messung eingeben (oder 'STOP'): 270
🔴 ALARM! Überdruck: 270.0 bar
SYSTEM WIRD ABGESCHALTET!
─────────────────────────────────
Überwachung beendet.
Gültige Messungen: 3
```

**Hinweise**:
- Verwende `while True:` für Endlosschleife
- Verwende `try-except` für robuste Eingabevalidierung
- `continue` überspringt ungültige Messungen
- `break` beendet bei kritischen Alarmen

---

### Aufgabe P3: Drehmoment-Tabelle für Schraubverbindungen (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25-30 Minuten  
**Vorkenntnisse**: Verschachtelte Schleifen, String-Formatierung  
**Maschinenbau-Kontext**: Anziehdrehmomente für ISO-Metrische Schrauben nach VDI 2230

Erstelle ein Programm zur Ausgabe einer **Anziehdrehmoment-Tabelle** für Schraubenverbindungen.

> [!NOTE]
> **Anziehdrehmoment**: Das Drehmoment, mit dem eine Schraube angezogen werden muss, um die gewünschte Vorspannkraft zu erreichen. Abhängig von:
> - **Gewindegröße** (M3, M4, M5, M6, M8, M10, M12, M16, M20...)
> - **Festigkeitsklasse** (4.6, 5.6, 8.8, 10.9, 12.9) - höhere Zahl = höhere Festigkeit
> - **Reibungsverhältnisse** (trocken, geölt, verzinkt)

**Aufgabe**:
Erstelle eine formatierte Tabelle mit Anziehdrehmomenten für verschiedene Schraubengrößen und Festigkeitsklassen.

**Vereinfachte Formel** (für trockene, verzinkte Schrauben):
$$M_A = 0.2 \times d \times F_{Vorspann}$$

Wobei:
- $M_A$ = Anziehdrehmoment [Nm]
- $d$ = Nenndurchmesser [mm]
- $F_{Vorspann}$ = Vorspannkraft [N] ≈ 0.7 × $A_S$ × $R_m$
- $A_S$ = Spannungsquerschnitt [mm²] ≈ 0.8 × $\frac{\pi d^2}{4}$
- $R_m$ = Zugfestigkeit [MPa] - abhängig von Festigkeitsklasse

**Festigkeitsklassen** (vereinfacht):
- 4.6: $R_m$ = 400 MPa
- 8.8: $R_m$ = 800 MPa
- 10.9: $R_m$ = 1000 MPa

**Anforderungen**:
- Eingabe: Liste der Gewindegrößen (z.B. M3, M4, M5, M6, M8, M10)
- Berechne Drehmomentwerte für Festigkeitsklassen 4.6, 8.8, 10.9
- Formatiere als übersichtliche Tabelle mit Überschriften
- Rechtsbündige Zahlenformatierung
- Trennlinie nach Kopfzeile

**Beispiel Ausgabe**:
```
═══════════════════════════════════════════════
  Anziehdrehmoment-Tabelle (trocken, verzinkt)
═══════════════════════════════════════════════
Gewinde |  4.6 [Nm] |  8.8 [Nm] | 10.9 [Nm]
────────|───────────|───────────|──────────
   M3   |      0.5  |      1.0  |      1.3
   M4   |      1.2  |      2.4  |      3.0
   M5   |      2.4  |      4.7  |      5.9
   M6   |      3.9  |      7.8  |      9.8
   M8   |      9.4  |     18.8  |     23.5
   M10  |     18.3  |     36.6  |     45.8
```

**Hinweise**:
- Verwende verschachtelte `for`-Schleifen: äußere für Gewindegrößen, innere für Festigkeitsklassen
- Extrahiere Durchmesser aus String "M6" → 6 mm
- Verwende f-String-Formatierung: `f"{wert:8.1f}"` für rechtsbündige Zahlen
- Die Trennlinie kann mit `"─" * breite` erzeugt werden

---

### Aufgabe P4: Prüfprotokoll-Generator für Qualitätskontrolle (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: List Comprehensions, String-Methoden, `random`-Modul  
**Maschinenbau-Kontext**: Automatisierte Generierung von Prüfprotokollen nach ISO 9001

Erstelle einen **Prüfprotokoll-Generator** für die Qualitätskontrolle in der Fertigung.

> [!NOTE]
> **Prüfprotokoll**: Dokumentation der Qualitätsprüfung mit Soll-Ist-Vergleich, Toleranzen und Bewertung (i.O./n.i.O.). Erforderlich nach ISO 9001, DIN EN 10204, IATF 16949. Enthält: Prüfmerkmal, Sollwert, Istwert, Toleranz, Status.

**Aufgabe**:
Generiere realistische Prüfprotokolle mit zufälligen, aber plausiblen Messwerten.

**Anforderungen**:
- Definiere Prüfmerkmale für ein Bauteil (z.B. Bohrdurchmesser, Länge, Oberflächenrauheit)
- Für jedes Merkmal: Sollwert und Toleranz
- Generiere zufällige Istwerte im realistischen Bereich (90% innerhalb Toleranz, 10% außerhalb)
- Bewertung: "i.O." wenn innerhalb Toleranz, sonst "n.i.O."
- Ausgabe als formatierte Tabelle
- Statistik: Gesamtbewertung (Alle i.O. → "Bauteil freigegeben", sonst "Bauteil gesperrt")

**Prüfmerkmale-Definition** (Beispiel für Wellenzapfen):
```python
pruefmerkmale = [
    {"name": "Durchmesser Ø20h7", "soll": 20.00, "toleranz": 0.021, "einheit": "mm"},
    {"name": "Länge gesamt", "soll": 150.0, "toleranz": 0.5, "einheit": "mm"},
    {"name": "Rauheit Ra", "soll": 1.6, "toleranz": 0.4, "einheit": "µm"},
    {"name": "Rundlauf", "soll": 0.0, "toleranz": 0.02, "einheit": "mm"},
    {"name": "Härte HRC", "soll": 58, "toleranz": 3, "einheit": "HRC"}
]
```

**Beispiel Ausgabe**:
```
═══════════════════════════════════════════════════════════════
  PRÜFPROTOKOLL - Qualitätskontrolle
═══════════════════════════════════════════════════════════════
Bauteil: Wellenzapfen WZ-2024-001
Datum: 2026-01-04
Prüfer: QK-42

─────────────────────────────────────────────────────────────
Prüfmerkmal          | Soll    | Ist     | Tol.   | Status
─────────────────────────────────────────────────────────────
Durchmesser Ø20h7    | 20.000  | 19.992  | ±0.021 | ✅ i.O.
Länge gesamt         | 150.0   | 150.3   | ±0.5   | ✅ i.O.
Rauheit Ra           | 1.6     | 1.4     | ±0.4   | ✅ i.O.
Rundlauf             | 0.0     | 0.015   | ±0.02  | ✅ i.O.
Härte HRC            | 58      | 62      | ±3     | ❌ n.i.O.
─────────────────────────────────────────────────────────────

GESAMT-BEWERTUNG: ❌ BAUTEIL GESPERRT
Grund: 1 von 5 Prüfmerkmalen außerhalb Toleranz
Maßnahme: Nacharbeit oder Ausschuss
```

**Hinweise**:
- Verwende `import random` und `random.uniform()` für Messwerte
- Verwende List Comprehensions für Filterung (z.B. alle n.i.O.-Merkmale)
- Berechne Abweichung: `abweichung = abs(ist - soll)`
- Status: `"i.O." if abweichung <= toleranz else "n.i.O."`
- Formatierung: f-Strings mit fester Breite für Tabellenausrichtung

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

### Aufgabe P5: Maschinendaten-Analyse-Tool (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: Alle Schleifen-Konzepte, List Comprehensions, String-Verarbeitung  
**Maschinenbau-Kontext**: Analyse von Maschinen-Logfiles für Predictive Maintenance

Erstelle ein umfassendes **Maschinendaten-Analyse-Tool** zur Auswertung von CNC-Maschinen-Logdateien.

> [!NOTE]
> **Predictive Maintenance**: Vorausschauende Wartung durch Analyse von Maschinendaten. Früherkennung von Verschleiß, Überlastung, Fehlermustern. Typische Datenquellen: CNC-Steuerung, SPS-Logs, Sensor-Streams. Format: Timestamped Events mit Parametern.

**Aufgabe**:
Analysiere einen Multi-Line-Maschinenlog und extrahiere relevante Statistiken.

**Log-Format** (Beispiel):
```
2026-01-04 08:15:23 | CNC-01 | SPINDLE_START | RPM=3000 | TOOL=T05
2026-01-04 08:15:45 | CNC-01 | FEED_RATE | F=500 | AXIS=X
2026-01-04 08:16:12 | CNC-01 | ALARM | CODE=E402 | MSG=Overload
2026-01-04 08:16:15 | CNC-01 | SPINDLE_STOP | RPM=0
2026-01-04 08:20:00 | CNC-02 | SPINDLE_START | RPM=5000 | TOOL=T12
```

**Eingabe**: 
Fordere den Benutzer auf, Log-Zeilen einzugeben (mehrzeilig, beendet durch Zeile mit nur "END")

**Zu analysierende Statistiken**:

1. **Grundlegende Statistiken**:
   - Anzahl der Log-Einträge gesamt
   - Anzahl verschiedener Maschinen (z.B. CNC-01, CNC-02...)
   - Zeitspanne (erste bis letzte Logzeile)
   - Anzahl verschiedener Event-Typen

2. **Event-Analyse**:
   - Anzahl SPINDLE_START / SPINDLE_STOP Events
   - Anzahl ALARM Events
   - Anzahl FEED_RATE Änderungen
   - Anzahl Werkzeugwechsel (TOOL=...)

3. **Maschinen-spezifisch**:
   - Welche Maschine hatte die meisten Events?
   - Welche Maschine hatte Alarme?
   - Liste aller verwendeten Werkzeuge (T01, T05, T12...)

4. **Alarm-Analyse**:
   - Alle Alarm-Codes mit Häufigkeit (z.B. E402: 3×, E101: 1×)
   - Durchschnittliche Drehzahl bei Alarmen
   - Kritischste Maschine (meiste Alarme)

5. **Drehzahl-Statistik**:
   - Minimale Drehzahl
   - Maximale Drehzahl
   - Durchschnittliche Drehzahl
   - Anzahl Hochgeschwindigkeits-Events (RPM > 8000)

6. **Werkzeug-Nutzung**:
   - Alle verwendeten Werkzeuge
   - Häufigstes Werkzeug
   - Anzahl Werkzeugwechsel

**Beispiel Ausgabe**:
```
═══════════════════════════════════════════════════
  MASCHINENDATEN-ANALYSE
═══════════════════════════════════════════════════

--- GRUNDSTATISTIKEN ---
Log-Einträge:              47
Erfasste Maschinen:         3 (CNC-01, CNC-02, CNC-03)
Zeitspanne:                 08:15:23 - 16:42:18
Event-Typen:                7

--- EVENT-ANALYSE ---
SPINDLE_START:             15
SPINDLE_STOP:              15
ALARM:                      5
FEED_RATE:                 12
Werkzeugwechsel:            8

--- MASCHINEN-ANALYSE ---
Aktivste Maschine:         CNC-01 (23 Events)
Maschinen mit Alarmen:     CNC-01 (3×), CNC-03 (2×)
Werkzeuge verwendet:       T01, T05, T08, T12, T15, T20

--- ALARM-DETAILS ---
Gesamt-Alarme:              5
Alarm-Codes:
  • E402 (Overload):        3×
  • E101 (Temp. High):      1×
  • E505 (Tool Broken):     1×
Kritischste Maschine:      CNC-01 (3 Alarme)

--- DREHZAHL-STATISTIK ---
Min. Drehzahl:             1200 RPM
Max. Drehzahl:             8500 RPM
Ø Drehzahl:                4750 RPM
Hochgeschw.-Events:         3 (RPM > 8000)

--- WERKZEUG-ANALYSE ---
Häufigstes Werkzeug:       T05 (5× verwendet)
Werkzeugwechsel-Rate:      0.17 pro Event
═══════════════════════════════════════════════════

⚠️  EMPFEHLUNG:
- CNC-01: Wartung prüfen (3 Alarme, davon 3× Overload)
- CNC-03: Temperatur überwachen (E101)
- Werkzeug T05: Verschleiß kontrollieren (häufig genutzt)
```

**Hinweise**:
- Verwende List Comprehensions für Filteroperationen
- Verwende `str.split("|")` zum Zerlegen der Log-Zeilen
- Verwende Dictionaries zum Zählen (Häufigkeiten)
- Strukturiere mit Funktionen (z.B. `parse_log_line()`, `analyze_alarms()`)
- Extrahiere Parameter mit String-Slicing oder `.split("=")`
- Verwende `try-except` für robuste Parsing-Fehlerbehandlung

**Bonus-Challenge** (optional):
- Erkenne Muster: Alarm immer nach hoher Drehzahl?
- Berechne durchschnittliche Zeit zwischen Alarmen
- Erstelle ASCII-Histogramm der Event-Verteilung pro Stunde


