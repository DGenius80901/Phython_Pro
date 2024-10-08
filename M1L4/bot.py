import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


    async def on_message(self, message):
        if message.content.startswith('#deleteme'):
            msg = await message.channel.send('Borrare este mensaje...')
            await msg.delete()


    async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)

client = MyClient(intents=intents)
client.run('MTI4OTYyODI2NjM3Mzg0NTAzMw.GcCj63.vG2Mi3f6wCpRw6ZGQGNMHY85JZqIdeDiT9cW6U')