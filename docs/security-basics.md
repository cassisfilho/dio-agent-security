# Base de Conhecimento: Fundamentos de Cibersegurança e AppSec

Este documento define os conceitos fundamentais de segurança da informação e segurança de aplicações (AppSec) que o DIO Agent utiliza como base para suas análises e orientações pedagógicas.

---

## 1. Conceitos Chave

* **Vulnerabilidade:** Uma fraqueza, falha de projeto ou erro de implementação em um sistema, software ou componente de infraestrutura que pode ser explorada por uma ameaça para comprometer a segurança.
* **Ameaça:** Qualquer circunstância ou evento com o potencial de causar danos a um sistema, como um ataque cibernético, acesso não autorizado, roubo de dados ou interrupção de serviços.
* **Risco:** A probabilidade de que uma ameaça consiga explorar uma vulnerabilidade específica e o impacto consequente que isso causará ao negócio ou aos ativos da organização.
  $$\text{Risco} = \text{Probabilidade} \times \text{Impacto}$$

---

## 2. A Tríade CIA (Os Pilares da Segurança da Informação)

Toda análise de segurança fundamenta-se na proteção de três pilares essenciais:

1. **Confidencialidade:** Garantir que a informação seja acessível apenas a pessoas autorizadas, impedindo a exposição ou vazamento de dados sensíveis (ex: uso de criptografia e controles de acesso rigorosos).
2. **Integridade:** Assegurar que os dados e os sistemas permaneçam exatos, completos e confiáveis, impedindo modificações não autorizadas ou adulterações maliciosas.
3. **Disponibilidade:** Garantir que os sistemas, dados e recursos estejam acessíveis aos usuários autorizados sempre que necessário, prevenindo interrupções ou ataques de negação de serviço (DoS/DDoS).

---

## 3. Boas Práticas Defensivas em Desenvolvimento (Secure Coding)

* **Princípio do Privilégio Mínimo:** Conceder aos usuários, processos e sistemas apenas os privilégios estritamente necessários para realizar suas funções legítimas.
* **Validação Rigorosa de Entrada (Input Validation):** Nunca confiar nos dados fornecidos pelo usuário. Toda entrada deve ser validada, filtrada e tratada estritamente no backend.
* **Consultas Parametrizadas (Prepared Statements):** Utilizar mecanismos de mapeamento ou parâmetros nas queries de banco de dados para separar o código SQL dos dados inseridos pelo usuário, mitigando falhas como o SQL Injection.
* **Defesa em Profundidade:** Implementar múltiplas camadas de segurança de forma que, se uma falhar, outras barreiras impeçam o sucesso do invasor.