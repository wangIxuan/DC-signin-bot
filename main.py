import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")
DISCORD_NAME_ENTRY = os.getenv("DISCORD_NAME_ENTRY")
TIME_ENTRY = os.getenv("TIME_ENTRY")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

signed_users = set()

@bot.event
async def on_ready():
    print(f"Bot 已登入：{bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash 指令同步：{len(synced)} 個")
    except Exception as e:
        print(e)

@bot.tree.command(name="出席")
async def 出席(interaction: discord.Interaction):
    if interaction.user.id in signed_users:
        await interaction.response.send_message("你已經簽到過了喔！", ephemeral=True)
        return

    buttons = [
        ("19:30", "19:30"),
        ("19:45", "19:45"),
        ("20:00", "20:00"),
        ("領土期間", "領土期間"),
        ("無法出席", "無法出席")
    ]

    view = discord.ui.View()
    for label, time in buttons:
        view.add_item(SignInButton(label=label, time=time))

    await interaction.response.send_message("請選擇出席時間：", view=view, ephemeral=True)

class SignInButton(discord.ui.Button):
    def __init__(self, label, time):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.time = time

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id in signed_users:
            await interaction.response.send_message("你已簽到，無法重複喔！", ephemeral=True)
            return

        data = {
            DISCORD_NAME_ENTRY: interaction.user.name,
            TIME_ENTRY: self.time
        }

        try:
            requests.post(GOOGLE_FORM_URL, data=data)
            signed_users.add(interaction.user.id)
            await interaction.response.send_message(f"簽到成功：{self.time}", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message("傳送資料失敗！", ephemeral=True)
            print("錯誤：", e)

bot.run(TOKEN)
