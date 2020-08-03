import discord

client = discord.Client()

@client.event
async def on_message(self,message):
    if message.author==self.user:
        return
    if message.content=='~ff':
        await message.channel.send('ff大大好厉害')
    if message.content=='~lake':
        await message.channel.send('湖宅森大大好厉害')
    if message.content=='~wgy':
        await message.channel.send('广药大大好厉害')
    if message.content=='~spg':
        await message.channel.send('SPG太太好厉害')
    if message.content=='~zyj':
        await message.channel.send('ZYJ大大好厉害')
    if message.content=='~dl':
        await message.channel.send('电量大大好厉害')

if __name__=='__main__':
    print("starting bot...")
    client.run('NzM4NjgxNzQzMzk3MjI0NDU5.XyPc-w.b5sUxu7E0NqkNZQap9UovcXyq7c')
