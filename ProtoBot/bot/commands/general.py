import discord
from discord import app_commands
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Responde com o ping do bot")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! Latência: {latency}ms")

    @app_commands.command(name="help", description="Mostra os comandos disponíveis")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📋 ProtoBot - Comandos",
            description="Lista de comandos disponíveis:",
            color=discord.Color.blue(),
        )
        embed.add_field(name="/ping", value="Responde com o ping do bot", inline=False)
        embed.add_field(name="/help", value="Mostra os comandos disponíveis", inline=False)
        embed.add_field(name="/about", value="Informações sobre o ProtoBot", inline=False)
        embed.add_field(name="/clear", value="Limpa mensagens (moderação)", inline=False)
        embed.add_field(name="/kick, /ban, /mute", value="Comandos de moderação", inline=False)
        embed.add_field(name="/userinfo, /serverinfo", value="Comandos utilitários", inline=False)
        embed.add_field(name="/roll, /8ball, /joke", value="Comandos divertidos", inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="about", description="Informações sobre o ProtoBot")
    async def about(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🤖 ProtoBot",
            description="Um bot básico do Discord criado para aprendizado.",
            color=discord.Color.green(),
        )
        embed.add_field(name="Versão", value="1.0.0", inline=True)
        embed.add_field(name="Autor", value="ProtoBot Dev", inline=True)
        embed.add_field(name="Discord.py", value=discord.__version__, inline=True)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))
