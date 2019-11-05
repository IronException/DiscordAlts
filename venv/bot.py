import discord
import Config

from discord.ext import commands

@bot.command()
async def name(ctx):
    embedMsg = discord.Embed(title="name", description="alt1, alt2, ...")
    await ctx.send(embed=embedMsg)
    
def start_bot():
    bot = commands.Bot(command_prefix='')
    bot.run(Config.token)

