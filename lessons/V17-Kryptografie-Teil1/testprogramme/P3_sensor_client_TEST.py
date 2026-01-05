"""
V17-P3: Sensor-Client (TEST-PROGRAMM)

Dieses Programm simuliert mehrere Sensoren und testet deinen Server.
Starte ZUERST deinen Server auf Port 6000, dann dieses Programm.
"""

import socket
import json
import time

def send_sensor_data(maschine_id, drehzahl, vibration, temperatur):
    """
    Sendet Sensordaten an Server und zeigt Antwort an.
    
    Args:
        maschine_id (str): ID der Maschine
        drehzahl (int): Drehzahl in RPM
        vibration (float): Vibration in mm/s
        temperatur (float): Temperatur in °C
    
    Returns:
        dict or None: Server-Antwort als Dictionary
    """
    
    try:
        # Verbinde zu Server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 6000))
        
        # Erstelle JSON-Daten
        daten = {
            "maschine_id": maschine_id,
            "drehzahl": drehzahl,
            "vibration": vibration,
            "temperatur": temperatur
        }
        daten_json = json.dumps(daten, indent=2)
        
        # Sende Daten
        client_socket.sendall(daten_json.encode("utf-8"))
        print(f"📤 {maschine_id}: Daten gesendet")
        print(f"   Drehzahl: {drehzahl} RPM, Vibration: {vibration} mm/s, Temp: {temperatur}°C")
        
        # Empfange Antwort
        antwort_bytes = client_socket.recv(1024)
        antwort_json = antwort_bytes.decode("utf-8")
        antwort = json.loads(antwort_json)
        
        # Zeige Antwort
        print(f"📥 Antwort: Status={antwort.get('status')}")
        if antwort.get("warnungen"):
            print(f"   ⚠️ Warnungen: {antwort['warnungen']}")
        else:
            print(f"   ✅ Keine Warnungen")
        
        # Schließe Verbindung
        client_socket.close()
        print()
        
        return antwort
        
    except ConnectionRefusedError:
        print(f"❌ FEHLER: Konnte nicht verbinden. Läuft dein Server auf Port 6000?")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ FEHLER: Server-Antwort ist kein gültiges JSON")
        return None
    except Exception as e:
        print(f"❌ FEHLER: {type(e).__name__}: {e}")
        return None

def main():
    """Simuliert mehrere Sensoren mit verschiedenen Messwerten."""
    
    print("=== Multi-Client Sensor-Server Test ===")
    print("Stelle sicher, dass dein Server auf Port 6000 läuft!\n")
    print("Simuliere 5 verschiedene Maschinen mit unterschiedlichen Zuständen...\n")
    
    # Test 1: Normale Werte (keine Warnungen)
    print("🧪 TEST 1: Normale Betriebswerte")
    antwort1 = send_sensor_data("Drehmaschine-01", 8000, 2.5, 65.0)
    time.sleep(0.5)  # Kurze Pause zwischen Tests
    
    # Test 2: Hohe Drehzahl (1 Warnung)
    print("🧪 TEST 2: Zu hohe Drehzahl")
    antwort2 = send_sensor_data("Drehmaschine-02", 12000, 3.0, 68.0)
    time.sleep(0.5)
    
    # Test 3: Hohe Vibration (1 Warnung)
    print("🧪 TEST 3: Zu hohe Vibration")
    antwort3 = send_sensor_data("Fräsmaschine-01", 9000, 6.5, 70.0)
    time.sleep(0.5)
    
    # Test 4: Hohe Temperatur (1 Warnung)
    print("🧪 TEST 4: Zu hohe Temperatur")
    antwort4 = send_sensor_data("CNC-03", 8500, 3.2, 85.0)
    time.sleep(0.5)
    
    # Test 5: Multiple Warnungen (alle 3 kritisch)
    print("🧪 TEST 5: Kritischer Zustand (alle Werte zu hoch)")
    antwort5 = send_sensor_data("Drehmaschine-03", 11000, 7.0, 90.0)
    time.sleep(0.5)
    
    # Zusammenfassung
    print("\n" + "="*50)
    print("📊 ZUSAMMENFASSUNG")
    print("="*50)
    
    tests_bestanden = 0
    
    if antwort1 and len(antwort1.get("warnungen", [])) == 0:
        print("✅ Test 1: Keine Warnungen bei normalen Werten")
        tests_bestanden += 1
    else:
        print("❌ Test 1: Fehlgeschlagen")
    
    if antwort2 and "Drehzahl" in str(antwort2.get("warnungen", [])):
        print("✅ Test 2: Drehzahl-Warnung erkannt")
        tests_bestanden += 1
    else:
        print("❌ Test 2: Fehlgeschlagen")
    
    if antwort3 and "Vibration" in str(antwort3.get("warnungen", [])):
        print("✅ Test 3: Vibrations-Warnung erkannt")
        tests_bestanden += 1
    else:
        print("❌ Test 3: Fehlgeschlagen")
    
    if antwort4 and "Temperatur" in str(antwort4.get("warnungen", [])):
        print("✅ Test 4: Temperatur-Warnung erkannt")
        tests_bestanden += 1
    else:
        print("❌ Test 4: Fehlgeschlagen")
    
    if antwort5 and len(antwort5.get("warnungen", [])) == 3:
        print("✅ Test 5: Alle 3 Warnungen erkannt")
        tests_bestanden += 1
    else:
        print("❌ Test 5: Fehlgeschlagen")
    
    print(f"\n🎯 Ergebnis: {tests_bestanden}/5 Tests bestanden")
    
    if tests_bestanden == 5:
        print("🎉 PERFEKT! Dein Server funktioniert korrekt!")
    elif tests_bestanden >= 3:
        print("👍 Gut! Noch kleine Verbesserungen möglich.")
    else:
        print("📚 Überprüfe deine Server-Logik nochmal.")

if __name__ == "__main__":
    main()
