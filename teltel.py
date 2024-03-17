import discord
from discord.ext import commands
from ossapi import *

TOKEN = ('token')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

client_id = your client_id
client_secret = 'yourclientsecret'

api = Ossapi(client_id, client_secret)

def DHMS(s):
    days = s // 86400
    s = s % 86400
    hours = s // 3600
    s = s % 3600
    minutes = s // 60
    s = s % 60
    return f"{days}日{hours}時間{minutes}分{s}秒"

def get_playerinfo(username):
    user = api.user(username)
    info = {
        "global_rank": user.statistics.global_rank,
        "ranking": user.statistics.country_rank,
        "rankscore": user.statistics.ranked_score,
        "level": user.statistics.level.current,
        "pp": round(user.statistics.pp),
        "playcount": user.statistics.play_count,
        "playtime": DHMS(user.statistics.play_time),
        "totalscore": user.statistics.total_score,
        "hitcount": user.statistics.total_hits,
        "maxcombo": user.statistics.maximum_combo,
        "精度": user.statistics.hit_accuracy
    }
    return info

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("起動しました")


@bot.hybrid_command()
async def sex(ctx, *, name):
    info = get_playerinfo(name)
    
    embed = discord.Embed(title=f"{name}の情報")
    embed.add_field(name=f"level",value={info['level']})
    embed.add_field(name=f"pp",value={info['pp']})
    embed.add_field(name=f"精度",value={info['精度']})
    embed.add_field(name=f"ranking",value={info['global_rank']})
    


    await ctx.send(embed=embed)


    

bot.run(TOKEN)