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

### Aufgabe P1: Keyword-Only Arguments und flexible Parameter (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 15 Minuten  
**Vorkenntnisse**: Funktionen (V10), Keyword Arguments, Keyword-Only Arguments (V11)

Implementiere eine Funktion zur Formatierung von Log-Nachrichten mit verschiedenen Stufen und Optionen.

**Aufgabenstellung**:

Erstelle eine Funktion `log_nachricht`, die:
- Einen verpflichtenden Parameter `nachricht` (String) akzeptiert
- Folgende Keyword-Only Parameter hat:
  - `level` (String): Log-Level mit Default `"INFO"` (mögliche Werte: `"DEBUG"`, `"INFO"`, `"WARNING"`, `"ERROR"`)
  - `timestamp` (bool): Ob ein Zeitstempel angehängt wird (Default: `True`)
  - `prefix` (String): Optionaler Präfix (Default: `""`)
- Eine formatierte Log-Nachricht zurückgibt

**Format der Ausgabe**:
```
[LEVEL] [Zeitstempel] Präfix: Nachricht
```

**Beispiel Ein-/Ausgabe**:
```python
log_nachricht("Server gestartet")
# "[INFO] [2026-01-02 15:30:45] Server gestartet"

log_nachricht("Debug-Info", level="DEBUG", timestamp=False, prefix="[Modul-X]")
# "[DEBUG] [Modul-X]: Debug-Info"

log_nachricht("Kritischer Fehler", level="ERROR", prefix="[Database]")
# "[ERROR] [2026-01-02 15:31:10] [Database]: Kritischer Fehler"
```

**Starter-Code**:
```python
from datetime import datetime

def log_nachricht(nachricht, *, level="INFO", timestamp=True, prefix=""):
    """
    Formatiert eine Log-Nachricht mit Level, Zeitstempel und Präfix.
    
    Args:
        nachricht (str): Die Log-Nachricht
        level (str): Log-Level (DEBUG, INFO, WARNING, ERROR)
        timestamp (bool): Ob Zeitstempel hinzugefügt werden soll
        prefix (str): Optionaler Präfix für die Nachricht
    
    Returns:
        str: Formatierte Log-Nachricht
    """
    # Dein Code hier
    pass

# Tests
print(log_nachricht("Server gestartet"))
print(log_nachricht("Debug-Info", level="DEBUG", timestamp=False, prefix="[Modul-X]"))
print(log_nachricht("Kritischer Fehler", level="ERROR", prefix="[Database]"))
```

---

### Aufgabe P2: `*args` und `**kwargs` kombinieren (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 20 Minuten  
**Vorkenntnisse**: `*args`, `**kwargs`, String-Formatierung (V02, V11)

Erstelle eine flexible Funktion zur Berechnung statistischer Kennzahlen.

**Aufgabenstellung**:

Implementiere eine Funktion `statistik`, die:
- Eine beliebige Anzahl numerischer Werte über `*args` akzeptiert
- Über `**kwargs` verschiedene Optionen steuert:
  - `mittelwert` (bool, Default: `True`): Berechne arithmetisches Mittel
  - `median` (bool, Default: `False`): Berechne Median
  - `minimum` (bool, Default: `False`): Finde Minimum
  - `maximum` (bool, Default: `False`): Finde Maximum
  - `runden` (int, Default: `2`): Anzahl Dezimalstellen
- Ein Dictionary mit den berechneten Kennzahlen zurückgibt

**Beispiel Ein-/Ausgabe**:
```python
statistik(10, 20, 30, 40, 50)
# {'mittelwert': 30.0}

statistik(10, 20, 30, 40, 50, median=True, maximum=True, runden=1)
# {'mittelwert': 30.0, 'median': 30.0, 'maximum': 50.0}

statistik(15, 23, 8, 42, 19, mittelwert=False, minimum=True, maximum=True, runden=0)
# {'minimum': 8.0, 'maximum': 42.0}
```

**Starter-Code**:
```python
def statistik(*werte, mittelwert=True, median=False, minimum=False, maximum=False, runden=2):
    """
    Berechnet statistische Kennzahlen für eine Menge von Werten.
    
    Args:
        *werte: Variable Anzahl numerischer Werte
        mittelwert (bool): Berechne Mittelwert
        median (bool): Berechne Median
        minimum (bool): Finde Minimum
        maximum (bool): Finde Maximum
        runden (int): Anzahl Dezimalstellen
    
    Returns:
        dict: Dictionary mit berechneten Kennzahlen
    """
    # Dein Code hier
    pass

# Tests
print(statistik(10, 20, 30, 40, 50))
print(statistik(10, 20, 30, 40, 50, median=True, maximum=True, runden=1))
print(statistik(15, 23, 8, 42, 19, mittelwert=False, minimum=True, maximum=True, runden=0))
```

**Hinweise**:
- Für Median: Sortiere die Werte, bei ungerader Länge nimm das mittlere Element, bei gerader Länge den Durchschnitt der beiden mittleren
- Nutze `round()` zum Runden der Ergebnisse

---

### Aufgabe P3: Lambda-Funktionen und `map`/`filter` (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25 Minuten  
**Vorkenntnisse**: Lambda-Funktionen, `map()`, `filter()`, List Comprehensions (V07, V11)

Verarbeite Textdaten mit Lambda-Funktionen und funktionaler Programmierung.

**Aufgabenstellung**:

Gegeben ist eine Liste von Benutzernamen:
```python
benutzernamen = ["alice_123", "Bob", "charlie_admin", "DIANA_99", "eve", "Frank_USER"]
```

Implementiere folgende Transformationen mit Lambda-Funktionen und `map()`/`filter()`:

a) **Normalisierung**: Alle Benutzernamen in Kleinbuchstaben konvertieren

b) **Filtern**: Nur Benutzernamen mit Unterstrichen (`_`) behalten

c) **Bereinigung**: Unterstriche und Zahlen entfernen (z.B. `"alice_123"` → `"alice"`)

d) **Validierung**: Nur Benutzernamen mit mindestens 4 Buchstaben (nach Bereinigung) behalten

e) **Sortierung**: Nach Länge sortieren (kürzeste zuerst)

f) **Bonus**: Implementiere dieselben Operationen als **eine** List Comprehension

**Beispiel Ein-/Ausgabe**:
```python
# Nach allen Transformationen:
["alice", "charlie"]  # oder ["charlie", "alice"] je nach Reihenfolge bei gleicher Länge
```

**Starter-Code**:
```python
benutzernamen = ["alice_123", "Bob", "charlie_admin", "DIANA_99", "eve", "Frank_USER"]

# a) Normalisierung
normalisiert = list(map(lambda x: ..., benutzernamen))
print(f"Normalisiert: {normalisiert}")

# b) Filtern nach Unterstrichen
mit_underscore = list(filter(lambda x: ..., normalisiert))
print(f"Mit Unterstrich: {mit_underscore}")

# c) Bereinigung
def bereinige(name):
    """Entfernt Unterstriche und Zahlen."""
    # Dein Code hier
    pass

bereinigt = list(map(bereinige, mit_underscore))
print(f"Bereinigt: {bereinigt}")

# d) Validierung (mind. 4 Buchstaben)
validiert = list(filter(lambda x: ..., bereinigt))
print(f"Validiert: {validiert}")

# e) Sortierung nach Länge
sortiert = sorted(validiert, key=lambda x: ...)
print(f"Sortiert: {sortiert}")

# f) Bonus: Als eine List Comprehension
ergebnis = [...]
print(f"List Comprehension: {ergebnis}")
```

---

### Aufgabe P4: API-Wrapper mit Docstrings und Type Hints (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 35-40 Minuten  
**Vorkenntnisse**: Alle Funktionskonzepte (V10-V11), Docstrings, Type Hints, Fehlerbehandlung (V09)

Implementiere einen erweiterten API-Wrapper für LLM-Aufrufe mit umfassender Dokumentation und Fehlerbehandlung.

**Aufgabenstellung**:

Erstelle ein Modul mit folgenden Funktionen:

**Teil 1**: Funktion `validiere_prompt(prompt, *, min_laenge=10, max_laenge=5000)`

Diese Funktion soll Prompts validieren und folgendes prüfen:
- Prompt ist nicht leer nach `strip()`
- Prompt-Länge liegt zwischen `min_laenge` und `max_laenge`
- Wirft `ValueError` mit aussagekräftiger Fehlermeldung bei Verletzung

**Teil 2**: Funktion `llm_textgenerierung(prompt, **einstellungen)`

Diese Funktion soll:
- `prompt` validieren (nutze `validiere_prompt`)
- Standard-Einstellungen definieren für:
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

**Hinweise**:
- Validierung ist entscheidend für robuste APIs
- `try-except` in Batch-Funktion: Fange `ValueError` ab und erzeuge Fehler-Dictionary
- Type Hints: Nutze `list[dict]` (Python 3.9+) oder `List[Dict[str, Any]]` (mit `from typing import List, Dict, Any`)

---

### Aufgabe P5: LLM Conversation Manager (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 50-60 Minuten  
**Vorkenntnisse**: Alle Konzepte aus V01-V11, insbesondere Funktionen, Fehlerbehandlung, Datenstrukturen

Implementiere einen vollständigen Konversations-Manager für LLM-Chat-Dialoge mit Persistenz.

**Aufgabenstellung**:

Erstelle ein System zur Verwaltung von Chat-Konversationen mit folgenden Komponenten:

**Klasse `Nachricht`** (nutze eine einfache Klasse oder Dictionary):
- Attribute: `rolle` (str: "user", "assistant", "system"), `inhalt` (str), `zeitstempel` (datetime)

**Funktion `erstelle_konversation(system_prompt, **optionen)`**:
- Initialisiert eine neue Konversation
- `system_prompt`: Optionaler System-Prompt
- `**optionen`: Konversations-Einstellungen (z.B. `max_laenge`, `modell`)
- Gibt Konversations-Dictionary zurück

**Funktion `fuege_nachricht_hinzu(konversation, rolle, inhalt)`**:
- Fügt Nachricht zur Konversation hinzu
- Validiert `rolle` (nur "user", "assistant", "system" erlaubt)
- Aktualisiert Statistiken (Nachrichtenanzahl, durchschnittliche Länge)

**Funktion `generiere_antwort(konversation, user_nachricht, **llm_einstellungen)`**:
- Fügt User-Nachricht hinzu
- Simuliert LLM-Antwort (in realer Anwendung: API-Call)
- Fügt Assistant-Antwort hinzu
- Gibt Assistant-Antwort zurück

**Funktion `speichere_konversation(konversation, dateiname)`**:
- Speichert Konversation als JSON-Datei
- Nutze `json.dump()` mit `indent=4`

**Funktion `lade_konversation(dateiname)`**:
- Lädt Konversation aus JSON-Datei
- Fehlerbehandlung für nicht-existierende Dateien

**Funktion `konversations_statistik(konversation)`**:
- Berechnet Statistiken:
  - Anzahl Nachrichten (gesamt, pro Rolle)
  - Durchschnittliche Nachrichtenlänge
  - Gesamte Token-Schätzung (ca. 1 Token pro 4 Zeichen)

**Bonus-Challenge**:
Implementiere eine Funktion `bereinige_konversation(konversation, *, max_nachrichten=None, nur_rolle=None)`, die:
- Die Konversation auf max. `max_nachrichten` beschränkt (älteste entfernen)
- Optional nur Nachrichten einer bestimmten Rolle behält

**Beispiel Ein-/Ausgabe**:
```python
# Neue Konversation erstellen
conv = erstelle_konversation(
    system_prompt="Du bist ein hilfreicher KI-Assistent für Python-Programmierung",
    modell="gpt-4",
    max_laenge=500
)

# Konversation führen
antwort1 = generiere_antwort(conv, "Was sind Lambda-Funktionen?", temperatur=0.5)
print(f"Assistent: {antwort1}")

antwort2 = generiere_antwort(conv, "Zeige mir ein Beispiel")
print(f"Assistent: {antwort2}")

# Statistiken
stats = konversations_statistik(conv)
print(f"Nachrichten: {stats['anzahl_nachrichten']}")
print(f"Token-Schätzung: {stats['geschaetzte_tokens']}")

# Speichern
speichere_konversation(conv, "konversation_001.json")

# Laden
geladene_conv = lade_konversation("konversation_001.json")
print(f"Konversation geladen mit {len(geladene_conv['nachrichten'])} Nachrichten")
```

**Starter-Code** (Struktur):
```python
from datetime import datetime
from typing import Optional
import json

def erstelle_konversation(system_prompt: Optional[str] = None, **optionen) -> dict:
    """
    Initialisiert eine neue Konversation.
    
    Args:
        system_prompt: Optionaler System-Prompt für Kontext
        **optionen: Zusätzliche Optionen (modell, max_laenge, etc.)
    
    Returns:
        Konversations-Dictionary mit Metadaten und Nachrichtenliste
    """
    konversation = {
        "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "erstellt_am": datetime.now().isoformat(),
        "optionen": optionen,
        "nachrichten": [],
        "statistiken": {
            "anzahl_nachrichten": 0,
            "anzahl_user": 0,
            "anzahl_assistant": 0
        }
    }
    
    if system_prompt:
        fuege_nachricht_hinzu(konversation, "system", system_prompt)
    
    return konversation


def fuege_nachricht_hinzu(konversation: dict, rolle: str, inhalt: str) -> None:
    """Fügt eine Nachricht zur Konversation hinzu."""
    # Dein Code hier
    pass


def generiere_antwort(konversation: dict, user_nachricht: str, **llm_einstellungen) -> str:
    """Generiert eine LLM-Antwort (simuliert) und fügt sie hinzu."""
    # Dein Code hier
    pass


def speichere_konversation(konversation: dict, dateiname: str) -> None:
    """Speichert Konversation als JSON-Datei."""
    # Dein Code hier
    pass


def lade_konversation(dateiname: str) -> dict:
    """Lädt Konversation aus JSON-Datei."""
    # Dein Code hier
    pass


def konversations_statistik(konversation: dict) -> dict:
    """Berechnet Statistiken zur Konversation."""
    # Dein Code hier
    pass


# Bonus
def bereinige_konversation(
    konversation: dict,
    *,
    max_nachrichten: Optional[int] = None,
    nur_rolle: Optional[str] = None
) -> dict:
    """Bereinigt Konversation nach Kriterien."""
    # Dein Code hier (optional)
    pass


# Tests
if __name__ == "__main__":
    # Test-Konversation
    conv = erstelle_konversation(
        system_prompt="Du bist ein Python-Experte",
        modell="gpt-4"
    )
    
    antwort1 = generiere_antwort(conv, "Erkläre *args", temperatur=0.3)
    print(f"Antwort 1: {antwort1[:100]}...")
    
    antwort2 = generiere_antwort(conv, "Und **kwargs?", temperatur=0.3)
    print(f"Antwort 2: {antwort2[:100]}...")
    
    stats = konversations_statistik(conv)
    print(f"\nStatistiken: {stats}")
    
    speichere_konversation(conv, "test_konversation.json")
    geladene_conv = lade_konversation("test_konversation.json")
    print(f"\nGeladen: {len(geladene_conv['nachrichten'])} Nachrichten")
```

**Hinweise**:
- Nutze `datetime.now().isoformat()` für Zeitstempel in JSON-kompatiblem Format
- Für simulierte Antworten: Einfache Templates oder kurze generische Antworten
- Fehlerbehandlung: `FileNotFoundError` beim Laden, `ValueError` bei ungültiger Rolle
- Token-Schätzung: `anzahl_zeichen / 4` (grobe Heuristik)

