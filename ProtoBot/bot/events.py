import logging
from discord.ext import commands

logger = logging.getLogger("ProtoBot")

def load_events(bot: commands.Bot):
    @bot.event
    async def on_ready():
        logger.info(f"Bot online como {bot.user}")