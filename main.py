import discord
from discord.ext import commands
import os
from logger import logger
from keep_alive import start_server

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(intents=intents, command_prefix=";", owner_id=673105565689446409)


def load_cogs():
  files = os.listdir("cogs")
  for f in files:
    if ".py" in f:
      bot.load_extension(f"cogs.{f[:-3]}")
  logger.log("Loaded all cogs", "INFO")
load_cogs()


@bot.event
async def on_connect():
  logger.log("Connected to gateway.","INFO")

@bot.event
async def on_ready():
  logger.log(f"Logged in as {bot.user.name}", "INFO")

@bot.event
async def on_guild_join(guild):
  logger.log(f"Joined {guild}","ADD")

@bot.event
async def on_guild_remove(guild):
  logger.log(f"Removed from {guild}", "REM")

@bot.event 
async def on_command_error(ctx: commands.Context, error: commands.CommandError): 
  if isinstance(error, commands.CommandOnCooldown): 
    logger.log(f"{ctx.author.name} is on cooldown for {str(error).split(' ')[-1]}", "ERR")
  else: 
    logger.log(str(error), "ERR")
    raise error

start_server()
bot.run(os.getenv('BOT_TOKEN'))
