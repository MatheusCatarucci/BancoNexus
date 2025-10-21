# Projeto Avaliativo: Sistema Bancário - NexusBank 💸
## 1️⃣ Introdução
Projeto avaliativo de programação back-end em Python com o objetivo de criar um sistema bancário para uma instituição. O sistema deve conter funções de saque, depósito, transferências e consulta de saldo. O banco deve conter também dois tipos de contas diferentes (Conta Corrente e Conta Poupança), cada um com suas regras, sendo utilizado POO (Programação Orientada a Objetos).

Projeto avaliativo de programação back-end em Python com o objetivo de criar um sistema bancário para uma instituição. O sistema deve conter funções de saque, depósito, transferências e consulta de saldo. O banco deve conter também dois tipos de contas diferentes (Conta Corrente e Conta Poupança), cada um com suas regras, sendo utilizado POO (Programação Orientada a Objetos). Utilizaremos a biblioteca "Getpass", no qual tem a função de ocultar senhas.
## 2️⃣ Grupo e obrigações
Cada integrante do grupo tem as seguintes obrigações:
1. Matheus: Construção de funções no arquivo fun.py
2. Guilherme: Construção de classes no arquivo classes.py
3. Moisés: Construção de classes no arquivo classes.py
4. Gabriel Leonardo: Diagrama de Classes UML
5. Gabriel Portocarrero: Documentação no README
6. João Vitor: Documentação no README
## 3️⃣ Requisitos Funcionais 💡
### Conta no geral
A conta deve conter as seguintes funções:
| 🧩 Requisito | ⚙ Função |
|-----------|-----------|
| Depósito | Depositar dinheiro na conta corrente ou poupança |
| Saque | Sacar dinheiro na conta corrente ou poupança |
| Transferência | Realiza a transferência bancária para outra conta |
| Saldo e extrato | Realiza a consulta do saldo e extrato da conta |
### Conta Corrente e Poupança
| Conta | Função |
|---------|---------|
| Corrente | Permite saques sem saldo mínimo. |
| Poupança | Exige saldo mínimo de R$ 100,00 para saques. |
#### Observações
- Cada cliente pode contar mais de uma conta
- Todas as operações devem ser registradas em um extrato vinculado à conta.