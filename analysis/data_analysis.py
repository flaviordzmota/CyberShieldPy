#📊 2. Análise de Dados

import pandas as pd

# Carregar logs
df = pd.read_csv('data/logs.csv', parse_dates=['timestamp'])

# Criar colunas auxiliares
df['hour'] = df['timestamp'].dt.hour
df['failed_login'] = df['status'].apply(lambda x: 1 if x == 'failed' else 0)

# Métricas básicas
summary = {
    'total_events': len(df),
    'failed_logins': df['failed_login'].sum(),
    'unique_users': df['user'].nunique(),
    'unique_ips': df['ip'].nunique()
}

print("Resumo Geral de Eventos:")
for k, v in summary.items():
    print(f"{k}: {v}")

# Agrupamento por usuário
user_stats = df.groupby('user')['failed_login'].sum().reset_index()
user_stats = user_stats.sort_values(by='failed_login', ascending=False)

print("\nUsuários com mais falhas de login:")
print(user_stats.head())
