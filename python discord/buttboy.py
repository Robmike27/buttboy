import discord

client = discord.Client()
frickSwears = 0
hasCounted = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
#Built on the quickstart from the discord.py documentation
@client.event
async def on_message(message):
    global frickSwears

    await channelCount(message.channel)

    if message.author == client.user:
        return

    if ('hi' in message.content.lower() or 'hello' in message.content.lower()) and 'buttboy' in message.content.lower():
        await message.channel.send("I'm Buttboy! Hello!")
    
    if 'fuck' in message.content.lower():
        frickSwears += 1
        await message.channel.send("Luggage :luggage: ")
    
    if message.content.startswith('point and laugh'):
        await message.channel.send('hahaaahahahhhahaahaha')

    if message.content.startswith('count'):
        await message.channel.send('Ok...')
        await message.channel.send('This channel has said the frick word '+ str(frickSwears) +' times!')

#This function counts how many times a channel has the word fuck or any variaton of it.
async def Channel_Count(channel):
    global hasCounted
    global frickSwears

    if hasCounted == False:
        channel = await channel.history(limit=None).flatten()
        for message in channel:
            if 'fuck' in message.content.lower() or 'fucking' in message.content.lower():
                frickSwears += 1
            hasCounted = True
    return frickSwears


client.run('')
