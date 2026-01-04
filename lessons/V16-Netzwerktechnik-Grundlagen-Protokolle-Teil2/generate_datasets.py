import csv
import random
from datetime import datetime, timedelta

# Generate sensoren_daten_erweitert.csv with >300 rows
print("Generating sensoren_daten_erweitert.csv...")
machines = ['CNC-01', 'CNC-02', 'Presse-01', 'Presse-02', 'Drehbank-01', 'Fraese-01']
sensor_types = ['Temperatur', 'Drehzahl', 'Druck', 'Schwingung']
units = {'Temperatur': '°C', 'Drehzahl': 'RPM', 'Druck': 'bar', 'Schwingung': 'mm/s'}
status_options = ['Normal', 'Warnung', 'Kritisch']

base_time = datetime(2024, 1, 15, 8, 0, 0)
rows = []

sensor_id = 1
for hour in range(24):  # 24 hours
    for minute in range(0, 60, 5):  # Every 5 minutes
        timestamp = base_time + timedelta(hours=hour, minutes=minute)
        for machine in machines:
            for sensor_type in sensor_types:
                # Generate realistic values based on sensor type
                if sensor_type == 'Temperatur':
                    value = random.uniform(60, 110)
                elif sensor_type == 'Drehzahl':
                    value = random.randint(1500, 3500)
                elif sensor_type == 'Druck':
                    value = random.uniform(100, 200)
                else:  # Schwingung
                    value = random.uniform(0.3, 1.5)
                
                # Occasionally mark as warning or critical
                rand_val = random.random()
                if rand_val < 0.05:
                    status = 'Kritisch'
                elif rand_val < 0.15:
                    status = 'Warnung'
                else:
                    status = 'Normal'
                
                rows.append({
                    'Sensor_ID': f'S{sensor_id:04d}',
                    'Maschine': machine,
                    'Typ': sensor_type,
                    'Wert': round(value, 1),
                    'Einheit': units[sensor_type],
                    'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'Status': status
                })
                sensor_id += 1

# Write to CSV
with open('sensoren_daten_erweitert.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Sensor_ID', 'Maschine', 'Typ', 'Wert', 'Einheit', 'Timestamp', 'Status'])
    writer.writeheader()
    writer.writerows(rows)

print(f"✓ Created sensoren_daten_erweitert.csv with {len(rows)} rows")

# Generate produktion_auftrage.csv with >300 rows
print("\nGenerating produktion_auftrage.csv...")
machines_prod = ['CNC-01', 'CNC-02', 'CNC-03', 'Presse-01', 'Presse-02', 'Drehbank-01', 'Drehbank-02', 'Fraese-01']
bauteile = ['Welle-A', 'Flansch-B', 'Gehaeuse-C', 'Bolzen-D', 'Platte-E', 'Buchse-F']
status_prod = ['Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen', 'Verzoegert']  # More completed

base_date = datetime(2024, 1, 1)
prod_rows = []

auftrag_id = 1
for day in range(45):  # 45 days
    date = base_date + timedelta(days=day)
    # Each day, 7-10 orders
    num_orders = random.randint(7, 10)
    for _ in range(num_orders):
        machine = random.choice(machines_prod)
        bauteil = random.choice(bauteile)
        zielmenge = random.randint(50, 500)
        
        # Calculate production with realistic scrap
        status = random.choice(status_prod)
        if status == 'Verzoegert':
            produziert = int(zielmenge * random.uniform(0.75, 0.92))
            ausschuss = int(produziert * random.uniform(0.05, 0.12))
        else:
            produziert = int(zielmenge * random.uniform(0.92, 0.99))
            ausschuss = int(produziert * random.uniform(0.01, 0.05))
        
        # Cycle time depends on part type
        if 'Welle' in bauteil or 'Bolzen' in bauteil:
            zykluszeit = random.uniform(10, 15)
        elif 'Gehaeuse' in bauteil:
            zykluszeit = random.uniform(20, 30)
        else:
            zykluszeit = random.uniform(5, 12)
        
        prod_rows.append({
            'Auftrag_ID': f'A{auftrag_id:04d}',
            'Maschine': machine,
            'Bauteil': bauteil,
            'Zielmenge': zielmenge,
            'Produziert': produziert,
            'Ausschuss': ausschuss,
            'Zykluszeit_s': round(zykluszeit, 1),
            'Datum': date.strftime('%Y-%m-%d'),
            'Status': status
        })
        auftrag_id += 1

# Write to CSV
with open('produktion_auftrage.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Auftrag_ID', 'Maschine', 'Bauteil', 'Zielmenge', 'Produziert', 'Ausschuss', 'Zykluszeit_s', 'Datum', 'Status'])
    writer.writeheader()
    writer.writerows(prod_rows)

print(f"✓ Created produktion_auftrage.csv with {len(prod_rows)} rows")
print("\nDataset generation complete!")
