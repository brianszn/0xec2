<p align="center">
  <code>0xec2</code>
</p>

<h3 align="center">Projeto educacional de Command & Control em Python</h3>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/propósito-estudo-green?style=flat-square" />
  <img src="https://img.shields.io/badge/status-em%20evolução-yellow?style=flat-square" />
</p>

---

## ⚠️ Aviso Legal (Disclaimer)

> **Este projeto existe exclusivamente para fins de estudo e aprendizado.**
>
> O objetivo **não é** criar um C2 comercial, de mercado ou indetectável. Não há intenção de uso malicioso ou ofensivo. O foco é puramente acadêmico: entender como conexões de rede funcionam na prática, explorar o módulo `socket` do Python e aprofundar conhecimentos em programação de redes.
>
> O uso indevido deste código é de inteira responsabilidade de quem o fizer. O autor não se responsabiliza por qualquer uso fora do contexto educacional.

---

## 📖 Sobre o Projeto

O **0xec2** é um estudo prático de redes e comunicação entre máquinas utilizando Python puro. Nasceu da curiosidade de entender, na prática, como funciona a arquitetura de um Command & Control — não para atacar, mas para **compreender o que acontece por baixo dos panos** em termos de:

- **Conexões TCP/IP** — Como um servidor escuta e aceita conexões de clientes
- **Programação concorrente** — Uso de `threading` para gerenciar múltiplas conexões simultâneas
- **Módulo `socket`** — Criação de sockets, bind, listen, accept, send e receive
- **Arquitetura cliente-servidor** — Separação de responsabilidades entre listener, sessão e controle
- **Serialização de dados** — Encoding/decoding de bytes para comunicação entre processos

O projeto vai evoluindo conforme eu estudo. Cada iteração reflete um novo conceito aprendido e aplicado. Conforme vou estudando, vou verificando o que é interessante de se ter em um C2 e implementando por aqui.

---

## 🧩 Estrutura do Projeto

```
0xec2/
├── 1to1.py        # Versão inicial — listener simples (1 conexão por vez)
├── Listener.py    # Versão evoluída — multi-session com menu interativo
├── Session.py     # Classe de sessão — gerencia conexões individuais
└── README.md
```

### `1to1.py` — O Ponto de Partida

Primeira versão do listener. Implementa um servidor TCP básico que:
- Cria um socket e faz bind em um host/porta
- Aceita **uma** conexão por vez
- Usa uma thread separada para escutar respostas do cliente
- Permite enviar comandos via prompt interativo (`cmd>`)

> **Conceitos estudados:** socket básico, `bind`, `listen`, `accept`, `sendall`, `recv`, threading para I/O não-bloqueante.

### `Listener.py` — Evolução com Multi-Session

Versão evoluída que introduz o conceito de **múltiplas sessões simultâneas**:
- Gerencia várias conexões ativas através de um dicionário de sessões
- Cada conexão recebe um ID incremental
- Menu interativo no terminal para:
  - Listar sessões ativas (`list sessions`)
  - Selecionar e interagir com uma sessão específica (`choice session`)
- Métodos `send_data` e `receive_data` como `@staticmethod` para reutilização

> **Conceitos estudados:** gerenciamento de estado, design patterns (separação listener/session), uso de `@staticmethod`, threading com múltiplos clientes, menus CLI.

### `Session.py` — Abstração de Conexão

Classe que encapsula uma conexão individual:
- Armazena `conn`, `addr`, `hostname` e status (`is_active`)
- `send_command()` — Envia comandos para o cliente conectado
- `start_listener()` — Loop de escuta contínua para receber respostas
- `close_connection()` — Encerra a conexão de forma limpa

> **Conceitos estudados:** OOP (encapsulamento), gerenciamento de ciclo de vida de conexões, tratamento de exceções em rede, imports circulares (`from Listener import Listener`).

---

## 🛠️ Como Executar (Ambiente de Lab)

> Execute **apenas** em ambientes controlados e de sua propriedade (ex: VMs locais, redes isoladas).

```bash
# Servidor (Listener com multi-session)
python Listener.py

# Ou a versão simples (1 conexão)
python 1to1.py
```

O listener vai iniciar escutando no endereço e porta configurados (padrão: `192.168.56.1:9090`).

---


<p align="center">
  <sub>Feito com curiosidade 🧠 e Python 🐍</sub>
</p>
