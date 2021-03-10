import discord
#import youtube_dl
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import random

client = commands.Bot(command_prefix = '')
status = cycle(['NOTHING', 'I am not playing'])
@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

players = {}

@client.command(aliases=['https://youtu.be/15b6Vm2t3EE'])
async def _pass(ctx):
    embed=discord.Embed(name = ctx.author.display_name, title="My Youtube channel", url="https://www.youtube.com/c/basitking453/videos", description="PASSWORD IS = `uHN12YAFI1HQGH3L0vO8u4Y7M5EJPk2a`", color=0x000000, icon_url=ctx.author.avatar_url, )
    await ctx.send(embed=embed)
@client.event
async def on_command_error(ctx, error):
    pass
    #if isinstance(error, commands.CommandNotFound):
        #await ctx.send('Invalid command')
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
@client.command()
async def ping(ctx):
    await ctx.send(f'ping {round(client.latency * 1000)}ms')
@client.command(aliases=['سوال', 'test'])
async def _soal(ctx, *, question):
    responses = [ "مسلم است",
                "تصمیم گرفته شده است تا",
                "بدون شک",
                "بله - قطعا",
                "ممکنه بهش تکيه کني",
                "همونطور که ميبينم، آره",
                "به احتمال زياد",
                "چشم انداز خوب",
                "بله",
                "نشانه ها به بله اشاره می کنند",
                "پاسخ مبهم، دوباره امتحان کنید.",
                "بعداً دوباره بپرس",
                "بهتره الان بهت نگم",
                "الان نميتونم پيش بيني کنم",
                "تمرکز کن و دوباره بپرس",
                "روي اون حساب نکن",
                "پاسخ من نه است",
                "منابع من ميگن نه",
                "چشم انداز نه چندان خوب.",
                "بسیار مشکوک است.",]
    await ctx.send(f'سوال: {question}\nپاسخ: {random.choice(responses)}')
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int(5)):
    await ctx.channel.purge(limit=amount)
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
def manam(ctx):
    return ctx.author.id == 533305742455865350

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_play(url)
    players[server.id] = player
    player.start()




client.run('ODE4ODU1MTg1OTc1MjE0MTYx.YEeIUQ.mnKbi5jP_UxT8csJWkBwaqhCZt8')
client.close