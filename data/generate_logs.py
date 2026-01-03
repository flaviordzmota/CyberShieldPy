import pandas as pd
import random
from datetime import datetime, timedelta

users = ['admin', 'user1', 'user2', 'user3', 'guest']
ips = ['192.168.0.10', '192.168.0.20', '10.0.0.5', '172.16.0.3']
actions = ['login']
statuses = ['success', 'failed']

logs = []

now = datetime.now()

for _ in range(200):
    timestamp = now - timedelta(minutes=random.randint(1, 1440))
    user = random.choice(users)
    ip = random.choice(ips)

    # Simular força bruta no admin
    if user == 'admin' and random.random() < 0.6:
        status = 'failed'
    else:
        status = random.choice(statuses)

    logs.append([
        timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        user,
        ip,
        'login',
        status
    ])

df = pd.DataFrame(logs, columns=['timestamp', 'user', 'ip', 'action', 'status'])
df.to_csv('data/logs.csv', index=False)

print("Logs gerados com sucesso!")
