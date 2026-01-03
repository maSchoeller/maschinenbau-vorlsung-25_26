# V07: Lösungen - Software Engineering & Schleifen Teil 2

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: Software-Prinzipien identifizieren

**Snippet 1 - Verletztes Prinzip: SRP (Single Responsibility Principle)**

**Lösung**:

Dieser Code verletzt massiv das Single Responsibility Principle. Die Funktion `verarbeite_kundendaten` hat mindestens **sechs verschiedene Verantwortlichkeiten**:

1. Datenbankzugriff (Kundendaten laden)
2. Datumsberechnung (Alter berechnen)
3. Geschäftslogik (Rabatt berechnen)
4. E-Mail-Versand (externe Kommunikation)
5. Logging (Protokollierung)
6. Statistik-Aktualisierung (Datenbankaktualisierung)

**Erklärung**:

Jede dieser Verantwortlichkeiten stellt einen eigenen "Grund zur Änderung" dar. Wenn sich beispielsweise die Rabatt-Berechnung ändert, muss diese Funktion geändert werden. Wenn der E-Mail-Server gewechselt wird, muss diese Funktion geändert werden. Wenn das Logging-Format geändert wird, muss diese Funktion geändert werden. Diese enge Kopplung verschiedener Anliegen macht den Code schwer wartbar und testbar.

**Verbesserte Struktur**:

```python
# Jede Funktion hat eine klare Verantwortlichkeit

def lade_kundendaten(kunde_id):
    """Lädt Kundendaten aus der Datenbank."""
    return db.query(f"SELECT * FROM kunden WHERE id = {kunde_id}")

def berechne_alter(geburtsdatum):
    """Berechnet Alter aus Geburtsdatum."""
    geburtsjahr = int(geburtsdatum.split("-")[0])
    return datetime.now().year - geburtsjahr

def berechne_rabatt(alter):
    """Berechnet altersabhängigen Rabatt."""
    if alter >= 65:
        return 0.15
    elif alter >= 18:
        return 0.05
    else:
        return 0.0

def sende_werbemail(kunde, rabatt):
    """Sendet Werbemail an Kunden."""
    email_text = f"Hallo {kunde.name}, Sie erhalten {rabatt * 100}% Rabatt!"
    smtp_server.send(kunde.email, email_text)

def protokolliere_verarbeitung(kunde_id):
    """Protokolliert Kundenverarbeitung."""
    with open("logs.txt", "a") as log:
        log.write(f"{kunde_id} verarbeitet am {datetime.now()}\n")

def aktualisiere_statistik(typ):
    """Aktualisiert Statistikzähler."""
    stats = db.query(f"SELECT count FROM statistik WHERE typ = '{typ}'")
    db.execute(f"UPDATE statistik SET count = {stats.count + 1} WHERE typ = '{typ}'")

# Orchestrierende Funktion
def verarbeite_kundendaten(kunde_id):
    """Koordiniert die Kundenverarbeitung."""
    kunde = lade_kundendaten(kunde_id)
    alter = berechne_alter(kunde.geburtsdatum)
    rabatt = berechne_rabatt(alter)
    sende_werbemail(kunde, rabatt)
    protokolliere_verarbeitung(kunde_id)
    aktualisiere_statistik('verarbeitungen')
```

**Häufige Fehler**:
- SRP mit "Funktion sollte nur eine Sache tun" verwechseln. SRP bezieht sich auf Verantwortlichkeit (Grund zur Änderung), nicht auf die Anzahl der Zeilen oder Operationen
- Orchestrierende Funktionen (die andere Funktionen koordinieren) können multiple Funktionsaufrufe enthalten, ohne SRP zu verletzen

---

**Snippet 2 - Verletztes Prinzip: DRY (Don't Repeat Yourself)**

**Lösung**:

Dieser Code verletzt das DRY-Prinzip durch **strukturelle Duplikation**. Alle Funktionen folgen demselben Muster: Berechnung einer Fläche und Rückgabe des Ergebnisses. Zudem wird die Konstante `pi` in `berechne_flaeche_kreis` hart codiert, was bei mehrfacher Verwendung zu Inkonsistenzen führen könnte.

**Erklärung**:

Obwohl die Formeln unterschiedlich sind, ist die Struktur identisch. Dies ist ein typischer Fall, in dem über-spezifische Funktionen erstellt wurden, wo eine generischere Lösung besser wäre. Zudem ist die Konstante `pi` nur lokal definiert, was bei mehrfacher Verwendung an anderen Stellen zu Duplikation führt.

**Verbesserte Struktur**:

```python
import math

# Konstanten zentral definieren
PI = math.pi

# Generischer Ansatz mit Strategy Pattern (fortgeschritten)
def berechne_flaeche(form, **parameter):
    """
    Berechnet Fläche verschiedener Formen.
    
    Args:
        form: Art der Form ('rechteck', 'quadrat', 'dreieck', 'kreis', 'trapez')
        **parameter: Formspezifische Parameter
    
    Returns:
        Berechnete Fläche
    """
    formeln = {
        'rechteck': lambda laenge, breite: laenge * breite,
        'quadrat': lambda seite: seite ** 2,
        'dreieck': lambda basis, hoehe: (basis * hoehe) / 2,
        'kreis': lambda radius: PI * radius ** 2,
        'trapez': lambda a, b, hoehe: ((a + b) / 2) * hoehe
    }
    
    if form not in formeln:
        raise ValueError(f"Unbekannte Form: {form}")
    
    return formeln[form](**parameter)

# Verwendung:
# flaeche_rechteck = berechne_flaeche('rechteck', laenge=5, breite=3)
# flaeche_kreis = berechne_flaeche('kreis', radius=2.5)

# Alternative: Wenn spezifische Funktionen gewünscht, aber DRY einhalten
def berechne_flaeche_rechteck(laenge, breite):
    return laenge * breite

def berechne_flaeche_quadrat(seite):
    return berechne_flaeche_rechteck(seite, seite)  # Wiederverwendung!

def berechne_flaeche_dreieck(basis, hoehe):
    return (basis * hoehe) / 2

def berechne_flaeche_kreis(radius):
    return PI * radius ** 2  # Zentrale Konstante

def berechne_flaeche_trapez(a, b, hoehe):
    return ((a + b) / 2) * hoehe
```

**Häufige Fehler**:
- DRY zu aggressiv anwenden: Zwei ähnliche Code-Stücke, die unterschiedliche Konzepte repräsentieren, sollten nicht zwingend zusammengefasst werden
- Die "Rule of Three" ignorieren: Erst beim dritten Vorkommen von Duplikation refaktorieren

---

**Snippet 3 - Verletztes Prinzip: KISS (Keep It Simple, Stupid)**

**Lösung**:

Dieser Code verletzt das KISS-Prinzip durch **unnötige Komplexität**:

1. Verschachtelte if-Statements für Validierung (cognitive complexity)
2. Manuelle Schleifen-Summierung statt eingebauter Funktionen
3. Wiederholte Rabatt-Berechnung mit Copy-Paste-Logik
4. Umständliche List-Iteration mit Index

**Erklärung**:

Die Validierungslogik ist tief verschachtelt und schwer zu lesen. Python bietet einfachere Wege, um mehrere Bedingungen zu prüfen. Die manuelle Summierung ist unnötig komplex, da Python `sum()` und List Comprehensions bietet. Die Rabatt-Berechnung wiederholt denselben Multiplikations-Ausdruck mehrfach.

**Verbesserte Struktur**:

```python
def verarbeite_bestellung(bestellung_id, kunde_name, kunde_email, 
                         artikel_liste, anzahl_liste, preis_liste, 
                         versand_adresse, zahlungsmethode, rabatt_code, notizen):
    # Einfache, flache Validierung mit frühen Returns (Guard Clauses)
    if not bestellung_id:
        return {"fehler": "Bestellung-ID fehlt"}
    if not kunde_name:
        return {"fehler": "Name fehlt"}
    if not kunde_email:
        return {"fehler": "Email fehlt"}
    
    # Einfache Gesamtpreis-Berechnung mit zip() und List Comprehension
    gesamt = sum(
        anzahl * preis 
        for anzahl, preis in zip(anzahl_liste, preis_liste)
        if anzahl > 0 and preis > 0
    )
    
    # Einfaches Rabatt-Mapping statt wiederholter if-elif
    rabatte = {
        "SOMMER2026": 0.10,
        "WINTER2026": 0.15,
        "NEUKUNDE": 0.20
    }
    
    rabatt_prozent = rabatte.get(rabatt_code, 0.0)
    gesamt = gesamt * (1 - rabatt_prozent)
    
    return {"gesamt": gesamt}
```

**Noch einfacher mit frühen Validierungen ausgelagert:**

```python
def validiere_pflichtfelder(bestellung_id, kunde_name, kunde_email):
    """Validiert Pflichtfelder und gibt Fehlermeldung zurück."""
    felder = {
        'bestellung_id': bestellung_id,
        'kunde_name': kunde_name,
        'kunde_email': kunde_email
    }
    
    for feld_name, wert in felder.items():
        if not wert:
            return {"fehler": f"{feld_name} fehlt"}
    
    return None  # Keine Fehler

def berechne_bestellwert(artikel_liste, anzahl_liste, preis_liste):
    """Berechnet Gesamtwert der Bestellung."""
    return sum(
        anzahl * preis 
        for anzahl, preis in zip(anzahl_liste, preis_liste)
        if anzahl > 0 and preis > 0
    )

def wende_rabatt_an(betrag, rabatt_code):
    """Wendet Rabattcode auf Betrag an."""
    rabatte = {
        "SOMMER2026": 0.10,
        "WINTER2026": 0.15,
        "NEUKUNDE": 0.20
    }
    rabatt = rabatte.get(rabatt_code, 0.0)
    return betrag * (1 - rabatt)

def verarbeite_bestellung(bestellung_id, kunde_name, kunde_email, 
                         artikel_liste, anzahl_liste, preis_liste, 
                         versand_adresse, zahlungsmethode, rabatt_code, notizen):
    # Validierung
    fehler = validiere_pflichtfelder(bestellung_id, kunde_name, kunde_email)
    if fehler:
        return fehler
    
    # Berechnung
    gesamt = berechne_bestellwert(artikel_liste, anzahl_liste, preis_liste)
    gesamt = wende_rabatt_an(gesamt, rabatt_code)
    
    return {"gesamt": gesamt}
```

**Häufige Fehler**:
- KISS mit "möglichst wenig Code" verwechseln. Manchmal ist mehr Code (durch Aufteilung in Funktionen) tatsächlich einfacher zu verstehen
- Etablierte Python-Idiome ignorieren (z.B. `zip()`, `sum()`, Dictionary-Lookups) zugunsten von "selbst implementierten" Lösungen

---

### Lösung T2: Refactoring-Strategien

**1. Identifizierte Verstöße**:

1. **DRY-Verstoß**: Manuelle Summierung mit Schleife statt `sum()`
2. **DRY-Verstoß**: String-Konkatenation mit `+` statt f-Strings oder `.join()`
3. **SRP-Verstoß**: Funktion berechnet Durchschnitt, bestimmt Status, bestimmt Altersgruppe und formatiert Ausgabe
4. **KISS-Verstoß**: Umständliche Bedingung `alter >= 20 and alter < 25` statt `20 <= alter < 25`
5. **KISS-Verstoß**: Verwendung von Index-basierten Tupeln statt benannter Datenstrukturen
6. **DRY-Verstoß**: Wiederholte Typ-Konvertierung zu String bei Formatierung
7. **KISS-Verstoß**: Lange Zeile mit vielen String-Konkatenationen schwer lesbar

**2. Refactoring-Plan**:

**Schritt 1**: Funktionen für einzelne Berechnungen extrahieren
- `berechne_durchschnitt(noten)` → berechnet Notendurchschnitt
- `bestimme_status(durchschnitt)` → bestimmt Bestanden/Nicht bestanden
- `bestimme_altersgruppe(alter)` → bestimmt Altersgruppe

**Schritt 2**: Datenstruktur verbessern
- Verwende Dictionaries oder Named Tuples statt Index-Tupel
- Input: `[{"name": "Max", "alter": 22, "noten": [4.5, 5.0, 4.0]}, ...]`

**Schritt 3**: Formatierung auslagern
- `formatiere_student_zeile(student_daten)` → formatiert einen Studenten

**Schritt 4**: Moderne Python-Features nutzen
- List Comprehension für die Hauptschleife
- f-Strings für Formatierung
- `sum()` für Durchschnittsberechnung

**Schritt 5**: Orchestrierende Funktion vereinfachen
- Hauptfunktion ruft nur noch Hilfsfunktionen auf

**3. Verbesserte Struktur** (Skizze):

```python
def berechne_durchschnitt(noten):
    """
    Berechnet Notendurchschnitt.
    
    Args:
        noten: Liste von Noten (float)
    
    Returns:
        Durchschnitt (float)
    """
    # return sum(noten) / len(noten)

def bestimme_status(durchschnitt):
    """
    Bestimmt Bestanden/Nicht bestanden.
    
    Args:
        durchschnitt: Notendurchschnitt (float)
    
    Returns:
        "Bestanden" oder "Nicht bestanden" (str)
    """
    # return "Bestanden" if durchschnitt >= 4.0 else "Nicht bestanden"

def bestimme_altersgruppe(alter):
    """
    Kategorisiert Alter in Gruppen.
    
    Args:
        alter: Alter (int)
    
    Returns:
        Altersgruppe (str)
    """
    # if alter < 20: return "Jung"
    # elif 20 <= alter < 25: return "Mittel"
    # else: return "Älter"

def formatiere_student_zeile(name, alter, gruppe, durchschnitt, status):
    """
    Formatiert Studentendaten als String.
    
    Args:
        name, alter, gruppe, durchschnitt, status
    
    Returns:
        Formatierte Zeile (str)
    """
    # return f"{name} | Alter: {alter} | Gruppe: {gruppe} | Durchschnitt: {durchschnitt:.2f} | Status: {status}"

def verarbeite_studentendaten(daten_liste):
    """
    Verarbeitet Liste von Studentendaten.
    
    Args:
        daten_liste: Liste von Dictionaries mit Keys 'name', 'alter', 'noten'
    
    Returns:
        Liste formatierter Zeilen
    """
    # ergebnis = []
    # for student in daten_liste:
    #     durchschnitt = berechne_durchschnitt(student['noten'])
    #     status = bestimme_status(durchschnitt)
    #     gruppe = bestimme_altersgruppe(student['alter'])
    #     zeile = formatiere_student_zeile(
    #         student['name'], student['alter'], gruppe, durchschnitt, status
    #     )
    #     ergebnis.append(zeile)
    # return ergebnis
    
    # Oder mit List Comprehension (kompakter):
    # return [
    #     formatiere_student_zeile(
    #         s['name'], 
    #         s['alter'], 
    #         bestimme_altersgruppe(s['alter']),
    #         (d := berechne_durchschnitt(s['noten'])),
    #         bestimme_status(d)
    #     )
    #     for s in daten_liste
    # ]
```

**4. Vorteile der refaktorisierten Version**:

**Wartbarkeit**:
- Änderungen an der Durchschnittsberechnung betreffen nur eine Funktion
- Änderungen am Formatierungs-String betreffen nur `formatiere_student_zeile`
- Änderungen an Altersgruppen-Kriterien betreffen nur `bestimme_altersgruppe`

**Testbarkeit**:
- Jede Funktion kann unabhängig getestet werden
- Unit Tests sind einfach und präzise: `assert berechne_durchschnitt([4, 5, 6]) == 5.0`
- Keine komplexen Test-Setups nötig

**Lesbarkeit**:
- Funktionsnamen dokumentieren, was passiert
- Keine verschachtelten Schleifen oder lange Zeilen
- Klare Trennung von Logik und Formatierung

**Wiederverwendbarkeit**:
- `berechne_durchschnitt` kann in anderen Kontexten verwendet werden
- `bestimme_altersgruppe` kann für andere Zwecke genutzt werden

**Erweiterbarkeit**:
- Neue Statustypen können einfach zu `bestimme_status` hinzugefügt werden
- Neue Formatierungen können als separate Funktion implementiert werden
- Neue Datenfelder können ohne große Umbauten integriert werden

**Häufige Fehler**:
- Über-Refactoring: Nicht jede Zeile Code muss in eine Funktion. Die Aufteilung sollte logisch sinnvoll sein
- Funktionen zu granular machen: `addiere_zwei_zahlen(a, b)` ist übertrieben für `a + b`

---

### Lösung T3: Code Review und Design-Entscheidungen

**1. Funktionale Analyse**:

**Akzeptierte Passwörter:**
- `"MyP@ssw0rd123"` ✅ (Groß, klein, Ziffer, Sonder, keine Triplets, keine Muster)
- `"Secure#123Xyz"` ✅
- `"TrG9!mP2&xL"` ✅

**Abgelehnte Passwörter:**
- `"short1!"` ❌ (zu kurz, < 8)
- `"nouppercase123!"` ❌ (kein Großbuchstabe)
- `"NOLOWERCASE123!"` ❌ (kein Kleinbuchstabe)
- `"NoDigits!"` ❌ (keine Ziffer)
- `"NoSpecial123"` ❌ (kein Sonderzeichen)
- `"Pass123!!!"` ❌ (drei aufeinanderfolgende `!`)
- `"MyPassword123!"` ❌ (enthält "password")
- `"Abc123!@#456"` ❌ (enthält "abc" und "123")

**Problematische Grenzfälle:**
- Sehr lange Passwörter (> 64 Zeichen) werden abgelehnt – aber warum diese Obergrenze?
- Passwörter mit Unicode-Zeichen (z.B. "Päss€123!") werden möglicherweise falsch verarbeitet
- Die Muster-Erkennung ist case-insensitive, könnte aber auch Teile legitimer Wörter finden (z.B. "Rabc" enthält "abc")
- Drei identische Zeichen hintereinander werden abgelehnt, aber "aabbaabb" wäre akzeptiert

**2. Prinzipienverletzungen**:

**DRY - Massiv verletzt:**
- Die Zeichentyp-Prüfungen (Groß, Klein, Ziffer, Sonder) folgen alle demselben Muster: Initialisiere Boolean-Flag, iteriere über String, setze Flag wenn gefunden, prüfe Flag
- Dieser Code-Block wird viermal wiederholt mit minimalen Variationen

**KISS - Moderat verletzt:**
- Die Funktion ist mit 40+ Zeilen relativ lang
- Jede Validierungsregel ist ein separater Code-Block, was zu Wiederholung führt
- Die verschachtelten Bedingungen (if not hat_gross: return False) machen den Kontrollfluss starr

**SRP - Leicht verletzt:**
- Die Funktion hat technisch eine Verantwortlichkeit (Passwort validieren), aber sie implementiert ~8 verschiedene Validierungsregeln in einer Funktion
- Bei Änderung einer Regel muss die gesamte Funktion geändert werden
- Schwer zu testen: Ein Unit Test muss alle Regeln gleichzeitig berücksichtigen

**Am stärksten verletzt: DRY**

**3. Alternative Refactoring-Ansätze**:

**Ansatz A: Fokus auf DRY und Modularität**

Struktur:
```python
# Liste von Validierungsfunktionen
def hat_mindestlaenge(passwort, min_laenge=8):
    return len(passwort) >= min_laenge

def hat_maximallaenge(passwort, max_laenge=64):
    return len(passwort) <= max_laenge

def hat_grossbuchstabe(passwort):
    return any(c.isupper() for c in passwort)

def hat_kleinbuchstabe(passwort):
    return any(c.islower() for c in passwort)

def hat_ziffer(passwort):
    return any(c.isdigit() for c in passwort)

def hat_sonderzeichen(passwort, sonderzeichen="!@#$%^&*()_+-=[]{}|;:,.<>?"):
    return any(c in sonderzeichen for c in passwort)

def hat_keine_triplets(passwort):
    for i in range(len(passwort) - 2):
        if passwort[i] == passwort[i+1] == passwort[i+2]:
            return False
    return True

def enthaelt_keine_muster(passwort, verbotene_muster=None):
    if verbotene_muster is None:
        verbotene_muster = ["123", "abc", "qwe", "password", "admin"]
    passwort_lower = passwort.lower()
    return not any(muster in passwort_lower for muster in verbotene_muster)

# Hauptfunktion koordiniert Validierungen
def validiere_passwort(passwort):
    """Validiert Passwort nach allen Regeln."""
    validierungen = [
        (hat_mindestlaenge(passwort), "Mindestens 8 Zeichen"),
        (hat_maximallaenge(passwort), "Maximal 64 Zeichen"),
        (hat_grossbuchstabe(passwort), "Mindestens ein Großbuchstabe"),
        (hat_kleinbuchstabe(passwort), "Mindestens ein Kleinbuchstabe"),
        (hat_ziffer(passwort), "Mindestens eine Ziffer"),
        (hat_sonderzeichen(passwort), "Mindestens ein Sonderzeichen"),
        (hat_keine_triplets(passwort), "Keine drei identischen Zeichen hintereinander"),
        (enthaelt_keine_muster(passwort), "Enthält verbotenes Muster")
    ]
    
    for erfuellt, fehlermeldung in validierungen:
        if not erfuellt:
            return (False, fehlermeldung)
    
    return (True, "Passwort ist gültig")
```

**Ansatz B: Fokus auf KISS und Lesbarkeit**

Struktur:
```python
def validiere_passwort(passwort):
    """
    Validiert Passwort nach Sicherheitsrichtlinien.
    Gibt (gueltig, fehlermeldung) zurück.
    """
    # Länge prüfen
    if not (8 <= len(passwort) <= 64):
        return (False, "Passwort muss zwischen 8 und 64 Zeichen lang sein")
    
    # Zeichentypen prüfen mit any()
    if not any(c.isupper() for c in passwort):
        return (False, "Mindestens ein Großbuchstabe erforderlich")
    
    if not any(c.islower() for c in passwort):
        return (False, "Mindestens ein Kleinbuchstabe erforderlich")
    
    if not any(c.isdigit() for c in passwort):
        return (False, "Mindestens eine Ziffer erforderlich")
    
    sonderzeichen = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in sonderzeichen for c in passwort):
        return (False, "Mindestens ein Sonderzeichen erforderlich")
    
    # Triplets prüfen
    for i in range(len(passwort) - 2):
        if passwort[i] == passwort[i+1] == passwort[i+2]:
            return (False, "Keine drei identischen Zeichen hintereinander erlaubt")
    
    # Verbotene Muster prüfen
    verbotene_muster = ["123", "abc", "qwe", "password", "admin"]
    passwort_lower = passwort.lower()
    for muster in verbotene_muster:
        if muster in passwort_lower:
            return (False, f"Verbotenes Muster '{muster}' enthalten")
    
    return (True, "Passwort ist gültig")
```

**4. Design-Diskussion**:

**Wartbarkeit:**
- **Ansatz A gewinnt**: Neue Validierungsregeln können als separate Funktionen hinzugefügt werden, ohne bestehende Logik zu ändern. Regeln können einzeln dokumentiert und getestet werden.
- **Ansatz B**: Neue Regeln erfordern Änderungen in der Hauptfunktion, was potenziell bestehende Regeln beeinflussen könnte.

**Testbarkeit:**
- **Ansatz A gewinnt deutlich**: Jede Validierungsfunktion kann unabhängig mit Unit Tests geprüft werden. `assert hat_grossbuchstabe("Test") == True` ist einfach und fokussiert.
- **Ansatz B**: Tests müssen vollständige Passwörter konstruieren, die alle anderen Regeln erfüllen, nur um eine Regel zu testen. Dies führt zu komplexen Test-Setups.

**Erweiterbarkeit:**
- **Ansatz A gewinnt**: Neue Regeln sind einfache neue Funktionen. Regeln können parametrisiert werden (z.B. `min_laenge` als Parameter). Regeln können dynamisch zur Laufzeit hinzugefügt oder entfernt werden (z.B. basierend auf User-Profil: Admins strengere Regeln).
- **Ansatz B**: Erweiterungen erfordern Änderungen in der Hauptfunktion. Dynamische Regeln sind schwierig umzusetzen.

**Performance:**
- **Ansatz B gewinnt leicht**: Alle Prüfungen sind inline, keine Funktionsaufrufe. Allerdings ist der Unterschied vernachlässigbar, da Passwort-Validierung nicht performance-kritisch ist.
- **Ansatz A**: Leichter Overhead durch Funktionsaufrufe, aber praktisch nicht messbar.

**Lesbarkeit:**
- **Unentschieden/Geschmackssache**: 
  - Ansatz A: Klare Funktionsnamen dokumentieren, was geprüft wird. Die Hauptfunktion ist eine übersichtliche Liste von Validierungen.
  - Ansatz B: Alle Logik in einer Funktion, keine Sprungs zwischen Funktionen nötig. Für einfache Fälle gut lesbar.

**Empfehlung: Ansatz A** für professionelle Anwendungen, da Wartbarkeit, Testbarkeit und Erweiterbarkeit langfristig wichtiger sind als minimale Performance-Unterschiede.

**5. Fehler-Reporting**:

Das aktuelle `True`/`False`-Rückgabeformat ist unzureichend für reale Anwendungen. Benutzer sollten wissen, *warum* ihr Passwort abgelehnt wurde.

**Ansatz 1: Tuple mit Fehlermeldung (einfach, KISS-konform)**
```python
def validiere_passwort(passwort):
    # ...
    return (True, "Gültig")  # oder (False, "Fehler: ...")
```

Vorteil: Einfach zu verwenden, kein zusätzlicher Typ nötig.  
Nachteil: Caller muss Tuple unpacking verwenden: `gueltig, meldung = validiere_passwort(pw)`

**Ansatz 2: Dictionary mit Details**
```python
def validiere_passwort(passwort):
    # ...
    return {
        "gueltig": True,
        "fehler": None,
        "erfuellte_regeln": ["laenge", "gross", "klein", ...],
        "nicht_erfuellte_regeln": []
    }
```

Vorteil: Sehr detailliert, maschinenlesbar.  
Nachteil: Komplexer, könnte gegen KISS verstoßen für einfache Anwendungsfälle.

**Ansatz 3: Liste aller Fehler**
```python
def validiere_passwort(passwort):
    fehler = []
    
    if len(passwort) < 8:
        fehler.append("Mindestens 8 Zeichen erforderlich")
    # ...
    
    return (len(fehler) == 0, fehler)
```

Vorteil: Zeigt *alle* Probleme auf einmal, nicht nur den ersten Fehler.  
Nachteil: Etwas komplexer, aber für UX besser.

**Empfehlung für KISS-Konformität: Ansatz 1 oder 3**

Ansatz 1 ist am einfachsten und reicht für die meisten Fälle. Ansatz 3 ist etwas komplexer, aber bietet deutlich bessere User Experience, ohne übermäßig komplex zu werden. Ansatz 2 ist für einfache Passwort-Validierung übertrieben.

**Best Practice**: Beginne mit Ansatz 1. Wenn sich herausstellt, dass mehrere Fehler gleichzeitig angezeigt werden sollen, refaktoriere zu Ansatz 3. "You Aren't Gonna Need It" (YAGNI) – implementiere nur, was tatsächlich gebraucht wird.

**Häufige Fehler**:
- Fehler-Reporting zu komplex machen (Ansatz 2 für einfache Anwendungsfälle)
- Fehler-Reporting ganz weglassen (nur True/False) – frustrierend für Benutzer
- Fehler-Reporting nicht konsistent über die Codebasis hinweg

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: Primzahlen-Finder mit break

**Vollständiger Code**:
```python
# Primzahlen-Finder mit break und else-Klausel

# Eingabe
obergrenze = int(input("Obergrenze eingeben: "))

print(f"Primzahlen bis {obergrenze}:")

# Für jede Zahl ab 2 bis zur Obergrenze
for zahl in range(2, obergrenze + 1):
    # Prüfe, ob die Zahl eine Primzahl ist
    # Teste alle möglichen Teiler von 2 bis zahl-1
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            # Teiler gefunden -> keine Primzahl
            break  # Innere Schleife abbrechen
    else:
        # else wird nur ausgeführt, wenn break NICHT aufgerufen wurde
        # Das bedeutet: Kein Teiler gefunden -> Primzahl
        print(zahl, end=" ")

print()  # Zeilenumbruch am Ende
```

**Erklärung**:

Das Programm verwendet zwei verschachtelte Schleifen. Die äußere Schleife iteriert über alle Zahlen von 2 bis zur Obergrenze. Für jede Zahl wird in der inneren Schleife geprüft, ob ein Teiler existiert.

Die innere Schleife testet alle Zahlen von 2 bis `zahl - 1` als potenzielle Teiler. Sobald ein Teiler gefunden wird (Rest der Division ist 0), wird `break` aufgerufen, um die Prüfung abzubrechen. Die `else`-Klausel der Schleife wird nur ausgeführt, wenn die Schleife vollständig durchlaufen wurde, ohne dass `break` aufgerufen wurde. Das bedeutet, dass kein Teiler gefunden wurde, also ist die Zahl eine Primzahl.

**Optimierte Version** (mit Quadratwurzel-Optimierung):
```python
import math

obergrenze = int(input("Obergrenze eingeben: "))

print(f"Primzahlen bis {obergrenze}:")

for zahl in range(2, obergrenze + 1):
    # Optimierung: Nur bis zur Quadratwurzel testen
    grenze = int(math.sqrt(zahl)) + 1
    
    for teiler in range(2, grenze):
        if zahl % teiler == 0:
            break
    else:
        print(zahl, end=" ")

print()
```

**Warum diese Optimierung funktioniert:**

Wenn eine Zahl n einen Teiler größer als √n hat, dann muss sie auch einen Teiler kleiner als √n haben. Beispiel: 36 = 6 × 6. Wenn wir also bis √n testen und keinen Teiler finden, können wir sicher sein, dass n eine Primzahl ist. Dies reduziert die Anzahl der Tests dramatisch: Für n=100 müssen wir nur bis 10 testen statt bis 99.

**Schritt-für-Schritt Durchlauf** (für Obergrenze = 10):

1. zahl = 2: Innere Schleife läuft von 2 bis 1 (leer) → else ausgeführt → 2 ausgegeben
2. zahl = 3: Teste teiler=2: 3 % 2 = 1 (kein Teiler) → else ausgeführt → 3 ausgegeben
3. zahl = 4: Teste teiler=2: 4 % 2 = 0 (Teiler!) → break → else übersprungen
4. zahl = 5: Teste teiler=2,3,4: Keine Teiler → else ausgeführt → 5 ausgegeben
5. zahl = 6: Teste teiler=2: 6 % 2 = 0 (Teiler!) → break → else übersprungen
6. zahl = 7: Teste teiler=2,3,4,5,6: Keine Teiler → else ausgeführt → 7 ausgegeben
7. zahl = 8: Teste teiler=2: 8 % 2 = 0 (Teiler!) → break → else übersprungen
8. zahl = 9: Teste teiler=2: 9 % 2 = 1, teiler=3: 9 % 3 = 0 (Teiler!) → break → else übersprungen
9. zahl = 10: Teste teiler=2: 10 % 2 = 0 (Teiler!) → break → else übersprungen

Ausgabe: `2 3 5 7`

**Häufige Fehler**:
- **Fehler**: Schleife beginnt bei 1 statt bei 2
  - **Warum falsch**: 1 ist per Definition keine Primzahl
  - **Richtig**: `for zahl in range(2, obergrenze + 1)`

- **Fehler**: `else` mit `if` verwechseln
  ```python
  # Falsch:
  for teiler in range(2, zahl):
      if zahl % teiler == 0:
          break
  if kein_teiler_gefunden:  # Wie setze ich dieses Flag?
      print(zahl)
  ```
  - **Warum falsch**: Erfordert zusätzliches Boolean-Flag
  - **Richtig**: `else`-Klausel verwenden

- **Fehler**: Bereich der inneren Schleife falsch
  ```python
  # Falsch:
  for teiler in range(2, zahl + 1):  # Testet auch zahl selbst
  ```
  - **Warum falsch**: Jede Zahl ist durch sich selbst teilbar, daher würde immer ein Teiler gefunden
  - **Richtig**: `range(2, zahl)` (exklusiv zahl)

---

### Lösung P2: Zahlenrate-Spiel mit continue

**Vollständiger Code**:
```python
import random

# Computer wählt Zufallszahl
geheimzahl = random.randint(1, 100)

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")

versuche = 0

while True:
    # Eingabe anfordern
    eingabe = input("Dein Tipp: ")
    versuche += 1
    
    # Validierung: Ist es eine Zahl?
    if not eingabe.strip().isdigit() or eingabe.strip().startswith('-'):
        print("Das ist keine gültige Zahl! Versuche es nochmal.")
        continue  # Nächste Iteration ohne Versuchszähler zu erhöhen
    
    tipp = int(eingabe)
    
    # Validierung: Ist die Zahl im Bereich?
    if not (1 <= tipp <= 100):
        print("Die Zahl muss zwischen 1 und 100 liegen!")
        continue  # Nächste Iteration
    
    # Vergleich mit Geheimzahl
    if tipp < geheimzahl:
        print("Zu niedrig!")
    elif tipp > geheimzahl:
        print("Zu hoch!")
    else:
        # Richtig geraten!
        print(f"Richtig! Du hast die Zahl in {versuche} Versuchen erraten.")
        break  # Spiel beenden
```

**Erklärung**:

Das Programm verwendet eine `while True`-Schleife, um kontinuierlich Eingaben zu erfragen. Diese Endlosschleife wird nur durch `break` bei korrekter Eingabe beendet.

Die Validierungslogik nutzt `continue`, um ungültige Eingaben zu überspringen, ohne den Vergleich mit der Geheimzahl durchzuführen. Dies ist ein typisches Anwendungsbeispiel für `continue`: Frühe Validierung und Überspringen des restlichen Schleifenkörpers bei ungültigen Daten.

**Schritt-für-Schritt Erklärung der Validierung**:

1. **Erste Validierung**: `if not eingabe.strip().isdigit() or eingabe.strip().startswith('-'):`
   - `eingabe.strip()` entfernt führende/nachfolgende Leerzeichen
   - `.isdigit()` prüft, ob alle Zeichen Ziffern sind
   - `startswith('-')` prüft auf negative Zahlen (die `.isdigit()` passieren würden, aber Minuszeichen hat)
   - Bei Fehler: Fehlermeldung und `continue` (überspringt Rest der Iteration)

2. **Konvertierung**: `tipp = int(eingabe)`
   - Erst nach erfolgreicher Validierung wird konvertiert

3. **Zweite Validierung**: `if not (1 <= tipp <= 100):`
   - Prüft, ob Zahl im gültigen Bereich liegt
   - Verwendet Python's chained comparison für Eleganz
   - Bei Fehler: Fehlermeldung und `continue`

4. **Vergleich**: Nur wenn beide Validierungen erfolgreich waren, wird die Zahl mit der Geheimzahl verglichen

**Verbesserte Version** (mit Versuchslimit und besserer Validierung):
```python
import random

geheimzahl = random.randint(1, 100)
max_versuche = 7
versuche = 0

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
print(f"Du hast {max_versuche} Versuche.")

while versuche < max_versuche:
    eingabe = input(f"Versuch {versuche + 1}/{max_versuche}: ")
    
    # Validierung
    eingabe = eingabe.strip()
    
    if not eingabe:
        print("Keine Eingabe! Bitte gib eine Zahl ein.")
        continue
    
    # Prüfe auf negative Zahlen
    if eingabe.startswith('-'):
        print("Negative Zahlen sind nicht erlaubt!")
        continue
    
    # Prüfe auf Nicht-Zahlen
    if not eingabe.isdigit():
        print("Das ist keine gültige Zahl!")
        continue
    
    tipp = int(eingabe)
    versuche += 1  # Nur gültige Versuche zählen
    
    # Bereichsprüfung
    if not (1 <= tipp <= 100):
        print("Die Zahl muss zwischen 1 und 100 liegen!")
        # Versuch wurde bereits gezählt
        continue
    
    # Vergleich
    if tipp < geheimzahl:
        print("Zu niedrig!")
    elif tipp > geheimzahl:
        print("Zu hoch!")
    else:
        print(f"Richtig! Du hast die Zahl in {versuche} Versuchen erraten.")
        break
else:
    # else-Klausel der while-Schleife: Wird ausgeführt, wenn break NICHT aufgerufen wurde
    print(f"\nSchade! Du hast alle {max_versuche} Versuche aufgebraucht.")
    print(f"Die richtige Zahl war {geheimzahl}.")
```

**Häufige Fehler**:
- **Fehler**: Versuchszähler an falscher Stelle inkrementieren
  ```python
  # Falsch:
  versuche += 1
  eingabe = input("Tipp: ")
  if not eingabe.isdigit():
      continue  # Versuch wurde bereits gezählt!
  ```
  - **Warum falsch**: Ungültige Eingaben zählen als Versuche
  - **Richtig**: Inkrementiere erst nach erfolgreicher Validierung

- **Fehler**: Negative Zahlen nicht abfangen
  ```python
  # Problematisch:
  if eingabe.isdigit():
      tipp = int(eingabe)
  # "-5" passiert isdigit() nicht, aber was ist mit dem Minuszeichen?
  ```
  - **Lösung**: Explizit auf führendes Minuszeichen prüfen

- **Fehler**: Endlos-Schleife ohne Abbruch
  ```python
  # Gefährlich:
  while True:
      # ... Validierung ...
      # Vergessen: break bei richtigem Tipp!
  ```
  - **Lösung**: Immer Abbruchbedingung einbauen

---

### Lösung P3: Multiplikationstabelle mit verschachtelten Schleifen

**Vollständiger Code**:
```python
# Multiplikationstabelle mit Formatierung

groesse = int(input("Größe der Tabelle: "))

# Berechne maximale Zahl (für Spaltenbreite)
max_zahl = groesse * groesse
spaltenbreite = len(str(max_zahl)) + 1

# Kopfzeile
# Erste Spalte (Zeilen-Header) leer lassen
print(" " * (spaltenbreite + 1), end="| ")

# Spalten-Überschriften
for spalte in range(1, groesse + 1):
    print(f"{spalte:>{spaltenbreite}}", end=" ")
print()

# Trennlinie
trennlinie_laenge = (spaltenbreite + 1) + (groesse * (spaltenbreite + 1))
print("-" * (spaltenbreite + 1) + "+" + "-" * (groesse * (spaltenbreite + 1)))

# Tabellenzeilen
for zeile in range(1, groesse + 1):
    # Zeilen-Header
    print(f"{zeile:>{spaltenbreite}} |", end=" ")
    
    # Zeilen-Inhalt (die Multiplikationen)
    for spalte in range(1, groesse + 1):
        produkt = zeile * spalte
        print(f"{produkt:>{spaltenbreite}}", end=" ")
    
    print()  # Zeilenumbruch nach jeder Zeile
```

**Erklärung**:

Das Programm erstellt eine formatierte Multiplikationstabelle mit Überschriften und Trennlinien.

**Schritt-für-Schritt Erklärung**:

1. **Spaltenbreite berechnen**:
   - Die maximale Zahl in der Tabelle ist `groesse * groesse`
   - Die Spaltenbreite muss groß genug sein, um diese Zahl darzustellen
   - `len(str(max_zahl))` gibt die Anzahl der Ziffern zurück
   - `+ 1` für zusätzlichen Abstand zwischen Spalten

2. **Kopfzeile erstellen**:
   - Erste Spalte leer lassen (Platz für Zeilen-Header)
   - Dann Spalten-Überschriften (1, 2, 3, ...) rechtsbündig formatieren
   - `f"{spalte:>{spaltenbreite}}"` formatiert rechtsbündig mit Breite `spaltenbreite`

3. **Trennlinie**:
   - Länge berechnen: Zeilen-Header + Trennzeichen + alle Spalten
   - `"-" * laenge` erstellt String mit wiederholten Bindestrichen

4. **Tabellenzeilen**:
   - Äußere Schleife: Zeilen (1 bis groesse)
   - Zeilen-Header ausgeben (Zeilennummer rechtsbündig)
   - Innere Schleife: Spalten (1 bis groesse)
   - Produkt berechnen und rechtsbündig ausgeben

**Erweiterte Version** (mit Quadratzahl-Hervorhebung):
```python
groesse = int(input("Größe der Tabelle: "))

max_zahl = groesse * groesse
spaltenbreite = len(str(max_zahl)) + 1

# Kopfzeile
print(" " * (spaltenbreite + 1), end="| ")
for spalte in range(1, groesse + 1):
    print(f"{spalte:>{spaltenbreite}}", end=" ")
print()

# Trennlinie
print("-" * (spaltenbreite + 1) + "+" + "-" * (groesse * (spaltenbreite + 1)))

# Tabellenzeilen
for zeile in range(1, groesse + 1):
    print(f"{zeile:>{spaltenbreite}} |", end=" ")
    
    for spalte in range(1, groesse + 1):
        produkt = zeile * spalte
        
        # Hervorhebung von Quadratzahlen (Diagonale)
        if zeile == spalte:
            # Quadratzahl mit Sternen markieren
            print(f"{produkt:>{spaltenbreite}}*", end="")
        else:
            print(f"{produkt:>{spaltenbreite}} ", end="")
    
    print()

# Summenzeile (optional)
print("-" * (spaltenbreite + 1) + "+" + "-" * (groesse * (spaltenbreite + 1)))
print(f"{'Σ':>{spaltenbreite}} |", end=" ")
for spalte in range(1, groesse + 1):
    summe = sum(zeile * spalte for zeile in range(1, groesse + 1))
    print(f"{summe:>{spaltenbreite}}", end=" ")
print()
```

**Formatierungs-Details**:

- `f"{wert:>{breite}}"`: Rechtsbündig mit Breite
- `f"{wert:<{breite}}"`: Linksbündig mit Breite
- `f"{wert:^{breite}}"`: Zentriert mit Breite
- `f"{wert:0{breite}d}"`: Rechtsbündig mit führenden Nullen (nur für Integers)

**Beispiel Ausgabe** (groesse = 5):
```
     |    1    2    3    4    5
------+-----------------------------
   1 |    1*   2    3    4    5 
   2 |    2    4*   6    8   10 
   3 |    3    6    9*  12   15 
   4 |    4    8   12   16*  20 
   5 |    5   10   15   20   25*
------+-----------------------------
   Σ |   15   30   45   60   75 
```

**Häufige Fehler**:
- **Fehler**: Spaltenbreite fest codieren
  ```python
  # Schlecht:
  print(f"{produkt:4d}")  # Was wenn groesse > 31? (31*31 = 961, 4 Ziffern)
  ```
  - **Warum falsch**: Funktioniert nicht für alle Größen
  - **Richtig**: Spaltenbreite dynamisch berechnen

- **Fehler**: Zeilenumbruch vergessen
  ```python
  # Problematisch:
  for zeile in range(1, groesse + 1):
      for spalte in range(1, groesse + 1):
          print(produkt, end=" ")
  # Vergessen: print() nach innerer Schleife
  ```
  - **Resultat**: Alle Zahlen in einer langen Zeile
  - **Richtig**: `print()` nach innerer Schleife für Zeilenumbruch

- **Fehler**: `range()` Grenzen falsch
  ```python
  # Falsch:
  for zeile in range(0, groesse):  # 0 bis groesse-1
  ```
  - **Resultat**: Tabelle beginnt bei 0 statt 1
  - **Richtig**: `range(1, groesse + 1)`

---

### Lösung P4: Passwort-Generator mit List Comprehension

**Vollständiger Code**:
```python
import random
import string

def generiere_passwort(laenge, verwende_gross, verwende_klein, verwende_ziffern, verwende_sonder):
    """
    Generiert ein sicheres Passwort nach den gegebenen Kriterien.
    
    Args:
        laenge: Gewünschte Passwortlänge (min. 8)
        verwende_gross: Boolean - Großbuchstaben verwenden
        verwende_klein: Boolean - Kleinbuchstaben verwenden
        verwende_ziffern: Boolean - Ziffern verwenden
        verwende_sonder: Boolean - Sonderzeichen verwenden
    
    Returns:
        Generiertes Passwort als String
    """
    # Zeichensets definieren
    gross = string.ascii_uppercase
    klein = string.ascii_lowercase
    ziffern = string.digits
    sonder = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Liste der verwendeten Zeichensets
    verfuegbare_sets = []
    passwort_zeichen = []
    
    # Sammle verwendete Sets und füge mindestens ein Zeichen aus jedem hinzu
    if verwende_gross:
        verfuegbare_sets.append(gross)
        passwort_zeichen.append(random.choice(gross))
    
    if verwende_klein:
        verfuegbare_sets.append(klein)
        passwort_zeichen.append(random.choice(klein))
    
    if verwende_ziffern:
        verfuegbare_sets.append(ziffern)
        passwort_zeichen.append(random.choice(ziffern))
    
    if verwende_sonder:
        verfuegbare_sets.append(sonder)
        passwort_zeichen.append(random.choice(sonder))
    
    # Alle Zeichen kombinieren
    alle_zeichen = ''.join(verfuegbare_sets)
    
    # Fülle restliche Zeichen zufällig auf
    restliche_laenge = laenge - len(passwort_zeichen)
    passwort_zeichen.extend([random.choice(alle_zeichen) for _ in range(restliche_laenge)])
    
    # Mische die Zeichen (damit die ersten Zeichen nicht vorhersehbar sind)
    random.shuffle(passwort_zeichen)
    
    # Konvertiere Liste zu String
    return ''.join(passwort_zeichen)


def ja_nein_eingabe(prompt):
    """Hilfsfunktion für J/N-Eingaben."""
    while True:
        antwort = input(prompt).strip().upper()
        if antwort in ['J', 'JA', 'Y', 'YES']:
            return True
        elif antwort in ['N', 'NEIN', 'NO']:
            return False
        else:
            print("Bitte 'J' für Ja oder 'N' für Nein eingeben.")


# Hauptprogramm
print("Willkommen beim Passwort-Generator!\n")

# Passwortlänge erfragen
while True:
    try:
        laenge = int(input("Passwortlänge (min. 8): "))
        if laenge >= 8:
            break
        else:
            print("Die Länge muss mindestens 8 Zeichen betragen.")
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")

# Zeichentypen erfragen
print("\nWelche Zeichentypen sollen enthalten sein?")
verwende_gross = ja_nein_eingabe("Großbuchstaben (J/N): ")
verwende_klein = ja_nein_eingabe("Kleinbuchstaben (J/N): ")
verwende_ziffern = ja_nein_eingabe("Ziffern (J/N): ")
verwende_sonder = ja_nein_eingabe("Sonderzeichen (J/N): ")

# Validierung: Mindestens ein Typ muss ausgewählt sein
if not any([verwende_gross, verwende_klein, verwende_ziffern, verwende_sonder]):
    print("\nFehler: Mindestens ein Zeichentyp muss ausgewählt werden!")
    exit()

# Generiere mehrere Passwörter
anzahl_passwoerter = 5
print(f"\nGenerierte Passwörter:")
for i in range(1, anzahl_passwoerter + 1):
    passwort = generiere_passwort(laenge, verwende_gross, verwende_klein, verwende_ziffern, verwende_sonder)
    print(f"{i}. {passwort}")

# Weitere Passwörter generieren?
while ja_nein_eingabe("\nWeiteres Passwort generieren? (J/N): "):
    passwort = generiere_passwort(laenge, verwende_gross, verwende_klein, verwende_ziffern, verwende_sonder)
    print(f"   {passwort}")
```

**Erklärung**:

Das Programm ist modular aufgebaut und demonstriert gute Software-Engineering-Praktiken:

1. **Funktion `generiere_passwort`**: Kapselt die Passwort-Generierung mit klaren Parametern
2. **Funktion `ja_nein_eingabe`**: Wiederverwendbare Hilfsfunktion für J/N-Fragen (DRY)
3. **Hauptprogramm**: Koordiniert Eingabe und Ausgabe

**Schritt-für-Schritt Erklärung der Passwort-Generierung**:

1. **Zeichensets definieren**: Nutze `string`-Modul für vordefinierte Zeichensets
2. **Sets sammeln**: Nur ausgewählte Sets werden verwendet
3. **Garantierte Zeichen**: Wähle mindestens ein Zeichen aus jedem verwendeten Set
4. **Auffüllen**: Fülle restliche Positionen mit zufälligen Zeichen aus allen Sets
5. **Mischen**: `random.shuffle()` mischt die Liste, sodass die garantierten Zeichen nicht am Anfang stehen
6. **String erzeugen**: `''.join()` konvertiert Liste zu String

**Kompaktere Version mit List Comprehensions**:
```python
# Alternative: Kompaktere Implementierung mit mehr List Comprehensions
def generiere_passwort_kompakt(laenge, sets):
    """
    Args:
        laenge: Passwortlänge
        sets: Liste von Zeichensets (z.B. [string.ascii_uppercase, string.digits])
    """
    # Garantiere mindestens ein Zeichen aus jedem Set
    passwort = [random.choice(s) for s in sets]
    
    # Fülle auf mit zufälligen Zeichen aus allen Sets
    alle_zeichen = ''.join(sets)
    passwort += [random.choice(alle_zeichen) for _ in range(laenge - len(passwort))]
    
    # Mische und konvertiere zu String
    random.shuffle(passwort)
    return ''.join(passwort)

# Verwendung:
# sets = []
# if verwende_gross: sets.append(string.ascii_uppercase)
# ...
# passwort = generiere_passwort_kompakt(laenge, sets)
```

**Design-Entscheidungen**:

- **Separate Funktion für Generierung**: Ermöglicht einfaches Testen und Wiederverwenden
- **Boolean-Parameter statt Flags**: Klarer als ein einzelner "mode"-Parameter
- **Garantierte Zeichen**: Stellt sicher, dass jeder ausgewählte Typ vorkommt
- **Mischen**: Verhindert Muster (z.B. Großbuchstabe immer am Anfang)

**Konzepte in dieser Lösung**:
- **List Comprehensions**: `[random.choice(alle_zeichen) for _ in range(n)]`
- **`any()`-Funktion**: Prüft, ob mindestens ein Boolean `True` ist
- **String-Modul**: `string.ascii_uppercase`, `string.digits` etc.
- **`random.shuffle()`**: Mischt Liste in-place
- **`''.join(liste)`**: Effiziente String-Erstellung aus Liste

**Häufige Fehler**:
- **Fehler**: Keine garantierten Zeichen aus jedem Set
  ```python
  # Problematisch:
  passwort = [random.choice(alle_zeichen) for _ in range(laenge)]
  # Könnte zufällig keine Ziffern enthalten, obwohl gewünscht
  ```
  - **Richtig**: Mindestens ein Zeichen aus jedem Set explizit hinzufügen

- **Fehler**: Nicht mischen
  ```python
  # Schlecht:
  passwort = [gross_zeichen] + [klein_zeichen] + [ziffer] + [rest...]
  # Vorhersehbares Muster: Großbuchstabe, Kleinbuchstabe, Ziffer, ...
  ```
  - **Richtig**: `random.shuffle()` verwenden

---

### Lösung P5: Text-Analyse-Tool

**Vollständiger Code**:
```python
# Text-Analyse-Tool mit umfassenden Statistiken

def lese_mehrzeiligen_text():
    """Liest mehrzeiligen Text bis 'END'."""
    zeilen = []
    print("Text eingeben (beende mit 'END' auf einer neuen Zeile):")
    
    while True:
        zeile = input("> ")
        if zeile.strip().upper() == "END":
            break
        zeilen.append(zeile)
    
    return '\n'.join(zeilen)


def zaehle_zeichen_typen(text):
    """Zählt verschiedene Zeichentypen."""
    gross = sum(1 for c in text if c.isupper())
    klein = sum(1 for c in text if c.islower())
    ziffern = sum(1 for c in text if c.isdigit())
    leerzeichen = sum(1 for c in text if c.isspace())
    sonderzeichen = len(text) - gross - klein - ziffern - leerzeichen
    
    return gross, klein, ziffern, leerzeichen, sonderzeichen


def analysiere_woerter(text):
    """Analysiert Wörter im Text."""
    # Text in Sätze splitten (grob)
    import re
    saetze = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    
    # Wörter extrahieren (Satzzeichen entfernen)
    woerter = []
    for wort in text.split():
        # Entferne Satzzeichen am Anfang und Ende
        gereinigtes_wort = wort.strip('.,!?;:"\'()[]{}')
        if gereinigtes_wort:
            woerter.append(gereinigtes_wort)
    
    return woerter, saetze


def finde_haeufigste_woerter(woerter, anzahl=5):
    """Findet die häufigsten Wörter (case-insensitive)."""
    # Wörter zählen mit Dictionary
    haeufigkeit = {}
    for wort in woerter:
        wort_lower = wort.lower()
        haeufigkeit[wort_lower] = haeufigkeit.get(wort_lower, 0) + 1
    
    # Sortiere nach Häufigkeit (absteigend)
    sortiert = sorted(haeufigkeit.items(), key=lambda x: x[1], reverse=True)
    
    return sortiert[:anzahl]


def finde_potenzielle_eigennamen(woerter):
    """Findet Wörter, die mit Großbuchstaben beginnen."""
    return [wort for wort in woerter if wort and wort[0].isupper()]


def finde_zahlen(text):
    """Findet alle Zahlen im Text."""
    import re
    # Findet Zahlen (auch mit Komma/Punkt)
    zahlen = re.findall(r'\b\d+(?:[.,]\d+)?\b', text)
    return zahlen


def finde_lange_woerter(woerter, min_laenge=10):
    """Findet Wörter mit mindestens min_laenge Buchstaben."""
    return [wort for wort in woerter if len(wort) >= min_laenge]


def hauptanalyse():
    """Hauptfunktion zur Textanalyse."""
    print("=== TEXT-ANALYSE ===\n")
    
    # Text einlesen
    text = lese_mehrzeiligen_text()
    
    if not text.strip():
        print("Kein Text eingegeben!")
        return
    
    # Wörter und Sätze extrahieren
    woerter, saetze = analysiere_woerter(text)
    
    # --- GRUNDSTATISTIKEN ---
    print("\n--- GRUNDSTATISTIKEN ---")
    zeichen_gesamt = len(text)
    zeichen_ohne_leer = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
    anzahl_woerter = len(woerter)
    anzahl_saetze = len(saetze)
    
    print(f"Zeichen (gesamt):        {zeichen_gesamt}")
    print(f"Zeichen (ohne Leerz.):   {zeichen_ohne_leer}")
    print(f"Wörter:                  {anzahl_woerter}")
    print(f"Sätze:                   {anzahl_saetze}")
    
    if anzahl_woerter > 0:
        durchschnitt_wortlaenge = sum(len(w) for w in woerter) / anzahl_woerter
        print(f"Ø Wortlänge:             {durchschnitt_wortlaenge:.1f}")
    
    if anzahl_saetze > 0:
        durchschnitt_satzlaenge = anzahl_woerter / anzahl_saetze
        print(f"Ø Satzlänge:             {durchschnitt_satzlaenge:.1f}")
    
    # --- ZEICHENANALYSE ---
    print("\n--- ZEICHENANALYSE ---")
    gross, klein, ziffern, leerzeichen, sonderzeichen = zaehle_zeichen_typen(text)
    
    print(f"Großbuchstaben:         {gross:3d} ({gross/zeichen_gesamt*100:4.1f}%)")
    print(f"Kleinbuchstaben:        {klein:3d} ({klein/zeichen_gesamt*100:4.1f}%)")
    print(f"Ziffern:                {ziffern:3d} ({ziffern/zeichen_gesamt*100:4.1f}%)")
    print(f"Sonderzeichen:          {sonderzeichen:3d} ({sonderzeichen/zeichen_gesamt*100:4.1f}%)")
    print(f"Leerzeichen:            {leerzeichen:3d} ({leerzeichen/zeichen_gesamt*100:4.1f}%)")
    
    # --- WORTANALYSE ---
    print("\n--- WORTANALYSE ---")
    
    if woerter:
        laengstes_wort = max(woerter, key=len)
        kuerzeste_woerter = [w for w in woerter if len(w) > 1]  # Ignoriere 1-Zeichen-Wörter
        
        if kuerzeste_woerter:
            kuerzestes_wort = min(kuerzeste_woerter, key=len)
            print(f"Längstes Wort:           \"{laengstes_wort}\" ({len(laengstes_wort)} Buchstaben)")
            print(f"Kürzestes Wort:          \"{kuerzestes_wort}\" ({len(kuerzestes_wort)} Buchstaben)")
        
        # Häufigste Wörter
        print("\nTop 5 häufigste Wörter:")
        haeufigste = finde_haeufigste_woerter(woerter, 5)
        for i, (wort, anzahl) in enumerate(haeufigste, 1):
            print(f"  {i}. {wort} ({anzahl}×)")
    
    # --- ERWEITERTE ANALYSE ---
    print("\n--- ERWEITERTE ANALYSE ---")
    
    eigennamen = finde_potenzielle_eigennamen(woerter)
    if eigennamen:
        # Entferne Duplikate und zeige erste 10
        eindeutige_eigennamen = list(dict.fromkeys(eigennamen))[:10]
        print(f"Potenzielle Eigennamen: {', '.join(eindeutige_eigennamen)}")
    else:
        print("Potenzielle Eigennamen: Keine gefunden")
    
    zahlen = finde_zahlen(text)
    if zahlen:
        print(f"Zahlen im Text: {', '.join(zahlen)}")
    else:
        print("Zahlen im Text: Keine gefunden")
    
    lange_woerter = finde_lange_woerter(woerter, 10)
    if lange_woerter:
        eindeutige_lange = list(dict.fromkeys(lange_woerter))
        print(f"Lange Wörter (>10): {', '.join(eindeutige_lange)}")
    else:
        print("Lange Wörter (>10): Keine gefunden")


# Programm ausführen
if __name__ == "__main__":
    hauptanalyse()
```

**Erklärung**:

Dieses Programm demonstriert fortgeschrittene Python-Konzepte und Software-Engineering-Prinzipien:

**Architektur-Überblick**:
1. **Modularität**: Jede Analyse-Aufgabe ist eine separate Funktion (SRP)
2. **Wiederverwendbarkeit**: Funktionen können einzeln getestet und in anderen Kontexten verwendet werden
3. **Lesbarkeit**: Klare Funktionsnamen dokumentieren, was passiert

**Schritt-für-Schritt Erklärung**:

1. **Text einlesen** (`lese_mehrzeiligen_text`):
   - Liste zum Sammeln der Zeilen
   - Schleife bis "END" eingegeben wird
   - `'\n'.join(zeilen)` kombiniert Zeilen zu einem Text

2. **Zeichentypen zählen** (`zaehle_zeichen_typen`):
   - Nutzt List Comprehensions mit `sum()` für effiziente Zählung
   - `sum(1 for c in text if c.isupper())` zählt, wie oft die Bedingung wahr ist

3. **Wörter analysieren** (`analysiere_woerter`):
   - Sätze splitten mit regulären Ausdrücken: `re.split(r'[.!?]+', text)`
   - Wörter reinigen: Satzzeichen entfernen mit `.strip('.,!?...')`

4. **Häufigste Wörter** (`finde_haeufigste_woerter`):
   - Dictionary zum Zählen: `haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1`
   - Sortieren mit `sorted()` und Lambda-Funktion: `key=lambda x: x[1]`
   - Top N auswählen mit Slicing: `[:anzahl]`

5. **Eigennamen finden** (`finde_potenzielle_eigennamen`):
   - List Comprehension mit Bedingung: `[wort for wort in woerter if wort[0].isupper()]`

6. **Zahlen finden** (`finde_zahlen`):
   - Reguläre Ausdrücke: `re.findall(r'\b\d+(?:[.,]\d+)?\b', text)`
   - Pattern erklärt: `\b` = Wortgrenze, `\d+` = eine oder mehr Ziffern, `(?:[.,]\d+)?` = optional Komma/Punkt und weitere Ziffern

7. **Lange Wörter** (`finde_lange_woerter`):
   - Einfache List Comprehension mit Längenprüfung

**Konzepte in dieser Lösung**:
- **List Comprehensions**: Kompakte Filterungen und Transformationen
- **Generator Expressions mit `sum()`**: Speicher-effizientes Zählen
- **Reguläre Ausdrücke**: Mustersuche und Text-Splitting
- **Dictionary für Häufigkeiten**: Klassisches Zähl-Pattern
- **Lambda-Funktionen**: Für Sortier-Keys
- **`enumerate()`**: Für nummerierte Ausgaben
- **`dict.fromkeys()`-Trick**: Entfernt Duplikate unter Beibehaltung der Reihenfolge

**Alternative Lösungsansätze**:

**Mit Collections.Counter** (einfacher für Häufigkeiten):
```python
from collections import Counter

def finde_haeufigste_woerter_v2(woerter, anzahl=5):
    """Vereinfachte Version mit Counter."""
    woerter_lower = [w.lower() for w in woerter]
    zaehler = Counter(woerter_lower)
    return zaehler.most_common(anzahl)
```

**Komplexitätsanalyse**:
- **Zeichentyp-Zählung**: O(n), wo n = Textlänge
- **Worthäufigkeit**: O(m), wo m = Anzahl Wörter
- **Sortierung**: O(m log m)
- **Gesamtkomplexität**: O(n + m log m)

**Häufige Fehler**:
- **Fehler**: Satzzeichen nicht berücksichtigen
  ```python
  # Problematisch:
  woerter = text.split()
  # "Hallo," und "Hallo" werden als unterschiedlich gezählt
  ```
  - **Richtig**: Satzzeichen mit `.strip()` entfernen

- **Fehler**: Case-Sensitivity bei Häufigkeit
  ```python
  # Problematisch:
  haeufigkeit[wort] += 1  # "Python" und "python" getrennt gezählt
  ```
  - **Richtig**: Konvertiere zu lowercase: `wort.lower()`

- **Fehler**: Division durch Null
  ```python
  # Gefährlich:
  durchschnitt = sum(laengen) / anzahl_woerter  # Was wenn anzahl_woerter == 0?
  ```
  - **Richtig**: Prüfe vor Division: `if anzahl_woerter > 0:`

**Bonus-Challenge Lösungen** (Auszug):

**Flesch Reading Ease Score**:
```python
def berechne_flesch_score(text, woerter, saetze):
    """
    Berechnet Flesch Reading Ease Score (vereinfacht für Deutsch).
    """
    anzahl_woerter = len(woerter)
    anzahl_saetze = len(saetze)
    
    if anzahl_woerter == 0 or anzahl_saetze == 0:
        return None
    
    # Zähle Silben (vereinfachte Methode: Vokal-Gruppen)
    import re
    silben = sum(len(re.findall(r'[aeiouäöüAEIOUÄÖÜ]+', w)) for w in woerter)
    
    # Flesch-Formel (angepasst für Deutsch)
    score = 180 - (anzahl_woerter / anzahl_saetze) - (58.5 * silben / anzahl_woerter)
    
    return score

# Interpretation:
# > 80: Sehr leicht
# 60-80: Leicht
# 40-60: Mittel
# < 40: Schwierig
```

**Wortlängen-Histogramm**:
```python
def erstelle_histogramm(woerter):
    """Erstellt ASCII-Histogramm der Wortlängen."""
    # Zähle Wortlängen
    laengen = [len(w) for w in woerter]
    laengen_verteilung = {}
    
    for laenge in laengen:
        laengen_verteilung[laenge] = laengen_verteilung.get(laenge, 0) + 1
    
    # Sortiere und ausgebe
    print("\nWortlängen-Verteilung:")
    max_anzahl = max(laengen_verteilung.values())
    
    for laenge in sorted(laengen_verteilung.keys()):
        anzahl = laengen_verteilung[laenge]
        balken_laenge = int((anzahl / max_anzahl) * 40)
        balken = '█' * balken_laenge
        print(f"{laenge:2d}: {balken} ({anzahl})")
```

Diese Lösung demonstriert professionelle Code-Organisation, Verwendung fortgeschrittener Python-Features und praktische Anwendung der Software-Engineering-Prinzipien aus dem Theorie-Teil der Vorlesung.
