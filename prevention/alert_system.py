import pandas as pd
import sqlite3

# Conectar ao banco
conn = sqlite3.connect('database/events.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    user TEXT,
    ip TEXT,
    risk TEXT
)
""")

df = pd.read_csv('data/logs_with_risk.csv')

alerts = df[df['risk_level'] == 'ALTO']

for _, row in alerts.iterrows():
    cursor.execute("""
        INSERT INTO alerts (timestamp, user, ip, risk)
        VALUES (?, ?, ?, ?)
    """, (row['timestamp'], row['user'], row['ip'], row['risk_level']))

conn.commit()
conn.close()

print(f"{len(alerts)} alertas de ALTO risco registrados.")
