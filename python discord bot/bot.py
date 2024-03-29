import discord
import responses
from discord.ext import commands
from subprocess import call
import os
import subprocess as sp



def run_discord_bot():
    TOKEN = 'MTA0MTc2NzUyNjcwMDQzMzU1OQ.Gkyq7r.Uq-6sDgBVQMf_R-Y1l2KaPGrwjcuIKNb8dXNaE' #you need to place your discord bot token here
    bot = commands.Bot(intents=discord.Intents.all(),command_prefix='!')

    #help command
    @bot.command()
    async def info(ctx):
        await ctx.send("use !sendtoaddress [address] [amount] to tip someone!, use !getbalance to get balance of wallet")

    #tipping command
    @bot.command()
    async def sendtoaddress(ctx, arg1, arg2):
        
        #checking if funds placed is an integer
        if arg2.isdigit():
            #command for linux to execute
            x = os.system(f'smileycoin-cli sendtoaddress {arg1} {arg2}')
        else:
            await ctx.send(f'Error: {arg2} is not an integer')
        

        #in this case linux has given the error code 256 which means that it could not proccess the json (something wrong with the funds value)
        if x == 256:
            await ctx.send(f'Error: Could not connect to server, not enough funds or could not process fund: {arg2}.')
        #in this case linux sends the error code 1280 indicating that the address given is incorrect
        elif x == 1280:
            await ctx.send(f'Error: Incorrect address: {arg1}.')

        #in this case linux has given the error code 32512 indicating that there is an error with the bash command (most likely server has not been connected to)
        elif x == 32512:
            await ctx.send(f'Linux error.')

        #everything works as it should
        elif x == 0:
            await ctx.send(f'{ctx.author} sent {arg2} to: {arg1}')


    #checking balance command
    @bot.command()
    async def getbalance(ctx):
        x = os.system(f'smileycoin-cli getbalance')
        output = sp.getoutput(f'smileycoin-cli getbalance')
        #in this case linux has given the error code 32512 indicating that there is an error with the bash command (most likely server has not been connected to)
        if x == 32512:
            await ctx.send(f'Linux error.')
        elif x == 0:
            await ctx.send(f'{ctx.author} has a balance of {output}')

    bot.run(TOKEN)