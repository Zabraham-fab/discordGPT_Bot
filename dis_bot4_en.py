import os
import discord
from dotenv import load_dotenv
import openai

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
openai.api_key=os.getenv('OPENAI_KEY')

intents=discord.Intents.all()
client=discord.Client(command_preffix='!', intents=intents)

@client.event
async def on_ready():
    print("{0.user} logged in with user account".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user in message.mentions:
        response= openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.content}",
        max_tokens=2048,
        temperature=0.5
    )
        await message.channel.send(response["choices"][0]["text"])

client.run(TOKEN)