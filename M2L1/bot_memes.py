import discord
from discord.ext import commands
import random, os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def meme6(ctx):
    img_name = random.choice(os.listdir('./M2L1/images'))
    with open(f'./M2L1/images/{img_name}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


bot.run('MTI4OTYyODI2NjM3Mzg0NTAzMw.G0PPqJ.jqRm-WRZ7jgPFw5zRUkHjKRXo64Hm4tZ3dj8pc')@bot.command()
