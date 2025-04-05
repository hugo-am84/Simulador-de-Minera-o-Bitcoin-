# Simulador-de-Minera-o-Bitcoin-
Simulador de Mineração de Blockchain em Python

# ⛏️ Simulador de Mineração de Blockchain em Python – `minerador.py`

Este projeto simula o processo de mineração de blocos em uma blockchain fictícia, validando hashes com base em dificuldade ajustável e garantindo o encadeamento entre blocos. Tudo é feito localmente com Python, salvando os dados em um arquivo `blocos.json` e registrando atividades no log `log_mineracao.txt`.

---

## 🧠 Funcionalidades

- Carrega blocos salvos em `blocos.json`
- Exibe blocos pendentes de mineração (`nonce = null`)
- Permite escolher qual bloco deseja minerar
- Verifica se o `prev` (hash do bloco anterior) está correto
- Testa **nonces sequenciais** até encontrar uma hash que atenda à **dificuldade**
- Exibe tentativas em tempo real com timestamp
- Valida o bloco, registra a hash e salva o `nonce` encontrado
- Gera um log em `log_mineracao.txt` com:
  - Número do bloco
  - Hash final
  - Nonce
  - Tempo de mineração
  - Tentativas
  - Recompensa (3.125 BTC)
- Menu interativo com opções de mineração, visualização do log e saída

---

## 📁 Estrutura dos Arquivos


---

## ⚙️ Requisitos

- Python 3.10 ou superior
- Biblioteca externa:
  - `colorama` (para exibição colorida no terminal)

Para instalar o `colorama`, execute:
```bash
pip install colorama

Como Usar
Certifique-se de que o arquivo blocos.json exista e contenha blocos com "nonce": null

Execute o script:

bash
Copiar
Editar
python3 minerador.py
No menu, escolha:

1 para atualizar a exibição dos blocos

2 para escolher um bloco e iniciar a mineração

3 para visualizar o log de mineração

4 para sair

📌 Observações
A dificuldade determina quantos zeros a hash deve conter no início (ex: 0000 para dificuldade 4)

A mineração utiliza nonces sequenciais (0, 1, 2...) por simplicidade e clareza didática

O log é cumulativo e registra cada bloco minerado com suas informações completas

INICIANDO MINERAÇÃO - BLOCO 5
========================================
12:45:01 | Nonce: 0 | Hash: a3c4b...
12:45:02 | Nonce: 1 | Hash: 09fa1...
...

✅ Hash minerada: 0000e1c29f8...
⏱️ Tempo: 12.84s | Tentativas: 23490


 Objetivo
Este projeto é 100% educacional e visa demonstrar os princípios de uma mineração simplificada em blockchain, com foco em:

Prova de trabalho (Proof of Work)

Hashing com SHA-256

Integridade encadeada entre blocos

Registro de log e simulação de recompensas

⚠️ Atenção: este projeto não possui valor financeiro real.

✍️ Autor
Hugo – desenvolvimento e testes
