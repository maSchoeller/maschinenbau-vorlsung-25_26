# V09: Übungsaufgaben - Listen und Datenstrukturen – Teil 2

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V09.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Binärbaum-Analyse (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Gegeben ist folgender Binärbaum:

```
        50
       /  \
      30   70
     / \   / \
   20  40 60  80
  /
 10
```

Beantworte die folgenden Fragen:

a) Was ist die **Wurzel** dieses Baums?  
b) Welche Knoten sind **Blätter**?  
c) Was ist die **Höhe** des Baums?  
d) Was ist die **Tiefe** des Knotens 40?  
e) Ist dies ein **Binärer Suchbaum**? Begründe deine Antwort.

**Hinweise**:
- Die Höhe eines Baums ist die maximale Tiefe aller Blätter
- Die Tiefe wird von der Wurzel aus gezählt (Wurzel hat Tiefe 0)

---

### Aufgabe T2: Traversierung verstehen (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

Gegeben ist folgender Binärer Suchbaum:

```
        15
       /  \
      10   20
     / \     \
    5  12    25
```

a) Gib die Reihenfolge der besuchten Knoten für die **Inorder-Traversierung** an.  
b) Gib die Reihenfolge der besuchten Knoten für die **Preorder-Traversierung** an.  
c) Gib die Reihenfolge der besuchten Knoten für die **Postorder-Traversierung** an.  
d) Gib die Reihenfolge der besuchten Knoten für die **Level-Order-Traversierung** an.  
e) Welche Traversierungsart liefert die Werte in sortierter Reihenfolge? Warum?

**Hinweise**:
- Inorder: Links → Wurzel → Rechts
- Preorder: Wurzel → Links → Rechts
- Postorder: Links → Rechts → Wurzel
- Level-Order: Ebenenweise von oben nach unten, links nach rechts

---

### Aufgabe T3: Hash-Tabellen-Design (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

Du sollst eine Hash-Tabelle mit der Größe **m = 7** implementieren. Verwende die Hash-Funktion `h(key) = key % 7`.

Die folgenden Schlüssel sollen in dieser Reihenfolge eingefügt werden: **10, 22, 31, 4, 15, 28, 17**

a) **Chaining**: Zeichne die Hash-Tabelle nach dem Einfügen aller Schlüssel mit der Chaining-Methode. Welche Schlüssel kollidieren?

b) **Linear Probing**: Zeichne die Hash-Tabelle nach dem Einfügen aller Schlüssel mit Linear Probing. Zeige für jeden kollidierenden Schlüssel die Sondierungssequenz.

c) **Vergleich**: Welche Methode hat für diese spezielle Schlüsselmenge bessere Performance? Begründe deine Antwort mit Bezug auf die durchschnittliche Suchzeit.

d) **Ladefaktor**: Berechne den Ladefaktor α = n/m nach dem Einfügen aller Schlüssel. Ist dieser Ladefaktor akzeptabel? Ab welchem Ladefaktor sollte die Tabelle vergrößert werden?

**Hinweise**:
- Bei Chaining: Füge kollidierende Elemente am Anfang der Liste ein
- Bei Linear Probing: Suche bei Kollision den nächsten freien Platz: `(h(key) + i) % 7`, i = 0, 1, 2, ...
- Typischer Schwellenwert für Rehashing: α ≈ 0.7 bei Open Addressing, α ≈ 1.0 bei Chaining

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Sichere Zahleneingabe (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: `try-except`, `ValueError`, `input()`, `int()`

Schreibe eine Funktion `eingabe_ganzzahl(prompt, min_wert, max_wert)`, die den Benutzer zur Eingabe einer Ganzzahl auffordert und sicherstellt, dass:
- Die Eingabe eine gültige Ganzzahl ist
- Die Zahl zwischen `min_wert` und `max_wert` liegt (inklusive)
- Bei ungültiger Eingabe wird eine Fehlermeldung ausgegeben und erneut gefragt

Die Funktion soll so lange wiederholt fragen, bis eine gültige Eingabe erfolgt.

**Beispiel Ein-/Ausgabe**:
```
>>> alter = eingabe_ganzzahl("Dein Alter: ", 0, 120)
Dein Alter: abc
Fehler: Bitte gib eine gültige Zahl ein.
Dein Alter: -5
Fehler: Zahl muss zwischen 0 und 120 liegen.
Dein Alter: 150
Fehler: Zahl muss zwischen 0 und 120 liegen.
Dein Alter: 25
>>> print(alter)
25
```

**Starter-Code**:
```python
def eingabe_ganzzahl(prompt, min_wert, max_wert):
    """
    Fordert den Benutzer zur Eingabe einer Ganzzahl auf.
    Wiederholt die Eingabe bei Fehlern.
    """
    # Dein Code hier
    pass
```

---

### Aufgabe P2: Dateiverarbeitung mit Fehlerbehandlung (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `try-except-else-finally`, `FileNotFoundError`, `open()`, `with`

Schreibe eine Funktion `zeilenanzahl_zaehlen(dateiname)`, die:
- Die Anzahl der Zeilen in einer Textdatei zählt
- Bei Erfolg die Anzahl zurückgibt
- Bei `FileNotFoundError`: Eine Fehlermeldung ausgibt und `None` zurückgibt
- Bei `PermissionError`: Eine Fehlermeldung ausgibt und `None` zurückgibt
- In der `finally`-Klausel eine Meldung ausgibt, dass der Vorgang abgeschlossen ist

Teste die Funktion mit:
- Einer existierenden Datei
- Einer nicht existierenden Datei
- Optional: Einer Datei ohne Leseberechtigung (nur unter Unix/Linux testbar)

**Beispiel Ein-/Ausgabe**:
```
>>> anzahl = zeilenanzahl_zaehlen("test.txt")
Datei erfolgreich gelesen.
Vorgang abgeschlossen.
>>> print(anzahl)
42

>>> anzahl = zeilenanzahl_zaehlen("nicht_vorhanden.txt")
Fehler: Datei 'nicht_vorhanden.txt' wurde nicht gefunden.
Vorgang abgeschlossen.
>>> print(anzahl)
None
```

---

### Aufgabe P3: Dictionary-Zugriff mit Fehlerbehandlung (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: `KeyError`, `TypeError`, Dictionaries, `try-except`

Schreibe eine Funktion `sicherer_dict_zugriff(daten, pfad)`, die einen verschachtelten Dictionary-Zugriff mit einem **Pfad** ermöglicht.

**Pfad-Format**: Eine Liste von Schlüsseln, z.B. `["benutzer", "adresse", "plz"]`  
**Rückgabe**: Den Wert am Ende des Pfads, oder `None` bei Fehler

Die Funktion soll folgende Fehler abfangen:
- `KeyError`: Wenn ein Schlüssel nicht existiert
- `TypeError`: Wenn ein Zwischenelement kein Dictionary ist

**Beispiel Ein-/Ausgabe**:
```python
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

print(sicherer_dict_zugriff(daten, ["benutzer", "name"]))
# Output: Alice

print(sicherer_dict_zugriff(daten, ["benutzer", "adresse", "plz"]))
# Output: 10115

print(sicherer_dict_zugriff(daten, ["benutzer", "telefon"]))
# Output: None (KeyError: 'telefon' existiert nicht)

print(sicherer_dict_zugriff(daten, ["benutzer", "hobbies", "stadt"]))
# Output: None (TypeError: 'hobbies' ist eine Liste, kein Dictionary)
```

**Hinweise**:
- Iteriere durch die Pfad-Liste und greife schrittweise auf das Dictionary zu
- Verwende `try-except`, um Fehler abzufangen

---

### Aufgabe P4: Benutzerdefinierte Exception für Validierung (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Benutzerdefinierte Exceptions, `raise`, Klassen, String-Methoden

Entwickle ein Validierungssystem für Benutzerdaten mit benutzerdefinierten Exceptions:

**Aufgabe**:
1. Erstelle drei benutzerdefinierte Exception-Klassen:
   - `UngueltigerBenutzernameError`: Für ungültige Benutzernamen
   - `UngueltigesPasswortError`: Für unsichere Passwörter
   - `UngueltigeEmailError`: Für ungültige E-Mail-Adressen

2. Implementiere eine Klasse `BenutzerValidator` mit Methoden:
   - `validiere_benutzername(name)`: Prüft, ob Benutzername 3-20 Zeichen hat und nur alphanumerische Zeichen enthält
   - `validiere_passwort(passwort)`: Prüft, ob Passwort mindestens 8 Zeichen hat, Groß-/Kleinbuchstaben und Ziffern enthält
   - `validiere_email(email)`: Prüft, ob E-Mail ein `@` und einen `.` nach dem `@` enthält
   - `validiere_benutzer(name, passwort, email)`: Ruft alle Validierungen auf und gibt bei Erfolg `True` zurück

**Beispiel Ein-/Ausgabe**:
```python
validator = BenutzerValidator()

try:
    validator.validiere_benutzer("alice123", "Passwort1", "alice@example.com")
    print("Benutzer erfolgreich validiert!")
except (UngueltigerBenutzernameError, UngueltigesPasswortError, UngueltigeEmailError) as e:
    print(f"Validierungsfehler: {e}")

# Output: Benutzer erfolgreich validiert!

try:
    validator.validiere_benutzer("ab", "passwort", "ungueltig")
    print("Benutzer erfolgreich validiert!")
except (UngueltigerBenutzernameError, UngueltigesPasswortError, UngueltigeEmailError) as e:
    print(f"Validierungsfehler: {e}")

# Output: Validierungsfehler: Benutzername muss 3-20 Zeichen haben.
```

**Hinweise**:
- Jede Exception-Klasse sollte aussagekräftige Fehlermeldungen liefern
- Nutze String-Methoden wie `.isalnum()`, `.isdigit()`, `.isupper()`, `.islower()`
- Die `validiere_benutzer`-Methode sollte alle Validierungen durchführen und die erste auftretende Exception werfen

---

### Aufgabe P5: Robustes Konfigurationssystem (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: `try-except-else-finally`, JSON, Datei-I/O, Benutzerdefinierte Exceptions, Dictionaries

Entwickle ein robustes Konfigurationssystem, das JSON-Konfigurationsdateien lädt, validiert und mit Default-Werten arbeitet.

**Anforderungen**:

1. **Benutzerdefinierte Exception**:
   - `KonfigurationsFehler`: Basisklasse für alle Konfigurationsfehler
   - `KonfigurationsDateiFehler`: Wenn Datei nicht gefunden oder nicht lesbar
   - `KonfigurationsFormatFehler`: Wenn JSON ungültig ist
   - `KonfigurationsValidierungsFehler`: Wenn erforderliche Felder fehlen

2. **Klasse `Konfiguration`**:
   - `__init__(dateiname, erforderliche_felder=None, defaults=None)`
   - `laden()`: Lädt die Konfiguration aus einer JSON-Datei
   - `validieren()`: Prüft, ob alle erforderlichen Felder vorhanden sind
   - `get(schluessel, default=None)`: Gibt einen Konfigurationswert zurück
   - `speichern(dateiname)`: Speichert die aktuelle Konfiguration in eine Datei

3. **Fehlerbehandlung**:
   - Alle Datei-Operationen müssen mit `try-except-finally` abgesichert sein
   - Bei fehlenden Feldern sollen Default-Werte verwendet werden
   - Aussagekräftige Fehlermeldungen für alle Exception-Typen

**Beispiel-Konfigurationsdatei** (`config.json`):
```json
{
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
```

**Beispiel Ein-/Ausgabe**:
```python
# Erfolgreiche Nutzung:
erforderliche = ["datenbank", "logging"]
defaults = {"datenbank": {"port": 3306}, "debug": False}

try:
    config = Konfiguration("config.json", erforderliche_felder=erforderliche, defaults=defaults)
    config.laden()
    
    print(config.get("datenbank"))
    # Output: {'host': 'localhost', 'port': 5432, 'name': 'mydb'}
    
    print(config.get("debug"))
    # Output: False (Default-Wert, da nicht in Datei)
    
    print(config.get("nicht_vorhanden", default="Fallback"))
    # Output: Fallback
    
except KonfigurationsFehler as e:
    print(f"Fehler beim Laden der Konfiguration: {e}")

# Fehlende Datei:
try:
    config = Konfiguration("nicht_vorhanden.json")
    config.laden()
except KonfigurationsDateiFehler as e:
    print(f"Dateifehler: {e}")
# Output: Dateifehler: Konfigurationsdatei 'nicht_vorhanden.json' nicht gefunden.

# Ungültiges JSON:
# Datei "kaputt.json" enthält: {invalid json}
try:
    config = Konfiguration("kaputt.json")
    config.laden()
except KonfigurationsFormatFehler as e:
    print(f"Formatfehler: {e}")
# Output: Formatfehler: Ungültiges JSON-Format in 'kaputt.json'.
```

**Bonus-Challenge**:
- Implementiere eine Methode `aktualisieren(schluessel, wert)`, die einen Konfigurationswert ändert
- Füge eine Methode `als_dict()` hinzu, die die gesamte Konfiguration als Dictionary zurückgibt
- Implementiere Unterstützung für verschachtelte Schlüssel im `get()`-Zugriff (z.B. `config.get("datenbank.host")`)

**Hinweise**:
- Nutze das `json`-Modul für das Parsen und Speichern
- Die `finally`-Klausel sollte sicherstellen, dass Datei-Handles immer geschlossen werden
- Verwende `with`-Statements für Datei-Operationen wo möglich
