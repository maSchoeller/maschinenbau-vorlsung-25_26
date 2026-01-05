# Informatik Grundlagen - Vorlesungsplan

Übersicht aller 22 Lektionen für das Modul "Informatik Grundlagen" im Bachelor Maschinenbau.
**Format:** Jeweils 3×45 Minuten pro Vorlesung (Theorie + Praktisches Python)

---

## Semesterplan: Zuordnung der 22 Termine

| Termin | Informatik-Theorie | Python-Praxis | Status |
|--------|-------------------|---------------|--------|
| V01 | Binäres Zahlensystem | Python Get Started: Variablen, print, input | ✅ [Verfügbar](lessons/V01-Binaeres-Zahlensystem/) |
| V02 | Fließkommazahlen | Eingaben/Ausgaben & Formatierung | ✅ [Verfügbar](lessons/V02-Fliesskommazahlen/) |
| V03 | Boolsche Algebra & Logische Schaltungen – Teil 1 | Variablen Management & Datentypen | ✅ [Verfügbar](lessons/V03-Boolsche-Algebra-Teil1/) |
| V04 | Boolsche Algebra & Logische Schaltungen – Teil 2 | Logische Ausdrücke (Boolsche Algebra) |✅ [Verfügbar](lessons/V04-Boolsche-Algebra-Teil2/)|
| V05 | Programm-Ablauf-Pläne – Teil 1 | Verzweigungen (if, if-elif-else) | ✅ [Verfügbar](lessons/V05-Programm-Ablauf-Plaene-Teil1/) |
| V06 | Programm-Ablauf-Pläne – Teil 2 | Schleifen (for, while) – Teil 1 | ✅ [Verfügbar](lessons/V06-Programm-Ablauf-Plaene-Teil2/) |
| V07 | Software Engineering (KISS, DRY, SRP) | Schleifen (for, while) – Teil 2 | ✅ [Verfügbar](lessons/V07-Software-Engineering-KISS-DRY-SRP/) |
| V08 | Listen und Datenstrukturen – Teil 1 | Listen & Datenstrukturen | ✅ [Verfügbar](lessons/V08-Listen-und-Datenstrukturen-Teil1/) |
| V09 | Listen und Datenstrukturen – Teil 2 | Try-Catch (Fehlerbehandlung) | ✅ [Verfügbar](lessons/V09-Listen-und-Datenstrukturen-Teil2/) |
| V10 | Laufzeitanalyse & Algorithmik | Methoden/Funktionen – Teil 1 | ✅ [Verfügbar](lessons/V10-Laufzeitanalyse-und-Algorithmik/) |
| V11 | GPTs, LLMs & Künstliche Intelligenz | Methoden/Funktionen – Teil 2 | ✅ [Verfügbar](lessons/V11-GPTs-LLMs-KI/) |
| V12 | Prompt Engineering & Best Practices | Imports & Code auf mehrere Dateien verteilen | ✅ [Verfügbar](lessons/V12-Prompt-Engineering-Best-Practices/) |
| V13 | Betriebssysteme & Rechnerarchitektur – Teil 1 | Plots & Grafiken (Matplotlib) – Teil 1 | ✅ [Verfügbar](lessons/V13-Betriebssysteme-Rechnerarchitektur-Teil1/) |
| V14 | Betriebssysteme & Rechnerarchitektur – Teil 2 | Plots & Grafiken (Matplotlib) – Teil 2 | ✅ [Verfügbar](lessons/V14-Betriebssysteme-Rechnerarchitektur-Teil2/) |
| V15 | Netzwerktechnik Grundlagen & Protokolle – Teil 1 | Große Datenmengen verarbeiten – Teil 1 | ✅ [Verfügbar](lessons/V15-Netzwerktechnik-Grundlagen-Protokolle-Teil1/) |
| V16 | Netzwerktechnik Grundlagen & Protokolle – Teil 2 | Große Datenmengen verarbeiten – Teil 2 | 🔄 In Planung |
| V17 | Kryptografie – Teil 1 | Netzwerk-Programmierung (Basics: Socket, HTTP) – Teil 1 | ✅ [Verfügbar](lessons/V17-Kryptografie-Teil1/) |
| V18 | Kryptografie – Teil 2 | Netzwerk-Programmierung (Basics: Socket, HTTP) – Teil 2 | 🔄 In Planung |
| V19 | Datenbanken – Teil 1 | Datenbankverbindung & SQL – Teil 1 | 🔄 In Planung |
| V20 | Datenbanken – Teil 2 | Datenbankverbindung & SQL – Teil 2 | 🔄 In Planung |
| V21 | **Wiederholung & Prüfungsvorbereitung** | **Wiederholung & Prüfungsvorbereitung** | 🔄 In Planung |
| V22 | **Wiederholung & Prüfungsvorbereitung** | **Wiederholung & Prüfungsvorbereitung** | 🔄 In Planung |

---

## Übersicht: Thematische Ordnung

### Informatik-Theorie Reihenfolge

1. **Binäres Zahlensystem** (V01)
   - Stellenwertsysteme allgemein (Dezimal, Binär, Hexadezimal, Oktal)
   - Umrechnung zwischen verschiedenen Zahlensystemen
   - Binäre Rechenoperationen (Addition, Subtraktion)
   - Negative Zahlen im Computer (Zweierkomplement)
   - Praktische Anwendung: Bit-Masken und Bit-Manipulation

2. **Fließkommazahlen** (V02)
   - IEEE 754 Standard für Gleitkommadarstellung
   - Aufbau: Vorzeichen, Exponent, Mantisse
   - Rundungsfehler und Genauigkeitsprobleme
   - Spezielle Werte (NaN, Inf, -Inf)
   - Best Practices beim Vergleichen von Fließkommazahlen

3. **Boolsche Algebra & Logische Schaltungen – Teil 1** (V03)
   - Grundlegende logische Operatoren (AND, OR, NOT)
   - Wahrheitstabellen erstellen und interpretieren
   - Logische Ausdrücke formulieren
   - Einfache logische Schaltungen
   
   **Boolsche Algebra & Logische Schaltungen – Teil 2** (V04)
   - Erweiterte Operatoren (XOR, NAND, NOR)
   - De Morgan'sche Gesetze und Vereinfachungsregeln
   - Logische Schaltungen: Halbaddierer und Volladdierer
   - Multiplexer und Demultiplexer
   - Praktische Anwendungen in digitalen Schaltungen

4. **Programm-Ablauf-Pläne – Teil 1** (V05)
   - Symbole und Notation (DIN 66001, ISO 5807)
   - Grundstrukturen: Sequenz, Verzweigung, Schleife
   - Einfache PAPs erstellen und lesen
   - Übungen: Alltagsprobleme als PAP darstellen
   
   **Programm-Ablauf-Pläne – Teil 2** (V06)
   - Von PAP zu Pseudocode und zurück
   - Komplexe Algorithmen visualisieren
   - Dokumentation von Programmabläufen
   - Vergleich verschiedener Darstellungsformen

5. **Software Engineering (KISS, DRY, SRP)** (V07)
   - KISS-Prinzip: Einfachheit als Designziel
   - DRY-Prinzip: Code-Duplikation vermeiden
   - Single Responsibility Principle: Eine Aufgabe pro Komponente
   - Code-Qualität und Wartbarkeit
   - Refactoring-Strategien für bessere Code-Struktur
   - Code Reviews und Best Practices

6. **Listen und Datenstrukturen – Teil 1** (V08) ✅
   - Arrays: Aufbau und Zugriff mit O-Notation
   - Verkettete Listen (Einfach und Doppelt verkettet)
   - Stacks (LIFO-Prinzip) und Anwendungen
   - Queues (FIFO-Prinzip) und Anwendungen
   - Zeitkomplexität verschiedener Operationen
   
   **Listen und Datenstrukturen – Teil 2** (V09) ✅
   - Bäume: Binärbäume und Binäre Suchbäume (BST)
   - Terminologie: Wurzel, Blätter, Höhe, Tiefe, vollständig, balanciert
   - BST-Operationen: Suchen, Einfügen, Löschen mit O-Notation (Best/Average/Worst Case)
   - Traversierungen: Inorder (LWR), Preorder (WLR), Postorder (LRW), Level-Order (Breitensuche)
   - Hash-Tabellen: Aufbau, Hash-Funktionen, Load Factor α
   - Kollisionsbehandlung: Chaining (verkettete Listen) vs. Open Addressing (Linear Probing, Quadratic Probing)
   - Komplexitätsanalyse aller Operationen: O(1) vs. O(n)

7. **Laufzeitanalyse & Algorithmik** (V10)
   - O-Notation (Big-O, Omega, Theta)
   - Zeitkomplexität vs. Speicherkomplexität
   - Best-Case, Average-Case, Worst-Case
   - Analyse einfacher Algorithmen und Schleifen
   - Rekursion und rekursive Komplexität
   - Sortieralgorithmen im Vergleich: Bubble Sort, Quick Sort, Merge Sort

8. **GPTs, LLMs & Künstliche Intelligenz** (V11) ✅
   - Geschichte der KI: Von Symbolischer KI über Machine Learning zu Deep Learning
   - KI-Paradigmen im Vergleich: Expertensysteme vs. ML vs. DL
   - Neuronale Netze: Perceptron, Multilayer Networks, Aktivierungsfunktionen, Backpropagation
   - Transformer-Architektur: Self-Attention-Mechanismus im Detail
   - Multi-Head Attention: Parallel processing verschiedener Beziehungsarten
   - Query, Key, Value Vektoren und deren Bedeutung
   - Large Language Models (LLMs): GPT (decoder-only), BERT (encoder-only), LLaMA
   - Training Pipeline: Pretraining, Supervised Fine-Tuning, RLHF (Reinforcement Learning from Human Feedback)
   - Anwendungsbereiche: Textgenerierung, Übersetzung, Code-Generierung, Reasoning
   - Halluzinationen: Ursachen, Beispiele, Gegenmaßnahmen (RAG, Fact-Checking, Confidence Scoring)
   - Bias in KI: Historische Daten, Proxy-Diskriminierung, Fairness-Constraints
   - Risikobewertung für verschiedene Use Cases (Medizin, Code-Gen, Recruiting, etc.)
   - Zukunftsperspektiven: Multimodale Modelle, Effizienz, Reasoning-Fähigkeiten

9. **Prompt Engineering & Best Practices** (V12)
   - Was ist Prompt Engineering und warum ist es wichtig?
   - Anatomie eines guten Prompts: Kontext, Aufgabe, Format, Constraints
   - Zero-Shot, One-Shot und Few-Shot Learning
   - Chain-of-Thought Prompting für komplexe Aufgaben
   - Role-Based Prompting: System-Prompts effektiv nutzen
   - Prompt-Patterns: ReAct, Tree-of-Thoughts, Self-Consistency
   - Iteratives Prompt-Design und Refinement
   - Temperatur und andere Parameter verstehen
   - Häufige Fehler und wie man sie vermeidet
   - Ethik im Prompt Engineering: Bias vermeiden, Sicherheit gewährleisten
   - Praktische Anwendungen: Code-Generierung, Datenanalyse, Content-Erstellung
   - Tools und Frameworks für Prompt Engineering

10. **Betriebssysteme & Rechnerarchitektur – Teil 1** (V13)
   - Von-Neumann-Architektur: CPU, RAM, I/O
   - CPU-Aufbau: ALU, Steuerwerk, Register
   - Fetch-Decode-Execute-Zyklus
   - Cache-Hierarchie (L1, L2, L3)
   
   **Betriebssysteme & Rechnerarchitektur – Teil 2** (V14)
   - Aufgaben eines Betriebssystems
   - Prozessverwaltung und Scheduling-Algorithmen
   - Prozesse vs. Threads
   - Virtueller Speicher und Paging
   - Dateisysteme und deren Organisation

11. **Netzwerktechnik Grundlagen & Protokolle – Teil 1** (V15) ✅
   - OSI-Modell: 7 Schichten im Detail (Physical, Data Link, Network, Transport, Session, Presentation, Application)
   - Protokoll-Zuordnung und Encapsulation-Prozess
   - TCP/IP-Modell: 4 Schichten im Vergleich zum OSI-Modell
   - IPv4-Adressen: 32-bit, Aufbau, private/public Ranges (RFC 1918), spezielle Adressen (127.0.0.1, 0.0.0.0, 255.255.255.255)
   - IPv6-Adressen: 128-bit, Aufbau, Shortening-Regeln, Adresstypen (Link-Local, Global Unicast, Multicast)
   - Subnetting mit CIDR-Notation: Netzwerk-/Host-Bits berechnen, Subnetz-Aufteilung, praktische Anwendungen
   - Mermaid-Diagramme für Visualisierungen (OSI-Schichten, TCP/IP-Vergleich, Sequenz, State, Class, Pipeline)
   
   **Netzwerktechnik Grundlagen & Protokolle – Teil 2** (V16)
   - TCP vs. UDP: Verbindungsorientiert vs. verbindungslos
   - HTTP/HTTPS und das Request-Response-Modell
   - REST-APIs: Prinzipien und Methoden
   - DNS: Name Resolution und Hierarchie
   - Ports und Socket-Kommunikation

12. **Kryptografie – Teil 1** (V17) ✅
    - Kryptografie-Grundlagen: Geschichte (Caesar-Chiffre), Kerckhoffs' Prinzip
    - Symmetrische Verschlüsselung: DES (Data Encryption Standard), AES (Advanced Encryption Standard)
    - Asymmetrische Verschlüsselung: RSA (Rivest-Shamir-Adleman) mit mathematischen Details
    - RSA-Workflow: Schlüsselerzeugung, Verschlüsselung, Entschlüsselung
    - Hybrid-Verschlüsselung: Kombination von symmetrisch + asymmetrisch für große Datenmengen
    - Schlüsselaustausch-Problematik und Lösungsansätze
    - Anwendungsbeispiele: HTTPS, E-Mail-Verschlüsselung, VPN
    
    **Kryptografie – Teil 2** (V18)
    - Hash-Funktionen und deren Eigenschaften (SHA-256, MD5)
    - Public-Key-Infrastruktur (PKI) und Zertifikate
    - Digitale Signaturen zur Authentifizierung
    - Anwendungsbeispiele: TLS/SSL, HTTPS
    - Passwort-Hashing und Salting

13. **Datenbanken – Teil 1** (V19)
    - Relationale Datenbanken und das Tabellenmodell
    - Entitäten, Attribute und Beziehungen
    - SQL-Grundlagen: SELECT, FROM, WHERE
    - SQL-DML: INSERT, UPDATE, DELETE
    - Primär- und Fremdschlüssel zur Datenintegrität
    - JOINs: INNER, LEFT, RIGHT, FULL
    - Aggregatfunktionen: COUNT, SUM, AVG, MIN, MAX
    
    **Datenbanken – Teil 2** (V20)
    - Normalisierung (1NF, 2NF, 3NF)
    - Indizes zur Performance-Optimierung
    - Transaktionen und ACID-Prinzipien
    - NoSQL-Datenbanken: Wann und warum?
    - MongoDB, Redis, Cassandra im Überblick
    - KI und Datenbanken: Vector Databases für Embeddings

---

### Python Reihenfolge

1. **Python Get Started: Variablen, print, input** (V01)
   - Installation und Entwicklungsumgebungen (IDLE, VS Code, PyCharm)
   - Erste Programme: Ausgabe mit `print()`
   - Variablen deklarieren und zuweisen
   - Benutzereingaben mit `input()` einlesen
   - Kommentare für lesbaren Code

2. **Eingaben/Ausgaben & Formatierung** (V02)
   - String-Formatierung (f-Strings, `.format()`, %-Operator)
   - Zahlen formatieren (Dezimalstellen, Tausender-Trenner)
   - Ausgaben in Dateien schreiben und Dateien einlesen
   - `print()`-Parameter: `sep`, `end`, `file`
   - Escape-Sequenzen und mehrzeilige Strings

3. **Variablen Management & Datentypen** (V03)
   - Grundlegende Datentypen: `int`, `float`, `str`, `bool`
   - Type Casting und Type Checking (`int()`, `type()`, `isinstance()`)
   - Unveränderliche vs. veränderliche Typen (Immutable vs. Mutable)
   - Variablen-Scope: Lokal vs. Global
   - Multiple Assignment und Value Unpacking

4. **Logische Ausdrücke (Boolsche Algebra)** (V04)
   - Vergleichsoperatoren (`==`, `!=`, `<`, `>`, `<=`, `>=`)
   - Logische Operatoren (`and`, `or`, `not`)
   - Wahrheitswerte und Kurzschlussauswertung (Short-Circuit Evaluation)
   - Komplexe Bedingungen formulieren und vereinfachen
   - Truthy und Falsy Values in Python

5. **Verzweigungen (if, if-elif-else)** (V05)
   - Einfache `if`-Anweisungen
   - `if-else` für binäre Entscheidungen
   - `if-elif-else` für mehrfache Verzweigungen
   - Verschachtelte Bedingungen und deren Lesbarkeit
   - Ternärer Operator für kompakte Ausdrücke

6. **Schleifen (for, while) – Teil 1** (V06)
   - `for`-Schleifen mit `range()` 
   - Iterieren über Listen, Strings und andere Iterables
   - `while`-Schleifen mit Abbruchbedingungen
   - Endlos-Schleifen vermeiden
   
   **Schleifen (for, while) – Teil 2** (V07)
   - `break` und `continue` zur Schleifensteuerung
   - Verschachtelte Schleifen und deren Komplexität
   - `else`-Klausel bei Schleifen
   - List Comprehensions als kompakte Alternative
   - Praktische Übungen: Muster, Zahlenreihen, Algorithmen

7. **Listen & Datenstrukturen** (V08) ✅
   - Listen erstellen, indexieren und slicen
   - Wichtige List-Methoden: `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `clear()`, `index()`, `count()`, `sort()`, `reverse()`, `copy()`
   - Tupel als unveränderliche Listen
   - Built-in Funktionen: `sorted()`, `sum()`, `all()`, `any()`, `zip()`
   - Operatoren für Listen: `+`, `*`, `in`, `del`
   - Slicing und Extended Unpacking
   - Aliasing vs. Copying (Shallow vs. Deep Copy)
   - Listen als Stacks (LIFO) und Queues (FIFO)

8. **Try-Catch (Fehlerbehandlung)** (V09) ✅
   - Exception-Konzept: Fehlerbehandlung statt Programmabsturz
   - `try-except`-Blöcke: Code gegen Fehler absichern
   - `else`-Klausel: Code für erfolgreichen Try-Block
   - `finally`-Klausel: Cleanup-Code der immer läuft
   - Mehrere Exception-Typen abfangen: Spezifisch vs. generisch
   - Exception-Objekte: Zugriff mit `as e`, Fehlermeldungen extrahieren
   - `raise`-Statement: Eigene Exceptions werfen
   - Benutzerdefinierte Exceptions: Von `Exception` ableiten
   - Exception-Hierarchie: ValueError, TypeError, KeyError, FileNotFoundError, PermissionError, IndexError, ZeroDivisionError
   - JSON-Modul: `json.load()`, `json.dump()`, `json.JSONDecodeError`
   - Best Practices: EAFP-Prinzip ("Easier to Ask for Forgiveness than Permission")
   - Anwendung: Robuste Eingabe-Validierung, Datei-Operationen, Konfigurationssysteme

9. **Methoden/Funktionen – Teil 1** (V10) ✅
   - Funktionen definieren mit `def`
   - Parameter und Rückgabewerte (`return`)
   - Default-Parameter und ihre Fallstricke
   - Positionale vs. Keyword Arguments
   - Multiple Return Values als Tupel
   - Funktionen als First-Class Objects
   - Scope und LEGB-Regel (Local, Enclosing, Global, Built-in)
   - Docstrings für Dokumentation
   - Zeit-Messung mit `time.time()`
   
   **Methoden/Funktionen – Teil 2** (V11) ✅
   - Keyword-Only Arguments mit `*` Separator
   - `*args` für variable Anzahl positionaler Parameter (Tupel)
   - `**kwargs` für variable Anzahl benannter Parameter (Dictionary)
   - Vollständige Parametersignatur: Reihenfolge und Kombinationen
   - Unpacking-Operatoren: `*iterable` und `**dict` bei Aufrufen und Definitionen
   - Dictionary Merging mit `{**dict1, **dict2}`
   - Lambda-Funktionen: Syntax, Verwendung, Einschränkungen
   - Funktionale Programmierung: `map()`, `filter()` vs. List Comprehensions
   - Type Hints (PEP 484): Parameter- und Rückgabewert-Annotationen
   - `typing`-Modul: `List`, `Dict`, `Optional`, `Union`, `Any`, `Callable`
   - Docstring-Formate: Google Style vs. NumPy Style
   - JSON mit `indent` und `ensure_ascii` für schöne Formatierung
   - DateTime: `.isoformat()` und `.strftime()` für Zeitstempel
   - Fehlertolerante Batch-Verarbeitung mit `try-except` in Schleifen
   - Praktische Übungen: Log-Formatter, Statistik-Funktion, LLM API-Wrapper, Conversation Manager mit Persistenz

10. **Imports & Code auf mehrere Dateien verteilen** (V12) ✅
    - Module importieren: `import`, `from ... import`, `as` Aliase
    - Eigene Module erstellen und organisieren
    - Packages und `__init__.py`, `__all__` für Public API
    - `if __name__ == "__main__":` Pattern für Dual-Use-Module
    - Relative vs. absolute Imports in Package-Hierarchien
    - Virtuelle Umgebungen: `python -m venv`, `pip freeze`, `requirements.txt`
    - CLI-Tools mit `argparse`: ArgumentParser, add_argument()
    - Praktische Übungen: Eigene Module, Packages mit Submodulen, venv-basiertes CLI-Tool

11. **Plots & Grafiken (Matplotlib) – Teil 1** (V13)
    - Matplotlib installieren und importieren
    - Grundlegende Plot-Typen: Liniendiagramme
    - Achsenbeschriftung, Titel und Legenden
    - Scatter Plots für Datenpunkte
    - Farben und Marker anpassen
    
    **Plots & Grafiken (Matplotlib) – Teil 2** (V14)
    - Bar Charts und Histogramme
    - Mehrere Plots in einer Figure (Subplots)
    - Verschiedene Achsenskalierungen (logarithmisch, etc.)
    - Anpassung: Linien-Stile, Füllungen, Annotationen
    - Plots speichern in verschiedenen Formaten (PNG, PDF, SVG)
    - Praktische Übung: Messdaten visualisieren

12. **Große Datenmengen verarbeiten – Teil 1** (V15) ✅
    - Speicher-effizientes Einlesen großer Dateien: for-Schleife auf file-Objekt vs. readlines()
    - Generator-Konzept: yield-Keyword, Lazy Evaluation, Memory-Effizienz O(1) vs. O(n)
    - Generator-Funktionen: Countdown-Beispiel, Zeilen-Filter, Pipeline-Architektur
    - Generator-Pipelines: Verkettung für Daten-Transformation (Extract-Transform-Load)
    - Iterator-Protokoll: __iter__() und __next__(), StopIteration
    - Iterator vs. Iterable: Unterschiede, Exhaustion-Problem, mehrfache Iteration
    - Praktische Iterator-Beispiele: CountDown-Klasse, Fibonacci-Iterator
    - CSV-Modul: csv.reader(), csv.writer(), csv.DictReader(), csv.DictWriter()
    - CSV Best Practices: newline=''-Parameter unter Windows, Encoding, delimiter
    - Built-in Funktionen: iter(), next() mit default-Parameter
    - itertools.tee(): Generator klonen für mehrfache Analysen
    - Anwendungen: Log-Datei-Analyse mit Generator-Pipeline, E-Commerce ETL mit decimal.Decimal
    
    **Große Datenmengen verarbeiten – Teil 2** (V16)
    - Pandas: Installation und erste Schritte
    - DataFrames erstellen und manipulieren
    - Daten filtern, sortieren und aggregieren
    - Performance-Tipps: Vektorisierung statt Schleifen
    - Praktische Übung: Analyse eines Datensatzes

13. **Netzwerk-Programmierung (Basics: Socket, HTTP) – Teil 1** (V17) ✅
    - Socket-Modul: socket.socket(), Konstanten (AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR)
    - Server-Socket-Methoden: .bind(), .listen(), .accept()
    - Client-Socket-Methoden: .connect()
    - Datenübertragung: .send(), .sendall(), .recv() mit Byte-Encoding/Decoding
    - Socket-Verwaltung: .close(), .setsockopt(), .settimeout()
    - TCP/IP Client-Server-Architektur: Ablauf und Best Practices
    - Multi-Client-Server: Sequenzielle Verarbeitung, Threading (Vorschau)
    - HMAC-ähnliche Authentifizierung: hashlib.sha256(), .hexdigest(), Message Authentication Codes
    - Praktische Übungen: Echo-Server, CNC-Temperatur-Monitor (JSON), Multi-Client Sensor-Server, Roboter-Steuerung, Sichere Maschinen-Kommunikation
    
    **Netzwerk-Programmierung (Basics: Socket, HTTP) – Teil 2** (V18)
    - HTTP-Protokoll verstehen
    - HTTP-Requests mit `requests`-Bibliothek
    - GET und POST Requests
    - JSON-Daten über APIs abrufen und parsen
    - Status Codes und Error Handling
    - Praktische Übung: Wetter-API oder ähnliches nutzen

14. **Datenbankverbindung & SQL – Teil 1** (V19)
    - SQLite: Eingebettete Datenbank ohne Server
    - Verbindung herstellen mit `sqlite3`-Modul
    - Tabellen erstellen (CREATE TABLE)
    - Daten einfügen (INSERT)
    - Einfache Queries (SELECT)
    
    **Datenbankverbindung & SQL – Teil 2** (V20)
    - Prepared Statements gegen SQL-Injection
    - Daten aktualisieren (UPDATE) und löschen (DELETE)
    - Transaktionen: Commit und Rollback
    - Cursor-Objekte und fetchall()/fetchone()
    - Context Manager für sichere Verbindungen
    - Praktische Übung: Datenbank für KI-Training-Logs erstellen