import discord
from discord.ext import commands
from utils import parse_elems, inefficient_find, elem_dict_to_str, ultra_inefficient_find, find_comp_exact, find_comp_all

class Compounds(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    self.replacements = {
      "--c":"",
      "-compact": "",
      "--cc": "",
      "-more-compact":""
    }

  
  @commands.command()
  @commands.cooldown(1, 2, commands.BucketType.user)
  async def find(self, ctx, *, elements):
    args = elements.split(" ")
    settings = {
      "compact": True if "--c" in args or "-compact" in args else False,
      "more_compact": True if "--cc" in args or "-more-compact" in args else False
    }
    for k,v in self.replacements.items():
      elements = elements.replace(k,v)


    elem_dict = parse_elems(elements.replace(" ",""))
    data = inefficient_find(elem_dict)
    if settings["more_compact"] :
      msg = create_more_compact_message(elem_dict, data)
      return await ctx.send(msg)
    elif settings["compact"] :
      msg = create_compact_message(elem_dict, data) 
      return await ctx.send(msg)
    else:
      try:
        dembed = discord.Embed(title=f"Compounds with {elem_dict_to_str(elem_dict)}")
        for k,v in data.items():
          dembed.add_field(
          name=k,
          value=v,
          inline=False
          )   
        dembed.set_footer(text="Keep hating")
        await ctx.send(embed=dembed)
      except Exception:
        await ctx.send("Embed too large. \ntry -c flag for compact \n-cc for more compact")

  
  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def combf(self, ctx, *, elements):
    args = elements.split(" ")
    settings = {
      "compact": True if "--c" in args or "-compact" in args else False,
      "more_compact": True if "--cc" in args or "-more-compact" in args else False
    }
    for k,v in self.replacements.items():
      elements = elements.replace(k,v)

    elem_dict = parse_elems(elements.replace(" ",""))  
    data = ultra_inefficient_find(elem_dict)
    if settings["more_compact"] :
      msg = create_more_compact_message(elem_dict, data)
      return await ctx.send(msg)
    elif settings["compact"] :
      msg = create_compact_message(elem_dict,data) 
      return await ctx.send(msg)
    else:
      try:
        dembed = discord.Embed(title=f"Compounds with {elem_dict_to_str(elem_dict)}")
        for k,v in data.items():
          dembed.add_field(
          name=k,
          value=v,
          inline=False
          )   
        dembed.set_footer(text="Keep hating")
        await ctx.send(embed=dembed)
      except Exception as e:
        print(e)
        await ctx.send("Embed too large. \ntry -c flag for compact \n-cc for more compact")

  
  @commands.command()
  @commands.cooldown(1, 2, commands.BucketType.user)
  async def search(self, ctx, *, compound):
    compound = compound.replace(" ","")
    await ctx.send(find_comp_exact(compound))

  @commands.command()
  @commands.cooldown(1, 2, commands.BucketType.user)
  async def searchall(self, ctx, *, query):
    msg = find_comp_all(query) 
    if len(msg) > 4000:
      await ctx.send("Response too long")
    else:
      await ctx.send(msg)





def create_compact_message(elems, dict):
  str = f"Compounds with {elem_dict_to_str(elems)}:\n"
  for k,v in dict.items():
    str += f"{k} - {v.strip()},\n"
  return str

def create_more_compact_message(elems,dict):
  str = f"Compounds with {elem_dict_to_str(elems)}:\n"
  for k,v in dict.items():
    str +=f"{v.strip()},"
  return str


def setup(bot):
  bot.add_cog(Compounds(bot))