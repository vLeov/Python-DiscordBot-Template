import discord
from discord.ext import commands

bot = commands.Bot(comamnd_prefix="!") #Discord Bot prefix

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="bot template")) #Your Discord Bot Status
    print(f"[{bot.user}] is Online") #Console output


cogs_list = [
    'ping', #here you can register your commands from your cogs folder

]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run('') #Put your Bot token inside the brackets
