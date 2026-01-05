# V17 Testprogramme - Netzwerk-Programmierung

Dieses Verzeichnis enthält **Testprogramme** und **Vorlagen** für die Python-Übungsaufgaben V17.

## Übersicht

| Aufgabe | Datei | Beschreibung |
|---------|-------|--------------|
| **P1** | `P1_echo_server_VORLAGE.py` | Vorlage für Echo-Server (zum Vervollständigen) |
| **P1** | `P1_echo_client_TEST.py` | Test-Client für deinen Echo-Server |
| **P2** | `P2_cnc_temp_client_TEST.py` | Test-Client für deinen Temperatur-Server |
| **P3** | `P3_sensor_client_TEST.py` | Test-Client für deinen Sensor-Server |
| **P4** | `P4_robot_client_TEST.py` | Test-Client für deinen Roboter-Server |
| **P5** | `P5_secure_client_TEST.py` | Test-Client für deinen Secure Machine Server |

## Nutzung

### Workflow für jede Aufgabe:

1. **Schreibe deinen Server** gemäß Aufgabenstellung
2. **Starte deinen Server** in einem Terminal
3. **Führe das Test-Programm aus** in einem zweiten Terminal
4. **Prüfe die Ausgabe**: ✅ = Test bestanden, ❌ = Fehler gefunden

### Beispiel: Aufgabe P2 (Temperatur-Monitor)

```bash
# Terminal 1: Starte deinen Server
python cnc_temp_server.py

# Terminal 2: Führe Test aus
python testprogramme/P2_cnc_temp_client_TEST.py
```

Das Test-Programm sendet automatisch verschiedene Temperaturwerte und prüft, ob dein Server korrekt antwortet.

## Aufgabendetails

### P1: Echo-Server
- **Vorlage**: `P1_echo_server_VORLAGE.py` – Vervollständige die TODO-Abschnitte
- **Test**: `P1_echo_client_TEST.py` – Testet deinen fertigen Server
- **Port**: 9000

### P2: CNC-Temperatur-Monitor
- **Deine Aufgabe**: Schreibe `cnc_temp_server.py`
- **Test**: `P2_cnc_temp_client_TEST.py` – Sendet 4 Tests mit verschiedenen Temperaturen
- **Port**: 5555
- **Tests**:
  - Normale Temperatur (55°C) → Status: OK
  - Erhöhte Temperatur (72°C) → Status: WARNUNG
  - Kritische Temperatur (85°C) → Status: KRITISCH
  - Grenzwert (60°C) → Status: WARNUNG

### P3: Multi-Client Sensor-Server
- **Deine Aufgabe**: Schreibe `sensor_server.py`
- **Test**: `P3_sensor_client_TEST.py` – Simuliert 5 verschiedene Maschinen
- **Port**: 6000
- **Tests**:
  - Normale Werte → Keine Warnungen
  - Hohe Drehzahl (>10000) → Warnung
  - Hohe Vibration (>5.0) → Warnung
  - Hohe Temperatur (>80) → Warnung
  - Multiple Kritische Werte → Alle Warnungen

### P4: Roboter-Steuerungs-Server
- **Deine Aufgabe**: Schreibe `robot_server.py`
- **Test**: `P4_robot_client_TEST.py` – Sendet 7 Tests mit verschiedenen Befehlen
- **Port**: 7000
- **Tests**:
  - STATUS (Initial) → Position [0,0,0], Greifer offen, Batterie 100%
  - BEWEGE → Position aktualisiert, Batterie -5%
  - GREIFE → Greifer geschlossen, Batterie -2%
  - OEFFNE → Greifer geöffnet, Batterie -2%
  - STATUS (nach Befehlen) → Zustand korrekt gespeichert
  - Batterie-Warnung → Warnung bei Batterie ≤ 10%
  - Unbekannter Befehl → Fehler-Antwort

### P5: Secure Machine Server
- **Deine Aufgabe**: Schreibe `secure_machine_server.py`
- **Test**: `P5_secure_client_TEST.py` – Testet Authentifizierung mit 6 Tests
- **Port**: 8000
- **Tests**:
  - START_PRODUKTION (auth) → Status: OK
  - STOPP_PRODUKTION (auth) → Status: OK
  - NOTAUS (auth) → Status: OK
  - Manipulierter Hash → Status: FEHLER (Angriff erkannt!)
  - Verschiedene Maschinen-IDs → Funktioniert
  - Ohne Auftrag-ID → Funktioniert

## Tipps

### Zwei Terminals gleichzeitig verwenden

**VS Code:**
1. Terminal öffnen: `Strg + ö` (oder View → Terminal)
2. Neues Terminal: Klick auf `+` Symbol oder `Strg + Shift + ö`
3. Zwischen Terminals wechseln: Dropdown-Menü oben rechts

**Windows (PowerShell/CMD):**
- Öffne zwei separate Fenster
- In einem: Server starten
- Im anderen: Test-Programm ausführen

**Linux/Mac:**
- Verwende `tmux` oder `screen` für Split-Terminals
- Oder öffne zwei Terminal-Fenster

### Debugging-Tipps

**Server antwortet nicht:**
- Prüfe, ob Server läuft und auf richtiger Port hört
- Prüfe `server_socket.bind()` Adresse: `("localhost", PORT)`
- Prüfe Firewall-Einstellungen (meist kein Problem bei localhost)

**JSON-Fehler:**
- Stelle sicher, dass du `json.dumps()` beim Senden verwendest
- Stelle sicher, dass du `json.loads()` beim Empfangen verwendest
- Prüfe, ob `.encode("utf-8")` und `.decode("utf-8")` verwendet werden

**Socket bleibt hängen:**
- Verwende `server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
- Beende Server mit `Strg+C` und warte 30 Sekunden, bevor du neu startest
- Oder ändere Port-Nummer temporär

**Test schlägt fehl:**
- Lies die Fehlermeldung genau durch
- Prüfe Server-Ausgabe im ersten Terminal
- Vergleiche erwartete mit tatsächlicher Antwort
- Prüfe JSON-Struktur und Feld-Namen

## Weitere Ressourcen

- **Vorlesungsskript**: `V17-Kryptografie-Teil1_skript.md` (Python-Teil)
- **Aufgabenstellung**: `V17-Kryptografie-Teil1_aufgaben.md`
- **Musterlösungen**: `V17-Kryptografie-Teil1_loesungen.md` (erst nach eigenem Versuch ansehen!)

## Erweiterungen (Optional)

Nach erfolgreicher Implementierung der Grundaufgaben kannst du folgende Erweiterungen ausprobieren:

1. **Multi-Threading**: Server kann mehrere Clients **gleichzeitig** bedienen
2. **Logging**: Schreibe alle Anfragen in eine Log-Datei
3. **GUI**: Verwende `tkinter` für eine grafische Oberfläche
4. **Datenbank**: Speichere Sensordaten in SQLite
5. **Echte Verschlüsselung**: Verwende `cryptography`-Bibliothek für AES/RSA

---

**Viel Erfolg bei den Übungen!** 🚀
