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


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("Merhaba Zabra"):
        await message.channel.send("Merhaba Dostum")


client.run(TOKEN)