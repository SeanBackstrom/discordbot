import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
     #use this to loop through guild to find the one to connect. a bot can be connected to multiple
     #because its the first guild, you can just do clinet.guilds[0] but...
    guild = discord.utils.get(client.guilds, name=GUILD)
           
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    #print out all members of guild
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)

#
