import discord
import Config

from discord.ext import commands


def start_bot():
    bot = commands.Bot(command_prefix='')
    bot.run(Config.token)


@bot.command()
async def name(ctx):
    embed_msg = discord.Embed(title="name", description="alt1, alt2, ...")
    await ctx.send(embed=embed_msg)
