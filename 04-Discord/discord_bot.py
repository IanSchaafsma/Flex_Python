import discord

client = discord.Client()

@client.event
async def on_ready():
   
    guild = client.guilds[0]
    
    print(guild.name, "is the name of the server")

    
    print(client.user, "has connected to the client")

client.run("OTA2MTcxMTEyNzg0NzkzNjUx.YYUvnQ.-vip5axhpwy1XXuirG4l2uPxcXI")