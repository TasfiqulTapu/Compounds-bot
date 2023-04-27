import discord
from discord.ext import commands

class Greetings(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def hello(self,ctx):
    name = ctx.author.name
    if name[-1]=="u": name += "wu"
    if name[-1]=="o": name += "wo"
    if name[-1]=="U": name += "wU"
    if name[-1]=="O": name += "wO"
    await ctx.send(f"Hallo *{name}*~")

  

def setup(bot):
  bot.add_cog(Greetings(bot))

