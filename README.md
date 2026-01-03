# 🔐 CyberShieldPy

## Sistema Inteligente de Prevenção a Cybercrimes com Python, Dados e Governança

---

## 📌 Visão Geral

O **CyberShieldPy** é um projeto de portfólio desenvolvido em **Python** com foco na **prevenção de cybercrimes**, unindo **Análise de Dados, Machine Learning, Automação, Governança da Informação e LGPD**.

O sistema simula um **pipeline real de segurança da informação**, desde a geração e coleta de logs até a **detecção de comportamentos anômalos**, atribuição de **score de risco**, registro de alertas e visualização em **dashboard gerencial**.

Mais do que detectar incidentes, o projeto foi pensado para demonstrar **maturidade técnica, visão preventiva e responsabilidade no uso de dados pessoais**.

---

## 🎯 Objetivos do Projeto

* Detectar atividades suspeitas em logs de acesso
* Identificar padrões anômalos de comportamento
* Prevenir ataques como força bruta e acessos indevidos
* Automatizar a análise de eventos de segurança
* Gerar indicadores para apoio à tomada de decisão
* Aplicar princípios de **Governança de Dados e LGPD** na prática

---

## 🧠 Problema Abordado

Organizações lidam com grandes volumes de logs e eventos de acesso, tornando inviável a análise manual e reativa. Isso pode resultar em:

* Ataques não detectados
* Vazamento de dados
* Falhas de conformidade
* Baixa maturidade em governança de segurança

O **CyberShieldPy** atua como uma **camada analítica e preventiva**, transformando dados brutos em **insights de risco acionáveis**.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **Pandas / NumPy** – tratamento e análise de dados
* **Scikit-learn** – detecção de anomalias
* **SQLite** – persistência de alertas
* **Streamlit** – dashboard interativo
* **Matplotlib** – visualização
* **Git / GitHub** – versionamento

---

## ⚙️ Funcionalidades

### 📥 Geração e Coleta de Logs

* Geração automatizada de logs simulando acessos reais
* Campos monitorados:

  * Usuário
  * IP
  * Data e hora
  * Status de login

---

### 📊 Análise de Comportamento

* Identificação de padrões como:

  * Múltiplas falhas de login
  * Acessos fora do horário padrão
  * IPs com comportamento suspeito

---

### 🤖 Detecção de Anomalias

* Aplicação de **Isolation Forest**
* Identificação de eventos fora do padrão histórico
* Suporte à priorização de riscos

---

### 🎯 Score de Risco (0–100)

Cada evento recebe um score baseado em:

* Falha de autenticação
* Horário do acesso
* Classificação como anomalia

Classificação final:

* **BAIXO**
* **MÉDIO**
* **ALTO**

---

### 🚨 Prevenção e Alertas

* Registro automático de eventos de alto risco
* Persistência em banco SQLite
* Suporte à auditoria e rastreabilidade

---

### 📊 Dashboard Gerencial

* Indicadores de segurança em tempo real
* Filtros por nível de risco
* Ranking de IPs suspeitos
* Visão executiva para tomada de decisão

---

## 🔐 LGPD & Governança de Dados

### 📌 Dados Tratados

| Dado             | Classificação    |
| ---------------- | ---------------- |
| Usuário          | Dado pessoal     |
| IP               | Dado pessoal     |
| Timestamp        | Dado pessoal     |
| Status de acesso | Dado operacional |

> O projeto **não utiliza dados sensíveis**, mas aplica a LGPD por envolver dados pessoais.

---

### ⚖️ Base Legal

* **Legítimo Interesse (Art. 7º, IX – LGPD)**
* Finalidade exclusiva: **segurança da informação**

---

### 🛡️ Princípios da LGPD Aplicados

* Finalidade
* Necessidade (minimização)
* Segurança
* Prevenção
* Responsabilização

---

## 🗂️ Estrutura do Projeto

```
cybershieldpy/
│
├── data/
│   ├── generate_logs.py
│   └── logs.csv
│
├── analysis/
│   ├── data_analysis.py
│   └── anomaly_detection.py
│
├── prevention/
│   └── alert_system.py
│
├── reports/
│   └── generate_report.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   └── events.db
│
├── requirements.txt
└── README.md
```

---

## ▶️ Execução do Pipeline

```bash
python data/generate_logs.py
python analysis/data_analysis.py
python analysis/anomaly_detection.py
python prevention/alert_system.py
python reports/generate_report.py
python -m streamlit run dashboard/app.py
```

---

## 📈 Resultados Esperados

* Detecção proativa de ameaças
* Redução do tempo de resposta a incidentes
* Melhoria na governança e auditoria
* Apoio à conformidade com LGPD

---

## 🚀 Roadmap

* Integração com Threat Intelligence
* NLP para detecção de phishing
* Logs em tempo real
* Arquitetura em nuvem
* Testes automatizados

---

## 💼 Valor para Portfólio

Este projeto demonstra competências em:

* Análise de Dados aplicada à segurança
* Automação com Python
* Machine Learning
* Governança da Informação
* LGPD na prática
* Pensamento preventivo

---

## 👨‍💻 Autor

**Flavio Rodrigues:**
Analista de Dados | Automação | Governança | Cybersecurity


---

📌 *Projeto desenvolvido para fins educacionais e portifólio
