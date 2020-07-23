import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    # use this to loop through guild to find the one to connect. a bot can be
    # connected to multiple
    # because its the first guild, you can just do clinet.guilds[0] but...
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # print out all members of guild
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord Server! \n'
        f'Please ENSURE your username is exactly the same as your instagram '
        f'username, and make sure you follow all the rules so we can all be '
        f'succesful and be fair.'

        # TODO: ADD RULES
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "www.instagram.com/p" in message.content:
        response = 'this is an instagram post'
        await message.channel.send(response)
        # TODO: ADD FUNCTIONALITY & DUPLICATE POST STOPPER
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)
