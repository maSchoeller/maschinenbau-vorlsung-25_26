"""
V17-P2: CNC-Temperatur-Client (TEST-PROGRAMM)

Dieses Programm testet deinen Temperatur-Server.
Starte ZUERST deinen Server auf Port 5555, dann dieses Programm.
"""

import socket
import json

def test_temperatur_server(maschine_id, temperatur):
    """
    Sendet Temperaturdaten an Server und zeigt Antwort an.
    
    Args:
        maschine_id (str): ID der CNC-Maschine
        temperatur (float): Gemessene Temperatur in °C
    """
    
    try:
        # Verbinde zu Server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 5555))
        print(f"✅ Verbunden mit Temperatur-Server")
        
        # Erstelle JSON-Daten
        daten = {
            "maschine_id": maschine_id,
            "temperatur": temperatur
        }
        daten_json = json.dumps(daten)
        
        # Sende Daten
        client_socket.sendall(daten_json.encode("utf-8"))
        print(f"📤 Gesendet: {daten_json}")
        
        # Empfange Antwort
        antwort_bytes = client_socket.recv(1024)
        antwort_json = antwort_bytes.decode("utf-8")
        antwort = json.loads(antwort_json)
        
        # Zeige Antwort formatiert
        print(f"📥 Antwort vom Server:")
        print(f"   Status: {antwort.get('status', 'N/A')}")
        print(f"   Meldung: {antwort.get('meldung', 'N/A')}")
        
        # Schließe Verbindung
        client_socket.close()
        print("✅ Verbindung geschlossen\n")
        
        return antwort
        
    except ConnectionRefusedError:
        print("❌ FEHLER: Konnte nicht verbinden. Läuft dein Server auf Port 5555?")
        return None
    except json.JSONDecodeError:
        print(f"❌ FEHLER: Server-Antwort ist kein gültiges JSON: {antwort_json}")
        return None
    except Exception as e:
        print(f"❌ FEHLER: {type(e).__name__}: {e}")
        return None

def main():
    """Führt mehrere Tests mit verschiedenen Temperaturen durch."""
    
    print("=== CNC-Temperatur-Server Test ===")
    print("Stelle sicher, dass dein Server auf Port 5555 läuft!\n")
    
    # Test 1: Normale Temperatur (< 60°C)
    print("🧪 TEST 1: Normale Temperatur (55°C)")
    antwort1 = test_temperatur_server("CNC-01", 55.0)
    if antwort1 and antwort1.get("status") == "OK":
        print("✅ Test 1 bestanden: Status OK für normale Temperatur\n")
    else:
        print("❌ Test 1 fehlgeschlagen\n")
    
    # Test 2: Erhöhte Temperatur (60-80°C)
    print("🧪 TEST 2: Erhöhte Temperatur (72°C)")
    antwort2 = test_temperatur_server("CNC-02", 72.0)
    if antwort2 and antwort2.get("status") == "WARNUNG":
        print("✅ Test 2 bestanden: Status WARNUNG für erhöhte Temperatur\n")
    else:
        print("❌ Test 2 fehlgeschlagen\n")
    
    # Test 3: Kritische Temperatur (>= 80°C)
    print("🧪 TEST 3: Kritische Temperatur (85°C)")
    antwort3 = test_temperatur_server("CNC-03", 85.0)
    if antwort3 and antwort3.get("status") == "KRITISCH":
        print("✅ Test 3 bestanden: Status KRITISCH für hohe Temperatur\n")
    else:
        print("❌ Test 3 fehlgeschlagen\n")
    
    # Test 4: Grenzwert-Test (exakt 60°C)
    print("🧪 TEST 4: Grenzwert (exakt 60°C)")
    antwort4 = test_temperatur_server("CNC-04", 60.0)
    if antwort4 and antwort4.get("status") == "WARNUNG":
        print("✅ Test 4 bestanden: Status WARNUNG bei Grenzwert\n")
    else:
        print("❌ Test 4 fehlgeschlagen\n")
    
    print("=== Alle Tests abgeschlossen ===")

if __name__ == "__main__":
    main()
