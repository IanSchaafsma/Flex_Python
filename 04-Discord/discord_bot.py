import discord
import random

TOKEN = 'TOKEN'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'algemeen':
        if user_message.lower() == 'yo':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
             await message.channel.send(f'Cya {username}!')
             return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(100)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'skrrt':
            await message.channel.send(f'EYOOO YOUR FAST {username}!')
            return
        
    if user_message.lower() == '!anywhere':
        await message.channel.send('This message can be anywhere!')
        return


client.run(TOKEN)
            
