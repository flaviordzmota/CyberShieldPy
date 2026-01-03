import pandas as pd

df = pd.read_csv('data/logs_with_risk.csv')

report = df.groupby('risk_level').size().reset_index(name='total_events')

# Exportar relatório
report.to_excel('reports/security_report.xlsx', index=False)

print("Relatório gerado em reports/security_report.xlsx")
