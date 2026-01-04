# V11: Übungsaufgaben - GPTs, LLMs & Künstliche Intelligenz

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V11.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Geschichte der KI und Paradigmenwechsel (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten

Die Entwicklung der Künstlichen Intelligenz lässt sich in verschiedene Phasen einteilen, die jeweils von unterschiedlichen Paradigmen geprägt wurden.

**Aufgabenstellung**:

a) Ordne die folgenden KI-Systeme chronologisch und benenne die zugehörige KI-Epoche:
   - AlexNet
   - MYCIN
   - GPT-3
   - Random Forest Classifier
   - Transformer-Modell

b) Erkläre in 2-3 Sätzen den fundamentalen Unterschied zwischen:
   - **Symbolischer KI** (regelbasiert) und **Machine Learning**
   - **Machine Learning** (klassisch) und **Deep Learning**

c) Nenne zwei konkrete Gründe, warum regelbasierte Expertensysteme in den 1980er Jahren scheiterten.

**Hinweise**:
- Orientiere dich an den im Skript genannten Meilensteinen
- Überlege, was das jeweilige Paradigma ausmacht (manuell vs. datengetrieben, Feature Engineering vs. automatisches Lernen)
- Denke an die Grenzen expliziter Regeln bei komplexen Problemen

---

### Aufgabe T2: Transformer-Architektur und Attention-Mechanismus (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 15-20 Minuten

Der **Self-Attention-Mechanismus** ist der Kern der Transformer-Architektur und ermöglicht es LLMs, kontextuelle Beziehungen zwischen Wörtern zu erfassen.

**Aufgabenstellung**:

a) Gegeben ist der Satz: **"Die Bank war geschlossen, weil Feiertag war."**

Erkläre, wie Self-Attention dabei hilft, die korrekte Bedeutung von "Bank" (Geldinstitut vs. Sitzgelegenheit) zu ermitteln. Welche anderen Wörter im Satz würden hohe Attention-Gewichte für "Bank" erhalten?

b) Der Attention-Mechanismus berechnet für jedes Token drei Vektoren: **Query (Q)**, **Key (K)** und **Value (V)**.

Beschreibe in eigenen Worten:
   - Was repräsentiert der Query-Vektor?
   - Was repräsentiert der Key-Vektor?
   - Was repräsentiert der Value-Vektor?
   - Wie werden diese Vektoren mathematisch kombiniert?

c) **Multi-Head Attention** verwendet mehrere Attention-Köpfe parallel. Welchen Vorteil bietet dies gegenüber einem einzelnen Attention-Kopf? Nenne ein konkretes Beispiel, was verschiedene Köpfe fokussieren könnten.

d) Vergleiche Transformer mit RNNs/LSTMs bezüglich:
   - **Parallelisierbarkeit beim Training**
   - **Umgang mit langreichweitigen Abhängigkeiten**
   - **Rechenaufwand**

**Hinweise**:
- Stelle dir vor, du erklärst Self-Attention jemandem ohne mathematischen Hintergrund
- Visualisiere mental, wie Attention-Gewichte als Heatmap über den Satz gelegt würden
- Multi-Head Attention = "mehrere Perspektiven gleichzeitig"

---

### Aufgabe T3: LLM-Problematiken – Halluzinationen und Bias (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 20-30 Minuten

Large Language Models weisen trotz beeindruckender Fähigkeiten signifikante Schwächen auf, die bei ihrer Nutzung kritisch berücksichtigt werden müssen.

**Aufgabenstellung**:

a) **Halluzinationen**:

Erkläre, warum LLMs halluzinieren (falsche, aber plausibel klingende Informationen generieren). Gehe dabei auf folgende Punkte ein:
   - Wie funktioniert die Textgenerierung auf technischer Ebene?
   - Warum führt das statistische Prinzip zu Halluzinationen?
   - Was bedeutet "das Modell weiß nicht, dass es nicht weiß"?

Nenne drei konkrete Gegenmaßnahmen gegen Halluzinationen und erkläre ihre Wirkungsweise.

b) **Bias in LLMs**:

Analysiere folgendes Szenario:

Ein Unternehmen setzt ein LLM-basiertes System für die Vorauswahl von Bewerbungen ein. Das System wurde auf historischen Bewerbungsdaten trainiert, bei denen bestimmte Abteilungen traditionell männlich dominiert waren.

   i) Erkläre, welche Arten von Bias in diesem Szenario auftreten können.
   
   ii) Beschreibe den Mechanismus, wie Bias aus Trainingsdaten ins Modell gelangt.
   
   iii) Diskutiere ethische und rechtliche Implikationen (Stichworte: Diskriminierung, Gleichbehandlung, Datenschutz).
   
   iv) Schlage konkrete Maßnahmen vor, um Bias zu reduzieren – sowohl auf Datenebene als auch auf Modellebene.

c) **Kritische Reflexion**:

Ein Unternehmen möchte ein LLM für folgende Anwendungsfälle einsetzen. Bewerte für jeden Fall das Risiko (niedrig/mittel/hoch) und begründe deine Einschätzung:

   - **Marketing-Texte** für Social Media generieren
   - **Medizinische Diagnose-Unterstützung** für Ärzte
   - **Code-Review-Kommentare** für Software-Entwickler
   - **Automatisierte Kreditwürdigkeitsprüfung**
   - **Zusammenfassung wissenschaftlicher Paper**

Nenne für jeden Hochrisiko-Fall spezifische Schutzmaßnahmen.

**Hinweise**:
- Denke über die Konsequenzen falscher Ausgaben nach (z.B. gesundheitliche Folgen vs. Marketing-Fehler)
- Bias ist nicht nur technisch, sondern auch ein gesellschaftliches Problem
- Regulatorische Aspekte: EU AI Act, DSGVO
- Kombination von technischen und organisatorischen Maßnahmen

---

## Teil B: Python-Aufgaben

### Aufgabe P1: CNC-Maschinen-Log-Formatter mit Keyword-Only Arguments (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 15 Minuten  
**Vorkenntnisse**: Funktionen (V10), Keyword Arguments, Keyword-Only Arguments (V11)  
**Maschinenbau-Kontext**: Maschinendaten-Logging für Produktionsüberwachung und Wartung

Implementiere eine Funktion zur Formatierung von CNC-Maschinen-Logs mit Prioritätsstufen und Kontext-Informationen.

> [!NOTE]
> **Maschinen-Logging**: In der Fertigung werden alle Maschinenereignisse protokolliert:
> - **OPERATING**: Normalbetrieb (Drehzahl, Vorschub, Werkzeugwechsel)
> - **WARNING**: Abweichungen (Vibration erhöht, Temperatur hoch)
> - **ALARM**: Kritische Zustände (Werkzeugbruch, Achsfehler)
> - **ERROR**: Maschinenstillstand erforderlich
> 
> Logs werden für Predictive Maintenance, Qualitätssicherung und Fehleranalyse verwendet.

**Aufgabenstellung**:

Erstelle eine Funktion `cnc_log_eintrag`, die:
- Einen verpflichtenden Parameter `ereignis` (String) akzeptiert
- Folgende Keyword-Only Parameter hat:
  - `prioritaet` (String): Log-Priorität mit Default `"OPERATING"` (mögliche Werte: `"OPERATING"`, `"WARNING"`, `"ALARM"`, `"ERROR"`)
  - `zeitstempel` (bool): Ob ein Zeitstempel angefügt wird (Default: `True`)
  - `maschine_id` (String): Optionale Maschinen-ID (Default: `""`)
  - `achse` (String): Optionale Achsen-Info (Default: `""`)
- Einen formatierten CNC-Log-Eintrag zurückgibt

**Format der Ausgabe**:
```
[PRIORITÄT] [Zeitstempel] [Maschine-ID] [Achse]: Ereignis
```

**Beispiel Ein-/Ausgabe**:
```python
cnc_log_eintrag("Spindeldrehzahl 3000 U/min erreicht")
# "[OPERATING] [2026-01-04 10:45:23] Spindeldrehzahl 3000 U/min erreicht"

cnc_log_eintrag("Vibration erhöht", prioritaet="WARNING", zeitstempel=False, maschine_id="CNC-01", achse="Z")
# "[WARNING] [CNC-01] [Z-Achse]: Vibration erhöht"

cnc_log_eintrag("Werkzeugbruch erkannt", prioritaet="ALARM", maschine_id="CNC-03")
# "[ALARM] [2026-01-04 10:46:15] [CNC-03]: Werkzeugbruch erkannt"
```

**Starter-Code**:
```python
from datetime import datetime

def cnc_log_eintrag(ereignis, *, prioritaet="OPERATING", zeitstempel=True, maschine_id="", achse=""):
    """
    Formatiert einen CNC-Maschinen-Log-Eintrag mit Priorität und Kontext.
    
    Args:
        ereignis (str): Beschreibung des Maschinenereignisses
        prioritaet (str): Prioritätsstufe (OPERATING, WARNING, ALARM, ERROR)
        zeitstempel (bool): Ob Zeitstempel hinzugefügt werden soll
        maschine_id (str): Optionale Maschinen-Identifikation
        achse (str): Optionale Achsen-Information (X, Y, Z, A, B, C)
    
    Returns:
        str: Formatierter CNC-Log-Eintrag
    """
    # Dein Code hier
    pass

# Tests
print(cnc_log_eintrag("Spindeldrehzahl 3000 U/min erreicht"))
print(cnc_log_eintrag("Vibration erhöht", prioritaet="WARNING", zeitstempel=False, maschine_id="CNC-01", achse="Z"))
print(cnc_log_eintrag("Werkzeugbruch erkannt", prioritaet="ALARM", maschine_id="CNC-03"))
```

---

### Aufgabe P2: Messwert-Statistik für Sensor-Arrays mit `*args` und `**kwargs` (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 20 Minuten  
**Vorkenntnisse**: `*args`, `**kwargs`, String-Formatierung (V02, V11)  
**Maschinenbau-Kontext**: Sensor-Datenauswertung für Qualitätskontrolle und Prozessüberwachung

Erstelle eine flexible Funktion zur Berechnung statistischer Kennzahlen für Sensor-Messwerte.

> [!NOTE]
> **Sensor-Statistik**: In der Produktion werden Sensordaten kontinuierlich erfasst:
> - **Temperatur-Sensoren**: Überwachung von Werkzeug- und Werkstücktemperatur
> - **Vibrations-Sensoren**: Erkennung von Lagerschäden und Unwuchten
> - **Kraft-Sensoren**: Prozessüberwachung bei Umformung und Zerspanung
> 
> Statistische Auswertung ermöglicht Prozessoptimierung und Früherkennung von Abweichungen.

**Aufgabenstellung**:

Implementiere eine Funktion `sensor_statistik`, die:
- Eine beliebige Anzahl numerischer Messwerte über `*args` akzeptiert
- Über `**kwargs` verschiedene Optionen steuert:
  - `mittelwert` (bool, Default: `True`): Berechne arithmetisches Mittel
  - `median` (bool, Default: `False`): Berechne Median
  - `minimum` (bool, Default: `False`): Finde Minimum
  - `maximum` (bool, Default: `False`): Finde Maximum
  - `runden` (int, Default: `2`): Anzahl Dezimalstellen
  - `einheit` (str, Default: `""`): Optionale Einheit für Ausgabe
- Ein Dictionary mit den berechneten Kennzahlen zurückgibt

**Beispiel Ein-/Ausgabe**:
```python
# Temperatur-Messwerte in °C
sensor_statistik(45.2, 46.8, 44.9, 47.1, 45.5, einheit="°C")
# {'mittelwert': '45.90°C'}

# Vibrations-Messwerte in mm/s mit Median und Maximum
sensor_statistik(2.1, 3.5, 2.8, 4.2, 3.1, median=True, maximum=True, runden=1, einheit="mm/s")
# {'mittelwert': '3.1mm/s', 'median': '3.1mm/s', 'maximum': '4.2mm/s'}

# Kraft-Messwerte in kN ohne Mittelwert
sensor_statistik(12.5, 15.3, 11.8, 14.9, 13.2, mittelwert=False, minimum=True, maximum=True, runden=0, einheit="kN")
# {'minimum': '12kN', 'maximum': '15kN'}
```

**Starter-Code**:
```python
def sensor_statistik(*messwerte, mittelwert=True, median=False, minimum=False, maximum=False, runden=2, einheit=""):
    """
    Berechnet statistische Kennzahlen für Sensor-Messwerte.
    
    Args:
        *messwerte: Variable Anzahl numerischer Messwerte
        mittelwert (bool): Berechne arithmetisches Mittel
        median (bool): Berechne Median
        minimum (bool): Finde Minimum
        maximum (bool): Finde Maximum
        runden (int): Anzahl Dezimalstellen
        einheit (str): Optionale Einheit (z.B. "°C", "mm/s", "kN")
    
    Returns:
        dict: Dictionary mit berechneten Kennzahlen inkl. Einheit
    """
    # Dein Code hier
    pass

# Tests
print(sensor_statistik(45.2, 46.8, 44.9, 47.1, 45.5, einheit="°C"))
print(sensor_statistik(2.1, 3.5, 2.8, 4.2, 3.1, median=True, maximum=True, runden=1, einheit="mm/s"))
print(sensor_statistik(12.5, 15.3, 11.8, 14.9, 13.2, mittelwert=False, minimum=True, maximum=True, runden=0, einheit="kN"))
```

**Hinweise**:
- Für Median: Sortiere die Werte, bei ungerader Länge nimm das mittlere Element, bei gerader Länge den Durchschnitt der beiden mittleren
- Nutze `round()` zum Runden der Ergebnisse
- Formatiere Ausgabe mit Einheit: `f"{wert}{einheit}"`

---

### Aufgabe P3: Lambda-Funktionen für Werkstoff-Datenbankfilterung (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25 Minuten  
**Vorkenntnisse**: Lambda-Funktionen, `map()`, `filter()`, List Comprehensions (V07, V11)  
**Maschinenbau-Kontext**: Werkstoffdatenbank-Filterung für Bauteilauswahl

Verarbeite Werkstoff-Bezeichnungen mit Lambda-Funktionen und funktionaler Programmierung.

> [!NOTE]
> **Werkstoff-Bezeichnungen**: In der Konstruktion werden Werkstoffe nach DIN/EN-Normen benannt:
> - **Stahl**: z.B. "S235JR", "C45E", "X5CrNi18-10"
> - **Aluminium**: z.B. "AlMgSi1_T6", "AlCu4Mg1"
> - **Kupfer**: z.B. "CuZn37_2.0321"
> 
> Filterung ermöglicht schnelle Werkstoffauswahl nach Kriterien wie Festigkeit, Korrosionsbeständigkeit, Schweißbarkeit.

**Aufgabenstellung**:

Gegeben ist eine Liste von Werkstoff-Bezeichnungen:
```python
werkstoffe = ["S235JR", "c45e", "AlMgSi1_T6", "X5CRNI18-10", "AlCu4Mg1", "s355j2", "CuZn37_2.0321"]
```

Implementiere folgende Transformationen mit Lambda-Funktionen und `map()`/`filter()`:

a) **Normalisierung**: Alle Bezeichnungen in Großbuchstaben konvertieren

b) **Filtern**: Nur Stahl-Werkstoffe behalten (beginnen mit "S", "C" oder "X")

c) **Bereinigung**: Bindestriche entfernen und Unterstriche durch Leerzeichen ersetzen

d) **Validierung**: Nur Werkstoffe mit mindestens 4 Zeichen (nach Bereinigung) behalten

e) **Sortierung**: Alphabetisch sortieren

f) **Bonus**: Implementiere dieselben Operationen als **eine** List Comprehension

**Beispiel Ein-/Ausgabe**:
```python
# Nach allen Transformationen:
["C45E", "S235JR", "S355J2", "X5CRNI1810"]
```

**Starter-Code**:
```python
werkstoffe = ["S235JR", "c45e", "AlMgSi1_T6", "X5CRNI18-10", "AlCu4Mg1", "s355j2", "CuZn37_2.0321"]

# a) Normalisierung
normalisiert = list(map(lambda x: ..., werkstoffe))
print(f"Normalisiert: {normalisiert}")

# b) Filtern nach Stahl (S, C, X am Anfang)
stahl = list(filter(lambda x: ..., normalisiert))
print(f"Nur Stahl: {stahl}")

# c) Bereinigung
def bereinige(bezeichnung):
    """Entfernt Bindestriche und ersetzt Unterstriche."""
    # Dein Code hier
    pass

bereinigt = list(map(bereinige, stahl))
print(f"Bereinigt: {bereinigt}")

# d) Validierung (mind. 4 Zeichen)
validiert = list(filter(lambda x: ..., bereinigt))
print(f"Validiert: {validiert}")

# e) Sortierung alphabetisch
sortiert = sorted(validiert, key=lambda x: ...)
print(f"Sortiert: {sortiert}")

# f) Bonus: Als eine List Comprehension
ergebnis = [...]
print(f"List Comprehension: {ergebnis}")
```

**Hinweise**:
- Stahl-Werkstoffe beginnen mit S (Baustahl), C (Kohlenstoffstahl) oder X (hochlegiert)
- `.replace()` für Bereinigung
- Verwende `x[0]` oder `x.startswith()` für Präfix-Check

---

### Aufgabe P4: CAD-Dokumentations-Generator mit LLM-API (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 35-40 Minuten  
**Vorkenntnisse**: Alle Funktionskonzepte (V10-V11), Docstrings, Type Hints, Fehlerbehandlung (V09)  
**Maschinenbau-Kontext**: Automatische Generierung von CAD-Bauteil-Dokumentationen mit LLM

Implementiere einen erweiterten API-Wrapper für LLM-gestützte CAD-Dokumentation mit umfassender Validierung.

> [!NOTE]
> **LLM für CAD/CAM**: Large Language Models werden in der Konstruktion eingesetzt für:
> - **Technische Dokumentation**: Automatische Beschreibung von CAD-Bauteilen
> - **Fertigungsanweisungen**: Generierung von NC-Programm-Kommentaren
> - **Spezifikationen**: Ableitung von Anforderungen aus Skizzen/Zeichnungen
> - **Wartungsanleitungen**: Erstellen von Service-Dokumenten
> 
> API-Wrapper vereinfachen LLM-Integration und gewährleisten Datenvalidierung.

**Aufgabenstellung**:

Erstelle ein Modul mit folgenden Funktionen:

**Teil 1**: Funktion `validiere_bauteil_beschreibung(beschreibung, *, min_laenge=20, max_laenge=2000)`

Diese Funktion soll CAD-Bauteil-Beschreibungen validieren:
- Beschreibung ist nicht leer nach `strip()`
- Länge liegt zwischen `min_laenge` und `max_laenge`
- Wirft `ValueError` mit aussagekräftiger Fehlermeldung bei Verletzung

**Teil 2**: Funktion `llm_cad_dokumentation(bauteil_beschreibung, **einstellungen)`

Diese Funktion soll:
- `bauteil_beschreibung` validieren (nutze `validiere_bauteil_beschreibung`)
- Standard-Einstellungen definieren für:
  - `modell`: `"gpt-4-turbo"`
  - `temperatur`: `0.3` (niedrig für technische Präzision)
  - `max_tokens`: `800`
  - `dokumentations_typ`: `"technisch"` (Optionen: "technisch", "wartung", "fertigung")
- Einstellungen mit `**einstellungen` überschreibbar machen
- Temperatur validieren (muss zwischen 0.0 und 1.0 liegen für technische Texte)
- `max_tokens` validieren (muss positiv sein, max. 2000)
- `dokumentations_typ` validieren (nur erlaubte Werte)
- Ein Dictionary mit Request-Details und simulierter Dokumentation zurückgeben

**Teil 3**: Funktion `llm_batch_bauteile(bauteil_beschreibungen, **gemeinsame_einstellungen)`

Diese Funktion soll:
- Eine Liste von Bauteil-Beschreibungen verarbeiten
- Für jede Beschreibung `llm_cad_dokumentation` aufrufen
- Fehlerhafte Eingaben überspringen (mit Warnung), statt gesamte Batch abzubrechen
- Liste von Ergebnissen zurückgeben

**Anforderungen**:
- Vollständige Docstrings (Google Style) für alle Funktionen
- Type Hints für alle Parameter und Rückgabewerte
- `try-except`-Fehlerbehandlung in Batch-Funktion
- Validierung mit aussagekräftigen Fehlermeldungen

**Beispiel Ein-/Ausgabe**:
```python
# Einzelne Anfrage
ergebnis = llm_cad_dokumentation(
    "Welle Ø50mm, Länge 200mm, Material C45E, mit Passfedernut DIN 6885",
    temperatur=0.2,
    max_tokens=500,
    dokumentations_typ="technisch"
)
print(ergebnis)
# {
#   "bauteil_beschreibung": "Welle Ø50mm...",
#   "einstellungen": {"modell": "gpt-4-turbo", "temperatur": 0.2, ...},
#   "dokumentation": "[Simulierte technische Dokumentation...]",
#   "status": "success"
# }

# Batch-Anfragen
bauteile = [
    "Gehäuse aus AlMgSi1, Wandstärke 3mm",
    "",  # Ungültig
    "Zahnrad Modul 2, z=30, Material 16MnCr5"
]
ergebnisse = llm_batch_bauteile(bauteile, temperatur=0.25, dokumentations_typ="fertigung")
# [
#   {"bauteil_beschreibung": "Gehäuse...", "status": "success", ...},
#   {"bauteil_beschreibung": "", "status": "error", "fehler": "Beschreibung ist leer"},
#   {"bauteil_beschreibung": "Zahnrad...", "status": "success", ...}
# ]
```

**Starter-Code**:
```python
from typing import Optional

def validiere_bauteil_beschreibung(beschreibung: str, *, min_laenge: int = 20, max_laenge: int = 2000) -> None:
    """
    Validiert eine CAD-Bauteil-Beschreibung auf Länge und Inhalt.
    
    Args:
        beschreibung: Zu validierende Bauteil-Beschreibung
        min_laenge: Minimale Beschreibungs-Länge
        max_laenge: Maximale Beschreibungs-Länge
    
    Raises:
        ValueError: Bei ungültiger Beschreibung
    
    Examples:
        >>> validiere_bauteil_beschreibung("Welle Ø50mm Material C45E")  # OK
        >>> validiere_bauteil_beschreibung("")  # ValueError
        >>> validiere_bauteil_beschreibung("Kurz")  # ValueError
    """
    # Dein Code hier
    pass


def llm_cad_dokumentation(bauteil_beschreibung: str, **einstellungen) -> dict:
    """
    Generiert CAD-Dokumentation mit LLM (simuliert).
    
    Args:
        bauteil_beschreibung: Technische Beschreibung des Bauteils
        **einstellungen: Optionale Einstellungen (modell, temperatur, max_tokens, dokumentations_typ)
    
    Returns:
        Dictionary mit Request-Details und simulierter Dokumentation
    
    Raises:
        ValueError: Bei ungültigen Parametern
    
    Examples:
        >>> ergebnis = llm_cad_dokumentation("Welle Ø50mm C45E", temperatur=0.2)
        >>> print(ergebnis["status"])
        success
    """
    # Dein Code hier
    pass


def llm_batch_bauteile(bauteil_beschreibungen: list[str], **gemeinsame_einstellungen) -> list[dict]:
    """
    Verarbeitet mehrere Bauteil-Beschreibungen als Batch.
    
    Args:
        bauteil_beschreibungen: Liste von Bauteil-Beschreibungen
        **gemeinsame_einstellungen: Einstellungen für alle Anfragen
    
    Returns:
        Liste von Ergebnis-Dictionaries
    
    Examples:
        >>> bauteile = ["Welle Ø50mm", "Gehäuse AlMgSi1"]
        >>> ergebnisse = llm_batch_bauteile(bauteile, temperatur=0.2)
        >>> len(ergebnisse)
        2
    """
    # Dein Code hier
    pass


# Tests
if __name__ == "__main__":
    # Test 1: Einzelne Anfrage
    print("Test 1: Einzelne CAD-Dokumentation")
    ergebnis = llm_cad_dokumentation(
        "Welle Ø50mm, Länge 200mm, Material C45E, mit Passfedernut DIN 6885",
        temperatur=0.2,
        max_tokens=500
    )
    print(ergebnis)
    
    # Test 2: Ungültige Parameter
    print("\nTest 2: Ungültige Parameter")
    try:
        llm_cad_dokumentation("Welle Ø50mm", temperatur=1.5)  # Sollte Fehler werfen
    except ValueError as e:
        print(f"Erwarteter Fehler: {e}")
    
    # Test 3: Batch-Anfragen
    print("\nTest 3: Batch-Verarbeitung")
    bauteile = [
        "Gehäuse aus AlMgSi1, Wandstärke 3mm, Oberflächenschutz eloxiert",
        "",  # Ungültig
        "Zahnrad Modul 2, z=30, Material 16MnCr5, Härte 58-62 HRC",
        "X" * 2500  # Zu lang
    ]
    ergebnisse = llm_batch_bauteile(bauteile, temperatur=0.25, dokumentations_typ="fertigung")
    for idx, erg in enumerate(ergebnisse):
        print(f"Ergebnis {idx + 1}: {erg.get('status', 'unknown')}")
```

**Hinweise**:
- Technische Dokumentation erfordert niedrige Temperatur (0.2-0.4) für Präzision
- Validierung verhindert ungültige API-Aufrufe und Kosten
- `try-except` in Batch-Funktion: Fange `ValueError` ab und erzeuge Fehler-Dictionary
- Simulierte Antwort: Generiere Platzhalter-Text für Dokumentation
  - `modell`: `"gpt-3.5-turbo"`
  - `temperatur`: `0.7`
  - `max_tokens`: `500`
  - `top_p`: `1.0`
- Einstellungen mit `**einstellungen` überschreibbar machen
- Temperatur validieren (muss zwischen 0.0 und 2.0 liegen)
- `max_tokens` validieren (muss positiv sein)
- Ein Dictionary mit Request-Details und simulierter Antwort zurückgeben

**Teil 3**: Funktion `llm_batch_anfragen(prompts, **gemeinsame_einstellungen)`

Diese Funktion soll:
- Eine Liste von Prompts verarbeiten
- Für jeden Prompt `llm_textgenerierung` aufrufen
- Fehlerhafte Prompts überspringen (mit Warnung), statt gesamte Batch abzubrechen
- Liste von Ergebnissen zurückgeben

**Anforderungen**:
- Vollständige Docstrings (Google Style) für alle Funktionen
- Type Hints für alle Parameter und Rückgabewerte
- `try-except`-Fehlerbehandlung in Batch-Funktion
- Validierung mit aussagekräftigen Fehlermeldungen

**Beispiel Ein-/Ausgabe**:
```python
# Einzelne Anfrage
ergebnis = llm_textgenerierung("Erkläre neuronale Netze", temperatur=0.5, max_tokens=200)
print(ergebnis)
# {
#   "prompt": "Erkläre neuronale Netze",
#   "einstellungen": {"modell": "gpt-3.5-turbo", "temperatur": 0.5, ...},
#   "antwort": "[Simulierte Antwort...]",
#   "status": "success"
# }

# Batch-Anfragen
prompts = [
    "Was sind Transformer?",
    "",  # Ungültig
    "Erkläre GPT-3"
]
ergebnisse = llm_batch_anfragen(prompts, temperatur=0.3)
# [
#   {"prompt": "Was sind Transformer?", ...},
#   {"prompt": "", "status": "error", "fehler": "Prompt ist leer"},
#   {"prompt": "Erkläre GPT-3", ...}
# ]
```

**Starter-Code**:
```python
from typing import Optional

def validiere_prompt(prompt: str, *, min_laenge: int = 10, max_laenge: int = 5000) -> None:
    """
    Validiert einen LLM-Prompt auf Länge und Inhalt.
    
    Args:
        prompt: Zu validierender Prompt
        min_laenge: Minimale Prompt-Länge
        max_laenge: Maximale Prompt-Länge
    
    Raises:
        ValueError: Bei ungültigem Prompt
    
    Examples:
        >>> validiere_prompt("Hallo Welt!")  # OK
        >>> validiere_prompt("")  # ValueError: Prompt ist leer
        >>> validiere_prompt("Kurz")  # ValueError: Prompt zu kurz
    """
    # Dein Code hier
    pass


def llm_textgenerierung(prompt: str, **einstellungen) -> dict:
    """
    Sendet eine Textgenerierungs-Anfrage an ein LLM (simuliert).
    
    Args:
        prompt: Eingabetext für das LLM
        **einstellungen: Optionale Einstellungen (modell, temperatur, max_tokens, top_p)
    
    Returns:
        Dictionary mit Request-Details und simulierter Antwort
    
    Raises:
        ValueError: Bei ungültigen Parametern
    
    Examples:
        >>> ergebnis = llm_textgenerierung("Erkläre KI", temperatur=0.5)
        >>> print(ergebnis["status"])
        success
    """
    # Dein Code hier
    pass


def llm_batch_anfragen(prompts: list[str], **gemeinsame_einstellungen) -> list[dict]:
    """
    Verarbeitet mehrere Prompts als Batch.
    
    Args:
        prompts: Liste von Prompts
        **gemeinsame_einstellungen: Einstellungen für alle Anfragen
    
    Returns:
        Liste von Ergebnis-Dictionaries
    
    Examples:
        >>> prompts = ["Erkläre ML", "Erkläre DL"]
        >>> ergebnisse = llm_batch_anfragen(prompts, temperatur=0.3)
        >>> len(ergebnisse)
        2
    """
    # Dein Code hier
    pass


# Tests
if __name__ == "__main__":
    # Test 1: Einzelne Anfrage
    print("Test 1: Einzelne Anfrage")
    ergebnis = llm_textgenerierung("Erkläre neuronale Netze", temperatur=0.5, max_tokens=200)
    print(ergebnis)
    
    # Test 2: Ungültige Parameter
    print("\nTest 2: Ungültige Parameter")
    try:
        llm_textgenerierung("Test", temperatur=3.0)  # Sollte Fehler werfen
    except ValueError as e:
        print(f"Erwarteter Fehler: {e}")
    
    # Test 3: Batch-Anfragen
    print("\nTest 3: Batch-Anfragen")
    prompts = [
        "Was sind Transformer?",
        "",  # Ungültig
        "Erkläre GPT-3",
        "A" * 6000  # Zu lang
    ]
    ergebnisse = llm_batch_anfragen(prompts, temperatur=0.3)
    for idx, erg in enumerate(ergebnisse):
        print(f"Ergebnis {idx + 1}: {erg.get('status', 'unknown')}")
```

---

### Aufgabe P5: Wartungsprotokoll-Manager mit LLM-Unterstützung (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 50-60 Minuten  
**Vorkenntnisse**: Alle Konzepte aus V01-V11, insbesondere Funktionen, Fehlerbehandlung, Datenstrukturen  
**Maschinenbau-Kontext**: Digitales Wartungsprotokoll-System mit LLM-gestützter Fehleranalyse

Implementiere einen vollständigen Manager für Maschinenwartungs-Protokolle mit LLM-Integration und Persistenz.

> [!NOTE]
> **Digitale Wartungsprotokolle**: Moderne Instandhaltung nutzt digitale Systeme für:
> - **Protokollierung**: Erfassung aller Wartungsmaßnahmen mit Zeitstempel
> - **Fehleranalyse**: LLM-gestützte Diagnose basierend auf Symptombeschreibungen
> - **Wissensmanagement**: Historische Daten für Predictive Maintenance
> - **Dokumentation**: Nachweisführung für ISO 9001, Maschinensicherheit
> 
> Systematische Protokollierung reduziert Ausfallzeiten und verbessert Anlagenverfügbarkeit.

**Aufgabenstellung**:

Erstelle ein System zur Verwaltung von Wartungsprotokollen mit folgenden Komponenten:

**Protokoll-Eintrag** (nutze Dictionary):
- Attribute: `typ` (str: "inspektion", "reparatur", "diagnose"), `beschreibung` (str), `maschine_id` (str), `zeitstempel` (datetime)

**Funktion `erstelle_wartungsprotokoll(maschine_id, system_prompt, **optionen)`**:
- Initialisiert neues Wartungsprotokoll für Maschine
- `maschine_id`: Eindeutige Maschinen-Identifikation
- `system_prompt`: LLM-Kontext für Fehleranalyse
- Gibt Protokoll-Dictionary zurück

**Funktion `fuege_eintrag_hinzu(protokoll, typ, beschreibung)`**:
- Fügt Wartungseintrag zum Protokoll hinzu
- Validiert `typ` (nur "inspektion", "reparatur", "diagnose" erlaubt)
- Aktualisiert Statistiken

**Funktion `llm_fehleranalyse(protokoll, symptombeschreibung, **llm_einstellungen)`**:
- Fügt Diagnose-Eintrag hinzu
- Simuliert LLM-Fehleranalyse basierend auf Symptomen
- Gibt Diagnose-Empfehlung zurück

**Funktion `speichere_protokoll(protokoll, dateiname)`**:
- Speichert Wartungsprotokoll als JSON-Datei

**Funktion `lade_protokoll(dateiname)`**:
- Lädt Wartungsprotokoll aus JSON-Datei

**Funktion `protokoll_statistik(protokoll)`**:
- Berechnet Statistiken: Anzahl Einträge pro Typ, durchschnittliche Beschreibungslänge

**Beispiel Ein-/Ausgabe**:
```python
# Neues Wartungsprotokoll
protokoll = erstelle_wartungsprotokoll(
    maschine_id="CNC-DMU-85",
    system_prompt="Experte für CNC-Maschinen-Diagnose und Wartung",
    modell="gpt-4"
)

# Einträge hinzufügen
fuege_eintrag_hinzu(protokoll, "inspektion", "Spindellager geprüft, kein Verschleiß erkennbar")
fuege_eintrag_hinzu(protokoll, "reparatur", "Kühlmittelpumpe ausgetauscht, Leckage behoben")

# LLM-Fehleranalyse
diagnose = llm_fehleranalyse(
    protokoll,
    "Erhöhte Vibration bei 3000 U/min in Z-Achse, sporadische Positionsfehler",
    temperatur=0.2
)
print(f"Diagnose: {diagnose}")

# Statistiken
stats = protokoll_statistik(protokoll)
print(f"Einträge gesamt: {stats['anzahl_eintraege']}")
print(f"Inspektionen: {stats['anzahl_inspektion']}, Reparaturen: {stats['anzahl_reparatur']}")

# Persistenz
speichere_protokoll(protokoll, "wartung_CNC-DMU-85_2026-01.json")
```

**Starter-Code**:
```python
from datetime import datetime
from typing import Optional
import json

def erstelle_wartungsprotokoll(maschine_id: str, system_prompt: Optional[str] = None, **optionen) -> dict:
    """Initialisiert ein neues Wartungsprotokoll."""
    protokoll = {
        "maschine_id": maschine_id,
        "erstellt_am": datetime.now().isoformat(),
        "system_prompt": system_prompt,
        "optionen": optionen,
        "eintraege": [],
        "statistiken": {
            "anzahl_eintraege": 0,
            "anzahl_inspektion": 0,
            "anzahl_reparatur": 0,
            "anzahl_diagnose": 0
        }
    }
    return protokoll

def fuege_eintrag_hinzu(protokoll: dict, typ: str, beschreibung: str) -> None:
    """Fügt Wartungseintrag hinzu."""
    # Dein Code hier
    pass

def llm_fehleranalyse(protokoll: dict, symptombeschreibung: str, **llm_einstellungen) -> str:
    """Generiert LLM-gestützte Fehleranalyse."""
    # Dein Code hier
    pass

def speichere_protokoll(protokoll: dict, dateiname: str) -> None:
    """Speichert Protokoll als JSON."""
    # Dein Code hier
    pass

def lade_protokoll(dateiname: str) -> dict:
    """Lädt Protokoll aus JSON."""
    # Dein Code hier
    pass

def protokoll_statistik(protokoll: dict) -> dict:
    """Berechnet Protokoll-Statistiken."""
    # Dein Code hier
    pass

# Tests
if __name__ == "__main__":
    protokoll = erstelle_wartungsprotokoll(
        maschine_id="CNC-DMU-85",
        system_prompt="Experte für CNC-Diagnose",
        modell="gpt-4"
    )
    
    fuege_eintrag_hinzu(protokoll, "inspektion", "Spindellager OK")
    fuege_eintrag_hinzu(protokoll, "reparatur", "Kühlmittelpumpe ersetzt")
    
    diagnose = llm_fehleranalyse(protokoll, "Erhöhte Vibration bei 3000 U/min", temperatur=0.2)
    print(f"Diagnose: {diagnose[:100]}...")
    
    stats = protokoll_statistik(protokoll)
    print(f"Statistiken: {stats}")
    
    speichere_protokoll(protokoll, "test_wartung.json")
```

**Hinweise**:
- Zeitstempel mit `datetime.now().isoformat()`
- Simulierte Diagnose: Template basierend auf Symptomen
- Validierung: `ValueError` bei ungültigem Typ
- JSON-Kompatibilität beachten

---


