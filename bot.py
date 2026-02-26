#!/usr/bin/envthon3
# mhs raid bot v5.5 - termux 100% fix
# criado por azael @_azaelx64

import discord
from discord.ext import commands
import asyncio
from colorama import init, Fore, Style
init(autoreset=True)

print(Fore.CYAN + """
██╗  ██╗ █████╗ ███╗   ███╗██████╗  ██████╗ ██╗
██║  ██║██╔══██╗████╗ ████║██╔══██╗██╔═══██╗██║
███████║███████║██╔████╔██║██║  ██║██║   ██║██║
██╔══██║██╔══██║██║╚██╔╝██║██║  ██║██║   ██║██║
██║  ██║██║  ██║██║ ╚═╝ ██║██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚══════╝
     raid v5.5 - termux fix - criado por azael @_azaelx64
""")

# ═══════════════════════════════════════════════════════════════
import os
from dotenv import load_dotenv

load_dotenv()
# ═══════════════════════════════════════════════════════════════

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class spamButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.button(label="cripta", style=discord.ButtonStyle.red)
    async def cripta_raid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()

        spam_msg = """# servidor purificado pela C.R.I.P.T.A
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
C.R.I.P.T.A purificou seu servidor
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# servidor purificado pela C.R.I.P.T.A
🥶⃤🥶⃤🥶⃤🥶⃤🥶⃤🥶⃤
C.R.I.P.T.A purificou seu servidor
# servidor purificado pela C.R.I.P.T.A
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
C.R.I.P.T.A purificou seu servidor
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# servidor purificado pela C.R.I.P.T.A
🥶⃤🥶⃤🥶⃤🥶⃤🥶⃤🥶⃤
C.R.I.P.T.A purificou seu servidor
# servidor purificado pela CRIPTA
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
C.R.I.P.T.A purificou seu servidor
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# servidor purificado pela C.R.I.P.T.A
🥶⃤🥶⃤🥶⃤🥶⃤🥶⃤🥶⃤
C.R.I.P.T.A purificou seu servidor

https://discord.gg/GpaVsbCJEX"""

        print(Fore.YELLOW + "🚀 raid iniciado - 30 mensagens")
        for i in range(30):
            try:
                await interaction.followup.send(spam_msg)
                print(f"[{i+1}/30] ✅ enviada!")
                await asyncio.sleep(1.0)
            except Exception as e:
                print(f"[{i+1}/30] ❌ erro: {e}")
                await asyncio.sleep(1.0)

        print(Fore.GREEN + "🎉 cripta raid concluída!")

@bot.command()
async def cripta(ctx):
    """ativa o raid cripta"""
    view = spamButton()
    await ctx.send("clique para cripta", view=view)

@bot.tree.command(name="cripta", description="cripta raid by azael")
async def slash_cripta(interaction: discord.Interaction):
    view = spamButton()
    await interaction.response.send_message("clique para cripta", view=view, ephemeral=True)

@bot.event
async def on_ready():
    print(Fore.GREEN + f"✅ {bot.user} online no termux!")
    print(Fore.BLUE + "📱 slash: /cripta | prefix: !cripta")

    try:
        synced = await bot.tree.sync()
        print(Fore.GREEN + f"✅ {len(synced)} slash comandos sync")
    except Exception as e:
        print(f"⚠️ sync erro: {e}")

print(Fore.GREEN + "🚀 iniciando mhs raid...")
bot.run(os.getenv("TOKEN"))
