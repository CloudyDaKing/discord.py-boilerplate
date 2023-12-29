import discord
from discord.ext import commands

#cog class defined here needed for all cogs
class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #hybrid command for both slash and normal commands
    @commands.hybrid_command(name='ping', description='Get the ping of the bot')
    async def ping(self, ctx):
        #sends latency of bot
        await ctx.send(f"🏓 Pong! {round(self.bot.latency * 1000)}ms")
       
async def setup(bot):
    #adds cog to bot
    await bot.add_cog(ping(bot))
