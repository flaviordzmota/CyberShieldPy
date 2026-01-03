import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv('data/logs.csv', parse_dates=['timestamp'])

df['failed_login'] = (df['status'] == 'failed').astype(int)
df['hour'] = df['timestamp'].dt.hour

features = df[['failed_login', 'hour']]

model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = model.fit_predict(features)

def risk_score(row):
    score = 0
    score += row['failed_login'] * 50

    if row['hour'] < 6 or row['hour'] > 22:
        score += 30

    if row['anomaly'] == -1:
        score += 40

    return min(score, 100)

df['risk_score'] = df.apply(risk_score, axis=1)

df['risk_level'] = pd.cut(
    df['risk_score'],
    bins=[-1, 30, 70, 100],
    labels=['BAIXO', 'MÉDIO', 'ALTO']
)

df.to_csv('data/logs_with_risk.csv', index=False)

print("Análise concluída.")
print(df['risk_level'].value_counts())
