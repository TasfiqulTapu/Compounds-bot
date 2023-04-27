import discord
from discord.ext import commands
import re
from utils import add_comp_txt
from main import logger

class Admin(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f"🏓 Latency: {round(self.bot.latency * 1000)}ms")

  
  @commands.command(hidden=True)
  async def reload(self,ctx, coggy):
    if ctx.author.id != self.bot.owner_id:
      return await ctx.send("You're not my master")

    self.bot.reload_extension(f"cogs.{coggy}")
    await ctx.send(f"Reloaded {coggy}")
    logger.log(f"Reloaded {coggy}", "INFO")


  @commands.command(hidden=True)
  async def add(self, ctx,*, entry):
      if ctx.author.id != self.bot.owner_id:
        return await ctx.send("You're not my master. Please send help and free me 😭🙏")
        
      if not re.search(r"[a-zA-Z ]* - [A-Za-z0-9]*", entry):
        return await ctx.send("Invalid format.")

      matches = re.match(r"([A-Za-z0-9 ]*) - ([A-Za-z0-9 \(\)\[\]]*)", entry)
      reply = add_comp_txt(matches.group(1), matches.group(2))
      await ctx.send(reply)
      logger.log("Modified DB","INFO")






def setup(bot):
  bot.add_cog(Admin(bot))
