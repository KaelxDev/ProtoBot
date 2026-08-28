# ProtoBot - Um bot Discord com suporte a slash commands e eventos
# Autor: KaelxDev

import logging
from bot.config import load_config
from bot.client import create_bot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger("ProtoBot")

def main():
    config = load_config()
    bot = create_bot(config)
    
    logger.info("Starting ProtoBot...")
    bot.run(config.token)

if __name__ == "__main__":
    main()