import logging
import discord
from discord.ext import commands
from bot.config import Config
from bot.events import load_events 

logger = logging.getLogger("ProtoBot")

def create_bot(config: Config) -> commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(
        command_prefix=config.default_prefix,
        intents=intents,
        help_command=None,
    )
    
    load_events(bot)
    
    async def setup_hook():
        extensions = [
            "bot.commands.general",
            "bot.commands.moderation",
            "bot.commands.utility",
            "bot.commands.fun",
        ]
        
        for ext in extensions:
            try:
                await bot.load_extension(ext)
                logger.info(f"Extensão carregada: {ext}")
            except Exception as e:
                logger.error(f"Falha ao carregar {ext}: {e}", exc_info=True)
        
        try:
            synced = await bot.tree.sync()
            logger.info(f"Sincronizados {len(synced)} slash commands")
        except Exception as e:
            logger.error(f"Falha ao sincronizar comandos: {e}", exc_info=True)

    bot.setup_hook = setup_hook
    return bot