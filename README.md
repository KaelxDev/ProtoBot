# ProtoBot 🤖

Um bot básico para **Discord**, desenvolvido em Python por **KaelxDev**, com comandos de utilidade, moderação, diversão e informações.

## ✨ Recursos

* 🏓 Comando de ping e informações do bot
* 🛡️ Ferramentas de moderação
* 👤 Informações de usuários e servidores
* 🎲 Comandos recreativos
* ⚙️ Configuração por variáveis de ambiente
* 🧩 Arquitetura modular para facilitar a manutenção e expansão

---

## 📁 Estrutura do projeto

```text
ProtoBot/
├── main.py                         # Ponto de entrada da aplicação
├── bot/                            # Código principal do ProtoBot
│   ├── __init__.py                 # Inicialização do pacote
│   ├── client.py                   # Configuração e inicialização do cliente Discord
│   ├── config.py                   # Carregamento das configurações e variáveis de ambiente
│   ├── events.py                   # Carregamento dos eventos do bot
│   │
│   ├── commands/                   # Comandos disponíveis no Discord
│   │   ├── general.py              # Comandos gerais
│   │   ├── moderation.py           # Comandos de moderação
│   │   ├── utility.py              # Comandos utilitários
│   │   └── fun.py                  # Comandos recreativos
│   │
│   ├── events/                     # Eventos recebidos do Discord
│   │   ├── ready.py                # Executado quando o bot fica online
│   │   └── errors.py               # Tratamento de erros e exceções
│   │
│   └── utils/                      # Funções auxiliares
│       └── helpers.py              # Funções compartilhadas
│
├── .env.example                    # Exemplo das variáveis de ambiente
├── .gitignore                      # Arquivos ignorados pelo Git
├── requirements.txt                # Dependências do projeto
├── README.md                       # Documentação
└── LICENSE                         # Licença MIT
```

---

## 🤖 Comandos

### 🛠️ Gerais

| Comando  | Descrição                          |
| -------- | ---------------------------------- |
| `/ping`  | Exibe a latência do bot            |
| `/help`  | Lista os comandos disponíveis      |
| `/about` | Exibe informações sobre o ProtoBot |

### 🛡️ Moderação

| Comando                  | Descrição                                   |
| ------------------------ | ------------------------------------------- |
| `/clear <quantidade>`    | Remove uma quantidade de mensagens do canal |
| `/kick <membro> [razão]` | Expulsa um membro do servidor               |
| `/ban <membro> [razão]`  | Bane um membro do servidor                  |
| `/mute <membro> [razão]` | Silencia um membro                          |

> ⚠️ Os comandos de moderação exigem as permissões adequadas no servidor.

### 🔧 Utilitários

| Comando              | Descrição                       |
| -------------------- | ------------------------------- |
| `/userinfo [membro]` | Exibe informações de um usuário |
| `/serverinfo`        | Exibe informações do servidor   |

### 🎮 Diversão

| Comando                      | Descrição                                           |
| ---------------------------- | --------------------------------------------------- |
| `/roll [faces]`              | Rola um dado com a quantidade de faces especificada |
| `/chooser <opção1> <opção2>` | Escolhe aleatoriamente entre duas opções            |
| `/8ball <pergunta>`          | Responde a uma pergunta usando a bola mágica        |
| `/joke`                      | Envia uma piada aleatória                           |

---

## 🚀 Instalação

### Pré-requisitos

Antes de começar, certifique-se de ter instalado:

* **Python 3.10+**
* **Git**
* Uma aplicação/bot criado no **Discord Developer Portal**

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd ProtoBot1
```

### 2. Configure as variáveis de ambiente

Crie um arquivo `.env` a partir do modelo fornecido:

```bash
cp .env.example .env
```

Depois, abra o `.env` e adicione o token do seu bot:

```env
DISCORD_TOKEN=seu_token_aqui
```

> 🔒 **Nunca publique seu token do Discord.** O arquivo `.env` deve permanecer no `.gitignore`.

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o bot

```bash
python main.py
```

Se tudo estiver configurado corretamente, o ProtoBot ficará online no servidor do Discord.

---

## ⚙️ Configuração

As configurações sensíveis do projeto são carregadas através de **variáveis de ambiente**, evitando que tokens e outras informações privadas sejam armazenados diretamente no código.

Utilize o arquivo:

```text
.env.example
```

como referência para configurar seu ambiente local.

---

## 🧩 Arquitetura

O ProtoBot utiliza uma estrutura modular para separar responsabilidades:

* **`client.py`** — responsável pelo cliente e inicialização do Discord.
* **`config.py`** — centraliza as configurações da aplicação.
* **`commands/`** — organiza os comandos por categoria.
* **`events/`** — contém os eventos disparados pelo Discord.
* **`utils/`** — reúne funções auxiliares reutilizáveis.
* **`main.py`** — ponto de entrada da aplicação.

Essa organização facilita a manutenção do código e permite adicionar novos comandos e eventos sem concentrar toda a lógica em um único arquivo.

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

Se você quiser contribuir com o projeto:

1. Faça um **fork** do repositório.
2. Crie uma branch para sua alteração:

```bash
git checkout -b feature/minha-feature
```

3. Faça suas alterações e crie um commit:

```bash
git commit -m "feat: adiciona nova funcionalidade"
```

4. Envie a branch:

```bash
git push origin feature/minha-feature
```

5. Abra um **Pull Request**.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.

Consulte o arquivo [`LICENSE`](LICENSE) para mais informações.

---

## 👨‍💻 Desenvolvedor

Desenvolvido por **KaelxDev**.

⭐ Se o projeto foi útil para você, considere deixar uma estrela no repositório!
