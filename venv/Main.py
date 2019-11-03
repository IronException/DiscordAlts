import discord
import Config

from discord.ext import commands

bot = commands.Bot(command_prefix='')

@bot.command()
async def name(ctx):
    embedMsg = discord.Embed(title="name", description="alt1, alt2, ...")
    await ctx.send(embed=embedMsg)

bot.run(Config.token)

