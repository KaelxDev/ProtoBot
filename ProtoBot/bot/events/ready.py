import logging

import discord

logger = logging.getLogger("ProtoBot")


def load_ready(bot):
    @bot.event
    async def on_ready():
        logger.info(f"✅ ProtoBot está online como {bot.user}")
        logger.info(f"   Servidores: {len(bot.guilds)}")

        activity = discord.Activity(
            name="/help | ProtoBot",
            type=discord.ActivityType.watching,
        )
        await bot.change_presence(activity=activity)

        for guild in bot.guilds:
            logger.info(f"   - {guild.name} ({guild.member_count} membros)")