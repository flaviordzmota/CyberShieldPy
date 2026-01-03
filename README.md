Sistema Inteligente de Prevenção a Cybercrimes com Python
🔐 Título do Projeto

CyberShieldPy – Sistema de Detecção e Prevenção de Atividades Maliciosas

🎯 Objetivo do Projeto

Desenvolver um sistema em Python capaz de identificar, analisar e prevenir potenciais cybercrimes, utilizando análise de dados, automação e técnicas básicas de Machine Learning, simulando cenários reais de segurança.

O projeto foca em:

Detecção de padrões suspeitos
Prevenção proativa
Geração de relatórios inteligentes
Apoio à tomada de decisão em segurança

🧠 Problema que o Projeto Resolve

Empresas e instituições sofrem com:
Tentativas de acesso não autorizado
Ataques de força bruta
Phishing
Uso indevido de credenciais
Tráfego anômalo em sistemas

O CyberShieldPy atua como uma camada preventiva, analisando logs e dados de comportamento para antecipar riscos.

🛠️ Tecnologias Utilizadas

Python 3
Pandas – análise e tratamento de dados
NumPy
Scikit-learn – detecção de anomalias
Matplotlib / Seaborn – visualização
SQLite – armazenamento de eventos
Regex – identificação de padrões suspeitos
Streamlit (opcional) – dashboard interativo
Git/GitHub – versionamento

🧩 Funcionalidades do Sistema
1️⃣ Coleta de Dados (Simulada ou Real)

Logs de acesso (IP, data, hora, usuário)
Tentativas de login
Ações realizadas no sistema
Origem geográfica (simulada)

📁 Exemplo de entrada:

timestamp, user, ip, action, status
2026-01-02 10:32, admin, 192.168.0.10, login, failed

2️⃣ Análise de Comportamento

O sistema identifica:
Muitas tentativas de login falhas
Acesso fora do horário padrão
IPs suspeitos
Usuários com comportamento fora do padrão

📌 Exemplo:

Usuário que sempre acessa de manhã → login às 3h da manhã
20 tentativas falhas em 2 minutos

3️⃣ Detecção de Anomalias (Machine Learning)

Utiliza algoritmos como:
Isolation Forest
Local Outlier Factor
Para identificar:
Padrões incomuns
Possíveis ataques de força bruta
Acessos automatizados (bots)

4️⃣ Mecanismo de Prevenção

Quando um risco é identificado, o sistema pode:
Marcar o evento como ALTO RISCO
Simular bloqueio de IP
Gerar alerta automático
Registrar evidência para auditoria

5️⃣ Geração de Relatórios Inteligentes

Relatórios em:
Excel
PDF
Dashboard Web

Indicadores:
Total de tentativas suspeitas
Usuários mais visados
Horários críticos
IPs de maior risco

📊 Exemplo de Métricas Geradas

Taxa de falha de login por usuário
Número de acessos por IP
Score de risco por evento
Ranking de ameaças