"""
V17-P1: Echo-Server (VORLAGE für Studenten)

Aufgabe: Vervollständige diesen Echo-Server, der eine Nachricht empfängt
         und mit "ECHO: " zurücksendet.

Maschinenbau-Kontext: CNC-Maschinen senden Statusmeldungen an Monitor
"""

import socket

def start_echo_server():
    """Startet den Echo-Server auf Port 9000."""
    
    # TODO: Erstelle Socket mit socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket = None  # Hier deinen Code einfügen
    
    # TODO: Binde Socket an localhost Port 9000 mit .bind()
    
    # TODO: Aktiviere Listening mit .listen()
    
    print("Echo-Server läuft auf Port 9000...")
    
    # TODO: Warte auf Client mit .accept() → gibt (client_socket, address) zurück
    client_socket, address = None, None  # Hier deinen Code einfügen
    print(f"Verbindung von {address}")
    
    # TODO: Empfange Daten mit .recv(1024)
    daten = None  # Hier deinen Code einfügen
    
    # TODO: Dekodiere Bytes zu String mit .decode("utf-8")
    nachricht = None  # Hier deinen Code einfügen
    print(f"Empfangen: {nachricht}")
    
    # TODO: Erstelle Antwort mit Präfix "ECHO: "
    antwort = None  # Hier deinen Code einfügen
    
    # TODO: Sende Antwort mit .sendall() (nicht vergessen: .encode())
    
    print(f"Gesendet: {antwort}")
    
    # TODO: Schließe Sockets mit .close()
    
    print("Verbindung geschlossen")

if __name__ == "__main__":
    start_echo_server()
