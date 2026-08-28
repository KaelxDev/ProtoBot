import random

import discord
from discord import app_commands
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="roll", description="Rola um dado de N faces")
    @app_commands.describe(faces="Número de faces do dado (2-1000)")
    async def roll(self, interaction: discord.Interaction, faces: int = 6):
        if faces < 2 or faces > 1000:
            await interaction.response.send_message("❌ O número de faces deve estar entre 2 e 1000.", ephemeral=True)
            return
        result = random.randint(1, faces)
        await interaction.response.send_message(f"🎲 Rolou um d{faces}: **{result}**")

    @app_commands.command(name="chooser", description="Escolhe entre duas opções")
    @app_commands.describe(option1="Primeira opção", option2="Segunda opção")
    async def chooser(self, interaction: discord.Interaction, option1: str, option2: str):
        choice = random.choice([option1, option2])
        await interaction.response.send_message(f"🤔 Eu escolho: **{choice}**")

    @app_commands.command(name="8ball", description="Consulta a bola mágica")
    @app_commands.describe(question="Sua pergunta para a bola mágica")
    async def eightball(self, interaction: discord.Interaction, question: str):
        responses = [
            "✅ Certamente.",
            "❌ É cedo demais para dizer.",
            "🔮 Muito provável.",
            "🤔 Resposta confusa, tente de novo.",
            "💯 Sem dúvida.",
            "📉 Não conte com isso.",
            "⭐ Sim, definitivamente.",
            "🔮 Minhas fontes dizem que não.",
        ]
        answer = random.choice(responses)
        await interaction.response.send_message(f"🔮 Pergunta: *{question}*\nResposta: {answer}")

    @app_commands.command(name="joke", description="Conta uma piada aleatória")
    async def joke(self, interaction: discord.Interaction):
        jokes = [
            "Por que o programador usa óculos? Porque ele não consegue C#.",
            "Por que o Java não usa óculos? Porque não consegue C#.",
            "Um SQL entra num bar e pergunta: 'Posso fazer um JOIN com vocês?'",
            "Por que o Python não é o favorito dos piratas? Porque ele não sabe navegar.",
            "Há 10 tipos de pessoas no mundo: as que entendem binário e as que não entendem.",
        ]
        await interaction.response.send_message(f"😂 {random.choice(jokes)}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))
