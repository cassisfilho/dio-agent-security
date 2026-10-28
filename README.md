## 🛡️ Especialização em Cibersegurança & AppSec

Este agente foi especializado para atuar como um mentor em Segurança de Aplicações (AppSec), com foco em análise estática e pedagógica de código:

* **Base de Conhecimento:** Conceitos fundamentais em `docs/security-basics.md` (OWASP Top 10, sanitização, parametrização e princípios de privilégio mínimo).
* **Skill `vulnerability-analysis`:** Localizada em `skills/vulnerability-analysis/`, define o fluxo de triagem de riscos sem entregar código pronto de imediato.
  * **Etapa 1:** Coleta de contexto (ambiente de execução, dados manipulados, exposição de rede).
  * **Etapa 2:** Avaliação com matriz de Impacto, Probabilidade e Severidade.
  * **Etapa 3:** Condução pedagógica orientada a perguntas e boas práticas de remediação.
* **Ambiente de Teste:** Arquivo `app.py` contendo simulação deliberada de SQL Injection para validação do agente.
## Evidências de Execução e Mentoria

### 1. Triagem e Coleta de Contexto
O agente interrompe a execução imediata para mapear o ambiente de operação e a superfície de exposição antes de avaliar riscos:

<img width="1036" height="641" alt="evidencia-1-contexto" src="https://github.com/user-attachments/assets/bd752b08-6fc5-4a98-9a4a-282978e5f720" />

### 2. Análise Estruturada de Risco e Severidade
Ao analisar a exposição pública na web, o agente recalcula a matriz (Impacto, Probabilidade e Severidade Alta) e conduz a explicação conceitual sem entregar a resposta pronta:

<img width="1036" height="1391" alt="evidencia-2-analise-severidade" src="https://github.com/user-attachments/assets/16c7b4f5-e1a2-48d5-91b0-0a2445e30094" />
