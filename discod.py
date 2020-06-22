import discord
import random
from discord.ext import commands
from random import choice

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'magic'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.'
                'It is decidedly so',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                 'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'Yes – definitely.',
                'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer:{random.choice(responses)}')


@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount + 1)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
@client.command()
async def dice6(ctx):
    dice =        ['1',
                   '2',
                   '3',
                   '4',
                   '5',
                   '6',]
    await ctx.send(f'{random.choice(dice)}')

@client.command()
async def dice20(ctx):
    dicek = ['1',
             '2',
             '3',
             '4',
             '5',
             '6',
             '7',
             '8',
             '9',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '16',
             '17',
             '18',
             '19',
             '20',]
    await ctx.send(f'{random.choice(dicek)}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.spiit('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) -- (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run('NzA2OTkyNzQ3NzgxMDI5OTI4.XvDnWQ._tbrgDQmCLxWz7gWf1EzKQhHHYk')