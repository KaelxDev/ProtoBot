import logging

import discord
from discord import app_commands
from discord.ext import commands

logger = logging.getLogger("ProtoBot")


def load_errors(bot: commands.Bot):
   
    @bot.event
    async def on_command_error(ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ Você não tem permissão para usar este comando.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Faltam argumentos obrigatórios. Use /help para ver os comandos.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Argumento inválido. Verifique os parâmetros.")
        else:
            logger.error(f"Erro no comando {ctx.command}: {error}", exc_info=error)
            try:
                await ctx.send("❌ Ocorreu um erro ao processar este comando.")
            except Exception:
                pass

  
    @bot.tree.error
    async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.MissingPermissions):
            msg = "❌ Você não tem permissão para usar este comando."
        elif isinstance(error, app_commands.CheckFailure):
            msg = "❌ Você não tem permissão suficiente."
        elif isinstance(error, app_commands.CommandOnCooldown):
            msg = f"⏳ Comando em cooldown. Tente novamente em {error.retry_after:.1f}s."
        else:
            logger.error(f"Erro em slash command {interaction.command}: {error}", exc_info=error)
            msg = "❌ Ocorreu um erro ao processar este comando."

        try:
            if interaction.response.is_done():
                await interaction.followup.send(msg, ephemeral=True)
            else:
                await interaction.response.send_message(msg, ephemeral=True)
        except Exception:
            pass
