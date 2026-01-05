"""
V17-P1: Echo-Client (TEST-PROGRAMM)

Dieses Programm testet deinen Echo-Server.
Starte ZUERST deinen Server, dann dieses Test-Programm.
"""

import socket

def test_echo_server():
    """Testet den Echo-Server mit einer Testnachricht."""
    
    try:
        # Verbinde zu Server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 9000))
        print("✅ Verbunden mit Echo-Server")
        
        # Sende Nachricht
        test_nachricht = "CNC-Maschine #42: Bereit"
        client_socket.sendall(test_nachricht.encode("utf-8"))
        print(f"📤 Gesendet: {test_nachricht}")
        
        # Empfange Antwort
        antwort_bytes = client_socket.recv(1024)
        antwort = antwort_bytes.decode("utf-8")
        print(f"📥 Antwort: {antwort}")
        
        # Prüfe Antwort
        erwartete_antwort = f"ECHO: {test_nachricht}"
        if antwort == erwartete_antwort:
            print("✅ TEST BESTANDEN: Server antwortet korrekt!")
        else:
            print(f"❌ TEST FEHLGESCHLAGEN")
            print(f"   Erwartet: {erwartete_antwort}")
            print(f"   Erhalten: {antwort}")
        
        # Schließe Verbindung
        client_socket.close()
        print("Verbindung geschlossen")
        
    except ConnectionRefusedError:
        print("❌ FEHLER: Konnte nicht verbinden. Läuft dein Server auf Port 9000?")
    except Exception as e:
        print(f"❌ FEHLER: {type(e).__name__}: {e}")

if __name__ == "__main__":
    print("=== Echo-Server Test ===")
    print("Stelle sicher, dass dein Server läuft!\n")
    test_echo_server()
