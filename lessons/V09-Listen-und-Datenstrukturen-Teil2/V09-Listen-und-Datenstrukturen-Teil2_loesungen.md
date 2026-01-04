# V09: Lösungen - Listen und Datenstrukturen – Teil 2

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: Binärbaum-Analyse

**Lösung**:

a) **Wurzel**: 50

b) **Blätter**: 10, 40, 60, 80  
(Knoten ohne Kinder)

c) **Höhe**: 3  
(Längster Pfad von Wurzel zu einem Blatt: 50 → 30 → 20 → 10 hat 3 Kanten)

d) **Tiefe von Knoten 40**: 2  
(Pfad von Wurzel: 50 → 30 → 40, das sind 2 Kanten)

e) **Ist dies ein BST?** Ja, dies ist ein Binärer Suchbaum.

**Erklärung**:

Ein Binärer Suchbaum erfüllt die Ordnungseigenschaft: Für jeden Knoten sind alle Werte im linken Teilbaum kleiner und alle im rechten Teilbaum größer.

Prüfung für jeden Knoten:
- **Knoten 50**: Links {10, 20, 30, 40} < 50 < {60, 70, 80} Rechts ✓
- **Knoten 30**: Links {10, 20} < 30 < {40} Rechts ✓
- **Knoten 70**: Links {60} < 70 < {80} Rechts ✓
- **Knoten 20**: Links {10} < 20, kein rechtes Kind ✓

Alle Knoten erfüllen die BST-Eigenschaft, daher ist dies ein gültiger Binärer Suchbaum.

**Häufige Fehler**:
- **Höhe falsch gezählt**: Häufig wird die Anzahl der Knoten statt der Kanten gezählt
  - Richtig: Anzahl der Kanten im längsten Pfad = 3
  - Falsch: Anzahl der Knoten im längsten Pfad = 4
- **Tiefe vs. Höhe verwechselt**: Tiefe wird von der Wurzel aus gezählt, Höhe ist die maximale Tiefe
- **BST-Eigenschaft nur lokal geprüft**: Man muss auch prüfen, dass alle Knoten im linken Teilbaum kleiner sind, nicht nur das direkte linke Kind

---

### Lösung T2: Traversierung verstehen

**Lösung**:

a) **Inorder-Traversierung**: 5, 10, 12, 15, 20, 25

b) **Preorder-Traversierung**: 15, 10, 5, 12, 20, 25

c) **Postorder-Traversierung**: 5, 12, 10, 25, 20, 15

d) **Level-Order-Traversierung**: 15, 10, 20, 5, 12, 25

e) **Sortierte Reihenfolge**: Die **Inorder-Traversierung** liefert die Werte in aufsteigend sortierter Reihenfolge.

**Erklärung**:

**Inorder-Traversierung** (Links → Wurzel → Rechts):
- Starte bei 15 (Wurzel)
- Gehe nach links zu 10
- Gehe weiter links zu 5 (Blatt) → **Besuche 5**
- Zurück zu 10 → **Besuche 10**
- Gehe rechts zu 12 (Blatt) → **Besuche 12**
- Zurück zu 15 → **Besuche 15**
- Gehe rechts zu 20
- Kein linkes Kind → **Besuche 20**
- Gehe rechts zu 25 (Blatt) → **Besuche 25**

**Reihenfolge**: 5, 10, 12, 15, 20, 25 (aufsteigend sortiert!)

**Preorder-Traversierung** (Wurzel → Links → Rechts):
- **Besuche 15** (Wurzel)
- Gehe links zu 10 → **Besuche 10**
- Gehe links zu 5 → **Besuche 5**
- Zurück zu 10, gehe rechts zu 12 → **Besuche 12**
- Zurück zu 15, gehe rechts zu 20 → **Besuche 20**
- Gehe rechts zu 25 → **Besuche 25**

**Reihenfolge**: 15, 10, 5, 12, 20, 25

**Postorder-Traversierung** (Links → Rechts → Wurzel):
- Starte bei 15, gehe ganz links runter zu 5 → **Besuche 5**
- Zurück zu 10, gehe rechts zu 12 → **Besuche 12**
- Kein weiteres rechts → **Besuche 10**
- Zurück zu 15, gehe rechts zu 20
- Gehe rechts zu 25 (Blatt) → **Besuche 25**
- Zurück zu 20 → **Besuche 20**
- Zurück zu 15 → **Besuche 15**

**Reihenfolge**: 5, 12, 10, 25, 20, 15

**Level-Order-Traversierung** (Ebenenweise):
- Ebene 0: 15
- Ebene 1: 10, 20
- Ebene 2: 5, 12, 25

**Reihenfolge**: 15, 10, 20, 5, 12, 25

**Warum liefert Inorder sortierte Werte?**

Bei einem Binären Suchbaum gilt: Alle Werte links sind kleiner, alle rechts größer. Inorder besucht zuerst alle kleineren Werte (linker Teilbaum), dann die Wurzel, dann alle größeren Werte (rechter Teilbaum). Dies erzeugt automatisch eine aufsteigende Sortierung.

**Lösungsweg Schritt für Schritt**:
1. Zeichne den Baum auf Papier
2. Markiere jeden Knoten mit seiner Besuchsreihenfolge für jede Traversierungsart
3. Folge dem Algorithmus strikt (z.B. Inorder: immer erst ganz links runter)
4. Überprüfe am Ende: Inorder muss sortiert sein bei BST

**Häufige Fehler**:
- **Reihenfolge verwechselt**: "Links-Wurzel-Rechts" vs. "Wurzel-Links-Rechts" genau beachten
- **Rekursion nicht vollständig durchgeführt**: Bei verschachtelten Teilbäumen den Algorithmus rekursiv anwenden
- **Level-Order ohne Queue**: Level-Order erfordert eine Queue-Struktur, nicht rekursive Tiefensuche

---

### Lösung T3: Hash-Tabellen-Design

**Lösung**:

**Schlüssel**: 10, 22, 31, 4, 15, 28, 17  
**Hash-Funktion**: `h(key) = key % 7`  
**Tabellengröße**: m = 7

**Hash-Werte berechnen**:
- h(10) = 10 % 7 = **3**
- h(22) = 22 % 7 = **1**
- h(31) = 31 % 7 = **3** ← Kollision mit 10
- h(4) = 4 % 7 = **4**
- h(15) = 15 % 7 = **1** ← Kollision mit 22
- h(28) = 28 % 7 = **0**
- h(17) = 17 % 7 = **3** ← Kollision mit 10 und 31

**a) Chaining**:

```
Index | Verkettete Liste
------|------------------
  0   | 28
  1   | 15 → 22
  2   | (leer)
  3   | 17 → 31 → 10
  4   | 4
  5   | (leer)
  6   | (leer)
```

**Kollidierende Schlüssel**:
- Index 1: 22 und 15
- Index 3: 10, 31 und 17

**Erklärung**: Bei Chaining wird jede Kollision durch Anhängen an eine verkettete Liste gelöst. Index 3 enthält drei Elemente, da alle den Hash-Wert 3 haben.

**b) Linear Probing**:

**Einfüge-Prozess mit Sondierungssequenzen**:

1. **10**: h(10) = 3 → Platz 3 frei → einfügen bei Index 3
2. **22**: h(22) = 1 → Platz 1 frei → einfügen bei Index 1
3. **31**: h(31) = 3 → Platz 3 **belegt** → sondiere (3+1) % 7 = 4 → Platz 4 frei → einfügen bei Index 4
4. **4**: h(4) = 4 → Platz 4 **belegt** → sondiere (4+1) % 7 = 5 → Platz 5 frei → einfügen bei Index 5
5. **15**: h(15) = 1 → Platz 1 **belegt** → sondiere (1+1) % 7 = 2 → Platz 2 frei → einfügen bei Index 2
6. **28**: h(28) = 0 → Platz 0 frei → einfügen bei Index 0
7. **17**: h(17) = 3 → Platz 3 **belegt** → sondiere (3+1) % 7 = 4 → **belegt** → (3+2) % 7 = 5 → **belegt** → (3+3) % 7 = 6 → Platz 6 frei → einfügen bei Index 6

**Finale Tabelle**:

```
Index | Schlüssel
------|----------
  0   | 28
  1   | 22
  2   | 15
  3   | 10
  4   | 31
  5   | 4
  6   | 17
```

**Kollidierende Schlüssel und deren Sondierungssequenzen**:
- **31**: h=3, kollidiert → Sequenz: 3, **4** (eingefügt)
- **4**: h=4, kollidiert → Sequenz: 4, **5** (eingefügt)
- **15**: h=1, kollidiert → Sequenz: 1, **2** (eingefügt)
- **17**: h=3, kollidiert → Sequenz: 3, 4, 5, **6** (eingefügt)

**c) Vergleich der Performance**:

**Chaining**:
- Durchschnittliche Listenlänge: (1+2+0+3+1+0+0) / 7 ≈ 1.0
- Suchzeit für Elemente:
  - Index 0, 4: 1 Vergleich
  - Index 1: 1-2 Vergleiche (durchschnittlich 1.5)
  - Index 3: 1-3 Vergleiche (durchschnittlich 2)
- **Durchschnittliche Suchzeit**: ≈ 1.4 Vergleiche

**Linear Probing**:
- Tabelle vollständig gefüllt (7/7)
- Suchzeit hängt von der Position ab:
  - 28, 22, 10: 1 Vergleich (direkt am Hash-Wert)
  - 15: 2 Vergleiche (1→2)
  - 31: 2 Vergleiche (3→4)
  - 4: 3 Vergleiche (4→5)
  - 17: 4 Vergleiche (3→4→5→6)
- **Durchschnittliche Suchzeit**: (1+1+1+2+2+3+4) / 7 = 14/7 = **2.0 Vergleiche**

**Ergebnis**: Für diese spezielle Schlüsselmenge hat **Chaining** bessere Performance (1.4 vs. 2.0 Vergleiche). Linear Probing leidet unter Primary Clustering (zusammenhängende Bereiche belegter Zellen von Index 3-6), was die Suchzeit erhöht.

**d) Ladefaktor**:

**Berechnung**: α = n / m = 7 / 7 = **1.0** (100% Auslastung)

**Bewertung**:
- **Chaining**: Ein Ladefaktor von 1.0 ist **akzeptabel**, da Chaining theoretisch unbegrenzt wachsen kann. In der Praxis wird oft bei α ≈ 0.75-1.0 ein Rehashing durchgeführt, um die Performance zu optimieren.
- **Open Addressing** (Linear Probing): Ein Ladefaktor von 1.0 ist **kritisch**. Bei Open Addressing sollte die Tabelle spätestens bei α ≈ **0.7** vergrößert werden, da die Performance bei hoher Auslastung dramatisch abnimmt (exponentieller Anstieg der Sondierungssequenz-Länge).

**Empfohlene Schwellenwerte für Rehashing**:
- **Chaining**: α ≈ 1.0 (oder sogar höher)
- **Linear Probing**: α ≈ 0.7
- **Quadratic Probing / Double Hashing**: α ≈ 0.5-0.7

**Lösungsweg Schritt für Schritt**:
1. Hash-Werte für alle Schlüssel berechnen
2. Kollisionen identifizieren (gleiche Hash-Werte)
3. Für Chaining: Kollidierende Elemente in Listen eintragen
4. Für Linear Probing: Sondierungssequenz durchführen bis freier Platz gefunden
5. Performance analysieren: Durchschnittliche Anzahl der Vergleiche berechnen
6. Ladefaktor berechnen und mit Schwellenwerten vergleichen

**Alternative Lösungsansätze**:
- **Quadratic Probing**: Würde Secondary Clustering reduzieren, aber nicht alle Plätze garantiert erreichen
- **Double Hashing**: Würde Clustering minimieren, z.B. mit `h₂(key) = 1 + (key % 5)` für bessere Verteilung
- **Größere Tabelle**: Mit m = 13 (Primzahl) würden Kollisionen seltener auftreten

**Häufige Fehler**:
- **Falsche Modulo-Berechnung**: 31 % 7 = 3, nicht 4 (31 / 7 = 4 Rest **3**)
- **Sondierungssequenz falsch**: Bei Linear Probing muss `(h + i) % m` berechnet werden, nicht `h + i`
- **Chaining-Reihenfolge**: Die Aufgabe spezifiziert nicht, ob vorne oder hinten eingefügt wird – beide sind korrekt, solange konsistent
- **Ladefaktor-Interpretation**: α = 1.0 ist bei Chaining weniger kritisch als bei Open Addressing

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: Sichere Messwert-Eingabe für Sensorkalibrierung

**Vollständiger Code**:
```python
def eingabe_messwert(prompt, min_wert, max_wert, einheit):
    while True:
        try:
            wert = float(input(prompt))
            
            if wert < min_wert or wert > max_wert:
                print(f"⚠️  Fehler: Wert muss zwischen {min_wert} und {max_wert} {einheit} liegen.")
                continue
            
            print(f"✅ Wert akzeptiert: {wert} {einheit}")
            return wert
            
        except ValueError:
            print("⚠️  Fehler: Bitte gib eine gültige Zahl ein.")

# Test
temp = eingabe_messwert("Referenztemperatur: ", -50, 1200, "°C")
print(f"Kalibriert auf: {temp}°C")
```

**Erklärung**:

`try-except` fängt `ValueError` bei ungültiger Eingabe ab. `continue` wiederholt bei Fehler. `float()` erlaubt Dezimalzahlen für präzise Sensorwerte.

---

### Lösung P2: Maschinen-Logfile-Analyse mit Fehlerbehandlung

**Vollständiger Code**:
```python
def analyse_maschinenlog(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as f:
            zeilen = f.readlines()
            
        alarme = sum(1 for z in zeilen if "ALARM" in z)
        errors = sum(1 for z in zeilen if "ERROR" in z)
        
        print("✅ Logfile erfolgreich analysiert.")
        return {"zeilen": len(zeilen), "alarme": alarme, "errors": errors}
        
    except FileNotFoundError:
        print(f"❌ Fehler: Datei '{dateiname}' wurde nicht gefunden.")
        return None
        
    except PermissionError:
        print(f"❌ Fehler: Keine Leseberechtigung für '{dateiname}'.")
        return None
        
    finally:
        print("Analyse abgeschlossen.")

# Test
stats = analyse_maschinenlog("maschine_01.log")
if stats:
    print(f"Alarme: {stats['alarme']}, Errors: {stats['errors']}")
```

**Erklärung**:

`with open()` schließt Datei automatisch. Generator-Expressions mit `sum()` zählen effizient. `finally` wird immer ausgeführt, auch bei Exceptions.

---

### Lösung P3: Verschachtelte Maschinen-Konfiguration

**Vollständiger Code**:
```python
def parameter_lesen(config, pfad):
    try:
        wert = config
        for schluessel in pfad:
            wert = wert[schluessel]
        return wert
        
    except KeyError as e:
        print(f"❌ Fehler: Schlüssel {e} nicht gefunden in Pfad {pfad}")
        return None
        
    except TypeError:
        print(f"❌ Fehler: Element in Pfad {pfad} ist kein Dictionary")
        return None

# Test
cnc_config = {
    "achsen": {
        "x_achse": {"max_geschwindigkeit": 15000},
        "y_achse": {"max_geschwindigkeit": 12000}
    },
    "spindel": {"max_drehzahl": 24000}
}

print(parameter_lesen(cnc_config, ["achsen", "x_achse", "max_geschwindigkeit"]))  # 15000
print(parameter_lesen(cnc_config, ["achsen", "z_achse", "max_geschwindigkeit"]))  # None
```

**Erklärung**:

Iteration durch Pfad mit Dictionary-Zugriff. `KeyError` für fehlende Schlüssel, `TypeError` für nicht-Dictionary-Elemente. Gibt `None` bei Fehler zurück.

---

### Lösung P4: Benutzerdefinierte Exception für Materialvalidierung

**Vollständiger Code**:
```python
class UngueltigerEModulError(Exception):
    pass

class UngueltigeDichteError(Exception):
    pass

class UngueltigeStreckgrenzeError(Exception):
    pass

class MaterialValidator:
    def validiere_e_modul(self, e_modul):
        if not (1 <= e_modul <= 1000):
            raise UngueltigerEModulError(
                f"E-Modul muss zwischen 1 und 1000 GPa liegen (erhalten: {e_modul} GPa)."
            )
    
    def validiere_dichte(self, dichte):
        if not (0.1 <= dichte <= 25):
            raise UngueltigeDichteError(
                f"Dichte muss zwischen 0.1 und 25 g/cm³ liegen (erhalten: {dichte} g/cm³)."
            )
    
    def validiere_streckgrenze(self, re):
        if not (1 <= re <= 3000):
            raise UngueltigeStreckgrenzeError(
                f"Streckgrenze muss zwischen 1 und 3000 MPa liegen (erhalten: {re} MPa)."
            )
    
    def validiere_material(self, e_modul, dichte, re, name):
        self.validiere_e_modul(e_modul)
        self.validiere_dichte(dichte)
        self.validiere_streckgrenze(re)
        return True

# Test
validator = MaterialValidator()

try:
    validator.validiere_material(210, 7.85, 235, "Baustahl S235")
    print("✅ Material 'Baustahl S235' erfolgreich validiert!")
except (UngueltigerEModulError, UngueltigeDichteError, UngueltigeStreckgrenzeError) as e:
    print(f"❌ Validierungsfehler: {e}")
```

**Erklärung**:

Benutzerdefinierte Exception-Klassen erben von `Exception`. `raise` wirft Exception mit Nachricht. Validator ruft Einzelprüfungen auf, erste Exception wird propagiert.

---

### Lösung P5: Robustes Maschinen-Konfigurationssystem

**Vollständiger Code**:
```python
import json

class KonfigurationsFehler(Exception):
    pass

class KonfigurationsDateiFehler(KonfigurationsFehler):
    pass

class KonfigurationsFormatFehler(KonfigurationsFehler):
    pass

class KonfigurationsValidierungsFehler(KonfigurationsFehler):
    pass

class FertigungszellenKonfiguration:
    def __init__(self, dateiname, erforderliche_felder=None, defaults=None):
        self.dateiname = dateiname
        self.erforderliche_felder = erforderliche_felder or []
        self.defaults = defaults or {}
        self.daten = {}
    
    def laden(self):
        try:
            with open(self.dateiname, 'r', encoding='utf-8') as f:
                self.daten = json.load(f)
                
        except FileNotFoundError:
            raise KonfigurationsDateiFehler(
                f"Konfigurationsdatei '{self.dateiname}' nicht gefunden."
            )
        except PermissionError:
            raise KonfigurationsDateiFehler(
                f"Keine Leseberechtigung für '{self.dateiname}'."
            )
        except json.JSONDecodeError:
            raise KonfigurationsFormatFehler(
                f"Ungültiges JSON-Format in '{self.dateiname}'."
            )
        
        # Defaults hinzufügen
        for key, value in self.defaults.items():
            if key not in self.daten:
                self.daten[key] = value
        
        # Validieren
        self.validieren()
    
    def validieren(self):
        for feld in self.erforderliche_felder:
            if feld not in self.daten:
                raise KonfigurationsValidierungsFehler(
                    f"Erforderliches Feld '{feld}' fehlt in Konfiguration."
                )
    
    def get(self, schluessel, default=None):
        return self.daten.get(schluessel, default)
    
    def speichern(self, dateiname):
        try:
            with open(dateiname, 'w', encoding='utf-8') as f:
                json.dump(self.daten, f, indent=2)
        except Exception as e:
            raise KonfigurationsFehler(f"Fehler beim Speichern: {e}")

# Test
try:
    config = FertigungszellenKonfiguration(
        "fertigungszelle_01.json",
        erforderliche_felder=["maschine", "qualitaet"],
        defaults={"debug_modus": False}
    )
    config.laden()
    print(f"✅ Maschine: {config.get('maschine')['typ']}")
    print(f"Debug-Modus: {config.get('debug_modus')}")
except KonfigurationsFehler as e:
    print(f"❌ Fehler: {e}")
```

**Erklärung**:

Exception-Hierarchie mit Basisklasse. `json.load()` für JSON-Parsing. Dictionary-Update für Defaults. Validierung prüft erforderliche Felder. `with open()` für sichere Datei-I/O.
            print("Fehler: Bitte gib eine gültige Zahl ein.")


# Beispielverwendung:
if __name__ == "__main__":
    alter = eingabe_ganzzahl("Dein Alter: ", 0, 120)
    print(f"Du bist {alter} Jahre alt.")
```

**Erklärung**:

Die Funktion verwendet eine **Endlosschleife** (`while True`), die nur durch ein erfolgreiches `return` verlassen wird. Der Ablauf ist:

1. **Eingabe einlesen**: `input(prompt)` zeigt den Prompt und wartet auf Benutzereingabe
2. **Konvertierung versuchen**: `int()` versucht, den String in eine Ganzzahl zu konvertieren
   - Bei Erfolg: Zahl wird in `zahl` gespeichert
   - Bei Fehler: `ValueError` wird geworfen und im `except`-Block abgefangen
3. **Bereichsprüfung**: `if zahl < min_wert or zahl > max_wert:` prüft den gültigen Bereich
   - Bei Verstoß: Fehlermeldung und `continue` (zurück zu Schritt 1)
   - Bei Erfolg: Weiter zu Schritt 4
4. **Rückgabe**: `return zahl` beendet die Schleife und gibt die gültige Zahl zurück

**Warum diese Lösung?**

- **Robustheit**: Alle Fehlerquellen werden abgefangen (ungültige Zeichen, außerhalb des Bereichs)
- **Benutzerfreundlichkeit**: Klare Fehlermeldungen zeigen, was falsch war
- **Wiederholung**: Benutzer kann Eingabe korrigieren, ohne das Programm neu zu starten

**Häufige Fehler**:
- **Fehler**: `return` vergessen nach erfolgreicher Validierung
  - **Warum falsch**: Ohne `return` läuft die Schleife ewig weiter
  - **Richtig**: `return zahl` beendet die Funktion und gibt den Wert zurück

- **Fehler**: Bereichsprüfung mit `and` statt `or`
  ```python
  if zahl < min_wert and zahl > max_wert:  # FALSCH!
  ```
  - **Warum falsch**: Diese Bedingung ist immer `False` (eine Zahl kann nicht gleichzeitig zu klein UND zu groß sein)
  - **Richtig**: `if zahl < min_wert or zahl > max_wert:`

- **Fehler**: Blanket `except:` ohne Exception-Typ
  ```python
  except:  # Zu breit!
      print("Fehler")
  ```
  - **Warum falsch**: Fängt auch `KeyboardInterrupt` (Strg+C) ab, Benutzer kann Programm nicht beenden
  - **Richtig**: `except ValueError:` fängt nur die erwartete Exception ab

---

### Lösung P2: Dateiverarbeitung mit Fehlerbehandlung

**Vollständiger Code**:
```python
def zeilenanzahl_zaehlen(dateiname):
    """
    Zählt die Anzahl der Zeilen in einer Textdatei.
    
    Args:
        dateiname: Pfad zur Textdatei
    
    Returns:
        int: Anzahl der Zeilen, oder None bei Fehler
    """
    datei = None  # Initialisiere Variable für finally-Block
    
    try:
        # Versuche, Datei zu öffnen
        datei = open(dateiname, 'r', encoding='utf-8')
        
    except FileNotFoundError:
        # Datei existiert nicht
        print(f"Fehler: Datei '{dateiname}' wurde nicht gefunden.")
        return None
        
    except PermissionError:
        # Keine Leseberechtigung
        print(f"Fehler: Keine Berechtigung zum Lesen von '{dateiname}'.")
        return None
        
    else:
        # Dieser Block wird nur ausgeführt, wenn keine Exception auftrat
        # Lese alle Zeilen und zähle sie
        zeilen = datei.readlines()
        anzahl = len(zeilen)
        print("Datei erfolgreich gelesen.")
        return anzahl
        
    finally:
        # Wird IMMER ausgeführt, auch bei Exception oder return
        # Stelle sicher, dass die Datei geschlossen wird
        if datei is not None:
            datei.close()
        print("Vorgang abgeschlossen.")


# Beispielverwendung:
if __name__ == "__main__":
    # Test mit existierender Datei (erstelle zuerst eine Test-Datei)
    with open("test.txt", "w") as f:
        f.write("Zeile 1\nZeile 2\nZeile 3\n")
    
    anzahl = zeilenanzahl_zaehlen("test.txt")
    print(f"Anzahl Zeilen: {anzahl}\n")
    
    # Test mit nicht existierender Datei
    anzahl = zeilenanzahl_zaehlen("nicht_vorhanden.txt")
    print(f"Anzahl Zeilen: {anzahl}")
```

**Erklärung**:

Die Funktion demonstriert die vollständige `try-except-else-finally`-Struktur:

1. **`try`-Block**: Öffnet die Datei
   - Bei Erfolg: Weiter zum `else`-Block
   - Bei Exception: Springe zum passenden `except`-Block

2. **`except`-Blöcke**: Fangen spezifische Fehler ab
   - `FileNotFoundError`: Datei existiert nicht
   - `PermissionError`: Keine Berechtigung
   - Beide geben `None` zurück und zeigen Fehlermeldung

3. **`else`-Block**: Wird nur ausgeführt, wenn `try` erfolgreich war
   - Liest alle Zeilen mit `.readlines()`
   - Zählt sie mit `len()`
   - Gibt Erfolgsmeldung aus
   - Gibt Anzahl zurück

4. **`finally`-Block**: Wird **immer** ausgeführt
   - Schließt die Datei, falls sie geöffnet wurde
   - Gibt Abschlussmeldung aus
   - Wird auch ausgeführt, wenn `return` im `else` steht!

**Schritt-für-Schritt Durchlauf**:

**Erfolgsfall** (Datei existiert):
1. `try`: `datei = open(...)` → Erfolg
2. `except`: Übersprungen (keine Exception)
3. `else`: Zeilen lesen, zählen, "Datei erfolgreich gelesen.", `return anzahl`
4. `finally`: Datei schließen, "Vorgang abgeschlossen."

**Fehlerfall** (Datei nicht gefunden):
1. `try`: `datei = open(...)` → `FileNotFoundError`
2. `except FileNotFoundError`: "Fehler: Datei ... wurde nicht gefunden.", `return None`
3. `else`: Übersprungen
4. `finally`: `datei` ist `None`, also nicht schließen, "Vorgang abgeschlossen."

**Warum diese Struktur?**

- **`else` statt im `try`**: Das Lesen der Zeilen könnte theoretisch auch eine Exception werfen. Durch Platzierung im `else` wird sichergestellt, dass nur Datei-Öffnen-Fehler in den `except`-Blöcken behandelt werden.
- **`finally` für Cleanup**: Garantiert, dass die Datei geschlossen wird, auch wenn mitten im Code ein `return` oder eine Exception auftritt.

**Häufige Fehler**:
- **Fehler**: Datei nicht im `finally` schließen
  ```python
  try:
      datei = open(dateiname)
      return len(datei.readlines())
  except FileNotFoundError:
      return None
  # Datei wird nie geschlossen!
  ```
  - **Warum falsch**: Bei `return` im `try` wird die Datei nie geschlossen
  - **Richtig**: Entweder `finally` verwenden oder `with`-Statement

- **Fehler**: `datei.close()` ohne Prüfung auf `None`
  ```python
  finally:
      datei.close()  # AttributeError wenn datei == None!
  ```
  - **Warum falsch**: Wenn `open()` fehlschlägt, ist `datei` nie zugewiesen oder `None`
  - **Richtig**: `if datei is not None: datei.close()`

- **Fehler**: Zu viel Code im `try`-Block
  ```python
  try:
      datei = open(dateiname)
      zeilen = datei.readlines()
      berechnung = komplexe_operation(zeilen)  # Könnte andere Exceptions werfen!
      return berechnung
  except FileNotFoundError:
      # Fängt nur FileNotFoundError, andere Exceptions nicht
  ```
  - **Warum problematisch**: Andere Exceptions aus `komplexe_operation()` werden nicht behandelt
  - **Besser**: Nur Datei-Operationen im `try`, Rest im `else`

**Alternative mit `with`-Statement** (moderne Best Practice):
```python
def zeilenanzahl_zaehlen_modern(dateiname):
    """Moderne Variante mit with-Statement."""
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            anzahl = len(datei.readlines())
        print("Datei erfolgreich gelesen.")
        return anzahl
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' wurde nicht gefunden.")
        return None
    except PermissionError:
        print(f"Fehler: Keine Berechtigung zum Lesen von '{dateiname}'.")
        return None
    finally:
        print("Vorgang abgeschlossen.")
```

**Vorteil**: `with` schließt die Datei automatisch, `finally` ist nur noch für die Abschlussmeldung nötig.

---

### Lösung P3: Dictionary-Zugriff mit Fehlerbehandlung

**Vollständiger Code**:
```python
def sicherer_dict_zugriff(daten, pfad):
    """
    Greift auf einen verschachtelten Dictionary-Wert über einen Pfad zu.
    
    Args:
        daten: Dictionary mit möglicherweise verschachtelten Dictionaries
        pfad: Liste von Schlüsseln, z.B. ["benutzer", "adresse", "plz"]
    
    Returns:
        Der Wert am Ende des Pfads, oder None bei Fehler
    """
    aktuell = daten  # Starte beim Wurzel-Dictionary
    
    # Iteriere durch jeden Schlüssel im Pfad
    for schluessel in pfad:
        try:
            # Versuche, auf den nächsten Schlüssel zuzugreifen
            aktuell = aktuell[schluessel]
            
        except KeyError:
            # Schlüssel existiert nicht
            print(f"Fehler: Schlüssel '{schluessel}' nicht gefunden im Pfad {pfad}")
            return None
            
        except TypeError:
            # aktuell ist kein Dictionary (z.B. Liste, String, int)
            print(f"Fehler: '{schluessel}' kann nicht auf Typ {type(aktuell).__name__} angewendet werden")
            return None
    
    # Wenn wir hier ankommen, haben wir den Wert erfolgreich erreicht
    return aktuell


# Beispielverwendung:
if __name__ == "__main__":
    daten = {
        "benutzer": {
            "name": "Alice",
            "adresse": {
                "stadt": "Berlin",
                "plz": "10115"
            },
            "hobbies": ["Lesen", "Wandern"]
        }
    }
    
    print("Test 1:", sicherer_dict_zugriff(daten, ["benutzer", "name"]))
    # Output: Alice
    
    print("Test 2:", sicherer_dict_zugriff(daten, ["benutzer", "adresse", "plz"]))
    # Output: 10115
    
    print("Test 3:", sicherer_dict_zugriff(daten, ["benutzer", "telefon"]))
    # Output: Fehler: Schlüssel 'telefon' nicht gefunden im Pfad [...] / None
    
    print("Test 4:", sicherer_dict_zugriff(daten, ["benutzer", "hobbies", "stadt"]))
    # Output: Fehler: 'stadt' kann nicht auf Typ list angewendet werden / None
    
    print("Test 5:", sicherer_dict_zugriff(daten, ["benutzer"]))
    # Output: {'name': 'Alice', 'adresse': {...}, 'hobbies': [...]}
```

**Erklärung**:

Die Funktion navigiert schrittweise durch das verschachtelte Dictionary:

1. **Initialisierung**: `aktuell = daten` – starte beim Wurzel-Dictionary

2. **Iteration**: Für jeden Schlüssel im Pfad:
   - **Zugriff versuchen**: `aktuell = aktuell[schluessel]`
     - Bei Erfolg: `aktuell` zeigt jetzt auf das nächste verschachtelte Dictionary
     - Bei `KeyError`: Schlüssel existiert nicht → `None` zurückgeben
     - Bei `TypeError`: `aktuell` ist kein Dictionary (z.B. Liste) → `None` zurückgeben

3. **Rückgabe**: Wenn alle Schlüssel erfolgreich durchlaufen wurden, gib den finalen Wert zurück

**Schritt-für-Schritt Durchlauf** (Beispiel: Pfad `["benutzer", "adresse", "plz"]`):

1. **Start**: `aktuell = daten` (gesamtes Dictionary)
2. **Schlüssel "benutzer"**:
   - `aktuell = aktuell["benutzer"]`
   - `aktuell` ist jetzt `{"name": "Alice", "adresse": {...}, "hobbies": [...]}`
3. **Schlüssel "adresse"**:
   - `aktuell = aktuell["adresse"]`
   - `aktuell` ist jetzt `{"stadt": "Berlin", "plz": "10115"}`
4. **Schlüssel "plz"**:
   - `aktuell = aktuell["plz"]`
   - `aktuell` ist jetzt `"10115"`
5. **Rückgabe**: `return aktuell` → `"10115"`

**Warum diese Lösung?**

- **Flexibel**: Funktioniert mit beliebig tiefen Verschachtelungen
- **Robust**: Fängt beide Fehlertypen ab (`KeyError`, `TypeError`)
- **Informativ**: Fehlermeldungen zeigen, wo das Problem auftrat
- **Einfach**: Klare Iteration statt komplexer Rekursion

**Konzepte in dieser Lösung**:
- **Exception-Handling**: `try-except` für robuste Fehlerbehandlung
- **Iterative Navigation**: Schrittweises Durchlaufen statt Rekursion
- **Type Safety**: `TypeError` fängt Fälle ab, wo der Wert kein Dictionary ist

**Häufige Fehler**:
- **Fehler**: Nur `KeyError` abfangen, nicht `TypeError`
  ```python
  try:
      aktuell = aktuell[schluessel]
  except KeyError:
      return None
  # TypeError wird nicht abgefangen!
  ```
  - **Problem**: Wenn `aktuell` eine Liste ist, wird `TypeError` geworfen, nicht `KeyError`
  - **Richtig**: Beide Exceptions abfangen

- **Fehler**: Pfad als String statt Liste
  ```python
  sicherer_dict_zugriff(daten, "benutzer.adresse.plz")  # FALSCH!
  ```
  - **Problem**: Iteriert über einzelne Zeichen statt Schlüssel
  - **Richtig**: Liste verwenden: `["benutzer", "adresse", "plz"]`

- **Fehler**: Originaldaten verändern
  ```python
  aktuell = daten
  for schluessel in pfad:
      daten = daten[schluessel]  # Überschreibt Original!
  ```
  - **Problem**: `daten` wird überschrieben, Original geht verloren
  - **Richtig**: Separate Variable `aktuell` verwenden

**Alternative Lösungsansätze**:

**Mit `.get()`-Methode** (nur für `KeyError`, nicht `TypeError`):
```python
def sicherer_dict_zugriff_alt(daten, pfad):
    aktuell = daten
    for schluessel in pfad:
        if isinstance(aktuell, dict):
            aktuell = aktuell.get(schluessel)
            if aktuell is None:
                return None
        else:
            return None  # Nicht-Dictionary erreicht
    return aktuell
```

**Mit Rekursion**:
```python
def sicherer_dict_zugriff_rekursiv(daten, pfad):
    if not pfad:
        return daten
    
    try:
        return sicherer_dict_zugriff_rekursiv(daten[pfad[0]], pfad[1:])
    except (KeyError, TypeError):
        return None
```

Beide Alternativen sind funktional äquivalent, aber die iterative Lösung ist in Python idiomatischer und vermeidet Rekursionslimit-Probleme bei sehr tiefen Verschachtelungen.

---

### Lösung P4: Benutzerdefinierte Exception für Validierung

**Vollständiger Code**:
```python
# Benutzerdefinierte Exception-Klassen
class UngueltigerBenutzernameError(Exception):
    """Exception für ungültige Benutzernamen."""
    pass


class UngueltigesPasswortError(Exception):
    """Exception für unsichere Passwörter."""
    pass


class UngueltigeEmailError(Exception):
    """Exception für ungültige E-Mail-Adressen."""
    pass


class BenutzerValidator:
    """Validator für Benutzerdaten mit strengen Regeln."""
    
    def validiere_benutzername(self, name):
        """
        Prüft, ob Benutzername gültig ist.
        
        Regeln:
        - Länge: 3-20 Zeichen
        - Nur alphanumerische Zeichen (Buchstaben und Ziffern)
        
        Raises:
            UngueltigerBenutzernameError: Wenn Validierung fehlschlägt
        """
        if not isinstance(name, str):
            raise UngueltigerBenutzernameError("Benutzername muss ein String sein.")
        
        if len(name) < 3 or len(name) > 20:
            raise UngueltigerBenutzernameError("Benutzername muss 3-20 Zeichen haben.")
        
        if not name.isalnum():
            raise UngueltigerBenutzernameError(
                "Benutzername darf nur Buchstaben und Ziffern enthalten."
            )
    
    def validiere_passwort(self, passwort):
        """
        Prüft, ob Passwort sicher ist.
        
        Regeln:
        - Mindestens 8 Zeichen
        - Mindestens einen Großbuchstaben
        - Mindestens einen Kleinbuchstaben
        - Mindestens eine Ziffer
        
        Raises:
            UngueltigesPasswortError: Wenn Validierung fehlschlägt
        """
        if not isinstance(passwort, str):
            raise UngueltigesPasswortError("Passwort muss ein String sein.")
        
        if len(passwort) < 8:
            raise UngueltigesPasswortError("Passwort muss mindestens 8 Zeichen haben.")
        
        # Prüfe auf Großbuchstaben
        hat_grossbuchstaben = any(c.isupper() for c in passwort)
        if not hat_grossbuchstaben:
            raise UngueltigesPasswortError("Passwort muss mindestens einen Großbuchstaben enthalten.")
        
        # Prüfe auf Kleinbuchstaben
        hat_kleinbuchstaben = any(c.islower() for c in passwort)
        if not hat_kleinbuchstaben:
            raise UngueltigesPasswortError("Passwort muss mindestens einen Kleinbuchstaben enthalten.")
        
        # Prüfe auf Ziffern
        hat_ziffern = any(c.isdigit() for c in passwort)
        if not hat_ziffern:
            raise UngueltigesPasswortError("Passwort muss mindestens eine Ziffer enthalten.")
    
    def validiere_email(self, email):
        """
        Prüft, ob E-Mail-Adresse gültig ist (vereinfacht).
        
        Regeln:
        - Muss ein @ enthalten
        - Nach dem @ muss ein . folgen
        - Mindestens 3 Zeichen
        
        Raises:
            UngueltigeEmailError: Wenn Validierung fehlschlägt
        """
        if not isinstance(email, str):
            raise UngueltigeEmailError("E-Mail muss ein String sein.")
        
        if len(email) < 3:
            raise UngueltigeEmailError("E-Mail ist zu kurz.")
        
        if "@" not in email:
            raise UngueltigeEmailError("E-Mail muss ein '@' enthalten.")
        
        # Prüfe, ob nach dem @ noch ein . kommt
        at_position = email.index("@")
        rest = email[at_position + 1:]  # Teil nach dem @
        
        if "." not in rest:
            raise UngueltigeEmailError("E-Mail muss einen Punkt nach dem '@' enthalten.")
        
        if rest.startswith(".") or rest.endswith("."):
            raise UngueltigeEmailError("E-Mail-Domäne darf nicht mit Punkt beginnen oder enden.")
    
    def validiere_benutzer(self, name, passwort, email):
        """
        Führt alle Validierungen durch.
        
        Returns:
            bool: True wenn alle Validierungen erfolgreich
        
        Raises:
            UngueltigerBenutzernameError, UngueltigesPasswortError, UngueltigeEmailError:
                Wenn eine Validierung fehlschlägt
        """
        # Validiere in dieser Reihenfolge - erste Exception wird geworfen
        self.validiere_benutzername(name)
        self.validiere_passwort(passwort)
        self.validiere_email(email)
        return True


# Beispielverwendung:
if __name__ == "__main__":
    validator = BenutzerValidator()
    
    # Test 1: Alles gültig
    print("Test 1: Gültige Daten")
    try:
        validator.validiere_benutzer("alice123", "Passwort1", "alice@example.com")
        print("✓ Benutzer erfolgreich validiert!")
    except (UngueltigerBenutzernameError, UngueltigesPasswortError, UngueltigeEmailError) as e:
        print(f"✗ Validierungsfehler: {e}")
    
    print("\nTest 2: Ungültiger Benutzername (zu kurz)")
    try:
        validator.validiere_benutzer("ab", "Passwort1", "alice@example.com")
        print("✓ Benutzer erfolgreich validiert!")
    except (UngueltigerBenutzernameError, UngueltigesPasswortError, UngueltigeEmailError) as e:
        print(f"✗ Validierungsfehler: {e}")
    
    print("\nTest 3: Unsicheres Passwort (keine Großbuchstaben)")
    try:
        validator.validiere_benutzer("alice123", "passwort1", "alice@example.com")
        print("✓ Benutzer erfolgreich validiert!")
    except (UngueltigerBenutzernameError, UngueltigesPasswortError, UngueltigeEmailError) as e:
        print(f"✗ Validierungsfehler: {e}")
    
    print("\nTest 4: Ungültige E-Mail (kein @)")
    try:
        validator.validiere_benutzer("alice123", "Passwort1", "ungueltig")
        print("✓ Benutzer erfolgreich validiert!")
    except (UngueltigerBenutzernameError, UngueltigesPasswortError, UngueltigeEmailError) as e:
        print(f"✗ Validierungsfehler: {e}")
    
    print("\nTest 5: Benutzername mit Sonderzeichen")
    try:
        validator.validiere_benutzer("alice@123", "Passwort1", "alice@example.com")
        print("✓ Benutzer erfolgreich validiert!")
    except (UngueltigerBenutzernameError, UngueltigesPasswortError, UngueltigeEmailError) as e:
        print(f"✗ Validierungsfehler: {e}")
```

**Erklärung**:

Diese Lösung demonstriert das Design eines robusten Validierungssystems mit benutzerdefinierten Exceptions:

**1. Benutzerdefinierte Exception-Klassen**:
```python
class UngueltigerBenutzernameError(Exception):
    pass
```
- Erben von `Exception` (Basisklasse für alle benutzerdefinierten Exceptions)
- Können später erweitert werden (z.B. mit `__init__` für zusätzliche Attribute)
- Ermöglichen spezifisches Exception-Handling

**2. Validator-Klasse**:
- Kapselt alle Validierungslogik in einer Klasse
- Jede Validierungsmethode ist eigenständig testbar
- Wirf Exceptions bei Fehlern, kein Boolean-Return

**3. Validierungsmethoden**:

**`validiere_benutzername`**:
- Prüft Typ mit `isinstance()`
- Prüft Länge: 3-20 Zeichen
- Prüft alphanumerisch mit `.isalnum()` (Buchstaben + Ziffern, keine Sonderzeichen)

**`validiere_passwort`**:
- Prüft Mindestlänge: 8 Zeichen
- Prüft Komplexität:
  - `any(c.isupper() for c in passwort)`: Mindestens ein Großbuchstabe
  - `any(c.islower() for c in passwort)`: Mindestens ein Kleinbuchstabe
  - `any(c.isdigit() for c in passwort)`: Mindestens eine Ziffer
- Nutzt Generator Expressions für effiziente Prüfung

**`validiere_email`**:
- Prüft Mindestlänge
- Prüft auf `@`-Zeichen
- Prüft, dass nach `@` noch ein `.` kommt
- Prüft, dass Domäne nicht mit `.` beginnt/endet

**4. Master-Validierung**:
```python
def validiere_benutzer(self, name, passwort, email):
    self.validiere_benutzername(name)
    self.validiere_passwort(passwort)
    self.validiere_email(email)
    return True
```
- Ruft alle Validierungen in Reihenfolge auf
- **Wichtig**: Wirft die **erste** auftretende Exception
- Gibt `True` zurück nur wenn alle erfolgreich

**Schritt-für-Schritt Durchlauf** (Beispiel: Ungültiger Benutzername):

1. `validiere_benutzer("ab", ...)` aufgerufen
2. `validiere_benutzername("ab")` aufgerufen
3. Typ-Check: OK (ist String)
4. Längen-Check: `len("ab") < 3` → **FEHLER**
5. `raise UngueltigerBenutzernameError(...)` wirft Exception
6. Exception propagiert zurück zu `validiere_benutzer`
7. Exception propagiert weiter zum Aufrufer (Testcode)
8. `except`-Block fängt Exception ab, gibt Fehlermeldung aus

**Warum diese Lösung?**

- **Klare Fehlerklassifikation**: Jeder Fehlertyp hat eigene Exception-Klasse
- **Separation of Concerns**: Jede Validierungsmethode prüft nur einen Aspekt
- **Erweiterbar**: Neue Validierungen einfach hinzufügbar
- **Testbar**: Jede Methode kann unabhängig getestet werden
- **Aussagekräftig**: Fehlermeldungen zeigen genau, was falsch ist

**Design-Entscheidungen**:
- **Exceptions statt Boolean**: `raise` bei Fehler statt `return False`
  - **Vorteil**: Erzwingt Fehlerbehandlung, kann nicht ignoriert werden
  - **Vorteil**: Fehlermeldung ist Teil der Exception
- **Keine Default-Werte**: Alle Parameter müssen explizit übergeben werden
- **Generator Expressions**: `any(c.isupper() for c in passwort)` ist effizienter als Loop mit Flag
- **Früher Abbruch**: Validierung stoppt bei erstem Fehler (Alternative: Alle Fehler sammeln)

**Komplexitätsanalyse**:
- **Benutzername-Validierung**: O(n), wobei n = Länge des Benutzernamens
- **Passwort-Validierung**: O(n), wobei n = Länge des Passworts
- **E-Mail-Validierung**: O(n), wobei n = Länge der E-Mail
- **Gesamt**: O(n), linear in der Eingabegröße

**Häufige Fehler**:
- **Fehler**: Exception-Klasse nicht von `Exception` ableiten
  ```python
  class UngueltigerBenutzernameError:  # FALSCH!
      pass
  ```
  - **Problem**: Kann nicht mit `except` abgefangen werden
  - **Richtig**: `class UngueltigerBenutzernameError(Exception):`

- **Fehler**: Boolean statt Exception zurückgeben
  ```python
  def validiere_benutzername(self, name):
      if len(name) < 3:
          return False  # SCHLECHT
  ```
  - **Problem**: Aufrufer kann Fehler ignorieren, keine Fehlermeldung
  - **Richtig**: `raise UngueltigerBenutzernameError("...")`

- **Fehler**: Alle Validierungen in einer Methode
  ```python
  def validiere_alles(self, name, passwort, email):
      if len(name) < 3:
          raise ...
      if len(passwort) < 8:
          raise ...
      # 50 Zeilen Code...
  ```
  - **Problem**: Schwer testbar, schwer wartbar, verstößt gegen SRP (Single Responsibility Principle)
  - **Richtig**: Separate Methoden für jede Validierung

- **Fehler**: `any()` falsch verwendet
  ```python
  hat_grossbuchstaben = any(passwort.isupper())  # FALSCH!
  ```
  - **Problem**: `passwort.isupper()` gibt Boolean zurück, nicht Iterable
  - **Richtig**: `any(c.isupper() for c in passwort)`

**Alternative Lösungsansätze**:

**Mit Regex für E-Mail**:
```python
import re

def validiere_email(self, email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise UngueltigeEmailError("E-Mail-Format ungültig.")
```
- **Vorteil**: Robuster, deckt mehr Fälle ab
- **Nachteil**: Komplexer, schwerer zu verstehen

**Mit Decorator für Validierung**:
```python
def validiere(validator_func):
    def wrapper(self, wert):
        validator_func(self, wert)
        return True
    return wrapper

@validiere
def validiere_benutzername(self, name):
    if len(name) < 3:
        raise UngueltigerBenutzernameError("...")
```
- **Vorteil**: DRY-Prinzip, weniger Boilerplate
- **Nachteil**: Komplexer für Einsteiger

---

### Lösung P5: Robustes Konfigurationssystem

**Vollständiger Code**:
```python
import json


# Benutzerdefinierte Exception-Hierarchie
class KonfigurationsFehler(Exception):
    """Basisklasse für alle Konfigurationsfehler."""
    pass


class KonfigurationsDateiFehler(KonfigurationsFehler):
    """Exception wenn Konfigurationsdatei nicht geladen werden kann."""
    pass


class KonfigurationsFormatFehler(KonfigurationsFehler):
    """Exception wenn JSON-Format ungültig ist."""
    pass


class KonfigurationsValidierungsFehler(KonfigurationsFehler):
    """Exception wenn erforderliche Felder fehlen."""
    pass


class Konfiguration:
    """
    Robustes Konfigurationssystem mit JSON-Unterstützung.
    
    Features:
    - Lädt Konfiguration aus JSON-Dateien
    - Validiert erforderliche Felder
    - Unterstützt Default-Werte
    - Fehlerbehandlung mit benutzerdefinierten Exceptions
    """
    
    def __init__(self, dateiname, erforderliche_felder=None, defaults=None):
        """
        Initialisiert das Konfigurationssystem.
        
        Args:
            dateiname: Pfad zur JSON-Konfigurationsdatei
            erforderliche_felder: Liste von Schlüsseln, die vorhanden sein müssen
            defaults: Dictionary mit Default-Werten für fehlende Felder
        """
        self.dateiname = dateiname
        self.erforderliche_felder = erforderliche_felder or []
        self.defaults = defaults or {}
        self.config = {}
    
    def laden(self):
        """
        Lädt die Konfiguration aus der JSON-Datei.
        
        Raises:
            KonfigurationsDateiFehler: Wenn Datei nicht gefunden oder nicht lesbar
            KonfigurationsFormatFehler: Wenn JSON ungültig ist
            KonfigurationsValidierungsFehler: Wenn erforderliche Felder fehlen
        """
        datei = None
        
        try:
            # Versuche Datei zu öffnen
            datei = open(self.dateiname, 'r', encoding='utf-8')
            
        except FileNotFoundError:
            raise KonfigurationsDateiFehler(
                f"Konfigurationsdatei '{self.dateiname}' nicht gefunden."
            )
        
        except PermissionError:
            raise KonfigurationsDateiFehler(
                f"Keine Berechtigung zum Lesen von '{self.dateiname}'."
            )
        
        else:
            # Datei erfolgreich geöffnet, versuche JSON zu parsen
            try:
                self.config = json.load(datei)
                
            except json.JSONDecodeError as e:
                raise KonfigurationsFormatFehler(
                    f"Ungültiges JSON-Format in '{self.dateiname}': {e}"
                )
            
            # Füge Default-Werte hinzu (nur für fehlende Schlüssel)
            for schluessel, wert in self.defaults.items():
                if schluessel not in self.config:
                    self.config[schluessel] = wert
            
            # Validiere erforderliche Felder
            self._validieren()
        
        finally:
            # Stelle sicher, dass Datei geschlossen wird
            if datei is not None:
                datei.close()
    
    def _validieren(self):
        """
        Prüft, ob alle erforderlichen Felder vorhanden sind.
        
        Raises:
            KonfigurationsValidierungsFehler: Wenn Felder fehlen
        """
        fehlende = []
        
        for feld in self.erforderliche_felder:
            if feld not in self.config:
                fehlende.append(feld)
        
        if fehlende:
            raise KonfigurationsValidierungsFehler(
                f"Erforderliche Felder fehlen: {', '.join(fehlende)}"
            )
    
    def get(self, schluessel, default=None):
        """
        Gibt einen Konfigurationswert zurück.
        
        Args:
            schluessel: Schlüssel des gewünschten Werts
            default: Rückgabewert wenn Schlüssel nicht existiert
        
        Returns:
            Der Wert für den Schlüssel, oder default
        """
        return self.config.get(schluessel, default)
    
    def speichern(self, dateiname):
        """
        Speichert die aktuelle Konfiguration in eine JSON-Datei.
        
        Args:
            dateiname: Pfad zur Zieldatei
        
        Raises:
            KonfigurationsDateiFehler: Wenn Datei nicht geschrieben werden kann
        """
        try:
            with open(dateiname, 'w', encoding='utf-8') as datei:
                json.dump(self.config, datei, indent=4, ensure_ascii=False)
        
        except PermissionError:
            raise KonfigurationsDateiFehler(
                f"Keine Berechtigung zum Schreiben von '{dateiname}'."
            )
        
        except Exception as e:
            raise KonfigurationsDateiFehler(
                f"Fehler beim Speichern von '{dateiname}': {e}"
            )
    
    def aktualisieren(self, schluessel, wert):
        """
        Aktualisiert einen Konfigurationswert.
        
        Args:
            schluessel: Schlüssel des zu ändernden Werts
            wert: Neuer Wert
        """
        self.config[schluessel] = wert
    
    def als_dict(self):
        """
        Gibt die gesamte Konfiguration als Dictionary zurück.
        
        Returns:
            dict: Kopie der Konfiguration
        """
        return self.config.copy()


# Beispielverwendung:
if __name__ == "__main__":
    # Test-Konfigurationsdatei erstellen
    test_config = {
        "datenbank": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb"
        },
        "logging": {
            "level": "INFO",
            "datei": "app.log"
        }
    }
    
    with open("config.json", "w") as f:
        json.dump(test_config, f, indent=4)
    
    print("=== Test 1: Erfolgreiche Nutzung ===")
    try:
        erforderliche = ["datenbank", "logging"]
        defaults = {"datenbank": {"port": 3306}, "debug": False}
        
        config = Konfiguration("config.json", erforderliche_felder=erforderliche, defaults=defaults)
        config.laden()
        
        print(f"Datenbank-Konfiguration: {config.get('datenbank')}")
        print(f"Debug-Modus: {config.get('debug')}")
        print(f"Nicht vorhanden (mit Default): {config.get('nicht_vorhanden', 'Fallback')}")
        print("✓ Konfiguration erfolgreich geladen!\n")
        
    except KonfigurationsFehler as e:
        print(f"✗ Fehler: {e}\n")
    
    print("=== Test 2: Fehlende Datei ===")
    try:
        config = Konfiguration("nicht_vorhanden.json")
        config.laden()
    except KonfigurationsDateiFehler as e:
        print(f"✓ Erwarteter Fehler abgefangen: {e}\n")
    
    print("=== Test 3: Ungültiges JSON ===")
    # Erstelle Datei mit ungültigem JSON
    with open("kaputt.json", "w") as f:
        f.write("{invalid json}")
    
    try:
        config = Konfiguration("kaputt.json")
        config.laden()
    except KonfigurationsFormatFehler as e:
        print(f"✓ Erwarteter Fehler abgefangen: {e}\n")
    
    print("=== Test 4: Fehlende erforderliche Felder ===")
    try:
        config = Konfiguration("config.json", erforderliche_felder=["datenbank", "api_key"])
        config.laden()
    except KonfigurationsValidierungsFehler as e:
        print(f"✓ Erwarteter Fehler abgefangen: {e}\n")
    
    print("=== Test 5: Konfiguration aktualisieren und speichern ===")
    try:
        config = Konfiguration("config.json")
        config.laden()
        
        # Aktualisiere Wert
        config.aktualisieren("version", "1.0.0")
        print(f"Version aktualisiert: {config.get('version')}")
        
        # Speichere in neue Datei
        config.speichern("config_neu.json")
        print("✓ Konfiguration gespeichert in 'config_neu.json'\n")
        
    except KonfigurationsFehler as e:
        print(f"✗ Fehler: {e}\n")
    
    print("=== Test 6: Komplette Konfiguration als Dictionary ===")
    try:
        config = Konfiguration("config.json")
        config.laden()
        
        vollstaendig = config.als_dict()
        print(f"Gesamte Konfiguration:\n{json.dumps(vollstaendig, indent=2)}")
        
    except KonfigurationsFehler as e:
        print(f"✗ Fehler: {e}")
```

**Erklärung**:

Dieses robuste Konfigurationssystem demonstriert fortgeschrittene Fehlerbehandlung und objektorientiertes Design:

**1. Exception-Hierarchie**:
```python
KonfigurationsFehler (Basisklasse)
├── KonfigurationsDateiFehler
├── KonfigurationsFormatFehler
└── KonfigurationsValidierungsFehler
```
- **Vorteil**: Ermöglicht sowohl spezifisches als auch generisches Exception-Handling
- Aufrufer kann entweder alle abfangen: `except KonfigurationsFehler`
- Oder spezifisch: `except KonfigurationsDateiFehler`

**2. `__init__`-Methode**:
- Speichert Dateiname, erforderliche Felder und Defaults
- `erforderliche_felder or []`: Nutzt leere Liste als Default, falls `None` übergeben
- `self.config = {}`: Initialisiert leeres Dictionary

**3. `laden()`-Methode** (Kernstück):

**Datei öffnen**:
```python
try:
    datei = open(self.dateiname, 'r', encoding='utf-8')
except FileNotFoundError:
    raise KonfigurationsDateiFehler(...)
except PermissionError:
    raise KonfigurationsDateiFehler(...)
```
- Fängt beide Fehlertypen ab und wirft einheitliche `KonfigurationsDateiFehler`

**JSON parsen (im `else`-Block)**:
```python
else:
    try:
        self.config = json.load(datei)
    except json.JSONDecodeError as e:
        raise KonfigurationsFormatFehler(...)
```
- `else`-Block wird nur ausgeführt, wenn Datei erfolgreich geöffnet wurde
- `json.load()` wirft `JSONDecodeError` bei ungültigem JSON
- Wird in `KonfigurationsFormatFehler` umgewandelt

**Defaults hinzufügen**:
```python
for schluessel, wert in self.defaults.items():
    if schluessel not in self.config:
        self.config[schluessel] = wert
```
- Fügt nur fehlende Schlüssel hinzu
- Überschreibt keine existierenden Werte

**Validierung**:
```python
self._validieren()
```
- Private Methode (Konvention: `_`-Präfix)
- Prüft erforderliche Felder
- Wirft `KonfigurationsValidierungsFehler` bei fehlenden Feldern

**Aufräumen (`finally`)**:
```python
finally:
    if datei is not None:
        datei.close()
```
- Garantiert Schließen der Datei
- Prüft `datei is not None`, da Variable bei Exception im `try` nicht zugewiesen sein könnte

**4. Weitere Methoden**:

**`get(schluessel, default=None)`**:
- Nutzt Dictionary-Methode `.get()` für sicheren Zugriff
- Gibt `default` zurück, wenn Schlüssel nicht existiert

**`speichern(dateiname)`**:
- Verwendet `with`-Statement für automatisches Schließen
- `json.dump()` mit Formatierung: `indent=4`, `ensure_ascii=False` (für Umlaute)
- Fängt alle Fehler ab und wirft `KonfigurationsDateiFehler`

**`aktualisieren(schluessel, wert)`**:
- Einfache Setter-Methode
- Könnte erweitert werden um Validierung

**`als_dict()`**:
- Gibt **Kopie** zurück (`self.config.copy()`), nicht Original
- Verhindert unbeabsichtigte Änderungen von außen

**Schritt-für-Schritt Durchlauf** (Erfolgsfall):

1. `config = Konfiguration("config.json", erforderliche_felder=["datenbank"], defaults={"debug": False})`
2. `config.laden()` aufgerufen
3. `try`: `open("config.json")` → Erfolg
4. `else`:
   - `json.load(datei)` → Erfolg, `self.config` gefüllt
   - Defaults hinzufügen: `"debug": False` wird ergänzt
   - `_validieren()`: Prüfe ob "datenbank" vorhanden → Ja
5. `finally`: `datei.close()`
6. Konfiguration erfolgreich geladen!

**Warum diese Architektur?**

- **Exception-Hierarchie**: Ermöglicht flexible Fehlerbehandlung auf verschiedenen Abstraktionsebenen
- **`try-except-else-finally`**: Klare Trennung: Datei öffnen (try) → Parsen (else) → Aufräumen (finally)
- **Defaults-Mechanismus**: Macht Konfiguration flexibler, Felder sind optional
- **Validierung**: Erzwingt Anwesenheit kritischer Felder
- **Kapselung**: Alle Konfigurationslogik in einer Klasse

**Design-Entscheidungen**:
- **`_validieren()` privat**: Nutzer soll nicht direkt validieren, passiert automatisch in `laden()`
- **Kopie in `als_dict()`**: Schützt interne Datenstruktur vor externen Änderungen
- **`with`-Statement in `speichern()`**: Sicherer als manuelles `open()`/`close()`
- **Generisches `Exception` in `speichern()`**: Fängt unvorhergesehene Fehler ab

**Komplexitätsanalyse**:
- **`laden()`**: O(n + m), wobei n = Anzahl Zeichen in JSON, m = Anzahl Default-Felder
- **`get()`**: O(1), Hash-Tabellen-Zugriff
- **`speichern()`**: O(n), wobei n = Anzahl Zeichen in JSON
- **`_validieren()`**: O(k), wobei k = Anzahl erforderliche Felder

**Bonus-Challenge Lösung** (Verschachtelte Schlüssel):
```python
def get_nested(self, pfad, default=None):
    """
    Greift auf verschachtelte Werte zu.
    
    Args:
        pfad: String mit punktsepariertem Pfad, z.B. "datenbank.host"
        default: Rückgabewert wenn Pfad nicht existiert
    
    Returns:
        Der Wert am Ende des Pfads, oder default
    """
    schluessel = pfad.split(".")
    aktuell = self.config
    
    for key in schluessel:
        if isinstance(aktuell, dict) and key in aktuell:
            aktuell = aktuell[key]
        else:
            return default
    
    return aktuell

# Verwendung:
# config.get_nested("datenbank.host") → "localhost"
```

**Häufige Fehler**:
- **Fehler**: Datei nicht im `finally` schließen
  - **Problem**: Bei Exception bleibt Datei offen
  - **Richtig**: `finally` mit `if datei is not None`

- **Fehler**: JSON-Parsing im `try` statt `else`
  ```python
  try:
      datei = open(...)
      self.config = json.load(datei)  # Beide im try!
  except FileNotFoundError:
      # Fängt nur FileNotFoundError ab, nicht JSONDecodeError
  ```
  - **Problem**: JSON-Fehler würden nicht abgefangen
  - **Richtig**: Datei öffnen im `try`, Parsen im `else` mit eigenem `try-except`

- **Fehler**: Defaults überschreiben existierende Werte
  ```python
  for key, value in self.defaults.items():
      self.config[key] = value  # FALSCH!
  ```
  - **Problem**: Überschreibt auch Werte aus der Datei
  - **Richtig**: `if key not in self.config:` prüfen

- **Fehler**: `.copy()` vergessen in `als_dict()`
  ```python
  def als_dict(self):
      return self.config  # Gibt Referenz zurück!
  ```
  - **Problem**: Externe Änderungen beeinflussen interne Konfiguration
  - **Richtig**: `return self.config.copy()`

