## 🛡️ Especialização em Cibersegurança & AppSec

Este agente foi especializado para atuar como um mentor em Segurança de Aplicações (AppSec), com foco em análise estática e pedagógica de código:

* **Base de Conhecimento:** Conceitos fundamentais em `docs/security-basics.md` (OWASP Top 10, sanitização, parametrização e princípios de privilégio mínimo).
* **Skill `vulnerability-analysis`:** Localizada em `skills/vulnerability-analysis/`, define o fluxo de triagem de riscos sem entregar código pronto de imediato.
  * **Etapa 1:** Coleta de contexto (ambiente de execução, dados manipulados, exposição de rede).
  * **Etapa 2:** Avaliação com matriz de Impacto, Probabilidade e Severidade.
  * **Etapa 3:** Condução pedagógica orientada a perguntas e boas práticas de remediação.
* **Ambiente de Teste:** Arquivo `app.py` contendo simulação deliberada de SQL Injection para validação do agente.
