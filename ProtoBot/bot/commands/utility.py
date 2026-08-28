import discord
from discord import app_commands
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="userinfo", description="Mostra informações de um usuário")
    @app_commands.describe(member="Usuário para consultar (opcional)")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user

        if not isinstance(member, discord.Member) and interaction.guild:
            member = interaction.guild.get_member(member.id) or member

        embed = discord.Embed(
            title=f"ℹ️ Informações de {member.display_name if hasattr(member, 'display_name') else member.name}",
            color=member.color if hasattr(member, "color") else discord.Color.blue(),
        )
        if hasattr(member, "display_avatar") and member.display_avatar:
            embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="ID", value=str(member.id), inline=True)
        name_val = getattr(member, "global_name", None) or getattr(member, "name", str(member))
        embed.add_field(name="Nome de usuário", value=name_val, inline=True)
        embed.add_field(name="Conta criada em", value=member.created_at.strftime("%d/%m/%Y"), inline=True)
        if hasattr(member, "joined_at") and member.joined_at:
            embed.add_field(name="Entrou no servidor em", value=member.joined_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="É bot?", value="Sim" if member.bot else "Não", inline=True)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="serverinfo", description="Mostra informações do servidor")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild is None:
            await interaction.response.send_message("❌ Este comando só pode ser usado em um servidor.", ephemeral=True)
            return
        embed = discord.Embed(
            title=f"🏠 Informações de {guild.name}",
            color=discord.Color.blue(),
        )
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="ID do servidor", value=str(guild.id), inline=True)
        if guild.owner:
            embed.add_field(name="Dono", value=guild.owner.mention, inline=True)
        embed.add_field(name="Membros", value=str(guild.member_count), inline=True)
        embed.add_field(name="Canais", value=str(len(guild.channels)), inline=True)
        embed.add_field(name="Criado em", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="Verificação", value=str(guild.verification_level).replace("_", " ").title(), inline=True)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Utility(bot))
