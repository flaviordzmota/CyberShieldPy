import streamlit as st
import pandas as pd

st.set_page_config(page_title="CyberShieldPy", layout="wide")

df = pd.read_csv('data/logs_with_risk.csv')

st.title("🔐 CyberShieldPy – Monitoramento Inteligente")

col1, col2, col3 = st.columns(3)
col1.metric("Eventos Totais", len(df))
col2.metric("Alto Risco", len(df[df['risk_level'] == 'ALTO']))
col3.metric("Usuários Monitorados", df['user'].nunique())

st.divider()

st.subheader("🎯 Filtros")
risk_filter = st.multiselect(
    "Nível de Risco",
    options=df['risk_level'].unique(),
    default=df['risk_level'].unique()
)

filtered = df[df['risk_level'].isin(risk_filter)]

st.subheader("📋 Eventos Monitorados")
st.dataframe(filtered)

st.subheader("📊 Distribuição de Risco")
st.bar_chart(filtered['risk_level'].value_counts())

st.subheader("🚨 Top IPs Suspeitos")
top_ips = (
    filtered[filtered['risk_level'] == 'ALTO']
    .groupby('ip')
    .size()
    .sort_values(ascending=False)
)

st.bar_chart(top_ips)
