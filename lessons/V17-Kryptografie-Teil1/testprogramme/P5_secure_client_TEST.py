"""
V17-P5: Secure Machine Client (TEST-PROGRAMM)

Dieses Programm testet deinen Secure Machine Server mit verschiedenen Szenarien.
Starte ZUERST deinen Server auf Port 8000, dann dieses Programm.
"""

import socket
import json
import hashlib

# Gemeinsames Geheimnis (MUSS mit Server übereinstimmen!)
SECRET_KEY = "GEHEIM_CNC_2024"

def berechne_hash(befehl, maschine_id, auftrag_id):
    """
    Berechnet SHA-256 Hash für Authentifizierung.
    
    Args:
        befehl (str): Befehlsname
        maschine_id (str): Maschinen-ID
        auftrag_id (str or None): Auftrag-ID
    
    Returns:
        str: Hexadezimaler Hash-String
    """
    data_string = f"{befehl}|{maschine_id}|{auftrag_id or ''}|{SECRET_KEY}"
    hash_object = hashlib.sha256(data_string.encode("utf-8"))
    return hash_object.hexdigest()

def send_command(befehl, maschine_id, auftrag_id=None, manipuliere_hash=False):
    """
    Sendet authentifizierten Befehl an Server.
    
    Args:
        befehl (str): Befehlsname
        maschine_id (str): Maschinen-ID
        auftrag_id (str or None): Auftrag-ID (optional)
        manipuliere_hash (bool): Wenn True, sende falschen Hash zum Testen
    
    Returns:
        dict or None: Server-Antwort
    """
    
    try:
        # Verbinde zu Server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 8000))
        
        # Berechne Hash
        if manipuliere_hash:
            hash_value = "FALSCHER_HASH_12345"
        else:
            hash_value = berechne_hash(befehl, maschine_id, auftrag_id)
        
        # Erstelle Befehl
        befehl_dict = {
            "befehl": befehl,
            "maschine_id": maschine_id,
            "auftrag_id": auftrag_id,
            "hash": hash_value
        }
        
        # Sende Befehl
        befehl_json = json.dumps(befehl_dict)
        client_socket.sendall(befehl_json.encode("utf-8"))
        
        # Empfange Antwort
        antwort_bytes = client_socket.recv(1024)
        antwort_json = antwort_bytes.decode("utf-8")
        antwort = json.loads(antwort_json)
        
        # Schließe Verbindung
        client_socket.close()
        
        return antwort
        
    except ConnectionRefusedError:
        print(f"❌ FEHLER: Konnte nicht verbinden. Läuft dein Server auf Port 8000?")
        return None
    except json.JSONDecodeError:
        print(f"❌ FEHLER: Server-Antwort ist kein gültiges JSON")
        return None
    except Exception as e:
        print(f"❌ FEHLER: {type(e).__name__}: {e}")
        return None

def main():
    """Führt Testsequenz für Secure Machine Server durch."""
    
    print("=== Secure Machine Server Test ===")
    print(f"🔑 Shared Secret: {SECRET_KEY}")
    print("Stelle sicher, dass dein Server auf Port 8000 läuft!\n")
    
    tests_bestanden = 0
    tests_gesamt = 6
    
    # Test 1: START_PRODUKTION (authentifiziert)
    print("🧪 TEST 1: START_PRODUKTION (authentifiziert)")
    antwort = send_command("START_PRODUKTION", "CNC-05", "A12345")
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("status") == "OK":
            print("✅ Test bestanden: Befehl authentifiziert und akzeptiert\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Befehl wurde abgelehnt\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    # Test 2: STOPP_PRODUKTION (authentifiziert)
    print("🧪 TEST 2: STOPP_PRODUKTION (authentifiziert)")
    antwort = send_command("STOPP_PRODUKTION", "CNC-05")
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("status") == "OK":
            print("✅ Test bestanden: Befehl authentifiziert\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Befehl wurde abgelehnt\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    # Test 3: NOTAUS (authentifiziert)
    print("🧪 TEST 3: NOTAUS (authentifiziert)")
    antwort = send_command("NOTAUS", "CNC-05")
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("status") == "OK":
            print("✅ Test bestanden: NOTAUS authentifiziert\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Befehl wurde abgelehnt\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    # Test 4: START_PRODUKTION mit manipuliertem Hash (Angriff)
    print("🧪 TEST 4: START_PRODUKTION mit manipuliertem Hash (Angriff)")
    print("⚠️ Simuliere Angreifer mit falschem Hash...")
    antwort = send_command("START_PRODUKTION", "CNC-05", "A99999", manipuliere_hash=True)
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("status") == "FEHLER":
            print("✅ Test bestanden: Angriff erkannt und abgelehnt\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen: Angriff NICHT erkannt (SICHERHEITSLÜCKE!)\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    # Test 5: Verschiedene Maschinen-IDs
    print("🧪 TEST 5: Verschiedene Maschinen-IDs")
    antwort = send_command("START_PRODUKTION", "CNC-10", "B54321")
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("status") == "OK":
            print("✅ Test bestanden: Andere Maschinen-ID funktioniert\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    # Test 6: Befehl ohne Auftrag-ID
    print("🧪 TEST 6: STOPP_PRODUKTION ohne Auftrag-ID")
    antwort = send_command("STOPP_PRODUKTION", "CNC-05", None)
    if antwort:
        print(f"📥 Antwort: {json.dumps(antwort, indent=2)}")
        if antwort.get("status") == "OK":
            print("✅ Test bestanden: Befehl ohne Auftrag-ID funktioniert\n")
            tests_bestanden += 1
        else:
            print("❌ Test fehlgeschlagen\n")
    else:
        print("❌ Test fehlgeschlagen: Keine Antwort\n")
    
    # Zusammenfassung
    print("\n" + "="*60)
    print("📊 ZUSAMMENFASSUNG")
    print("="*60)
    print(f"🎯 Ergebnis: {tests_bestanden}/{tests_gesamt} Tests bestanden")
    
    if tests_bestanden == tests_gesamt:
        print("🎉 PERFEKT! Dein Secure Machine Server ist korrekt implementiert!")
        print("🔒 Sicherheit: Manipulierte Hashes werden erkannt!")
    elif tests_bestanden >= 4:
        print("👍 Gut! Fast alle Tests bestanden.")
        if tests_bestanden < tests_gesamt:
            print("⚠️ Prüfe nochmal die fehlgeschlagenen Tests.")
    else:
        print("📚 Überprüfe deine Server-Logik und Hash-Verifizierung.")
    
    print("\n💡 WICHTIG: Dieses Verfahren ist eine Vereinfachung!")
    print("   In der Praxis: Verwende HMAC (hmac.new()) oder TLS/SSL.")

if __name__ == "__main__":
    main()
