---
name: create-lesson
description: Erstellt eine vollständige Vorlesungslektion mit allen erforderlichen Markdown-Dateien
argument-hint: "Lektionsnummer (z.B. V01), Thema (optional), Format (Vorlesung/Übung/beides)"
agent: Informatik-Dozent
tools: ['edit', 'read/readFile', 'search']
---

# Aufgabe

Erstelle eine vollständige Vorlesungslektion für das Modul "Informatik Grundlagen" im Bachelor Maschinenbau. Die Lektion soll didaktisch aufbereitet sein und alle erforderlichen Markdown-Dateien im `lessons/` Ordner strukturiert ablegen.

> [!CRITICAL]
> **Maschinenbau-Kontext ist PFLICHT**: Alle Aufgaben, Beispiele und Testdaten MÜSSEN einen konkreten Bezug zum Maschinenbau-Studium haben! Nutze realistische Szenarien aus:
> - Sensordatenanalyse (Temperatur, Druck, Vibration, Drehzahl)
> - Materialeigenschaften (Zugfestigkeit, E-Modul, Dichte)
> - Fertigungsdaten (CNC, Qualitätskontrolle, Produktionsmetriken)
> - CAD/Simulation (Geometriedaten, FEM-Ergebnisse)
> - Prüfprotokolle und Messungen
> - Maschinenüberwachung und Wartung

## Eingabeparameter

Der Benutzer kann folgende Parameter angeben (alle optional):

- **Lektionsnummer**: `${input:lektionsnummer:V01}` - Die Vorlesungsnummer (z.B. V01, V02, V03, etc.)
- **Thema**: `${input:thema}` - Spezifisches Thema oder leer lassen für automatische Auswahl aus [lesson.md](../../lesson.md)
- **Format**: `${input:format:komplett}` - Standard ist `komplett` (Theorie+Praxis in einer Datei)

## Arbeitsablauf

> [!IMPORTANT]
> **Schrittweise Ausführung**: Führe jeden Schritt einzeln aus, liefere eine kurze Ausgabe pro Schritt und fahre automatisch mit dem nächsten Schritt fort. Halte Antworten knapp, um große Ausgaben zu vermeiden.

> [!WARNING]
> **Token-Limit beachten**: Die Schritte sind bewusst KLEIN gehalten, damit die generierten Dateiinhalte pro Schritt nicht zu umfangreich werden (max. ~200 Zeilen pro Schritt). Jeder Schritt erstellt oder erweitert nur einen TEIL der finalen Datei. Dies verhindert, dass GPT-Token-Limits erreicht werden.

**Schritt-Übersicht** (Gesamt ~21 Schritte):
- Schritt 1-2: Vorbereitung (Kontext + Ordner)
- Schritt 3a-3c: Skript Theorie-Teil (3 Unterschritte)
- Schritt 4a-4c: Skript Python-Teil (3 Unterschritte)
- Schritt 5a-5b: Aufgaben Theorie (2 Unterschritte)
- Schritt 6a-6c: Aufgaben Python (3 Unterschritte)
- Schritt 6d: Testdaten erstellen (CSV, SQLite, TXT, etc.)
- Schritt 7a-7c: Lösungen Theorie (3 Unterschritte)
- Schritt 8a-8c: Lösungen Python P1-P3 (3 Unterschritte)
- Schritt 9a-9b: Lösungen Python P4-P5 (2 Unterschritte)
- Schritt 10-11: Abschluss (Python-Tracking + Zusammenfassung)

---

### Schritt 1: Kontext sammeln und Planung

**Aktion**: Lies die folgenden Dateien und erstelle einen kurzen Überblick:

1. **Vorlesungsplan**: [lesson.md](../../lesson.md) - Enthält die komplette Übersicht aller 22 Lektionen
2. **Python-Tracking**: [python_topics.md](../../python_topics.md) - Liste aller bereits eingeführten Python-Konzepte
3. **Bestehende Lektionen**: Prüfe `lessons/` Ordner auf bereits vorhandene Lektionen

**Ausgabe**: 
- Zeige die gewählte Lektionsnummer (V{XX})
- Zeige das Theorie-Thema
- Zeige das Python-Praxis-Thema
- Status: Lektion existiert bereits? (Ja/Nein)

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 2 fortfahren.

---

### Schritt 2: Ordner erstellen

**Aktion**: Erstelle den Lektionsordner:

- Ordnername: `lessons/V{XX}-{Theorie-Titel}/`
- Beispiel: `lessons/V03-Boolsche-Algebra/`

**Ausgabe**: Bestätige die Ordner-Erstellung

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 3 fortfahren.

---

### Schritt 3: Skript-Datei erstellen - Grundgerüst

**Aktion**: Erstelle `V{XX}-{Theorie-Titel}_skript.md` aber NUR mit:

1. Titel und Lernzielen
2. Überblicks-Abschnitt "Teil 1: Theorie"
3. ERSTEN Hauptabschnitt der Theorie (ca. 30-50 Zeilen)

> [!NOTE]
> Erstelle NICHT die komplette Theorie! Nur Grundgerüst + erster Abschnitt.

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 3b fortfahren.

---

### Schritt 3b: Skript-Datei erweitern - Theorie Fortsetzung

**Aktion**: Ergänze die Skript-Datei um:

1. ZWEITEN und DRITTEN Hauptabschnitt der Theorie (ca. 40-60 Zeilen)
2. Optional: Weitere Theorie-Abschnitte falls nötig

> [!NOTE]
> Noch KEINE Zusammenfassung! Die kommt im nächsten Schritt.

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 3c fortfahren.

---

### Schritt 3c: Skript-Datei abschließen - Theorie Ende

**Aktion**: Ergänze die Skript-Datei um:

1. Letzte Theorie-Abschnitte (falls noch nicht vollständig)
2. Zusammenfassung Theorie (3-5 Bullet Points)
3. Trennlinie `---` für Teil 2

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 4 fortfahren.

---

### Schritt 4: Skript-Datei erweitern - Python Grundlagen

**Aktion**: Ergänze die Skript-Datei um:

1. Überschrift "Teil 2: Python-Praxis - {Python-Thema}"
2. WARNING-Block zur Python-Konsistenz
3. Überblick-Abschnitt
4. ERSTEN Python-Hauptabschnitt mit Beispielen (ca. 40-60 Zeilen)

> [!NOTE]
> Nur erster Python-Abschnitt! Rest folgt in nächsten Schritten.

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 4b fortfahren.

---

### Schritt 4b: Skript-Datei erweitern - Python Fortsetzung

**Aktion**: Ergänze die Skript-Datei um:

1. ZWEITEN und ggf. DRITTEN Python-Hauptabschnitt (ca. 50-70 Zeilen)
2. Code-Beispiele mit TIP-Blöcken

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 4c fortfahren.

---

### Schritt 4c: Skript-Datei abschließen - Python Ende

**Aktion**: Ergänze die Skript-Datei um:

1. Abschnitt "Häufige Fehler und Lösungen" (2-3 WARNING-Blöcke)
2. Zusammenfassung Python (3-5 Bullet Points)
3. "Neue Python-Funktionen/Methoden" Liste
4. "Weiterführende Ressourcen" (Theorie + Python)

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 5 fortfahren.

---

### Schritt 5: Aufgaben-Datei erstellen - Grundgerüst + T1-T2

**Aktion**: Erstelle `V{XX}-{Theorie-Titel}_aufgaben.md` mit:

1. Kopfbereich und NOTE-Block mit Einleitung
2. Überschrift "Teil A: Theorie-Aufgaben"
3. Aufgabe T1 (Leicht) - vollständig
4. Aufgabe T2 (Mittel) - vollständig

> [!NOTE]
> NUR T1 und T2! T3 kommt im nächsten Schritt.

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 5b fortfahren.

---

### Schritt 5b: Aufgaben-Datei erweitern - T3 + Python-Beginn

**Aktion**: Ergänze die Aufgaben-Datei um:

1. Aufgabe T3 (Schwer) - vollständig
2. Trennlinie `---`
3. Überschrift "Teil B: Python-Aufgaben"
4. Aufgabe P1 (Leicht) - vollständig

> [!IMPORTANT]
> Bei ALLEN Python-Aufgaben:
> - Stelle sicher, dass die Aufgabe einen **konkreten Maschinenbau-Bezug** hat!
> - Falls externe Daten benötigt werden (CSV, DB, TXT, JSON, etc.), notiere welche Testdaten später in Schritt 6d erstellt werden müssen
> - Bei API-Aufgaben: Wähle maschinenbau-relevante APIs oder erstelle Mock-Daten

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 6 fortfahren.

---

### Schritt 6: Aufgaben-Datei erweitern - P2 und P3

**Aktion**: Ergänze die Aufgaben-Datei um:

1. Aufgabe P2 (Leicht-Mittel) - vollständig
2. Aufgabe P3 (Mittel) - vollständig

> [!NOTE]
> P4 und P5 folgen in separaten Schritten, da sie komplexer sind.

> [!IMPORTANT]
> Notiere weiterhin, welche Testdaten für P2 und P3 benötigt werden!

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 6b fortfahren.

---

### Schritt 6b: Aufgaben-Datei erweitern - P4

**Aktion**: Ergänze die Aufgaben-Datei um:

1. Aufgabe P4 (Mittel-Schwer) - vollständig mit allen Teilaufgaben

> [!IMPORTANT]
> Notiere, welche Testdaten für P4 benötigt werden!

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 6c fortfahren.

---

### Schritt 6c: Aufgaben-Datei abschließen - P5

**Aktion**: Ergänze die Aufgaben-Datei um:

1. Aufgabe P5 (Schwer/Komplex) - vollständig
2. Optional: Bonus-Challenge

> [!IMPORTANT]
> Notiere, welche Testdaten für P5 (und ggf. Bonus) benötigt werden!

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 6d fortfahren.

---

### Schritt 6d: Testdaten erstellen

**Aktion**: Analysiere alle Python-Aufgaben (P1-P5) und erstelle benötigte Testdaten:

1. Prüfe jede Aufgabe: Werden externe Daten benötigt?
2. Erstelle im Ordner `lessons/V{XX}-{Theorie-Titel}/testdaten/` alle notwendigen Dateien:
   - **CSV-Dateien**: Für Datenanalyse, Tabellen-Verarbeitung
   - **SQLite-Datenbanken**: Für Datenbank-Aufgaben
   - **TXT-Dateien**: Für Text-Verarbeitung, File-I/O
   - **JSON-Dateien**: Für strukturierte Daten
   - **Weitere Formate**: Je nach Aufgabenstellung
3. Erstelle eine `README.md` im `testdaten/` Ordner mit Beschreibung aller Dateien
4. Aktualisiere die Aufgaben-Datei: Füge bei jeder Aufgabe, die Testdaten nutzt, einen Hinweis auf die Datei hinzu

> [!IMPORTANT]
> Testdaten müssen:
> - **Realistisch** sein (sinnvolle Werte aus dem Maschinenbau, plausible Szenarien)
> - **Gut strukturiert** sein (saubere Formatierung, konsistente Daten)
> - **Ausreichend umfangreich** sein (mindestens 10-20 Datensätze bei CSV/DB)
> - **Varianz** aufweisen (verschiedene Fälle, auch Edge-Cases)
> - **Dokumentiert** sein (README.md erklärt Struktur, Verwendung und Maschinenbau-Kontext)
> - **Maschinenbau-relevant** sein (Sensordaten, Materialeigenschaften, Fertigungsdaten, etc.)

> [!TIP]
> **REST APIs für Maschinenbau-Aufgaben**:
> Falls eine Aufgabe API-Abfragen beinhaltet, verwende maschinenbau-relevante APIs:
> - **OpenWeatherMap API**: Wetterdaten für Außeneinsatz-Szenarien (Maschinen, Baustellen)
> - **Material Properties API**: Materialdatenbanken (z.B. MatWeb-ähnliche Mock-APIs)
> - **IoT/Sensor APIs**: Simulierte Maschinensensor-Daten
> - **CAD/PLM APIs**: Geometriedaten, Stücklisten (Mock-Endpoints)
> - **Energy/Power APIs**: Energieverbrauch, Leistungsdaten
> - Erstelle bei Bedarf eigene Mock-API-Antworten als JSON-Dateien in `testdaten/`

**Beispiele für Testdaten (Maschinenbau-Kontext)**:
- `sensordaten.csv`: Temperatur, Druck, Vibration, Drehzahl, Zeitstempel von Maschinen
- `materialdaten.csv`: Werkstoff, Zugfestigkeit, E-Modul, Dichte, Bruchdehnung
- `fertigungsdaten.db`: SQLite mit Produktionsdaten, Qualitätsmetriken, Ausschuss
- `messwerte.txt`: Rohdaten von Messgeräten (z.B. Kraftmessung, Weg-Zeit-Diagramm)
- `cad_parameter.json`: Geometrische Parameter, Toleranzen, Materialzuordnungen
- `pruefprotokoll.csv`: Prüfergebnisse, Sollwerte, Istwerte, Status (i.O./n.i.O.)
- `simulation.csv`: FEM-Ergebnisse, Spannungen, Verformungen, Knotenpunkte

**Ausgabe**: 
```
✅ Testdaten erstellt: [X] Dateien in testdaten/
   - [Liste der erstellten Dateien]
✅ Aufgaben aktualisiert mit Datei-Referenzen
```

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 7 fortfahren.

---

### Schritt 7: Lösungen erstellen - Grundgerüst + Lösung T1

**Aktion**: Erstelle `V{XX}-{Theorie-Titel}_loesungen.md` mit:

1. Kopfbereich mit WARNING-Block ("Versuche die Aufgaben zuerst selbstständig...")
2. Trennlinie `---`
3. Überschrift "Teil A: Theorie-Aufgaben - Lösungen"
4. Lösung T1 - vollständig (Lösung, Erklärung, Häufige Fehler)

> [!NOTE]
> NUR T1! T2 und T3 folgen in den nächsten Schritten.

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 7b fortfahren.

---

### Schritt 7b: Lösungen erweitern - Lösung T2

**Aktion**: Ergänze die Lösungen-Datei um:

1. Lösung T2 - vollständig (Lösung, Erklärung, Lösungsweg Schritt-für-Schritt, Häufige Fehler)

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 7c fortfahren.

---

### Schritt 7c: Lösungen erweitern - Lösung T3

**Aktion**: Ergänze die Lösungen-Datei um:

1. Lösung T3 - vollständig (Lösung, Sehr detaillierte Erklärung, Lösungsweg Schritt-für-Schritt, Alternative Lösungsansätze, Häufige Fehler)
2. Trennlinie `---` vor Teil B

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 8 fortfahren.

---

### Schritt 8: Lösungen erweitern - Python Lösung P1

**Aktion**: Ergänze die Lösungen-Datei um:

1. Überschrift "Teil B: Python-Aufgaben - Lösungen"
2. Lösung P1 - vollständig (Code, Erklärung, "Warum diese Lösung?", Häufige Fehler)

> [!NOTE]
> NUR P1! Weitere Lösungen folgen einzeln.

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 8b fortfahren.

---

### Schritt 8b: Lösungen erweitern - Python Lösung P2

**Aktion**: Ergänze die Lösungen-Datei um:

1. Lösung P2 - vollständig (Code, Erklärung, Schritt-für-Schritt Durchlauf)

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 8c fortfahren.

---

### Schritt 8c: Lösungen erweitern - Python Lösung P3

**Aktion**: Ergänze die Lösungen-Datei um:

1. Lösung P3 - vollständig (Code, Erklärung, "Konzepte in dieser Lösung")

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 9 fortfahren.

---

### Schritt 9: Lösungen erweitern - Python Lösung P4

**Aktion**: Ergänze die Lösungen-Datei um:

1. Lösung P4 - vollständig (Code mit ausführlichen Kommentaren, Sehr detaillierte Erklärung, Design-Entscheidungen, Komplexitätsanalyse)

> [!NOTE]
> P4 ist komplex - nimm dir Zeit für ausführliche Erklärungen.

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 9b fortfahren.

---

### Schritt 9b: Lösungen abschließen - Python Lösung P5

**Aktion**: Ergänze die Lösungen-Datei um:

1. Lösung P5 - vollständig (Umfangreicher Code, Sehr ausführliche Erklärung, Architektur-Überblick, Schritt-für-Schritt Erklärung, Alternative Lösungsansätze)
2. Optional: Bonus-Challenge Lösung falls vorhanden

> [!NOTE]
> P5 ist die komplexeste Aufgabe - gib detaillierte, didaktisch wertvolle Erklärungen.

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 10 fortfahren.

---

### Schritt 10: Python-Tracking aktualisieren

**Aktion**: Falls neue Python-Konzepte eingeführt wurden:

1. Öffne [python_topics.md](../../python_topics.md)
2. Füge unter der entsprechenden Vorlesung (V{XX}) alle neu eingeführten Funktionen/Methoden/Module hinzu
3. Markiere sie als "Neu eingeführt in V{XX}"

**Ausgabe**: Liste der hinzugefügten Python-Konzepte

**Weiter**: Nach der kurzen Ausgabe automatisch mit Schritt 11 fortfahren.

---

### Schritt 11: Abschluss und Zusammenfassung

**Aktion**: 

1. Prüfe alle Verlinkungen (relativ und korrekt)
2. Erstelle finale Zusammenfassung

**Ausgabe**: Zeige die vollständige Übersicht (siehe Abschnitt "Ausgabe" unten)

---

## Dateistruktur-Vorlagen

Die folgenden Vorlagen dienen als Referenz für die Struktur. Erstelle die Inhalte **schrittweise** gemäß dem Arbeitsablauf (Schritt 3-9).

#### Ordnerstruktur

**`lessons/V{XX}-{Theorie-Titel}/`**

Beispiel: `lessons/V03-Boolsche-Algebra/`

Die Struktur umfasst:
```
lessons/V{XX}-{Theorie-Titel}/
├── V{XX}-{Theorie-Titel}_skript.md
├── V{XX}-{Theorie-Titel}_aufgaben.md
├── V{XX}-{Theorie-Titel}_loesungen.md
└── testdaten/                          (falls benötigt)
    ├── README.md                       (Beschreibung aller Testdaten)
    ├── beispiel.csv                    (Beispiel-CSV)
    ├── datenbank.db                    (SQLite-Datenbank)
    ├── textfile.txt                    (Text-Datei)
    └── ...                             (weitere Dateien je nach Aufgaben)
```

---

#### Datei 1: Skript (Theorie + Praxis kombiniert)

**`V{XX}-{Theorie-Titel}_skript.md`**

Diese Datei enthält das vollständige Lernskript für den gesamten Vorlesungstag (Theorie + Python-Praxis):

```markdown
# V{XX}: {Theorie-Thema-Titel}

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - [Theoretisches Lernziel 1]
> - [Theoretisches Lernziel 2]
> - [Python-Lernziel 1]
> - [Python-Lernziel 2]
> - [Weitere 1-3 Lernziele]

---

## Teil 1: Theorie - {Theorie-Thema}

### Überblick

[Einführung ins theoretische Thema mit Motivation und Praxisbezug]

### {Hauptabschnitt 1}

[Inhalt mit Fachbegriffen **fett**, NOTE/TIP/WARNING Blöcken]

> [!NOTE]
> **{Fachbegriff}**: Präzise Definition

> [!TIP]
> Beispiel oder Merkhilfe

### {Hauptabschnitt 2}

[Weitere Theorie-Abschnitte je nach Thema]

### Zusammenfassung Theorie

[Kernaussagen in 3-5 Punkten]

---

## Teil 2: Python-Praxis - {Python-Thema}

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte!

### Überblick

[Einführung in das Python-Thema mit Bezug zur Theorie]

### {Python-Hauptabschnitt 1}

[Python-Konzepte erklären]

> [!TIP]
> ```python
> # Beispiel-Code mit Kommentaren
> def beispiel_funktion():
>     """Docstring erklärt die Funktion."""
>     pass
> ```

### {Python-Hauptabschnitt 2}

[Weitere Python-Konzepte]

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1**: [Beschreibung des typischen Fehlers]
> 
> **Lösung**: [Wie man es richtig macht]

> [!WARNING]
> **Fehler 2**: [Weiterer typischer Fehler]
> 
> **Lösung**: [Korrekter Ansatz]

### Zusammenfassung Python

[Kernaussagen zu Python-Konzepten in 3-5 Punkten]

### Neue Python-Funktionen/Methoden

[Liste aller in dieser Lektion NEU eingeführten Python-APIs mit Signatur und kurzer Erklärung]

---

## Weiterführende Ressourcen

### Theorie
- [Relevante Quelle 1 für Theorie-Thema]
- [Relevante Quelle 2 für Theorie-Thema]

### Python
- [Python-Dokumentation Link]
- [Tutorial oder Artikel Link]
- [Weitere Ressource]
```

---

#### Datei 2: Aufgaben

**`V{XX}-{Theorie-Titel}_aufgaben.md`**

Diese Datei enthält **3 Theorie-Aufgaben** (leicht → mittel → schwer) und **5 Python-Aufgaben** (leicht → schwer/komplex):

```markdown
# V{XX}: Übungsaufgaben - {Thema}

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V{XX}.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: {Titel} (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

[Aufgabenstellung für leichte Theorie-Aufgabe]

**Hinweise**:
- [Hilfreicher Hinweis falls nötig]

---

### Aufgabe T2: {Titel} (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

[Aufgabenstellung für mittelschwere Theorie-Aufgabe]

**Hinweise**:
- [Hilfreicher Hinweis falls nötig]

---

### Aufgabe T3: {Titel} (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

[Aufgabenstellung für schwere Theorie-Aufgabe]

**Hinweise**:
- [Hilfreicher Hinweis falls nötig]

---

## Teil B: Python-Aufgaben

### Aufgabe P1: {Titel} (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: [Liste benötigter Python-Konzepte]  
**Maschinenbau-Kontext**: [Kurze Beschreibung des Praxisbezugs, z.B. "Analyse von Maschinensensordaten", "Berechnung von Materialkennwerten", "Auswertung von Fertigungsdaten"]

[Aufgabenstellung mit konkretem Maschinenbau-Szenario]

**Benötigte Testdaten**: 
- Falls externe Dateien benötigt werden: `testdaten/dateiname.csv` (oder .db, .txt, .json, etc.)
- Beschreibung der Datei und Struktur (z.B. "Sensordaten von CNC-Maschine mit Spalten: Zeitstempel, Drehzahl, Temperatur, Vibration")
- Bei API-Aufgaben: Beschreibung der API und Endpunkte (z.B. Mock-API für Materialdatenbank)

**Beispiel Ein-/Ausgabe**:
```
Eingabe: sensordaten.csv
Ausgabe: Durchschnittliche Temperatur: 65.3°C, Max. Vibration: 2.8 mm/s
```

**Starter-Code** (optional):
```python
# Dein Code hier
```

> [!TIP]
> Die Testdaten findest du im Ordner `testdaten/` neben dieser Aufgaben-Datei.

---

### Aufgabe P2: {Titel} (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: [Liste benötigter Python-Konzepte]

[Aufgabenstellung]

---

### Aufgabe P3: {Titel} (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: [Liste benötigter Python-Konzepte]

[Aufgabenstellung]

---

### Aufgabe P4: {Titel} (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: [Liste benötigter Python-Konzepte]

[Aufgabenstellung - komplexer, eventuell mehrere Teilaufgaben]

---

### Aufgabe P5: {Titel} (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: [Liste benötigter Python-Konzepte]

[Aufgabenstellung - herausfordernd, kombiniert mehrere Konzepte]

**Bonus-Challenge** (optional):
[Erweiterte Anforderung für besonders interessierte Studierende]
```

---

#### Datei 3: Lösungen

**`V{XX}-{Theorie-Titel}_loesungen.md`**

Diese Datei enthält ausführliche Lösungen mit Erklärungen:

```markdown
# V{XX}: Lösungen - {Thema}

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: {Titel}

**Lösung**:

[Ausführliche Lösung]

**Erklärung**:

[Detaillierte Erklärung, warum die Lösung so ist]

**Häufige Fehler**:
- [Typischer Fehler 1 und warum er falsch ist]
- [Typischer Fehler 2 und warum er falsch ist]

---

### Lösung T2: {Titel}

**Lösung**:

[Ausführliche Lösung]

**Erklärung**:

[Detaillierte Erklärung mit Zwischenschritten]

**Lösungsweg Schritt für Schritt**:
1. [Schritt 1 mit Begründung]
2. [Schritt 2 mit Begründung]
3. [...]

**Häufige Fehler**:
- [Typische Fehlerquelle und Korrektur]

---

### Lösung T3: {Titel}

**Lösung**:

[Ausführliche Lösung]

**Erklärung**:

[Sehr detaillierte Erklärung, da schwere Aufgabe]

**Lösungsweg Schritt für Schritt**:
1. [Detaillierter Schritt 1]
2. [Detaillierter Schritt 2]
3. [...]

**Alternative Lösungsansätze**:
- [Alternativer Ansatz 1 mit Vor-/Nachteilen]
- [Alternativer Ansatz 2 mit Vor-/Nachteilen]

**Häufige Fehler**:
- [Typische Denkfehler und Missverständnisse]

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: {Titel}

**Vollständiger Code**:
```python
# Lösung mit ausführlichen Kommentaren
def funktion_name():
    """
    Docstring erklärt die Funktion.
    """
    # Zeile-für-Zeile Kommentare
    pass
```

**Erklärung**:

[Zeilenweise Erklärung des Codes]

**Warum diese Lösung?**

[Begründung der gewählten Herangehensweise]

**Häufige Fehler**:
- **Fehler**: [Typischer Code-Fehler]
  - **Warum falsch**: [Erklärung]
  - **Richtig**: [Korrektur]

---

### Lösung P2: {Titel}

**Vollständiger Code**:
```python
# Musterlösung
```

**Erklärung**:

[Detaillierte Code-Erklärung]

**Schritt-für-Schritt Durchlauf**:

[Beispiel-Eingabe durchgehen und zeigen, was in jedem Schritt passiert]

---

### Lösung P3: {Titel}

**Vollständiger Code**:
```python
# Musterlösung
```

**Erklärung**:

[Code-Erklärung mit Fokus auf wichtige Konzepte]

**Konzepte in dieser Lösung**:
- **{Konzept 1}**: [Wie und warum es hier verwendet wird]
- **{Konzept 2}**: [Wie und warum es hier verwendet wird]

---

### Lösung P4: {Titel}

**Vollständiger Code**:
```python
# Musterlösung mit ausführlichen Kommentaren
```

**Erklärung**:

[Sehr detaillierte Erklärung der komplexeren Lösung]

**Design-Entscheidungen**:
- [Warum wurde diese Datenstruktur gewählt?]
- [Warum wurde dieser Algorithmus gewählt?]
- [Welche Alternativen gäbe es?]

**Komplexitätsanalyse**:
- **Zeitkomplexität**: O(...)
- **Speicherkomplexität**: O(...)
- **Begründung**: [Warum diese Komplexität?]

---

### Lösung P5: {Titel}

**Vollständiger Code**:
```python
# Umfangreiche Musterlösung
```

**Erklärung**:

[Sehr ausführliche Erklärung der komplexen Lösung]

**Architektur-Überblick**:

[Wie die verschiedenen Teile zusammenspielen]

**Schritt-für-Schritt Erklärung**:

1. **Initialisierung**: [Was wird vorbereitet?]
2. **Hauptlogik**: [Wie funktioniert der Kern?]
3. **Edge Cases**: [Wie werden Spezialfälle behandelt?]
4. **Ausgabe**: [Wie wird das Ergebnis aufbereitet?]

**Alternative Lösungsansätze**:

**Ansatz 1**: [Beschreibung]
- ✅ Vorteile: [...]
- ❌ Nachteile: [...]

**Ansatz 2**: [Beschreibung]
- ✅ Vorteile: [...]
- ❌ Nachteile: [...]

**Bonus-Challenge Lösung** (falls vorhanden):
```python
# Erweiterte Lösung
```

[Erklärung der erweiterten Funktionalität]
```

**Aktion**: Falls neue Python-Konzepte eingeführt wurden:

1. Öffne [python_topics.md](../../python_topics.md)
2. Füge unter der entsprechenden Vorlesung (V{XX}) alle neu eingeführten Funktionen/Methoden/Module hinzu
3. Markiere sie als "Neu eingeführt in V{XX}"

**Ausgabe**: Liste der hinzugefügten Python-Konzepte

**⏸️ STOPP**: Warte auf Bestätigung für die finale Zusammenfassung.

---

### Schritt 11: Abschluss und Zusammenfassung

**Aktion**: 

1. Prüfe alle Verlinkungen (relativ und korrekt)
2. Erstelle finale Zusammenfassung

**Ausgabe**: Zeige die vollständige Übersicht (siehe Abschnitt "Ausgabe" unten)

## Qualitätskriterien

> [!NOTE]
> Diese Kriterien gelten für alle erstellten Inhalte. Prüfe sie während der schrittweisen Erstellung.

Stelle sicher, dass alle Inhalte:

✅ **Didaktisch wertvoll**: Klare Lernziele, progressive Schwierigkeit  
✅ **Formatierung korrekt**: Fachbegriffe **fett**, NOTE/TIP/WARNING Blöcke eingesetzt  
✅ **Code-Beispiele**: Vollständig, ausführbar, kommentiert  
✅ **Keine Duplikation**: Python-Konzepte nur einmal einführen (siehe python_topics.md)  
✅ **Praxisbezug Maschinenbau**: ALLE Aufgaben haben konkreten Bezug zum Maschinenbau-Studium! Nutze Szenarien wie: Sensordaten, CAD-Parameter, Materialeigenschaften, Fertigungsdaten, Prüfprotokolle, Messwerte, Simulationsergebnisse, etc.  
✅ **Übungen**: 3 Theorie-Aufgaben (⭐ → ⭐⭐ → ⭐⭐⭐) + 5 Python-Aufgaben (⭐ → ⭐⭐⭐⭐) - IMMER mit Maschinenbau-Kontext!  
✅ **Lösungen**: Ausführliche Erklärungen, Schritt-für-Schritt, häufige Fehler adressiert  
✅ **Testdaten vorhanden**: ALLE Python-Aufgaben, die externe Daten benötigen, haben entsprechende Testdateien im `testdaten/` Ordner. Keine Aufgabe soll scheitern, weil Dateien fehlen!  
✅ **Testdaten-Qualität**: Realistische, gut strukturierte, ausreichend umfangreiche Daten (min. 10-20 Datensätze bei CSV/DB), mit Varianz und Edge-Cases  
✅ **Testdaten dokumentiert**: `testdaten/README.md` erklärt Struktur und Verwendung aller Dateien  
✅ **Visualisierung**: Mermaid-Diagramme sind Pflicht für Abläufe/Strukturen. Nur weglassen, wenn du kurz begründest, warum Mermaid hier keinen Sinn macht. Referenzen: Grundlagen https://mermaid.js.org/intro/, Flowcharts https://mermaid.js.org/syntax/flowchart.html  
✅ **Schrittweise Erstellung**: WICHTIG! Erstelle große Dateien in KLEINEN Schritten (siehe Arbeitsablauf). Jeder Schritt sollte max. ~200 Zeilen generieren, um Token-Limits zu vermeiden.

## Ausgabe

Nach erfolgreicher Erstellung gib eine kurze Zusammenfassung:

```
✅ Lektion V{XX} erstellt
📁 Struktur:
   lessons/V{XX}-{Theorie-Titel}/
   ├── V{XX}-{Theorie-Titel}_skript.md (Theorie + Python kombiniert)
   ├── V{XX}-{Theorie-Titel}_aufgaben.md (3 Theorie + 5 Python Aufgaben)
   ├── V{XX}-{Theorie-Titel}_loesungen.md (Ausführliche Lösungen)
   └── testdaten/ ([X] Dateien: CSV, DB, TXT, etc.)
📝 Python-Tracking aktualisiert: [X neue Konzepte]
🗂️ Testdaten: [X] Dateien erstellt (z.B. students.csv, sensor.db, log.txt)
```

## Beispielaufruf im Chat

```
/create-lesson lektionsnummer=V03
```

oder einfach:

```
/create-lesson V05
```

oder mit spezifischem Thema:

```
/create-lesson thema="Rekursion in Python"
```
