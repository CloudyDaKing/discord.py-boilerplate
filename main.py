import discord
from discord.ext import commands
import os
import asyncio
import dotenv
from cogwatch import watch

#load .env file
dotenv.load_dotenv()

#define useful variables
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()


#bot class (using cogwatch to auto reload cogs)
class bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents)

    #cogwatch decorator
    @watch(path='cogs', preload=True)
    async def on_ready(self):
        print('Bot ready.')

discordbot = bot()

async def run():
    #load cogs found in ./cogs and has .py extension
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await discordbot.load_extension(f'cogs.{filename[:-3]}')
    #load jishaku debug cog
    await discordbot.load_extension('jishaku')



if __name__ == '__main__':
    #loads cogs then runs bot
    asyncio.run(run())
    discordbot.run(TOKEN)
