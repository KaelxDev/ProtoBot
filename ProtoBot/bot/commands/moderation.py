import datetime

import discord
from discord import app_commands
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Limpa mensagens de um canal")
    @app_commands.describe(amount="Número de mensagens para apagar (1-100)")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int = 5):
        if amount < 1 or amount > 100:
            await interaction.response.send_message("❌ A quantidade deve estar entre 1 e 100.", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.followup.send(f"🗑️ Apagadas {len(deleted)} mensagens.", ephemeral=True)

    @app_commands.command(name="kick", description="Expulsa um membro do servidor")
    @app_commands.describe(member="Membro a expulsar", reason="Motivo da expulsão")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "Sem razão"):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="👢 Membro Expulso",
            description=f"{member.mention} foi expulso.\nMotivo: {reason}",
            color=discord.Color.orange(),
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="ban", description="Bane um membro do servidor")
    @app_commands.describe(member="Membro a banir", reason="Motivo do banimento")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "Sem razão"):
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="🔨 Membro Banido",
            description=f"{member.mention} foi banido.\nMotivo: {reason}",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="mute", description="Silencia um membro no servidor por 60 minutos")
    @app_commands.describe(member="Membro a silenciar", reason="Motivo do mute")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def mute(self, interaction: discord.Interaction, member: discord.Member, reason: str = "Sem razão"):
        until = discord.utils.utcnow() + datetime.timedelta(minutes=60)
        await member.timeout(until, reason=reason)
        await interaction.response.send_message(f"🔇 {member.mention} foi silenciado por 60 minutos. Motivo: {reason}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))
