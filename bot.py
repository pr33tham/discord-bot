import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

f = open("rules.txt",'r')
rules = f.readlines()

@client.command(aliases=['rules'])
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@client.command(aliases=['c'])
@commands.has_permissions(manage_permissions = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason = 'No reason provided'):
    await member.send("you have been kicked from because :" + reason) 
    await member.kick(reason=reason)

@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx,member:discord.Member):
    muted_role = ctx.guild.get_role(783318763063607337)
    await member.add_roles(muted_role)
    await ctx.send(member.mention + ' has been muted')

@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def ummute(ctx,member:discord.Member):
    muted_role = ctx.guild.get_role()
    await member.remove_roles(muted_role)
    await ctx.send(member.mention + ' has been unmuted')

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason = 'No reason provided'):
    await ctx.send(member.display_name +" you have been banned from server because : " + reason) 
    await member.ban(reason=reason)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name,member_disc = member.split('#')
    for banned_entry in banned_users:
        user = banned_entry.user
        if (user.name, user.discriminator) == (member_name,member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name +' has been unbanned')
            return
        
    await ctx.send(member +'was not found')
client.run()     