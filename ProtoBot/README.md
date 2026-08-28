# ProtoBot 🤖

Um bot básico do Discord desenvolvido por KaelxDev.

## Arquitetura

```
ProtoBot1/
├── main.py                         # Ponto de entrada: inicia o bot
├── bot/                            # Código principal do ProtoBot
│   ├── __init__.py                 # Define o pacote principal
│   ├── client.py                   # Configura e inicializa o cliente Discord
│   ├── config.py                   # Carrega configurações e variáveis de ambiente
│   ├── events.py                   # Aqui que o client.py vai buscar a função load_events.
│   ├── commands/                   # Comandos disponíveis no Discord
│   │   ├── general.py              # Comandos gerais (/ping, /help, /about)
│   │   ├── moderation.py           # Comandos de moderação (/clear, /kick, /ban, /mute)
│   │   ├── utility.py              # Comandos utilitários (/userinfo, /serverinfo)
│   │   └── fun.py                  # Comandos recreativos (/roll, /chooser, /8ball, /joke)
│   ├── events/                     # Eventos recebidos do Discord
│   │   ├── ready.py                # Executado quando o bot fica online
│   │   └── errors.py               # Tratamento de erros e exceções
│   └── utils/                      # Funções auxiliares reutilizáveis
│       └── helpers.py              # Funções auxiliares compartilhadas
├── .env.example                    # Modelo das variáveis de ambiente
├── .gitignore                      # Arquivos ignorados pelo Git
├── requirements.txt                # Dependências Python do projeto
├── README.md                       # Documentação do projeto
└── LICENSE                         # Licença de uso
```

## Comandos

### Gerais
- `/ping` - Responde com o ping do bot
- `/help` - Mostra os comandos disponíveis
- `/about` - Informações sobre o ProtoBot

### Moderação
- `/clear <quantidade>` - Limpa mensagens de um canal
- `/kick <membro> [razão]` - Expulsa um membro
- `/ban <membro> [razão]` - Ban um membro
- `/mute <membro> [razão]` - Silencia um membro

### Utilitários
- `/userinfo [membro]` - Mostra informações de um usuário
- `/serverinfo` - Mostra informações do servidor

### Diversão
- `/roll [faces]` - Rolla um dado
- `/chooser <opção1> <opção2>` - Escolhe entre duas opções
- `/8ball <pergunta>` - Consulta a bola mágica
- `/joke` - Conta uma piada aleatória

## Instalação

1. Clone o repositório
2. Crie um arquivo `.env` copiando o `.env.example` e adicione seu token
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o bot:

```bash
python main.py
```

## Licença

MIT