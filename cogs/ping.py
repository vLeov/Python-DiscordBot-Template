import discord
from discord.ext import commands
from discord import slash_command #import discord slash_command

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="ping", description="this is the ping command") #make a new SlashCommand
    async def ping(self, ctx): #input
        await ctx.respond("Pong!") #output 



def setup(bot):
    bot.add_cog(Ping(bot))
