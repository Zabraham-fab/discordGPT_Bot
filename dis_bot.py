import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')

intents=discord.Intents.all()
client=discord.Client(command_preffix='!', intents=intents)

@client.event
async def on_ready():
    print("{0.user} kullanıcı hesabıyla oturum açıldı".format(client))

client.run(TOKEN)