"""
V17-P4: Roboter-Client (TEST-PROGRAMM)

Dieses Programm testet deinen Roboter-Steuerungs-Server.
Starte ZUERST deinen Server auf Port 7000, dann dieses Programm.
"""

import socket
import json
import time

def send_robot_command(befehl_dict):
    """
    Sendet einen Befehl an Roboter-Server und gibt Antwort zurück.
    
    Args:
        befehl_dict (dict): Befehl als Dictionary
    
    Returns:
        dict or None: Server-Antwort
    """
    
    try:
        # Verbinde zu Server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 7000))
        
        # Sende Befehl
        befehl_json = json.dumps(befehl_dict)
        client_socket.sendall(befehl_json.encode("utf-8"))
        
        # Empfange Antwort
        antwort_bytes = client_socket.recv(4096)
        antwort_json = antwort_bytes.decode("utf-8")
        antwort = json.loads(antwort_json)
        
        # Schließe Verbindung
        client_socket.close()
        
        return antwort
        
    except ConnectionRefusedError:
        print(f"❌ FEHLER: Konnte nicht verbinden. Läuft dein Server auf Port 7000?")
        return None
    except json.JSONDecodeError:
        print(f"❌ FEHLER: Server-Antwort ist kein gültiges JSON")
        return None
    except Exception as e:
        print(f"❌ FEHLER: {type(e).__name__}: {e}")
        return None

def main():
    """Führt Testsequenz für Roboter-Server durch."""
    
    print("=== Roboter-Steuerungs-Server Test ===")
    print("Stelle sicher, dass dein Server auf Port 7000 läuft!\n")
    
    tests_bestanden = 0
    tests_gesamt = 7
    
    # Test 1: STATUS-Abfrage (Initial)
    print("🧪 TEST 1: STATUS-Abfrage (Initial)")
    antwort = send_robot_command({"befehl": "STATUS"})
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("position") == [0, 0, 0] and antwort.get("greifer") == "offen" and antwort.get("batterie") == 100:
            print("✅ Test bestanden: Initial-Zustand korrekt\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Initial-Zustand inkorrekt\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    time.sleep(0.5)
    
    # Test 2: BEWEGE-Befehl
    print("🧪 TEST 2: BEWEGE zu Position (100, 50, 30)")
    antwort = send_robot_command({"befehl": "BEWEGE", "x": 100, "y": 50, "z": 30})
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("position") == [100, 50, 30] and antwort.get("batterie") == 95:
            print("✅ Test bestanden: Bewegung korrekt, Batterie -5%\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Position oder Batterie inkorrekt\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    time.sleep(0.5)
    
    # Test 3: GREIFE-Befehl
    print("🧪 TEST 3: GREIFE (Greifer schließen)")
    antwort = send_robot_command({"befehl": "GREIFE"})
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("greifer") == "geschlossen" and antwort.get("batterie") == 93:
            print("✅ Test bestanden: Greifer geschlossen, Batterie -2%\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Greifer-Status oder Batterie inkorrekt\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    time.sleep(0.5)
    
    # Test 4: OEFFNE-Befehl
    print("🧪 TEST 4: OEFFNE (Greifer öffnen)")
    antwort = send_robot_command({"befehl": "OEFFNE"})
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("greifer") == "offen" and antwort.get("batterie") == 91:
            print("✅ Test bestanden: Greifer geöffnet, Batterie -2%\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Greifer-Status oder Batterie inkorrekt\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    time.sleep(0.5)
    
    # Test 5: STATUS-Abfrage (nach Befehlen)
    print("🧪 TEST 5: STATUS-Abfrage (nach Befehlen)")
    antwort = send_robot_command({"befehl": "STATUS"})
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("position") == [100, 50, 30] and antwort.get("batterie") == 91:
            print("✅ Test bestanden: Zustand korrekt gespeichert\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Zustand inkorrekt\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    time.sleep(0.5)
    
    # Test 6: Batterie auf kritischen Wert bringen
    print("🧪 TEST 6: Batterie-Warnung testen (mehrfache Bewegungen)")
    print("   Führe mehrere Bewegungen aus, um Batterie < 10% zu bringen...")
    
    for i in range(18):  # 18 Bewegungen à 5% = 90% Verbrauch
        send_robot_command({"befehl": "BEWEGE", "x": i*10, "y": i*5, "z": i*2})
        time.sleep(0.1)
    
    antwort = send_robot_command({"befehl": "STATUS"})
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("batterie") <= 10 and "warnung" in antwort:
            print("✅ Test bestanden: Batterie-Warnung bei < 10%\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Keine Batterie-Warnung\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    time.sleep(0.5)
    
    # Test 7: Unbekannter Befehl
    print("🧪 TEST 7: Unbekannter Befehl (Fehlerbehandlung)")
    antwort = send_robot_command({"befehl": "FLIEGE"})
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("status") == "FEHLER":
            print("✅ Test bestanden: Fehler bei unbekanntem Befehl\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Kein Fehler bei unbekanntem Befehl\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    # Zusammenfassung
    print("\n" + "="*50)
    print("📊 ZUSAMMENFASSUNG")
    print("="*50)
    print(f"🎯 Ergebnis: {tests_bestanden}/{tests_gesamt} Tests bestanden")
    
    if tests_bestanden == tests_gesamt:
        print("🎉 PERFEKT! Dein Roboter-Server funktioniert korrekt!")
    elif tests_bestanden >= 5:
        print("👍 Gut! Noch kleine Verbesserungen möglich.")
    else:
        print("📚 Überprüfe deine Server-Logik nochmal.")

if __name__ == "__main__":
    main()
