import discord
from discord.ext import commands
from utils import parse_elems
import json
import itertools


class Clash(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  @commands.cooldown(1, 2, commands.BucketType.user)
  async def coc(self, ctx, *, inventory):
    compound = inventory.replace(" ","")
    elements = parse_elems(compound)
    comps = producibles(elements, compound )
    desc = ""
    for k,v in comps.items():
      desc += f"**{k}:** {v['Shape']}\n" 
    
    dembed = discord.Embed(title="Compounds producible", description=desc)
    dembed.set_footer(text="Keep hating")
    await ctx.send(embed=dembed)
      




def producible(inv, compound):
  with open("COC-compounds.txt") as f:
    dict = json.load(f)
  all = {}
  for comp,data in dict.items():
    add = True
    for k,v in inv.items():
      if not add: continue 
      if k not in comp:
        add = False
        continue
      if data["Constituents"][k] > v:
        add = False
    for k,v in data["Constituents"].items():
      if k not in compound: 
        add = False
        continue 
    if add: all[comp] = data
  return all

def producibles(elems, compound):
  di = {} 
  combs = get_combinations(elems) 
  for a in combs:
    comp = "".join(a)
    inv = {}
    for d in a:
      inv[d] = elems[d]
    data = producible(inv,comp)
    di.update(data)
  return di


def get_combinations(dct):
    keys = list(dct.keys())
    combinations_list = []
    for i in range(1, len(keys) + 1):
        combinations_list += list(itertools.combinations(keys, i))
    return combinations_list



def setup(bot):
  bot.add_cog(Clash(bot))
