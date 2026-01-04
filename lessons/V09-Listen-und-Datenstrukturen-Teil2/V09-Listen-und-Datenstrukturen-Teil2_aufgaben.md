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

### Aufgabe P1: Sichere Messwert-Eingabe für Sensorkalibrierung (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: `try-except`, `ValueError`, `input()`, `float()`  
**Maschinenbau-Kontext**: Robuste Eingabe von Kalibrierwerten für Sensoren

Schreibe eine Funktion `eingabe_messwert(prompt, min_wert, max_wert, einheit)`, die den Benutzer zur Eingabe eines Messwerts auffordert und sicherstellt, dass:
- Die Eingabe eine gültige Dezimalzahl ist
- Der Wert zwischen `min_wert` und `max_wert` liegt (inklusive)
- Bei ungültiger Eingabe wird eine Fehlermeldung ausgegeben und erneut gefragt

> [!NOTE]
> **Sensorkalibrierung**: Bei der Kalibrierung von Sensoren (Temperatur, Druck, Drehzahl) müssen Referenzwerte präzise eingegeben werden. Fehlerhafte Eingaben können zu Messfehlern und Produktionsausschuss führen. Typische Bereiche:
> - Temperatur: -50°C bis 1200°C
> - Druck: 0 bar bis 400 bar
> - Drehzahl: 0 U/min bis 20000 U/min

Die Funktion soll so lange wiederholt fragen, bis eine gültige Eingabe erfolgt.

**Beispiel Ein-/Ausgabe**:
```
>>> temp = eingabe_messwert("Referenztemperatur: ", -50, 1200, "°C")
Referenztemperatur: abc
⚠️  Fehler: Bitte gib eine gültige Zahl ein.
Referenztemperatur: -100
⚠️  Fehler: Wert muss zwischen -50 und 1200 °C liegen.
Referenztemperatur: 1500
⚠️  Fehler: Wert muss zwischen -50 und 1200 °C liegen.
Referenztemperatur: 850.5
✅ Wert akzeptiert: 850.5 °C
>>> print(temp)
850.5
```

**Starter-Code**:
```python
def eingabe_messwert(prompt, min_wert, max_wert, einheit):
    """
    Fordert den Benutzer zur Eingabe eines Messwerts auf.
    Wiederholt die Eingabe bei Fehlern.
    """
    # Dein Code hier
    pass
```

---

### Aufgabe P2: Maschinen-Logfile-Analyse mit Fehlerbehandlung (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `try-except-else-finally`, `FileNotFoundError`, `open()`, `with`  
**Maschinenbau-Kontext**: Analyse von Maschinen-Protokolldateien für Wartungsberichte

Schreibe eine Funktion `analyse_maschinenlog(dateiname)`, die:
- Ein Maschinen-Logfile einliest und Alarm-Einträge zählt (Zeilen, die "ALARM" oder "ERROR" enthalten)
- Bei Erfolg ein Dictionary mit Statistiken zurückgibt: `{"zeilen": n, "alarme": x, "errors": y}`
- Bei `FileNotFoundError`: Eine Fehlermeldung ausgibt und `None` zurückgibt
- Bei `PermissionError`: Eine Fehlermeldung ausgibt und `None` zurückgibt
- In der `finally`-Klausel eine Meldung ausgibt, dass die Analyse abgeschlossen ist

> [!NOTE]
> **Maschinen-Logfiles**: Produktionsmaschinen protokollieren kontinuierlich Ereignisse. Typische Einträge:
> - `INFO`: Normale Betriebsmeldungen
> - `WARNING`: Hinweise auf potenzielle Probleme
> - `ALARM`: Kritische Zustände (Überhitzung, Überlast)
> - `ERROR`: Systemfehler, Sensorfehler
> Regelmäßige Analyse erkennt Ausfallmuster.

**Beispiel Ein-/Ausgabe**:
```
>>> stats = analyse_maschinenlog("maschine_01.log")
✅ Logfile erfolgreich analysiert.
Analyse abgeschlossen.
>>> print(stats)
{'zeilen': 1247, 'alarme': 12, 'errors': 3}

>>> stats = analyse_maschinenlog("nicht_vorhanden.log")
❌ Fehler: Datei 'nicht_vorhanden.log' wurde nicht gefunden.
Analyse abgeschlossen.
>>> print(stats)
None
```

**Hinweise**:
- Verwende `with open(dateiname, 'r') as f:` für sicheres Datei-Handling
- Zähle Zeilen mit `"ALARM" in zeile` und `"ERROR" in zeile`
- `try-except-else-finally`-Struktur für vollständige Fehlerbehandlung

---

### Aufgabe P3: Verschachtelte Maschinen-Konfiguration (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: `KeyError`, `TypeError`, Dictionaries, `try-except`  
**Maschinenbau-Kontext**: Zugriff auf verschachtelte CNC-Maschinenparameter

Schreibe eine Funktion `parameter_lesen(config, pfad)`, die einen verschachtelten Dictionary-Zugriff mit einem **Pfad** ermöglicht.

> [!NOTE]
> **CNC-Maschinenkonfiguration**: Moderne CNC-Steuerungen verwenden hierarchische Konfigurationen:
> ```
> Maschine
> ├── Achsen
> │   ├── X-Achse (Geschwindigkeit, Beschleunigung, Grenzen)
> │   ├── Y-Achse
> │   └── Z-Achse
> ├── Spindel (Drehzahl, Drehmoment)
> └── Werkzeugmagazin (Kapazität, Wechselzeit)
> ```

**Pfad-Format**: Eine Liste von Schlüsseln, z.B. `["achsen", "x_achse", "max_geschwindigkeit"]`  
**Rückgabe**: Den Wert am Ende des Pfads, oder `None` bei Fehler

Die Funktion soll folgende Fehler abfangen:
- `KeyError`: Wenn ein Schlüssel nicht existiert
- `TypeError`: Wenn ein Zwischenelement kein Dictionary ist

**Beispiel Ein-/Ausgabe**:
```python
cnc_config = {
    "maschine_id": "CNC-42",
    "achsen": {
        "x_achse": {
            "max_geschwindigkeit": 15000,  # mm/min
            "beschleunigung": 2000,         # mm/s²
            "arbeitsbereich": 800           # mm
        },
        "y_achse": {
            "max_geschwindigkeit": 12000,
            "beschleunigung": 1800,
            "arbeitsbereich": 600
        }
    },
    "spindel": {
        "max_drehzahl": 24000,  # U/min
        "leistung": 18.5         # kW
    },
    "werkzeuge": [1, 5, 8, 12, 20]
}

print(parameter_lesen(cnc_config, ["achsen", "x_achse", "max_geschwindigkeit"]))
# Output: 15000

print(parameter_lesen(cnc_config, ["spindel", "max_drehzahl"]))
# Output: 24000

print(parameter_lesen(cnc_config, ["achsen", "z_achse", "max_geschwindigkeit"]))
# Output: None (KeyError: 'z_achse' existiert nicht)

print(parameter_lesen(cnc_config, ["werkzeuge", "max_geschwindigkeit"]))
# Output: None (TypeError: 'werkzeuge' ist eine Liste, kein Dictionary)
```

**Hinweise**:
- Iteriere durch die Pfad-Liste und greife schrittweise auf das Dictionary zu
- Verwende `try-except`, um Fehler abzufangen
- Bei Fehler gib informative Meldung aus und return `None`

---

### Aufgabe P4: Benutzerdefinierte Exception für Materialvalidierung (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Benutzerdefinierte Exceptions, `raise`, Klassen  
**Maschinenbau-Kontext**: Validierung von Materialparametern für Simulation/FEM

Entwickle ein Validierungssystem für Materialparameter mit benutzerdefinierten Exceptions:

> [!NOTE]
> **Materialparameter-Validierung**: FEM-Simulationen und CAD-Systeme benötigen valide Materialdaten:
> - **E-Modul** (Elastizitätsmodul): 1-1000 GPa
> - **Dichte**: 0.1-25 g/cm³
> - **Streckgrenze**: 1-3000 MPa
> Falsche Werte führen zu unrealistischen Simulationsergebnissen.

**Aufgabe**:
1. Erstelle drei benutzerdefinierte Exception-Klassen:
   - `UngueltigerEModulError`: Für ungültiges Elastizitätsmodul
   - `UngueltigeDichteError`: Für ungültige Dichte
   - `UngueltigeStreckgrenzeError`: Für ungültige Streckgrenze

2. Implementiere eine Klasse `MaterialValidator` mit Methoden:
   - `validiere_e_modul(e_modul)`: Prüft, ob E-Modul zwischen 1 und 1000 GPa liegt
   - `validiere_dichte(dichte)`: Prüft, ob Dichte zwischen 0.1 und 25 g/cm³ liegt
   - `validiere_streckgrenze(re)`: Prüft, ob Streckgrenze zwischen 1 und 3000 MPa liegt
   - `validiere_material(e_modul, dichte, re, name)`: Ruft alle Validierungen auf

**Beispiel Ein-/Ausgabe**:
```python
validator = MaterialValidator()

try:
    validator.validiere_material(
        e_modul=210,      # GPa
        dichte=7.85,      # g/cm³
        re=235,           # MPa
        name="Baustahl S235"
    )
    print("✅ Material 'Baustahl S235' erfolgreich validiert!")
except (UngueltigerEModulError, UngueltigeDichteError, UngueltigeStreckgrenzeError) as e:
    print(f"❌ Validierungsfehler: {e}")

# Output: ✅ Material 'Baustahl S235' erfolgreich validiert!

try:
    validator.validiere_material(
        e_modul=5000,     # Zu hoch!
        dichte=0.05,      # Zu niedrig!
        re=5000,          # Zu hoch!
        name="Ungültiges Material"
    )
except (UngueltigerEModulError, UngueltigeDichteError, UngueltigeStreckgrenzeError) as e:
    print(f"❌ Validierungsfehler: {e}")

# Output: ❌ Validierungsfehler: E-Modul muss zwischen 1 und 1000 GPa liegen (erhalten: 5000 GPa).
```

**Hinweise**:
- Jede Exception-Klasse sollte aussagekräftige Fehlermeldungen mit dem tatsächlichen Wert liefern
- Die `validiere_material`-Methode sollte alle Validierungen durchführen und die erste auftretende Exception werfen
- Verwende f-Strings für informative Fehlermeldungen

---

### Aufgabe P5: Robustes Maschinen-Konfigurationssystem (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: `try-except-else-finally`, JSON, Datei-I/O, Benutzerdefinierte Exceptions  
**Maschinenbau-Kontext**: Produktions-Konfigurationsverwaltung für Fertigungszellen

Entwickle ein robustes Konfigurationssystem für Fertigungszellen, das JSON-Konfigurationsdateien lädt, validiert und mit Default-Werten arbeitet.

> [!NOTE]
> **Fertigungszellen-Konfiguration**: Moderne Produktionsanlagen verwenden zentrale Konfigurationsdateien für:
> - Maschinenparameter (Geschwindigkeiten, Temperaturen, Drücke)
> - Qualitätsgrenzen (Toleranzen, Prüfintervalle)
> - Prozessparameter (Zykluszeiten, Werkzeugwechsel)
> - Netzwerkeinstellungen (IP, Ports, Protokolle)

**Anforderungen**:

1. **Benutzerdefinierte Exceptions**:
   - `KonfigurationsFehler`: Basisklasse für alle Konfigurationsfehler
   - `KonfigurationsDateiFehler`: Wenn Datei nicht gefunden oder nicht lesbar
   - `KonfigurationsFormatFehler`: Wenn JSON ungültig ist
   - `KonfigurationsValidierungsFehler`: Wenn erforderliche Felder fehlen

2. **Klasse `FertigungszellenKonfiguration`**:
   - `__init__(dateiname, erforderliche_felder=None, defaults=None)`
   - `laden()`: Lädt die Konfiguration aus einer JSON-Datei
   - `validieren()`: Prüft, ob alle erforderlichen Felder vorhanden sind
   - `get(schluessel, default=None)`: Gibt einen Konfigurationswert zurück
   - `speichern(dateiname)`: Speichert die aktuelle Konfiguration

3. **Fehlerbehandlung**:
   - Alle Datei-Operationen mit `try-except-finally` abgesichert
   - Bei fehlenden Feldern Default-Werte verwenden
   - Aussagekräftige Fehlermeldungen

**Beispiel-Konfigurationsdatei** (`fertigungszelle_01.json`):
```json
{
  "maschine": {
    "typ": "CNC-Drehmaschine",
    "id": "CNC-42",
    "max_drehzahl": 6000,
    "spindel_leistung": 15.0
  },
  "qualitaet": {
    "toleranz_durchmesser": 0.02,
    "pruefintervall_minuten": 30,
    "ausschussgrenze_prozent": 2.0
  },
  "netzwerk": {
    "ip": "192.168.1.42",
    "port": 8080,
    "protokoll": "OPC-UA"
  }
}
```

**Beispiel Ein-/Ausgabe**:
```python
erforderliche = ["maschine", "qualitaet"]
defaults = {"netzwerk": {"port": 502}, "debug_modus": False}

try:
    config = FertigungszellenKonfiguration(
        "fertigungszelle_01.json",
        erforderliche_felder=erforderliche,
        defaults=defaults
    )
    config.laden()
    
    print(config.get("maschine"))
    # Output: {'typ': 'CNC-Drehmaschine', 'id': 'CNC-42', ...}
    
    print(config.get("debug_modus"))
    # Output: False (Default-Wert)
    
except KonfigurationsFehler as e:
    print(f"❌ Fehler: {e}")
```

**Bonus-Challenge**:
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
