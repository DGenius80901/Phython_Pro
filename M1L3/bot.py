# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random

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
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def subtract(ctx, left: int, right: int):
    """Subtract two numbers"""
    if left < right:
        await ctx.send("El resultado es un número negativo, intenta que el primer numero sea mayor que el segundo.")
    else:
        await ctx.send(left - right)



@bot.command()
async def multiply(ctx, left: int, right: int):
    """Multiply two numbers"""
    await ctx.send(left * right)


@bot.command()
async def divide(ctx, left: int, right: int):
    """Divide two numbers"""
    if right == 0 or left == 0:
        await ctx.send("No se puede dividir por cero. Intentalo otra vez con otro número.")
    else:
        await ctx.send(left / right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run('MTI4OTYyODI2NjM3Mzg0NTAzMw.Gjyyt-.HV9GmlekI5KvP1aU8_eVr7_50V1N91irRhSi1M')