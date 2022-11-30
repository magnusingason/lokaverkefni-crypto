import discord
import responses
from discord.ext import commands
from subprocess import call
import os


def run_discord_bot():
    TOKEN = 'MTA0MTc2NzUyNjcwMDQzMzU1OQ.G_g0bt.NA68F4J-xnl49TwmcWDnJe_iWD6qmM2nsj6uHk'
    bot = commands.Bot(intents=discord.Intents.all(),command_prefix='!')


    @bot.command()
    async def info(ctx):
        await ctx.send("use !sendtoaddress [address] [amount] to tip someone!")

    @bot.command()
    async def sendtoaddress(ctx, arg1, arg2):
        x = os.system(f'smileycoin-cli sendtoaddress {arg1} {arg2}')
        await ctx.send(x)
        if x == 256:
            await ctx.send(f'Error: Could not connect to server, not enough funds or could not process fund: {arg2}.')
        elif x == 1280:
            await ctx.send(f'Error: Incorrect address: {arg1}.')
        elif x == 32512:
            await ctx.send(f'Linux error.')
        elif x == 0:
            await ctx.send(f'{ctx.author} sent {arg2} to: {arg1}')

    bot.run(TOKEN)